#!/usr/bin/env python3
"""Abu Ghazi Village, Wadi Musa: 10-year model with grace-period debt.

Study-specific model. The team's tools/fin_model.py is a 5-year model with no
grace period and no rent lines, so this project needs its own script (the
team's shared files are left unchanged).

Usage: python3 agv_model.py            -> writes results.json, tables.md, AGV-financial-model.xlsx
Year 1 = March 2027 - February 2028. Currency: JOD.
"""
import copy
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
YEARS = 10

# ---------------------------------------------------------------- base inputs
BASE = {
    # Leased units, stabilized monthly rent [SOURCE: owner brief, Oct 2026]
    "rents": {
        "LU-19+LU-20 restaurant": 1678.74,
        "LU-12 family cafe": 997.10,
        "LU-15 local products": 845.10,
        "LU-17 crafts": 681.00,
        "LU-18 juice & ice cream": 339.04,
        "Tower sunset lookout": 640.00,
    },
    "occupancy": [0.85] + [0.95] * 9,          # [ASSUMPTION] Y1 lease-up / fit-out months, then 5% structural vacancy
    "rent_growth": 0.02,                       # [ASSUMPTION] per year from Y3
    "rent_growth_from_year": 3,
    "tower_rent": True,
    # Owner-run
    "pos1": [14000, 15000],                    # [SOURCE: owner brief] minimal gallery in working case; +2%/yr after Y2 [ASSUMPTION]
    "pos1_growth": 0.02,
    "pos2": [21349],                           # [SOURCE: owner brief] Y1
    "pos2_y2_growth": 0.10, "pos2_growth": 0.03,  # [ASSUMPTION]
    "pos2_cogs": [0.38, 0.33] + [0.29] * 8,    # [ASSUMPTION] mix retail 50% margin / experiences 80% margin, shifting to experiences
    "other_revenue": [0.0] * 10,               # night market, domestic-tourism programme: kept out of base case
    "revenue_factor": 1.0,                     # stress: multiply all revenue
    "pos_factor": 1.0,                         # stress: multiply owner-run (POS) revenue only
    # OPEX Y1 [SOURCE: owner brief unless marked]
    "payroll": 30024.90, "seventh_day": 5004.0, "guard": 4113.0,
    "non_payroll": 6080.0, "insurance": 1500.0,
    "licences_fees": 1500.0,                   # [ASSUMPTION][VERIFY] PDTRA/municipal fees, building tax
    "maintenance_from_y2": 1500.0,             # [ASSUMPTION] ~1% of BOQ CAPEX
    "commission_pct": 0.03,                    # [SOURCE: owner brief] hotel & guide commissions on POS revenue
    "card_fee_pct": 0.015,                     # [ASSUMPTION] card/e-payment fees on POS revenue
    "cost_inflation": 0.025,                   # [ASSUMPTION] from Y2
    "opex_factor": 1.0,
    "extra_opex": [0.0] * 10,
    # CAPEX and depreciation
    "capex_boq": 151682.0, "contingency": 7584.10,   # [SOURCE: owner brief / BOQ]
    "dep_years": 20,                                 # [SOURCE: brief] 159,266 / 20 = 7,963
    "extra_capex": 0.0, "extra_capex_life": 7,
    "tax_rate": 0.20,                                # [SOURCE: brief working assumption][VERIFY basis]
    # Uses beyond CAPEX [SOURCE: owner brief]
    "y1_opex_reserve": 36104.90, "working_capital": 12300.0, "liquidity_reserve": 12329.0,
    # Financing: list of facilities
    "facilities": [
        {"name": "CBJ programme term loan", "amount": 200000.0, "rate": 0.03,
         "grace_months": 12, "repay_months": 108, "start_month": 1},
    ],
    "grant": 0.0, "owner_cash": 20000.0,
}


def pmt(p, r_annual, n):
    r = r_annual / 12
    return p / n if r == 0 else p * r / (1 - (1 + r) ** -n)


def schedule(f, months=YEARS * 12):
    """Monthly schedule: interest-only during grace, then level annuity."""
    rows, bal = [], 0.0
    pay = pmt(f["amount"], f["rate"], f["repay_months"])
    for m in range(1, months + 1):
        if m == f["start_month"]:
            bal = f["amount"]
        if m < f["start_month"] or bal <= 1e-6:
            rows.append((m, 0.0, 0.0, 0.0, bal))
            continue
        i = bal * f["rate"] / 12
        k = m - f["start_month"] + 1
        if k <= f["grace_months"]:
            p = 0.0
        else:
            p = min(pay - i, bal)
        bal -= p
        rows.append((m, i, p, i + p, bal))
    return rows, pay


def run(a):
    yrs = range(1, YEARS + 1)
    infl = [(1 + a["cost_inflation"]) ** (y - 1) for y in yrs]
    out = []
    # debt
    scheds = [schedule(f) for f in a["facilities"]]
    tax_loss_cf = 0.0
    total_debt = sum(f["amount"] for f in a["facilities"])
    capex = a["capex_boq"] + a["contingency"]
    cash = a["y1_opex_reserve"] + a["working_capital"] + a["liquidity_reserve"]
    opening_cash = cash
    for y in yrs:
        rg = (1 + a["rent_growth"]) ** max(0, y - a["rent_growth_from_year"] + 1)
        rent_month = sum(v for k, v in a["rents"].items() if a["tower_rent"] or not k.startswith("Tower"))
        rent = rent_month * 12 * a["occupancy"][y - 1] * rg
        pos1 = a["pos1"][y - 1] if y <= len(a["pos1"]) else a["pos1"][-1] * (1 + a["pos1_growth"]) ** (y - len(a["pos1"]))
        if y == 1:
            pos2 = a["pos2"][0]
        else:
            pos2 = a["pos2"][0] * (1 + a["pos2_y2_growth"]) * (1 + a["pos2_growth"]) ** (y - 2)
        other = a["other_revenue"][y - 1]
        f = a["revenue_factor"]
        pf = f * a["pos_factor"]
        rent, pos1, pos2, other = rent * f, pos1 * pf, pos2 * pf, other * pf
        pos = pos1 + pos2 + other
        revenue = rent + pos
        cogs = pos2 * a["pos2_cogs"][y - 1]
        commissions = pos * a["commission_pct"]
        card = pos * a["card_fee_pct"]
        staff = (a["payroll"] + a["seventh_day"] + a["guard"]) * infl[y - 1] * a["opex_factor"]
        other_opex = (a["non_payroll"] + a["insurance"] + a["licences_fees"]
                      + (a["maintenance_from_y2"] if y > 1 else 0)) * infl[y - 1] * a["opex_factor"]
        extra = a["extra_opex"][y - 1] * infl[y - 1] * a["opex_factor"]
        opex = staff + other_opex + extra + commissions + card
        ebitda = revenue - cogs - opex
        dep = capex / a["dep_years"] + (a["extra_capex"] / a["extra_capex_life"] if y <= a["extra_capex_life"] else 0)
        mrange = range((y - 1) * 12, y * 12)
        interest = sum(s[0][m][1] for s in scheds for m in mrange)
        principal = sum(s[0][m][2] for s in scheds for m in mrange)
        ds = interest + principal
        ebt = ebitda - dep - interest
        taxable = ebt - tax_loss_cf
        if taxable > 0:
            tax, tax_loss_cf = taxable * a["tax_rate"], 0.0
        else:
            tax, tax_loss_cf = 0.0, -taxable
        cfads = ebitda - tax
        dscr = cfads / ds if ds > 0 else None
        cash = cash + cfads - ds
        bal = sum(s[0][y * 12 - 1][4] for s in scheds)
        out.append(dict(year=y, rent=rent, pos1=pos1, pos2=pos2, other=other, revenue=revenue,
                        cogs=cogs, staff=staff, other_opex=other_opex + extra, commissions=commissions,
                        card=card, opex=opex, ebitda=ebitda, depreciation=dep, interest=interest,
                        ebt=ebt, tax=tax, net_profit=ebt - tax, cfads=cfads, principal=principal,
                        debt_service=ds, dscr=dscr, closing_cash=cash, debt_balance=bal,
                        rent_cover=(rent / 12) / (ds / 12) if ds else None))
    pays = [s[1] for s in scheds]
    dscrs = [r["dscr"] for r in out[1:] if r["dscr"]]
    summary = dict(
        total_debt=total_debt, opening_cash=opening_cash,
        monthly_payment=sum(pays), payments=[round(p, 2) for p in pays],
        dscr_y2=out[1]["dscr"], dscr_min=min(dscrs) if dscrs else None,
        dscr_avg=sum(dscrs) / len(dscrs) if dscrs else None, dscr_y10=out[-1]["dscr"],
        min_cash=min(r["closing_cash"] for r in out),
        total_interest=sum(r["interest"] for r in out),
        sources=total_debt + a["grant"] + a["owner_cash"],
        uses=capex + a["extra_capex"] + a["y1_opex_reserve"] + a["working_capital"] + a["liquidity_reserve"],
    )
    return out, summary, scheds


def variant(**kw):
    a = copy.deepcopy(BASE)
    if kw.pop("core", False):
        a.update(copy.deepcopy(CORE_KW))
    for k, v in kw.items():
        a[k] = v
    return a


def fac(name, amount, rate, grace=12, repay=108, start=1):
    return {"name": name, "amount": amount, "rate": rate, "grace_months": grace,
            "repay_months": repay, "start_month": start}


# ---------------------------------------------------------------- funding structures (core)
FUNDING = {
    "F0 CBJ working case (brief): 200k @3.00%, 12m grace + 108": [fac("CBJ working case", 200000, 0.03)],
    "F1 Brief structure at verified floor: 200k CBJ sectors programme @3.25%, 12m grace + 108": [fac("CBJ sectors programme", 200000, 0.0325)],
    "F5 RECOMMENDED: 165k CBJ sectors programme @3.25%, 12m grace + 108 (no Y1 opex reserve)": [fac("CBJ sectors programme", 165000, 0.0325)],
    "F1b same, bank margin higher @4.50%": [fac("CBJ sectors programme", 200000, 0.045)],
    "F1c same @3.25% with 24m grace + 96": [fac("CBJ sectors programme", 200000, 0.0325, 24, 96)],
    "F2 Split: 160k CBJ @3.25% + 40k WC commercial @8.5% / 5y": [fac("CBJ term", 160000, 0.0325), fac("Commercial WC", 40000, 0.085, 0, 60)],
    "F3 Islamic (diminishing musharaka/ijara) unsubsidised @7.0%, 12m grace + 108": [fac("Islamic", 200000, 0.07)],
    "F4 Commercial SME loan + JLGC 70% @9.5% all-in, 72m incl. 12m grace": [fac("Commercial+JLGC", 200000, 0.095, 12, 60)],
}

# ---------------------------------------------------------------- gallery scenarios
def gallery(rev_stab, capex, extra_hosts, facilities, grant=0.0, owner_extra=0.0):
    ramp = [0.6, 0.85] + [1.0 * 1.02 ** i for i in range(8)]
    pos1 = [rev_stab * r for r in ramp]
    extra = [capex * 0.06 + 2400 + 5004 * extra_hosts] * 10   # [ASSUMPTION] media upkeep 6%/yr, power/HVAC 2,400, hosts
    return variant(core=True, pos1=pos1, pos1_growth=0.0, extra_opex=extra, extra_capex=capex,
                   facilities=facilities, grant=grant, owner_cash=20000 + owner_extra)


CORE = [fac("CBJ sectors programme", 165000, 0.0325)]
CORE_KW = dict(facilities=CORE, y1_opex_reserve=0.0)
GALLERY = {
    "G0 No gallery investment (base case)": variant(core=True),
    "G1 Study approach: 100k loan, base revenue 52,434": gallery(52434, 100000, 1, CORE + [fac("Gallery loan", 100000, 0.0325)]),
    "G1c Study approach: 100k loan, conservative 22,500": gallery(22500, 100000, 0, CORE + [fac("Gallery loan", 100000, 0.0325)]),
    "G1s Study approach: 100k loan, ~study price/volume 15,000 stabilized": gallery(15000 / 1.0, 100000, 0, CORE + [fac("Gallery loan", 100000, 0.0325)]),
    "G2 RECOMMENDED Phase 1: 50k tranche, conservative 22,500": gallery(22500, 50000, 0, CORE + [fac("Gallery tranche", 50000, 0.0325, 12, 72)]),
    "G2b Phase 1: 50k tranche, base 52,434": gallery(52434, 50000, 1, CORE + [fac("Gallery tranche", 50000, 0.0325, 12, 72)]),
    "G3 Phase 1+2: 50k tranche + 50k grant/partner, base 52,434": gallery(52434, 100000, 1, CORE + [fac("Gallery tranche", 50000, 0.0325, 12, 72)], grant=50000),
    "G4 High-end 128k: 50k tranche + 78k grant/partner, upside 104,859": gallery(104859, 128000, 2, CORE + [fac("Gallery tranche", 50000, 0.0325, 12, 72)], grant=78000),
}

# ---------------------------------------------------------------- refinancing the owner's existing ~140k loan (added 15 Oct 2026)
# Owner says total debt must be >= 250k because an existing loan of ~140k sits on the project.
# Its lender, rate and remaining term are unknown [VERIFY]; these cases assume it is fully refinanced.
REFI = {
    "R1 250k CBJ sectors programme @3.25%, 12m grace + 108": variant(core=True, facilities=[fac("CBJ", 250000, 0.0325)]),
    "R2 305k (140k refi + 165k new) CBJ @3.25%, 12m grace + 108": variant(core=True, facilities=[fac("CBJ", 305000, 0.0325)]),
    "R3 110k CBJ @3.25% + 140k refi commercial @8.5% 10y": variant(core=True, facilities=[fac("CBJ", 110000, 0.0325), fac("Refi", 140000, 0.085)]),
    "R4 110k CBJ @3.25% + 140k refi Islamic @7% 15y (12m grace + 168)": variant(core=True, facilities=[fac("CBJ", 110000, 0.0325), fac("Refi", 140000, 0.07, 12, 168)]),
    "R5 RECOMMENDED if 250k: one 250k Islamic diminishing musharaka/ijara @7% 15y (12m grace + 168)": variant(core=True, facilities=[fac("Islamic", 250000, 0.07, 12, 168)]),
    "R5s R5 with revenue -10%": variant(core=True, facilities=[fac("Islamic", 250000, 0.07, 12, 168)], revenue_factor=0.9),
    "R6 250k commercial @8.5% 15y (12m grace + 168)": variant(core=True, facilities=[fac("Commercial", 250000, 0.085, 12, 168)]),
    "R7 305k: 165k CBJ + 140k refi Islamic @7% 15y": variant(core=True, facilities=[fac("CBJ", 165000, 0.0325), fac("Refi", 140000, 0.07, 12, 168)]),
    "Cap: 205k CBJ @3.25% 10y (DSCR ~1.25 limit)": variant(core=True, facilities=[fac("CBJ", 205000, 0.0325)]),
}

# ---------------------------------------------------------------- stress tests on recommended core
def occ(level):
    return [min(0.85, level)] + [level] * 9

STRESS = {
    "Base (recommended F5)": variant(core=True),
    "Occupancy 85% from Y2": variant(core=True, occupancy=occ(0.85)),
    "Occupancy 70% from Y2": variant(core=True, occupancy=occ(0.70)),
    "Revenue -10%": variant(core=True, revenue_factor=0.9),
    "Revenue -20%": variant(core=True, revenue_factor=0.8),
    "Revenue -30%": variant(core=True, revenue_factor=0.7),
    "OPEX +20%": variant(core=True, opex_factor=1.2),
    "Loss of tower rent": variant(core=True, tower_rent=False),
    "Revenue -30% and OPEX +20%": variant(core=True, revenue_factor=0.7, opex_factor=1.2),
    "Tax 21% (company: 20% + 1% national contribution)": variant(core=True, tax_rate=0.21),
    "No rent growth": variant(core=True, rent_growth=0.0),
    "Rate 4.5% (higher bank margin)": variant(core=True, facilities=[fac("CBJ", 165000, 0.045)]),
    "Owner-run (POS) revenue -30%": variant(core=True, pos_factor=0.7),
    "Owner-run (POS) revenue -50%": variant(core=True, pos_factor=0.5),
    "Rents -20% (vacancy + discounts) and POS -30%": variant(core=True, occupancy=[0.85*0.8/0.95*0.95]+[0.95*0.8]*9, pos_factor=0.7),
}


def fmt(x, d=0):
    if x is None:
        return "–"
    return f"{x:,.{d}f}"


def main():
    results = {"funding": {}, "gallery": {}, "stress": {}, "refinance": {}}
    md = []
    base_rows, base_sum, base_sched = run(variant(core=True))
    wc_rows, wc_sum, _ = run(variant())
    # annual table
    md.append("## Base case (recommended F5) annual cash flow, JOD\n")
    keys = ["rent", "pos1", "pos2", "revenue", "cogs", "staff", "other_opex", "commissions", "card", "ebitda",
            "depreciation", "interest", "ebt", "tax", "net_profit", "cfads", "principal", "debt_service", "dscr",
            "closing_cash", "debt_balance"]
    md.append("| Line | " + " | ".join(f"Y{r['year']}" for r in base_rows) + " |")
    md.append("|---|" + "---:|" * YEARS)
    for k in keys:
        md.append(f"| {k} | " + " | ".join(fmt(r[k], 2 if k == 'dscr' else 0) for r in base_rows) + " |")
    md.append("")
    for name, facs in FUNDING.items():
        rows, s, _ = run(variant(facilities=facs, y1_opex_reserve=0.0) if name.startswith("F5") else variant(facilities=facs))
        results["funding"][name] = dict(summary=s, dscr=[r["dscr"] for r in rows], cash=[r["closing_cash"] for r in rows])
    for name, a in GALLERY.items():
        rows, s, _ = run(a)
        results["gallery"][name] = dict(summary=s, dscr=[r["dscr"] for r in rows], cash=[r["closing_cash"] for r in rows],
                                        revenue=[r["revenue"] for r in rows])
    for name, a in REFI.items():
        rows, s, _ = run(a)
        results["refinance"][name] = dict(summary=s, dscr=[r["dscr"] for r in rows], cash=[r["closing_cash"] for r in rows])
    for name, a in STRESS.items():
        rows, s, _ = run(a)
        results["stress"][name] = dict(summary=s, dscr=[r["dscr"] for r in rows], cash=[r["closing_cash"] for r in rows])
    for grp in ("funding", "gallery", "stress", "refinance"):
        md.append(f"## {grp}\n")
        md.append("| Case | Debt | Monthly pmt | DSCR Y2 | Min DSCR Y2-10 | Avg DSCR | DSCR Y10 | Min cash | Total interest |")
        md.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for name, r in results[grp].items():
            s = r["summary"]
            md.append(f"| {name} | {fmt(s['total_debt'])} | {fmt(s['monthly_payment'],2)} | {fmt(s['dscr_y2'],2)} | "
                      f"{fmt(s['dscr_min'],2)} | {fmt(s['dscr_avg'],2)} | {fmt(s['dscr_y10'],2)} | {fmt(s['min_cash'])} | {fmt(s['total_interest'])} |")
        md.append("")
    results["base_rows"] = base_rows
    results["working_case_rows"] = wc_rows
    results["base_summary"] = base_sum
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=1, default=float)
    with open(os.path.join(HERE, "tables.md"), "w") as f:
        f.write("\n".join(md))
    write_xlsx(variant(core=True), base_rows, results)
    print("\n".join(md))


# ---------------------------------------------------------------- Excel with live formulas
def write_xlsx(a, rows, results):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    wb = Workbook()
    bold = Font(bold=True)
    inp = PatternFill("solid", fgColor="FFF2CC")

    ws = wb.active
    ws.title = "Inputs"
    f = a["facilities"][0]
    inputs = [
        ("Loan amount (JOD)", f["amount"], "[SOURCE: owner brief] 160k long-term + 40k working capital"),
        ("Annual rate", f["rate"], "[SOURCE: HBTF CBJ sectors programme page: outside Amman 0.5% + margin, min 3.25%][VERIFY bank offer]"),
        ("Grace months (interest only)", f["grace_months"], "[SOURCE: owner brief; programme allows up to 24]"),
        ("Repayment months", f["repay_months"], "[SOURCE: owner brief]"),
        ("Tax rate", a["tax_rate"], "[ASSUMPTION per brief][VERIFY individual vs company basis]"),
        ("Depreciable CAPEX (BOQ + contingency)", a["capex_boq"] + a["contingency"], "[SOURCE: BOQ 151,682 + 5% 7,584.10]"),
        ("Depreciation years", a["dep_years"], "[ASSUMPTION] lease term 20 years"),
        ("Opening cash reserves", a["y1_opex_reserve"] + a["working_capital"] + a["liquidity_reserve"], "[SOURCE: brief uses] 36,104.90 + 12,300 + 12,329"),
    ]
    ws.append(["Input", "Value", "Basis"])
    for r in inputs:
        ws.append(list(r))
    for c in ws["B"][1:]:
        c.fill = inp
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["C"].width = 95
    ws["A12"] = "Yellow cells are inputs. Change them and the Debt and CashFlow sheets recalculate (debt service, tax, DSCR)."

    # Debt sheet: monthly schedule with formulas
    d = wb.create_sheet("Debt")
    d.append(["Month", "Year", "Opening balance", "Interest", "Principal", "Payment", "Closing balance"])
    d["I1"] = "Level payment after grace"
    d["J1"] = "=PMT(Inputs!B3/12,Inputs!B5,-Inputs!B2)"
    for m in range(1, YEARS * 12 + 1):
        r = m + 1
        d.cell(r, 1, m)
        d.cell(r, 2, f"=INT((A{r}-1)/12)+1")
        d.cell(r, 3, "=Inputs!B2" if m == 1 else f"=G{r-1}")
        d.cell(r, 4, f"=C{r}*Inputs!B3/12")
        d.cell(r, 5, f"=IF(A{r}<=Inputs!B4,0,MIN($J$1-D{r},C{r}))")
        d.cell(r, 6, f"=D{r}+E{r}")
        d.cell(r, 7, f"=C{r}-E{r}")
    for col in "CDEFGJ":
        for c in d[col][1:]:
            c.number_format = "#,##0.00"

    # Cash flow: lines as values (from the model), aggregates and debt as formulas
    c = wb.create_sheet("CashFlow")
    c.append(["JOD, Year 1 = Mar 2027-Feb 2028"] + [f"Y{y}" for y in range(1, YEARS + 1)])
    lines = [("Rent income", "rent"), ("POS1 gallery (minimal, base)", "pos1"), ("POS2 crafts shop", "pos2"),
             ("POS2 cost of goods", "cogs"), ("Staff (payroll, 7th-day cover, guard)", "staff"),
             ("Other OPEX (non-payroll, insurance, fees, maintenance)", "other_opex"),
             ("Hotel & guide commissions 3% POS", "commissions"), ("Card fees 1.5% POS", "card")]
    for label, k in lines:
        c.append([label] + [round(r[k], 2) for r in rows])
    # rows 2..9 values
    L = lambda i: chr(ord("B") + i)
    formulas = [
        ("Revenue", lambda i: f"={L(i)}2+{L(i)}3+{L(i)}4"),
        ("EBITDA", lambda i: f"={L(i)}10-{L(i)}5-{L(i)}6-{L(i)}7-{L(i)}8-{L(i)}9"),
        ("Depreciation", lambda i: f"=Inputs!$B$7/Inputs!$B$8"),
        ("Interest", lambda i: f"=SUMIF(Debt!$B:$B,{i+1},Debt!$D:$D)"),
        ("Profit before tax", lambda i: f"={L(i)}11-{L(i)}12-{L(i)}13"),
        ("Tax loss brought forward", lambda i: "=0" if i == 0 else f"=MAX(0,{L(i-1)}15-{L(i-1)}14)"),
        ("Income tax", lambda i: f"=MAX(0,{L(i)}14-{L(i)}15)*Inputs!$B$6"),
        ("Net profit", lambda i: f"={L(i)}14-{L(i)}16"),
        ("CFADS (EBITDA - tax)", lambda i: f"={L(i)}11-{L(i)}16"),
        ("Principal", lambda i: f"=SUMIF(Debt!$B:$B,{i+1},Debt!$E:$E)"),
        ("Debt service", lambda i: f"={L(i)}13+{L(i)}19"),
        ("DSCR (CFADS / debt service)", lambda i: f"=IF({L(i)}20=0,\"-\",{L(i)}18/{L(i)}20)"),
        ("Closing cash", lambda i: (f"=Inputs!$B$9+{L(i)}18-{L(i)}20" if i == 0 else f"={L(i-1)}22+{L(i)}18-{L(i)}20")),
        ("Rent cover of debt service", lambda i: f"=IF({L(i)}20=0,\"-\",{L(i)}2/{L(i)}20)"),
    ]
    for label, fn in formulas:
        c.append([label] + [fn(i) for i in range(YEARS)])
    # tax loss row 15: loss carried = max(0, prior carried - prior PBT) when PBT<carried; simple version
    c.column_dimensions["A"].width = 52
    for row in c.iter_rows(min_row=2, min_col=2):
        for cell in row:
            cell.number_format = "#,##0.00" if cell.row in (21, 23) else "#,##0"
    for r in (10, 11, 18, 21):
        c.cell(r, 1).font = bold

    # Scenario sheets (values from the Python engine)
    for grp, title in (("funding", "Funding options"), ("gallery", "Gallery scenarios"), ("stress", "Stress tests"), ("refinance", "Refinance 140k")):
        s = wb.create_sheet(title)
        s.append(["Case", "Total debt", "Monthly payment", "DSCR Y2", "Min DSCR Y2-10", "Avg DSCR", "DSCR Y10", "Min closing cash", "Total interest 10y"]
                 + [f"DSCR Y{y}" for y in range(1, 11)])
        for name, r in results[grp].items():
            sm = r["summary"]
            s.append([name, sm["total_debt"], sm["monthly_payment"], sm["dscr_y2"], sm["dscr_min"], sm["dscr_avg"],
                      sm["dscr_y10"], sm["min_cash"], sm["total_interest"]] + [x if x else None for x in r["dscr"]])
        s.column_dimensions["A"].width = 70
        for row in s.iter_rows(min_row=2, min_col=2):
            for cell in row:
                cell.number_format = "#,##0.00"
    wb.save(os.path.join(HERE, "AGV-financial-model.xlsx"))


if __name__ == "__main__":
    main()
