#!/usr/bin/env python3
"""Petra surgical hospital (20-bed specialised surgical hospital with 24/7 trauma ER, Wadi Musa): 10-year bank model.

Revised 16 Oct 2026 at the owner's request: smallest licensable hospital (specialised, 20 beds),
scope = trauma/orthopaedics + general surgery + gynaecological surgery + small paediatric ward + day surgery.

Study-specific model. The team's tools/fin_model.py is a 5-year model with no
grace period, so this study has its own script (team files left unchanged).

Timeline: C1 = 2027 and C2 = 2028 are construction years; Y1 = 2029 ... Y10 = 2038.
Currency JOD. Annual periods. Prices net of sales tax (medical services are exempt
or zero-rated in practice [VERIFY]).

Usage: python3 ptc_model.py  -> results.json, tables.md, PTC-financial-model.xlsx
"""
import copy
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
N = 10                     # operating years
YEARS = list(range(2029, 2029 + N))

# ------------------------------------------------------------------ inputs
BASE = {
    # ---- capacity [brief]
    "ward_beds": 17, "icu_beds": 3,   # 17 ward beds (surgical/ortho 9, gynaecology 4, paediatrics 4) + ICU 2 + 1 isolation = 20 licensed beds; day-surgery trolleys are not licensed beds [VERIFY with MoH]
    # ---- volumes by operating year [ASSUMPTION unless noted]
    "ward_occ": [0.38, 0.50, 0.60, 0.66, 0.70, 0.72, 0.72, 0.72, 0.72, 0.72],
    "icu_occ":  [0.30, 0.42, 0.52, 0.60, 0.62, 0.65, 0.65, 0.65, 0.65, 0.65],
    "surgeries": [500, 700, 850, 950, 1000, 1050, 1050, 1080, 1080, 1080],   # admitted operations: general, ortho/trauma, gynaecological, paediatric
    "day_surgeries": [600, 1000, 1400, 1700, 1900, 2000, 2050, 2100, 2100, 2100],   # same-day cases (hernia, lap chole day-case, arthroscopy, hardware removal, D&C/hysteroscopy, circumcision, minor)
    "endoscopies": [300, 500, 700, 800, 900, 950, 1000, 1000, 1000, 1000],
    "er_per_day": [25, 32, 38, 42, 45, 46, 48, 50, 50, 50],
    "ct_scans": [2000, 2700, 3300, 3800, 4100, 4200, 4300, 4400, 4400, 4400],
    "opd_visits": [7000, 11000, 14000, 16000, 17500, 18000, 18500, 19000, 19000, 19000],   # surgery, ortho, gynaecology and paediatric clinics
    "physio": [2500, 4000, 5000, 6000, 6500, 7000, 7000, 7000, 7000, 7000],
    "tourist_cases": [400, 500, 600, 600, 650, 650, 700, 700, 700, 700],
    # ---- prices, JOD at 2029 prices [ASSUMPTION; public unit costs 2019: bed-day 172.9, ICU 377.8, ER 31.8, surgery 449.6, OPD 58.4]
    "p_ward_day": 120.0, "p_icu_day": 420.0,
    "p_surgery": 750.0,          # hospital fee per operation (OR, anaesthesia, recovery, routine consumables); surgeons bill their own fees (open-staff model)
    "p_implant": 220.0,          # average implant/mesh billing per admitted operation (ortho share lower in the mixed case-mix)
    "p_day_surgery": 350.0,      # hospital fee per day case
    "p_day_implant": 30.0,       # average implant/mesh per day case
    "p_endoscopy": 120.0,
    "p_er": 45.0,                # per ER visit incl. basic X-ray and lab
    "p_ct": 85.0, "p_opd": 30.0, "p_physio": 15.0,
    "p_tourist": 220.0,          # per tourist ER case billed to travel-assistance companies
    "pharmacy_pct": 0.06,        # outpatient/discharge pharmacy sales as % of ER + OPD revenue
    "price_growth": 0.015,       # from Y2; PHA says private prices flat for 22 years, so kept low
    "discount_pct": 0.05,        # insurer discounts and claim denials, off gross revenue
    "bad_debt_pct": 0.02,        # of net revenue
    "volume_factor": 1.0, "price_factor": 1.0, "tourist_factor": [1.0] * N,
    # ---- payroll: monthly gross at full staffing, 2029 JOD [ASSUMPTION from salary research; see 03-operations]
    "staff": [
        # (role, count, monthly gross)
        ("Medical director (owner, physician)", 1, 5000),
        ("Anaesthetists (also cover the 3-bed ICU)", 2, 4000),
        ("Emergency physicians (specialists)", 2, 3000),
        ("Paediatrician (paediatric ward, newborn cover)", 1, 3000),
        ("Internist (part-time consults)", 1, 2000),
        ("GPs / residents (ER, wards, ICU cover)", 8, 1100),
        ("Director of nursing", 1, 1500),
        ("Charge nurses", 3, 1100),
        ("Staff nurses and midwife (ER, ICU, OR/day unit, wards)", 37, 700),
        ("Radiographers / CT technologists", 5, 750),
        ("Lab and blood-bank technicians", 5, 750),
        ("Pharmacists", 2, 900),
        ("Physiotherapists", 2, 750),
        ("Anaesthesia technicians", 2, 800),
        ("Paramedics / ambulance crew", 6, 650),
        ("CSSD and endoscopy technicians", 3, 500),
        ("Biomedical / maintenance", 2, 800),
        ("Administrative manager", 1, 2500),
        ("Finance and insurance claims", 5, 750),
        ("HR", 1, 900),
        ("IT", 1, 900),
        ("Reception and medical records", 7, 450),
        ("Purchasing and stores", 2, 600),
        ("Contracts and marketing officer", 1, 1000),
        ("Housekeeping and porters", 11, 380),
        ("Security", 5, 400),
    ],
    "staffing_factor": [0.80, 0.88, 0.95, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    "oncost_pct": 0.18,          # employer social security 14.25% (capped) + group health insurance and allowances
    "wage_growth": 0.03,
    "pre_open_payroll_months": 3,   # recruitment and training before opening (in pre-opening costs)
    # ---- other opex
    "consumables_pct": 0.18,     # drugs and medical consumables, % of net revenue excl. implants [Ennab used 20%]
    "implant_cost_pct": 0.75,    # implants cost as % of implant billing
    "doctor_incentive_pct": 0.05,  # incentive pool on surgery + ER revenue
    "radiology_read_fee": 12.0,  # per CT, external radiologist/teleradiology
    "utilities": 140000.0,       # electricity ~0.8m kWh x 0.12 + water + generator fuel [ASSUMPTION]
    "outsourced": 160000.0,      # laundry, catering, medical-waste, linen
    "insurance_malpractice": 45000.0,
    "marketing_contracts": [80000.0] + [50000.0] * (N - 1),
    "it_licences": 40000.0,
    "general_admin": 80000.0,
    "ground_rent": 0.0,          # annual land lease (lean option leases the land instead of buying)
    "licence_fees": 16000.0,     # MoH bed licence renewals, EMRC, syndicates, municipal
    "maint_equip_pct": [0.02, 0.02, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06],  # of medical equipment cost (warranty first 2 years)
    "maint_building_pct": 0.01,
    "cost_growth": 0.025,
    "opex_factor": 1.0,
    "maint_capex_pct": 0.015,    # replacement capex from Y3, % of net revenue; depreciated over 8 years
    # ---- capex (JOD) [ASSUMPTION; see 03-operations for line items]
    "land_dunum": 3.0, "land_price_per_dunum": 60000.0, "land_fees_pct": 0.09,   # land not chosen; reference study ~61.6k/dunum + 8.3% fees
    "gfa_m2": 3000.0, "build_cost_m2": 650.0,
    "design_supervision_pct": 0.06,
    "mep_special": 380000.0,     # medical gases, OR HVAC/HEPA, 2 generators, nurse call, fire, CCTV, 250 m3 water tank
    "med_equipment": 1650000.0,
    "furniture_it": 200000.0,    # furniture 65k, HIS/EMR/PACS/network 135k
    "vehicles": 90000.0,         # 2 equipped ambulances (licensing minimum)
    "contingency_pct": 0.10,     # on building, MEP and equipment
    "pre_opening": 320000.0,
    "expansion_provision": 0.0,  # built-in provision for Phase 2 (stronger foundations/columns for an extra floor, spare risers, shell for OR 3)     # licences, recruitment and 3-month training payroll, commissioning, launch
    "no_tax_exemption_uplift": 0.0,   # set 0.16 if customs/sales-tax exemption on equipment and MEP is NOT granted
    "cash_reserve": 900000.0,    # ramp-up and debt-service reserve funded at opening
    "arrangement_fee_pct": 0.005,
    "capex_phasing_c1": 0.40,    # share of building/MEP spent in 2027 (land 100% in 2027, equipment 100% in 2028)
    # ---- working capital
    "dso_days": 105,             # payer mix: cash 20% (0 d), insurers 40% (120 d), MoH/RMS contracts 30% (180 d), assistance 5% (60 d), other 5%
    "inventory_days": 45, "payables_days": 60,
    # ---- tax [SOURCE: CIT 20% + 1% national contribution; Investment Environment Regulation 2023 Art. 21, class (ب) 75% reduction 5 years][VERIFY]
    "tax_rate": 0.21, "tax_relief_pct": 0.75, "tax_relief_years": 5,
    # ---- valuation
    "discount_rate": 0.10, "terminal_growth": 0.02,
    # ---- funding (filled by structure)
    "t1_amount": 3000000.0, "t1_rate": 0.0375, "t1_grace": 2, "t1_repay": 8,   # CBJ economic-sectors programme, health window; drawn 2028; grace 2028-2029
    "t2_amount": 0.0,       "t2_rate": 0.075,  "t2_grace": 2, "t2_repay": 8,   # Islamic ijara / diminishing musharaka or commercial loan
    "t3_amount": 600000.0,  "t3_rate": 0.07,   "t3_grace": 0, "t3_repay": 5,   # equipment finance lease (CT, C-arms), from opening
    "grant": 0.0,
}

# ------------------------------------------------------------------ lean, expandable Phase 1 (owner request 08:04: least money, upgradable)
STANDARD = copy.deepcopy(BASE)   # the 16 Oct 07:50 version (land bought, full build), kept as a comparison option
_lean_staff = []
for role, cnt, wage in STANDARD["staff"]:
    if role.startswith("Housekeeping"):
        continue                         # outsourced (cost moved to outsourced services)
    if role.startswith("Security"):
        cnt = 4
    if role.startswith("GPs"):
        cnt = 7
    if role.startswith("Staff nurses"):
        cnt = 34
    if role.startswith("Reception"):
        cnt = 6
    if role.startswith("Finance"):
        cnt = 4
    if role.startswith("Purchasing"):
        cnt = 1
    if role.startswith("Lab"):
        cnt = 4
    if role.startswith("Radiographers"):
        cnt = 4
    _lean_staff.append((role, cnt, wage))
BASE.update({
    "staff": _lean_staff,
    "staffing_factor": [0.75, 0.85, 0.95, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    "land_price_per_dunum": 0.0, "land_fees_pct": 0.0,   # land on a long lease (municipality, PDTRA, Awqaf or family) instead of purchase
    "ground_rent": 18000.0,                               # [ASSUMPTION][VERIFY] 3 dunum long lease
    "gfa_m2": 2600.0, "build_cost_m2": 600.0,             # compact 2-floor design, single core; 20 beds fitted out
    "expansion_provision": 120000.0,                      # foundations/columns sized for a 3rd floor (+20 beds), spare MEP risers, OR-3 shell
    "design_supervision_pct": 0.06,
    "mep_special": 330000.0,
    "med_equipment": 1300000.0,   # refurbished 64-slice CT (~120k), 1 C-arm, reagent-rental lab, basic endoscopy tower, leaner instrument sets
    "furniture_it": 160000.0,     # cloud HIS/EMR/PACS (subscription in IT licences)
    "vehicles": 70000.0,          # 2 ambulances (one refurbished)
    "pre_opening": 280000.0,
    "outsourced": 200000.0,       # + housekeeping outsourced
    "it_licences": 50000.0,       # cloud HIS subscription
    "consumables_pct": 0.19,      # +1 point for reagent-rental lab model
    "cash_reserve": 700000.0,
    "t1_amount": 2500000.0,
    "t3_amount": 500000.0,
})

STAFF_COUNT = lambda inp: sum(c for _, c, _ in inp["staff"])


def pmt(rate, n, pv):
    if n <= 0:
        return 0.0
    if rate == 0:
        return pv / n
    return pv * rate / (1 - (1 + rate) ** -n)


def capex(inp):
    land = inp["land_dunum"] * inp["land_price_per_dunum"] * (1 + inp["land_fees_pct"])
    building = inp["gfa_m2"] * inp["build_cost_m2"] + inp["expansion_provision"]
    design = building * inp["design_supervision_pct"]
    up = 1 + inp["no_tax_exemption_uplift"]
    mep = inp["mep_special"] * up
    equip = inp["med_equipment"] * up
    furn = inp["furniture_it"] * up
    veh = inp["vehicles"] * up
    cont = (building + mep + equip) * inp["contingency_pct"]
    cont_build = (building + mep) * inp["contingency_pct"]
    cont_equip = equip * inp["contingency_pct"]
    items = {
        "Land (purchase + registration fees)": land,
        "Building (GFA x cost/m2, incl. expansion provision)": building,
        "Design and supervision": design,
        "Specialised MEP systems": mep,
        "Medical equipment": equip,
        "Furniture and IT (HIS/EMR/PACS)": furn,
        "Ambulances": veh,
        "Contingency": cont,
        "Pre-opening costs": inp["pre_opening"],
    }
    fixed = sum(items.values())
    c1 = land + (building + design + mep + cont_build) * inp["capex_phasing_c1"]
    c2 = fixed - c1
    return {"items": items, "fixed": fixed, "c1": c1, "c2": c2,
            "classes": {"land": land, "building": building + design + cont_build * building / (building + mep),
                        "mep": mep + cont_build * mep / (building + mep), "equipment": equip + cont_equip,
                        "furniture_it": furn, "vehicles": veh, "pre_opening": inp["pre_opening"]}}


DEP_LIFE = {"building": 33, "mep": 10, "equipment": 8, "furniture_it": 5, "vehicles": 7, "pre_opening": 5}


def debt_schedule(amount, rate, grace, repay, draw_year_index):
    """Annual schedule over periods [C2, Y1..Y10] (11 periods). Drawn mid-C2 (half-year interest in C2).
    Grace counts from the draw year: C2 is grace year 1. Returns dict of lists for periods C2..Y10."""
    P = N + 1
    bal_open, interest, principal, bal_close = [0.0] * P, [0.0] * P, [0.0] * P, [0.0] * P
    bal = 0.0
    inst = pmt(rate, repay, amount)
    for p in range(P):
        bal_open[p] = bal
        if p == draw_year_index:
            bal += amount
            interest[p] = amount * rate * 0.5
        else:
            interest[p] = bal * rate
        k = p - draw_year_index - grace   # repayment number (0-based)
        if amount > 0 and 0 <= k < repay and p != draw_year_index:
            principal[p] = inst - interest[p]
        elif amount > 0 and grace == 0 and p == draw_year_index:
            principal[p] = 0.0
        bal -= principal[p]
        bal_close[p] = bal
    return {"open": bal_open, "interest": interest, "principal": principal, "close": bal_close, "installment": inst}


def lease_schedule(amount, rate, repay):
    """Finance lease starting at opening (Y1): annual annuity Y1..Y_repay. Periods C2..Y10."""
    P = N + 1
    inst = pmt(rate, repay, amount)
    bal = 0.0
    out = {"open": [0.0] * P, "interest": [0.0] * P, "principal": [0.0] * P, "close": [0.0] * P, "installment": inst}
    for p in range(P):
        out["open"][p] = bal
        if p == 0:
            bal = amount   # equipment delivered end-C2
        else:
            k = p - 1
            if k < repay:
                out["interest"][p] = bal * rate
                out["principal"][p] = inst - out["interest"][p]
            bal -= out["principal"][p]
        out["close"][p] = bal
    return out


def irr(cfs, lo=-0.99, hi=1.0):
    def npv(r):
        return sum(c / (1 + r) ** i for i, c in enumerate(cfs))
    f_lo, f_hi = npv(lo), npv(hi)
    if f_lo * f_hi > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        f = npv(mid)
        if f_lo * f < 0:
            hi, f_hi = mid, f
        else:
            lo, f_lo = mid, f
    return (lo + hi) / 2


def run(inp):
    cx = capex(inp)
    # ------------- revenue
    vf, pf = inp["volume_factor"], inp["price_factor"]
    rev = {k: [] for k in ["Ward bed-days", "ICU days", "Surgery (hospital fee)", "Day surgery", "Endoscopy", "Implants", "Emergency visits",
                           "CT scans", "Outpatient clinics", "Physiotherapy", "Tourist cases (travel insurance)", "Pharmacy (outpatient)"]}
    vols = {k: [] for k in ["ward_days", "icu_days", "surgeries", "er_visits", "ct", "opd", "physio", "tourists", "day", "endo"]}
    for i in range(N):
        idx = (1 + inp["price_growth"]) ** i * pf
        wd = inp["ward_beds"] * 365 * min(inp["ward_occ"][i] * vf, 0.95)
        idd = inp["icu_beds"] * 365 * min(inp["icu_occ"][i] * vf, 0.95)
        su = inp["surgeries"][i] * vf
        er = inp["er_per_day"][i] * 365 * vf
        ct = inp["ct_scans"][i] * vf
        op = inp["opd_visits"][i] * vf
        ph = inp["physio"][i] * vf
        tu = inp["tourist_cases"][i] * inp["tourist_factor"][i]
        dsu = inp["day_surgeries"][i] * vf
        en = inp["endoscopies"][i] * vf
        for k, v in zip(vols, [wd, idd, su, er, ct, op, ph, tu, dsu, en]):
            vols[k].append(v)
        rev["Ward bed-days"].append(wd * inp["p_ward_day"] * idx)
        rev["ICU days"].append(idd * inp["p_icu_day"] * idx)
        rev["Surgery (hospital fee)"].append(su * inp["p_surgery"] * idx)
        rev["Day surgery"].append(dsu * inp["p_day_surgery"] * idx)
        rev["Endoscopy"].append(en * inp["p_endoscopy"] * idx)
        rev["Implants"].append((su * inp["p_implant"] + dsu * inp["p_day_implant"]) * idx)
        rev["Emergency visits"].append(er * inp["p_er"] * idx)
        rev["CT scans"].append(ct * inp["p_ct"] * idx)
        rev["Outpatient clinics"].append(op * inp["p_opd"] * idx)
        rev["Physiotherapy"].append(ph * inp["p_physio"] * idx)
        rev["Tourist cases (travel insurance)"].append(tu * inp["p_tourist"] * idx)
        rev["Pharmacy (outpatient)"].append(inp["pharmacy_pct"] * (rev["Emergency visits"][i] + rev["Outpatient clinics"][i]))
    gross = [sum(rev[k][i] for k in rev) for i in range(N)]
    discounts = [g * inp["discount_pct"] for g in gross]
    net = [g - d for g, d in zip(gross, discounts)]
    implants_net = [rev["Implants"][i] * (1 - inp["discount_pct"]) for i in range(N)]
    # ------------- opex
    base_payroll = sum(c * w for _, c, w in inp["staff"]) * 12 * (1 + inp["oncost_pct"])
    of = inp["opex_factor"]
    opex = {k: [] for k in ["Payroll", "Drugs and consumables", "Implants cost", "Doctor incentives", "Radiology reading",
                            "Utilities", "Outsourced services", "Insurance and malpractice", "Marketing and contracts",
                            "IT licences", "General and admin", "Licence fees", "Maintenance", "Bad debts"]}
    for i in range(N):
        ci = (1 + inp["cost_growth"]) ** i
        wi = (1 + inp["wage_growth"]) ** i
        opex["Payroll"].append(base_payroll * inp["staffing_factor"][i] * wi)
        opex["Drugs and consumables"].append((net[i] - implants_net[i]) * inp["consumables_pct"])
        opex["Implants cost"].append(rev["Implants"][i] * inp["implant_cost_pct"])
        opex["Doctor incentives"].append((rev["Surgery (hospital fee)"][i] + rev["Day surgery"][i] + rev["Endoscopy"][i] + rev["Emergency visits"][i]) * inp["doctor_incentive_pct"])
        opex["Radiology reading"].append(vols["ct"][i] * inp["radiology_read_fee"] * ci)
        opex["Utilities"].append(inp["utilities"] * ci * of)
        opex["Outsourced services"].append(inp["outsourced"] * ci * of)
        opex["Insurance and malpractice"].append(inp["insurance_malpractice"] * ci * of)
        opex["Marketing and contracts"].append(inp["marketing_contracts"][i] * ci * of)
        opex["IT licences"].append(inp["it_licences"] * ci * of)
        opex["General and admin"].append((inp["general_admin"] + inp["ground_rent"]) * ci * of)
        opex["Licence fees"].append(inp["licence_fees"] * ci * of)
        opex["Maintenance"].append((cx["classes"]["equipment"] * inp["maint_equip_pct"][i]
                                    + cx["classes"]["building"] * inp["maint_building_pct"]) * ci * of)
        opex["Bad debts"].append(net[i] * inp["bad_debt_pct"])
    total_opex = [sum(opex[k][i] for k in opex) for i in range(N)]
    ebitda = [net[i] - total_opex[i] for i in range(N)]
    # ------------- depreciation and maintenance capex
    maint_capex = [0.0 if i < 2 else net[i] * inp["maint_capex_pct"] for i in range(N)]
    dep = []
    for i in range(N):
        d = sum(cx["classes"][k] / DEP_LIFE[k] for k in DEP_LIFE if i < DEP_LIFE[k])
        d += sum(maint_capex[j] / 8 for j in range(i) if i - j <= 8)   # from year after spend
        dep.append(d)
    # ------------- debt
    t1 = debt_schedule(inp["t1_amount"], inp["t1_rate"], inp["t1_grace"], inp["t1_repay"], 0)
    t2 = debt_schedule(inp["t2_amount"], inp["t2_rate"], inp["t2_grace"], inp["t2_repay"], 0)
    t3 = lease_schedule(inp["t3_amount"], inp["t3_rate"], inp["t3_repay"])
    debt_total = inp["t1_amount"] + inp["t2_amount"] + inp["t3_amount"]
    idc = t1["interest"][0] + t2["interest"][0]
    fees = (inp["t1_amount"] + inp["t2_amount"]) * inp["arrangement_fee_pct"]
    total_uses = cx["fixed"] + idc + fees + inp["cash_reserve"]
    equity = total_uses - debt_total - inp["grant"]
    interest = [t1["interest"][p] + t2["interest"][p] + t3["interest"][p] for p in range(1, N + 1)]
    principal = [t1["principal"][p] + t2["principal"][p] + t3["principal"][p] for p in range(1, N + 1)]
    debt_service = [interest[i] + principal[i] for i in range(N)]
    # ------------- tax
    pbt = [ebitda[i] - dep[i] - interest[i] for i in range(N)]
    tax, loss_cf = [], 0.0
    for i in range(N):
        taxable = pbt[i] + loss_cf
        if taxable < 0:
            loss_cf, t = taxable, 0.0
        else:
            loss_cf = 0.0
            rate = inp["tax_rate"] * ((1 - inp["tax_relief_pct"]) if i < inp["tax_relief_years"] else 1.0)
            t = taxable * rate
        tax.append(t)
    net_income = [pbt[i] - tax[i] for i in range(N)]
    # ------------- working capital
    ar = [net[i] * inp["dso_days"] / 365 for i in range(N)]
    inv = [(opex["Drugs and consumables"][i] + opex["Implants cost"][i]) * inp["inventory_days"] / 365 for i in range(N)]
    ap = [(total_opex[i] - opex["Payroll"][i] - opex["Bad debts"][i] - opex["Doctor incentives"][i]) * inp["payables_days"] / 365 for i in range(N)]
    nwc = [ar[i] + inv[i] - ap[i] for i in range(N)]
    d_nwc = [nwc[i] - (nwc[i - 1] if i else 0.0) for i in range(N)]
    # ------------- cash flow
    cfads = [ebitda[i] - tax[i] - d_nwc[i] - maint_capex[i] for i in range(N)]
    dscr = [cfads[i] / debt_service[i] if debt_service[i] > 1 else None for i in range(N)]
    equity_cf_ops = [cfads[i] - debt_service[i] for i in range(N)]
    cash, bal = [], inp["cash_reserve"]
    for i in range(N):
        bal += equity_cf_ops[i]
        cash.append(bal)
    # ------------- valuation (project, unlevered)
    unlev_tax = []
    for i in range(N):
        e = ebitda[i] - dep[i]
        r = inp["tax_rate"] * ((1 - inp["tax_relief_pct"]) if i < inp["tax_relief_years"] else 1.0)
        unlev_tax.append(max(e, 0) * r)
    fcf = [ebitda[i] - unlev_tax[i] - d_nwc[i] - maint_capex[i] for i in range(N)]
    r, g = inp["discount_rate"], inp["terminal_growth"]
    tv = fcf[-1] * (1 + g) / (r - g)
    proj = [-cx["c1"], -(cx["c2"])] + fcf
    proj_tv = proj[:-1] + [proj[-1] + tv]
    npv = lambda cfs: sum(c / (1 + r) ** t for t, c in enumerate(cfs))
    debt_end = t1["close"][-1] + t2["close"][-1] + t3["close"][-1]
    eq_c1 = min(equity, cx["c1"])
    eq_c2 = equity - eq_c1
    eq_flows = [-eq_c1, -eq_c2] + equity_cf_ops
    eq_flows_tv = eq_flows[:-1] + [eq_flows[-1] + tv - debt_end + inp["cash_reserve"]]   # exit: TV less remaining debt plus reserve returned
    # cumulative payback (project, from start of construction)
    cum, payback = 0.0, None
    for t, c in enumerate(proj):
        prev = cum
        cum += c
        if payback is None and cum >= 0 and t > 0:
            payback = (t - 1) + (-prev / c if c else 0) - 2 + 1   # years after opening
    stab = 5  # Y6 index for "stabilised"
    res = {
        "capex": cx, "idc": idc, "fees": fees, "total_uses": total_uses, "equity": equity, "debt_total": debt_total,
        "equity_share": equity / total_uses, "revenue_lines": rev, "volumes": vols, "gross": gross, "discounts": discounts,
        "net_revenue": net, "opex_lines": opex, "total_opex": total_opex, "ebitda": ebitda,
        "ebitda_margin": [ebitda[i] / net[i] for i in range(N)], "dep": dep, "interest": interest, "pbt": pbt, "tax": tax,
        "net_income": net_income, "ar": ar, "inv": inv, "ap": ap, "nwc": nwc, "d_nwc": d_nwc, "maint_capex": maint_capex,
        "cfads": cfads, "principal": principal, "debt_service": debt_service, "dscr": dscr, "cash": cash,
        "min_cash": min(cash), "min_cash_year": YEARS[cash.index(min(cash))],
        "fcf": fcf, "tv": tv, "npv_no_tv": npv(proj), "npv_tv": npv(proj_tv), "irr_no_tv": irr(proj), "irr_tv": irr(proj_tv),
        "equity_irr_tv": irr(eq_flows_tv), "debt_end": debt_end, "payback_after_opening": payback,
        "t1": t1, "t2": t2, "t3": t3, "base_payroll_full": base_payroll, "staff_count": STAFF_COUNT(inp),
        "min_dscr": min(dscr[i] for i in range(N) if principal[i] > 1),
        "min_dscr_year": min((dscr[i], YEARS[i]) for i in range(N) if principal[i] > 1)[1],
        "funding_gap": max(0.0, -min(cash)),
        "first_dscr_above_125": next((YEARS[i] for i in range(N) if dscr[i] is not None and dscr[i] >= 1.25), None),
        "dscr_y4": dscr[3], "dscr_y6": dscr[stab], "avg_dscr_repay": sum(d for d in dscr[1:9] if d) / len([d for d in dscr[1:9] if d]),
        "breakeven_ebitda_year": next((YEARS[i] for i in range(N) if ebitda[i] > 0), None),
    }
    return res


# ------------------------------------------------------------------ scenarios and structures
def variant(**kw):
    v = copy.deepcopy(BASE)
    for k, val in kw.items():
        v[k] = val
    return v


def equity_fill(inp):
    return inp


def general40():
    """Rough fallback if MoH classifies a multi-department hospital as GENERAL (min 40 beds incl. surgery,
    OB/GYN, internal medicine, paediatrics). Scales beds, space, equipment and staff [ASSUMPTION]."""
    v = variant(ward_beds=36, icu_beds=4, gfa_m2=5200.0, mep_special=560000.0, med_equipment=2250000.0,
                furniture_it=280000.0, pre_opening=400000.0, land_dunum=5.0, utilities=210000.0, outsourced=240000.0,
                insurance_malpractice=60000.0, general_admin=95000.0, licence_fees=22000.0,
                ward_occ=[0.30, 0.40, 0.48, 0.55, 0.58, 0.60, 0.60, 0.60, 0.60, 0.60],
                opd_visits=[x * 1.4 for x in BASE["opd_visits"]], er_per_day=[x * 1.1 for x in BASE["er_per_day"]])
    extra = [("Internists", 2, 3000), ("Obstetrician-gynaecologist (resident)", 1, 3500), ("Midwives", 6, 700),
             ("Additional staff nurses", 18, 700), ("Additional GPs", 3, 1100), ("Additional support staff", 8, 420)]
    v["staff"] = [x for x in BASE["staff"] if not x[0].startswith("Internist")] + extra
    v["deliveries_note"] = "Deliveries revenue not modelled (conservative)"
    return v


SCENARIOS = {
    "Base": variant(),
    "Prudent (volumes -20%, prices -5%, DSO 150)": variant(volume_factor=0.80, price_factor=0.95, dso_days=150),
    "Optimistic (volumes +15%)": variant(volume_factor=1.15),
    "Tourism shock (tourists -80% Y1-Y2, ER -10%)": variant(tourist_factor=[0.2, 0.2] + [1.0] * 8,
                                                         er_per_day=[x * 0.9 for x in BASE["er_per_day"]]),
    "No customs/sales-tax exemption (+16% on equipment and MEP)": variant(no_tax_exemption_uplift=0.16),
    "Construction 780/m2 (+30% on lean 600)": variant(build_cost_m2=780.0),
    "Payroll +15%": variant(staff=[(r, c, w * 1.15) for r, c, w in BASE["staff"]]),
    "MoH/RMS purchasing contract (+15% inpatient and surgery, DSO 150)": variant(
        ward_occ=[min(x * 1.15, 0.9) for x in BASE["ward_occ"]], icu_occ=[min(x * 1.15, 0.9) for x in BASE["icu_occ"]],
        surgeries=[x * 1.15 for x in BASE["surgeries"]], dso_days=150),
    "Conditions met: contracted volumes +20%": variant(volume_factor=1.20),
    "If MoH requires a general hospital (40 beds, internal medicine + obstetrics)": general40(),
}

OPTIONS = {
    "A. Lean expandable Phase 1 (recommended base)": variant(),
    "B. Standard build, land purchased (previous version)": copy.deepcopy(STANDARD),
    "C. Lean Phase 1 + land bought instead of leased": variant(land_price_per_dunum=60000.0, land_fees_pct=0.09, ground_rent=0.0),
    "D. Lean Phase 1 without expansion provision": variant(expansion_provision=0.0),
}

STRUCTURES = {
    "F1 CBJ 2.5m + equipment lease 0.5m + equity": variant(),
    "F2 CBJ 2.5m + Islamic ijara 1.2m + lease 0.5m + equity": variant(t2_amount=1200000.0),
    "F3 Commercial loan only 3.6m at 8.5% (no CBJ)": variant(t1_amount=0.0, t2_amount=3600000.0, t2_rate=0.085, t3_amount=0.0),
    "F4 Doctor-investor company: CBJ 2.0m + lease 0.5m, more equity from 10-15 doctors": variant(t1_amount=2000000.0),
}

SENS = [  # (label, key, low, high) one-at-a-time on base
    ("Volumes", "volume_factor", 0.85, 1.15),
    ("Prices", "price_factor", 0.90, 1.10),
    ("Build cost/m2", "build_cost_m2", 550.0, 900.0),
    ("Consumables % of revenue", "consumables_pct", 0.15, 0.22),
    ("DSO days", "dso_days", 75, 180),
]


def scal(r):
    return {
        "total_uses": r["total_uses"], "equity": r["equity"], "equity_share": r["equity_share"], "debt": r["debt_total"],
        "net_rev_y1": r["net_revenue"][0], "net_rev_y6": r["net_revenue"][5], "ebitda_y1": r["ebitda"][0],
        "ebitda_y6": r["ebitda"][5], "ebitda_margin_y6": r["ebitda_margin"][5], "min_dscr": r["min_dscr"],
        "min_dscr_year": r["min_dscr_year"], "dscr_y6": r["dscr_y6"], "min_cash": r["min_cash"], "min_cash_year": r["min_cash_year"],
        "npv_no_tv": r["npv_no_tv"], "npv_tv": r["npv_tv"], "irr_no_tv": r["irr_no_tv"], "irr_tv": r["irr_tv"],
        "equity_irr_tv": r["equity_irr_tv"], "funding_gap": r["funding_gap"],
        "fully_funded_uses": r["total_uses"] + r["funding_gap"], "first_dscr_above_125": r["first_dscr_above_125"],
        "dscr_y1": r["dscr"][0], "dscr_y2": r["dscr"][1], "dscr_y3": r["dscr"][2], "dscr_y4": r["dscr"][3],
    }


def f0(x):
    return "n/a" if x is None else f"{x:,.0f}"


def pc(x):
    return "n/a" if x is None else f"{x * 100:.1f}%"


def f2(x):
    return "n/a" if x is None else f"{x:.2f}"


# ------------------------------------------------------------------ outputs
def write_tables(base, scen, struct, sens):
    L = []
    L.append("# Petra Trauma Centre: model tables (generated by ptc_model.py)\n")
    L.append("## Uses and sources (Base, F1)\n")
    L.append("| Item | JOD |\n|---|---:|")
    for k, v in base["capex"]["items"].items():
        L.append(f"| {k} | {f0(v)} |")
    L.append(f"| Interest during construction | {f0(base['idc'])} |")
    L.append(f"| Arrangement fees | {f0(base['fees'])} |")
    L.append(f"| Ramp-up and debt-service cash reserve | {f0(BASE['cash_reserve'])} |")
    L.append(f"| **Total uses** | **{f0(base['total_uses'])}** |")
    L.append(f"| CBJ programme loan (T1) | {f0(BASE['t1_amount'])} |")
    L.append(f"| Equipment finance lease (T3) | {f0(BASE['t3_amount'])} |")
    L.append(f"| Owner equity | {f0(base['equity'])} ({pc(base['equity_share'])}) |\n")
    L.append("## Income statement and cash flow (Base, F1)\n")
    L.append("| JOD | " + " | ".join(str(y) for y in YEARS) + " |")
    L.append("|---|" + "---:|" * N)
    rows = [("Net revenue", base["net_revenue"]), ("Total opex", base["total_opex"]), ("EBITDA", base["ebitda"]),
            ("EBITDA margin", base["ebitda_margin"]), ("Depreciation", base["dep"]), ("Interest", base["interest"]),
            ("Tax", base["tax"]), ("Net income", base["net_income"]), ("Change in working capital", base["d_nwc"]),
            ("Maintenance capex", base["maint_capex"]), ("CFADS", base["cfads"]), ("Debt service", base["debt_service"]),
            ("DSCR", base["dscr"]), ("Closing cash", base["cash"])]
    for name, vals in rows:
        if name in ("EBITDA margin",):
            L.append(f"| {name} | " + " | ".join(pc(v) for v in vals) + " |")
        elif name == "DSCR":
            L.append(f"| {name} | " + " | ".join(f2(v) for v in vals) + " |")
        else:
            L.append(f"| {name} | " + " | ".join(f0(v) for v in vals) + " |")
    L.append("\n## Revenue by service line (Base)\n")
    L.append("| JOD | " + " | ".join(str(y) for y in YEARS) + " |")
    L.append("|---|" + "---:|" * N)
    for k, v in base["revenue_lines"].items():
        L.append(f"| {k} | " + " | ".join(f0(x) for x in v) + " |")
    L.append("\n## Scenarios\n")
    L.append("| Scenario | Net rev Y6 | EBITDA Y6 | Margin Y6 | Min DSCR (year) | DSCR Y6 | Min cash (year) | Extra cash needed | NPV 10% no TV | NPV with TV | Project IRR with TV | Equity IRR with TV |")
    L.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for k, s in scen.items():
        L.append(f"| {k} | {f0(s['net_rev_y6'])} | {f0(s['ebitda_y6'])} | {pc(s['ebitda_margin_y6'])} | {f2(s['min_dscr'])} ({s['min_dscr_year']}) | {f2(s['dscr_y6'])} | {f0(s['min_cash'])} ({s['min_cash_year']}) | {f0(s['funding_gap'])} | {f0(s['npv_no_tv'])} | {f0(s['npv_tv'])} | {pc(s['irr_tv'])} | {pc(s['equity_irr_tv'])} |")
    L.append("\n## Funding structures\n")
    L.append("| Structure | Debt | Equity | Equity % | Min DSCR (year) | DSCR Y6 | Min cash (year) | Extra cash needed | Equity IRR with TV |")
    L.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for k, s in struct.items():
        L.append(f"| {k} | {f0(s['debt'])} | {f0(s['equity'])} | {pc(s['equity_share'])} | {f2(s['min_dscr'])} ({s['min_dscr_year']}) | {f2(s['dscr_y6'])} | {f0(s['min_cash'])} ({s['min_cash_year']}) | {f0(s['funding_gap'])} | {pc(s['equity_irr_tv'])} |")
    L.append("\n## Sensitivity (one at a time, Base)\n")
    L.append("| Driver | Low | High | NPV with TV (low) | NPV with TV (high) | DSCR Y6 (low) | DSCR Y6 (high) |")
    L.append("|---|---:|---:|---:|---:|---:|---:|")
    for lab, lo, hi, rlo, rhi in sens:
        L.append(f"| {lab} | {lo} | {hi} | {f0(rlo['npv_tv'])} | {f0(rhi['npv_tv'])} | {f2(rlo['dscr_y6'])} | {f2(rhi['dscr_y6'])} |")
    L.append("\n## Staffing at full complement\n")
    L.append("| Role | Count | Monthly gross JOD |\n|---|---:|---:|")
    for r_, c, w in BASE["staff"]:
        L.append(f"| {r_} | {c} | {f0(w)} |")
    L.append(f"| **Total** | **{base['staff_count']}** | annual cost with on-costs {f0(base['base_payroll_full'])} |")
    with open(os.path.join(HERE, "tables.md"), "w") as f:
        f.write("\n".join(L) + "\n")


def write_excel(inp, base):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter as CL

    wb = Workbook()
    bold = Font(bold=True)
    blue = Font(color="0000CC")
    hdr = PatternFill("solid", fgColor="DDEBF7")
    num = '#,##0;[Red]-#,##0'

    # ---------------- Inputs (scalars)
    ws = wb.active
    ws.title = "Inputs"
    ws["A1"] = "Petra Trauma Centre - inputs (blue = editable). JOD. Tags: see report."
    ws["A1"].font = bold
    scal_keys = ["ward_beds", "icu_beds", "p_ward_day", "p_icu_day", "p_surgery", "p_implant", "p_day_surgery", "p_day_implant", "p_endoscopy", "p_er", "p_ct", "p_opd",
                 "p_physio", "p_tourist", "pharmacy_pct", "price_growth", "discount_pct", "bad_debt_pct", "volume_factor",
                 "price_factor", "oncost_pct", "wage_growth", "consumables_pct", "implant_cost_pct", "doctor_incentive_pct",
                 "radiology_read_fee", "utilities", "outsourced", "insurance_malpractice", "it_licences", "general_admin", "ground_rent",
                 "licence_fees", "maint_building_pct", "cost_growth", "maint_capex_pct", "dso_days", "inventory_days",
                 "payables_days", "tax_rate", "tax_relief_pct", "tax_relief_years", "discount_rate", "terminal_growth",
                 "t1_amount", "t1_rate", "t1_grace", "t1_repay", "t2_amount", "t2_rate", "t2_grace", "t2_repay",
                 "t3_amount", "t3_rate", "t3_repay", "cash_reserve", "arrangement_fee_pct"]
    ref = {}
    for i, k in enumerate(scal_keys, start=3):
        ws.cell(i, 1, k)
        c = ws.cell(i, 2, inp[k])
        c.font = blue
        ref[k] = f"Inputs!$B${i}"
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 14

    # ---------------- Capex
    wc = wb.create_sheet("Capex")
    wc["A1"] = "Capital cost (values from model; edit in ptc_model.py or here)"
    wc["A1"].font = bold
    r0 = 3
    for j, (k, v) in enumerate(base["capex"]["items"].items()):
        wc.cell(r0 + j, 1, k)
        wc.cell(r0 + j, 2, round(v, 2)).number_format = num
    rt = r0 + len(base["capex"]["items"])
    wc.cell(rt, 1, "Fixed capex total").font = bold
    wc.cell(rt, 2, f"=SUM(B{r0}:B{rt - 1})").number_format = num
    wc.cell(rt + 1, 1, "Interest during construction")
    wc.cell(rt + 1, 2, "=Debt!B6+Debt!B14").number_format = num
    wc.cell(rt + 2, 1, "Arrangement fees")
    wc.cell(rt + 2, 2, f"=({ref['t1_amount']}+{ref['t2_amount']})*{ref['arrangement_fee_pct']}").number_format = num
    wc.cell(rt + 3, 1, "Cash reserve")
    wc.cell(rt + 3, 2, f"={ref['cash_reserve']}").number_format = num
    wc.cell(rt + 4, 1, "TOTAL USES").font = bold
    wc.cell(rt + 4, 2, f"=SUM(B{rt}:B{rt + 3})").number_format = num
    wc.cell(rt + 5, 1, "Debt (T1+T2+T3)")
    wc.cell(rt + 5, 2, f"={ref['t1_amount']}+{ref['t2_amount']}+{ref['t3_amount']}").number_format = num
    wc.cell(rt + 6, 1, "Owner equity").font = bold
    wc.cell(rt + 6, 2, f"=B{rt + 4}-B{rt + 5}").number_format = num
    wc.cell(rt + 7, 1, "Equity share")
    wc.cell(rt + 7, 2, f"=B{rt + 6}/B{rt + 4}").number_format = "0.0%"
    wc.cell(rt + 9, 1, "Depreciable classes")
    wc.cell(rt + 9, 3, "Life (years)")
    cls_row = {}
    for j, k in enumerate(DEP_LIFE):
        rr = rt + 10 + j
        wc.cell(rr, 1, k)
        wc.cell(rr, 2, round(base["capex"]["classes"][k], 2)).number_format = num
        wc.cell(rr, 3, DEP_LIFE[k])
        cls_row[k] = rr
    wc.column_dimensions["A"].width = 40
    wc.column_dimensions["B"].width = 16
    equip_ref = f"Capex!$B${cls_row['equipment']}"
    build_ref = f"Capex!$B${cls_row['building']}"
    uses_ref = f"Capex!$B${rt + 4}"
    equity_ref = f"Capex!$B${rt + 6}"
    c1_val, c2_val = base["capex"]["c1"], base["capex"]["c2"]

    # ---------------- Drivers (per year)
    wd = wb.create_sheet("Drivers")
    wd["A1"] = "Annual drivers (blue = editable)"
    wd["A1"].font = bold
    wd.cell(2, 1, "Year")
    for i, y in enumerate(YEARS):
        wd.cell(2, 2 + i, y).font = bold
    drv = [("ward_occ", inp["ward_occ"]), ("icu_occ", inp["icu_occ"]), ("surgeries", inp["surgeries"]), ("day_surgeries", inp["day_surgeries"]), ("endoscopies", inp["endoscopies"]),
           ("er_per_day", inp["er_per_day"]), ("ct_scans", inp["ct_scans"]), ("opd_visits", inp["opd_visits"]),
           ("physio", inp["physio"]), ("tourist_cases", [inp["tourist_cases"][i] * inp["tourist_factor"][i] for i in range(N)]),
           ("staffing_factor", inp["staffing_factor"]), ("marketing_contracts", inp["marketing_contracts"]),
           ("maint_equip_pct", inp["maint_equip_pct"]), ("op_year_index", list(range(N)))]
    dref = {}
    for j, (k, vals) in enumerate(drv, start=3):
        wd.cell(j, 1, k)
        for i, v in enumerate(vals):
            wd.cell(j, 2 + i, v).font = blue
        dref[k] = j
    wd.cell(18, 1, "Full-staff payroll incl. on-costs (2029)")
    wd.cell(18, 2, f"={sum(c * w for _, c, w in inp['staff']) * 12}*(1+{ref['oncost_pct']})").number_format = num
    wd.column_dimensions["A"].width = 36

    def D(k, i):
        return f"Drivers!{CL(2 + i)}${dref[k]}"

    # ---------------- PnL
    wp = wb.create_sheet("PnL")
    wp["A1"] = "Income statement, JOD (live formulas)"
    wp["A1"].font = bold
    wp.cell(2, 1, "Year")
    for i, y in enumerate(YEARS):
        wp.cell(2, 2 + i, y).font = bold
    lines = []

    def add(label, fn, fmt=num, b=False):
        rr = 3 + len(lines)
        wp.cell(rr, 1, label)
        if b:
            wp.cell(rr, 1).font = bold
        for i in range(N):
            c = wp.cell(rr, 2 + i, fn(i, CL(2 + i)))
            c.number_format = fmt
        lines.append(label)
        return rr

    IDX = lambda i: f"(1+{ref['price_growth']})^{D('op_year_index', i)}*{ref['price_factor']}"
    VF = ref["volume_factor"]
    r_ward = add("Ward bed-days revenue", lambda i, c: f"={ref['ward_beds']}*365*MIN({D('ward_occ', i)}*{VF},0.95)*{ref['p_ward_day']}*{IDX(i)}")
    r_icu = add("ICU days revenue", lambda i, c: f"={ref['icu_beds']}*365*MIN({D('icu_occ', i)}*{VF},0.95)*{ref['p_icu_day']}*{IDX(i)}")
    r_sur = add("Surgery (hospital fee)", lambda i, c: f"={D('surgeries', i)}*{VF}*{ref['p_surgery']}*{IDX(i)}")
    r_day = add("Day surgery", lambda i, c: f"={D('day_surgeries', i)}*{VF}*{ref['p_day_surgery']}*{IDX(i)}")
    r_end = add("Endoscopy", lambda i, c: f"={D('endoscopies', i)}*{VF}*{ref['p_endoscopy']}*{IDX(i)}")
    r_imp = add("Implants", lambda i, c: f"=({D('surgeries', i)}*{ref['p_implant']}+{D('day_surgeries', i)}*{ref['p_day_implant']})*{VF}*{IDX(i)}")
    r_er = add("Emergency visits", lambda i, c: f"={D('er_per_day', i)}*365*{VF}*{ref['p_er']}*{IDX(i)}")
    r_ct = add("CT scans", lambda i, c: f"={D('ct_scans', i)}*{VF}*{ref['p_ct']}*{IDX(i)}")
    r_opd = add("Outpatient clinics", lambda i, c: f"={D('opd_visits', i)}*{VF}*{ref['p_opd']}*{IDX(i)}")
    r_ph = add("Physiotherapy", lambda i, c: f"={D('physio', i)}*{VF}*{ref['p_physio']}*{IDX(i)}")
    r_tu = add("Tourist cases", lambda i, c: f"={D('tourist_cases', i)}*{ref['p_tourist']}*{IDX(i)}")
    r_pha = add("Pharmacy (outpatient)", lambda i, c: f"={ref['pharmacy_pct']}*({c}{r_er}+{c}{r_opd})")
    r_gross = add("Gross revenue", lambda i, c: f"=SUM({c}{r_ward}:{c}{r_pha})", b=True)
    r_disc = add("Insurer discounts and denials", lambda i, c: f"=-{c}{r_gross}*{ref['discount_pct']}")
    r_net = add("NET REVENUE", lambda i, c: f"={c}{r_gross}+{c}{r_disc}", b=True)
    CI = lambda i: f"(1+{ref['cost_growth']})^{D('op_year_index', i)}"
    r_pay = add("Payroll", lambda i, c: f"=Drivers!$B$18*{D('staffing_factor', i)}*(1+{ref['wage_growth']})^{D('op_year_index', i)}")
    r_con = add("Drugs and consumables", lambda i, c: f"=({c}{r_net}-{c}{r_imp}*(1-{ref['discount_pct']}))*{ref['consumables_pct']}")
    r_ic = add("Implants cost", lambda i, c: f"={c}{r_imp}*{ref['implant_cost_pct']}")
    r_inc = add("Doctor incentives", lambda i, c: f"=({c}{r_sur}+{c}{r_day}+{c}{r_end}+{c}{r_er})*{ref['doctor_incentive_pct']}")
    r_rad = add("Radiology reading", lambda i, c: f"={D('ct_scans', i)}*{VF}*{ref['radiology_read_fee']}*{CI(i)}")
    r_ut = add("Utilities", lambda i, c: f"={ref['utilities']}*{CI(i)}")
    r_out = add("Outsourced services", lambda i, c: f"={ref['outsourced']}*{CI(i)}")
    r_ins = add("Insurance and malpractice", lambda i, c: f"={ref['insurance_malpractice']}*{CI(i)}")
    r_mk = add("Marketing and contracts", lambda i, c: f"={D('marketing_contracts', i)}*{CI(i)}")
    r_it = add("IT licences", lambda i, c: f"={ref['it_licences']}*{CI(i)}")
    r_ga = add("General and admin", lambda i, c: f"=({ref['general_admin']}+{ref['ground_rent']})*{CI(i)}")
    r_lf = add("Licence fees", lambda i, c: f"={ref['licence_fees']}*{CI(i)}")
    r_mt = add("Maintenance", lambda i, c: f"=({equip_ref}*{D('maint_equip_pct', i)}+{build_ref}*{ref['maint_building_pct']})*{CI(i)}")
    r_bd = add("Bad debts", lambda i, c: f"={c}{r_net}*{ref['bad_debt_pct']}")
    r_opx = add("TOTAL OPEX", lambda i, c: f"=SUM({c}{r_pay}:{c}{r_bd})", b=True)
    r_ebitda = add("EBITDA", lambda i, c: f"={c}{r_net}-{c}{r_opx}", b=True)
    r_mrg = add("EBITDA margin", lambda i, c: f"={c}{r_ebitda}/{c}{r_net}", fmt="0.0%")
    r_mcx = add("Maintenance capex", lambda i, c: "=0" if i < 2 else f"={c}{r_net}*{ref['maint_capex_pct']}")

    def dep_formula(i, c):
        parts = [f"IF({i}<Capex!$C${cls_row[k]},Capex!$B${cls_row[k]}/Capex!$C${cls_row[k]},0)" for k in DEP_LIFE]
        if i > 0:
            lo = max(0, i - 8)
            parts.append(f"SUM({CL(2 + lo)}{r_mcx}:{CL(2 + i - 1)}{r_mcx})/8")
        return "=" + "+".join(parts)
    r_dep = add("Depreciation and amortisation", dep_formula)
    r_int = add("Interest", lambda i, c: f"=Debt!{CL(3 + i)}6+Debt!{CL(3 + i)}14+Debt!{CL(3 + i)}22")
    r_pbt = add("Profit before tax", lambda i, c: f"={c}{r_ebitda}-{c}{r_dep}-{c}{r_int}", b=True)

    def lcf(i, c):   # loss carried forward into this year (<=0)
        if i == 0:
            return "=0"
        p = CL(1 + i)
        return f"=MIN({p}{r_pbt}+{p}{r_pbt + 1},0)"
    r_lcf = add("Loss brought forward", lcf)
    r_tax = add("Income tax", lambda i, c: f"=MAX({c}{r_pbt}+{c}{r_lcf},0)*{ref['tax_rate']}*IF({D('op_year_index', i)}<{ref['tax_relief_years']},1-{ref['tax_relief_pct']},1)")
    r_ni = add("NET INCOME", lambda i, c: f"={c}{r_pbt}-{c}{r_tax}", b=True)
    wp.column_dimensions["A"].width = 34
    for i in range(N):
        wp.column_dimensions[CL(2 + i)].width = 13

    # ---------------- Debt (columns: B = C2 2028, C..L = 2029..2038)
    wdb = wb.create_sheet("Debt")
    wdb["A1"] = "Debt schedules (annual; T1/T2 drawn mid-2028, grace from draw year; T3 lease from 2029)"
    wdb["A1"].font = bold
    periods = [2028] + YEARS

    def tranche(top, label, amt, rate, grace, repay, lease=False):
        wdb.cell(top, 1, label).font = bold
        for p, y in enumerate(periods):
            wdb.cell(top, 2 + p, y).font = bold
        names = ["Opening balance", "Drawdown", "Installment", "Interest", "Principal", "Closing balance"]
        for j, n_ in enumerate(names):
            wdb.cell(top + 1 + j, 1, n_)
        for p in range(len(periods)):
            c = CL(2 + p)
            prv = CL(1 + p)
            o, dr, ins, it, pr, cl = (f"{c}{top + k}" for k in range(1, 7))
            wdb[o] = "=0" if p == 0 else f"={prv}{top + 6}"
            if lease:
                wdb[dr] = f"={amt}" if p == 0 else "=0"
                wdb[ins] = "=0" if p == 0 else f"=IF({p}<={repay},PMT({rate},{repay},-{amt}),0)"
                wdb[it] = "=0" if p == 0 else f"=IF({p}<={repay},{o}*{rate},0)"
            else:
                wdb[dr] = f"={amt}" if p == 0 else "=0"
                wdb[ins] = "=0" if p == 0 else f"=IF(AND({p}>={grace},{p}<{grace}+{repay}),PMT({rate},{repay},-{amt}),0)"
                wdb[it] = f"={dr}*{rate}*0.5" if p == 0 else f"={o}*{rate}"
            wdb[pr] = f"=IF({ins}>0,{ins}-{it},0)"
            wdb[cl] = f"={o}+{dr}-{pr}"
            for cell in (o, dr, ins, it, pr, cl):
                wdb[cell].number_format = num
    # rows: T1 top=1 -> interest at row 1+4=5? set tops so interest rows are 6, 14, 22
    tranche(2, "T1 CBJ economic-sectors programme", ref["t1_amount"], ref["t1_rate"], ref["t1_grace"], ref["t1_repay"])
    tranche(10, "T2 Islamic / commercial", ref["t2_amount"], ref["t2_rate"], ref["t2_grace"], ref["t2_repay"])
    tranche(18, "T3 Equipment finance lease", ref["t3_amount"], ref["t3_rate"], 0, ref["t3_repay"], lease=True)
    wdb.column_dimensions["A"].width = 34

    # ---------------- CashFlow
    wcf = wb.create_sheet("CashFlow")
    wcf["A1"] = "Cash flow, DSCR and valuation (live formulas)"
    wcf["A1"].font = bold
    wcf.cell(2, 1, "Year")
    for i, y in enumerate(YEARS):
        wcf.cell(2, 2 + i, y).font = bold
    cl_ = []

    def addc(label, fn, fmt=num, b=False):
        rr = 3 + len(cl_)
        wcf.cell(rr, 1, label)
        if b:
            wcf.cell(rr, 1).font = bold
        for i in range(N):
            wcf.cell(rr, 2 + i, fn(i, CL(2 + i))).number_format = fmt
        cl_.append(label)
        return rr
    P = lambda r: (lambda i, c: f"=PnL!{c}{r}")
    c_e = addc("EBITDA", P(r_ebitda))
    c_t = addc("Tax", P(r_tax))
    c_ar = addc("Receivables", lambda i, c: f"=PnL!{c}{r_net}*{ref['dso_days']}/365")
    c_inv = addc("Inventory", lambda i, c: f"=(PnL!{c}{r_con}+PnL!{c}{r_ic})*{ref['inventory_days']}/365")
    c_ap = addc("Payables", lambda i, c: f"=(PnL!{c}{r_opx}-PnL!{c}{r_pay}-PnL!{c}{r_bd}-PnL!{c}{r_inc})*{ref['payables_days']}/365")
    c_nwc = addc("Net working capital", lambda i, c: f"={c}{c_ar}+{c}{c_inv}-{c}{c_ap}")
    c_dn = addc("Change in working capital", lambda i, c: f"={c}{c_nwc}" if i == 0 else f"={c}{c_nwc}-{CL(1 + i)}{c_nwc}")
    c_mc = addc("Maintenance capex", P(r_mcx))
    c_cfads = addc("CFADS", lambda i, c: f"={c}{c_e}-{c}{c_t}-{c}{c_dn}-{c}{c_mc}", b=True)
    c_ds = addc("Debt service", lambda i, c: f"=Debt!{CL(3 + i)}5+Debt!{CL(3 + i)}13+Debt!{CL(3 + i)}21+IF(Debt!{CL(3 + i)}5=0,Debt!{CL(3 + i)}6,0)+IF(Debt!{CL(3 + i)}13=0,Debt!{CL(3 + i)}14,0)")
    c_dscr = addc("DSCR", lambda i, c: f"=IF({c}{c_ds}>0,{c}{c_cfads}/{c}{c_ds},\"\")", fmt="0.00", b=True)
    c_eq = addc("Cash flow after debt service", lambda i, c: f"={c}{c_cfads}-{c}{c_ds}")
    c_cash = addc("Closing cash (from reserve)", lambda i, c: f"={ref['cash_reserve']}+{c}{c_eq}" if i == 0 else f"={CL(1 + i)}{c_cash if False else 0}" )
    # fix closing cash recursion (needs own row number)
    for i in range(N):
        c = CL(2 + i)
        wcf[f"{c}{c_cash}"] = f"={ref['cash_reserve']}+{c}{c_eq}" if i == 0 else f"={CL(1 + i)}{c_cash}+{c}{c_eq}"
    c_ut = addc("Unlevered tax", lambda i, c: f"=MAX(PnL!{c}{r_ebitda}-PnL!{c}{r_dep},0)*{ref['tax_rate']}*IF({D('op_year_index', i)}<{ref['tax_relief_years']},1-{ref['tax_relief_pct']},1)")
    c_fcf = addc("Project free cash flow", lambda i, c: f"={c}{c_e}-{c}{c_ut}-{c}{c_dn}-{c}{c_mc}", b=True)
    base_r = 3 + len(cl_) + 1
    wcf.cell(base_r, 1, "Construction outflow 2027").font = bold
    wcf.cell(base_r, 2, -round(c1_val, 2)).number_format = num
    wcf.cell(base_r + 1, 1, "Construction outflow 2028").font = bold
    wcf.cell(base_r + 1, 2, -round(c2_val, 2)).number_format = num
    wcf.cell(base_r + 2, 1, "Terminal value at 2038")
    wcf.cell(base_r + 2, 2, f"=K{c_fcf}*(1+{ref['terminal_growth']})/({ref['discount_rate']}-{ref['terminal_growth']})").number_format = num
    wcf.cell(base_r + 3, 1, "Project NPV @ discount rate, no TV").font = bold
    wcf.cell(base_r + 3, 2, f"=B{base_r}+B{base_r + 1}/(1+{ref['discount_rate']})+NPV({ref['discount_rate']},B{c_fcf}:K{c_fcf})/(1+{ref['discount_rate']})").number_format = num
    wcf.cell(base_r + 4, 1, "Project NPV with TV").font = bold
    wcf.cell(base_r + 4, 2, f"=B{base_r + 3}+B{base_r + 2}/(1+{ref['discount_rate']})^11").number_format = num
    wcf.cell(base_r + 5, 1, "Minimum DSCR")
    wcf.cell(base_r + 5, 2, f"=MIN(B{c_dscr}:K{c_dscr})").number_format = "0.00"
    wcf.cell(base_r + 6, 1, "Minimum cash")
    wcf.cell(base_r + 6, 2, f"=MIN(B{c_cash}:K{c_cash})").number_format = num
    wcf.cell(base_r + 7, 1, "Python check: NPV with TV (should match)")
    wcf.cell(base_r + 7, 2, round(base["npv_tv"], 0)).number_format = num
    wcf.column_dimensions["A"].width = 38
    for i in range(N):
        wcf.column_dimensions[CL(2 + i)].width = 13

    # ---------------- Scenarios (values)
    wsx = wb.create_sheet("Scenarios")
    wsx["A1"] = "Scenario and structure results (values from ptc_model.py)"
    wsx["A1"].font = bold
    cols = ["net_rev_y6", "ebitda_y6", "ebitda_margin_y6", "min_dscr", "min_dscr_year", "dscr_y6", "min_cash", "npv_no_tv", "npv_tv", "irr_tv", "equity_irr_tv", "equity", "debt"]
    wsx.cell(2, 1, "Case").font = bold
    for j, k in enumerate(cols):
        wsx.cell(2, 2 + j, k).font = bold
    rr = 3
    for k, s in list(RESULTS["scenarios"].items()) + list(RESULTS["structures"].items()):
        wsx.cell(rr, 1, k)
        for j, kk in enumerate(cols):
            v = s[kk]
            wsx.cell(rr, 2 + j, None if v is None else round(v, 4) if isinstance(v, float) and abs(v) < 10 else v)
        rr += 1
    wsx.column_dimensions["A"].width = 60

    # ---------------- Ennab comparison
    we = wb.create_sheet("Vs_reference_study")
    we["A1"] = "Comparison with the owner-supplied reference study (Ennab 2025, 80-bed general hospital, Wadi Musa)"
    we["A1"].font = bold
    rows = [("Metric", "Reference study (80 beds)", "This study (20 beds, lean Phase 1)"),
            ("Total investment JOD", 7574640, round(base["total_uses"])),
            ("Investment per bed", round(7574640 / 80), round(base["total_uses"] / 20)),
            ("Building cost per m2 (structure+finishing)", 298, BASE["build_cost_m2"]),
            ("Medical equipment JOD", 3150400, round(base["capex"]["items"]["Medical equipment"])),
            ("Staff", 100, base["staff_count"]),
            ("Annual payroll Y1 JOD", 609960, round(base["opex_lines"]["Payroll"][0])),
            ("Average monthly cost per employee", round(609960 / 100 / 12), round(base["opex_lines"]["Payroll"][0] / base["staff_count"] / 12 / BASE["staffing_factor"][0])),
            ("Revenue Y1 JOD", 3311250, round(base["net_revenue"][0])),
            ("Revenue ramp-up", "none (+3%/yr)", "38% -> 72% ward occupancy over 6 years"),
            ("Debt", "none", round(base["debt_total"])),
            ("Receivables", "ignored (all cash)", f"{BASE['dso_days']} days"),
            ("Net profit Y1 JOD", 150054, round(base["net_income"][0]))]
    for j, row in enumerate(rows, start=3):
        for k, v in enumerate(row):
            we.cell(j, 1 + k, v)
    we.column_dimensions["A"].width = 44
    we.column_dimensions["B"].width = 26
    we.column_dimensions["C"].width = 30

    out = os.path.join(HERE, "PTC-financial-model.xlsx")
    wb.save(out)
    return out


RESULTS = {}

if __name__ == "__main__":
    base = run(BASE)
    scen = {k: scal(run(v)) for k, v in SCENARIOS.items()}
    struct = {k: scal(run(v)) for k, v in STRUCTURES.items()}
    sens = []
    for lab, key, lo, hi in SENS:
        sens.append((lab, lo, hi, scal(run(variant(**{key: lo}))), scal(run(variant(**{key: hi})))))
    opts = {k: scal(run(v)) for k, v in OPTIONS.items()}
    RESULTS.update({"base": scal(base), "scenarios": scen, "structures": struct, "options": opts,
                    "sensitivity": [{"driver": a, "low": b, "high": c, "low_res": d, "high_res": e} for a, b, c, d, e in sens],
                    "base_detail": {k: base[k] for k in ["net_revenue", "total_opex", "ebitda", "ebitda_margin", "dep", "interest",
                                                         "tax", "net_income", "cfads", "debt_service", "dscr", "cash", "d_nwc", "fcf"]},
                    "capex_items": base["capex"]["items"], "idc": base["idc"], "fees": base["fees"],
                    "t1_installment": base["t1"]["installment"], "t3_installment": base["t3"]["installment"],
                    "staff_count": base["staff_count"], "payroll_full": base["base_payroll_full"],
                    "revenue_lines": base["revenue_lines"], "opex_lines": base["opex_lines"],
                    "breakeven_ebitda_year": base["breakeven_ebitda_year"]})
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(RESULTS, f, indent=1, default=float)
    write_tables(base, scen, struct, sens)
    write_excel(BASE, base)
    b = RESULTS["base"]
    print(json.dumps(b, indent=1, default=str))
    print("staff", base["staff_count"], "payroll_full", round(base["base_payroll_full"]))
    for k, s in scen.items():
        print(f"{k[:50]:50s} EBITDA6 {s['ebitda_y6']:>10,.0f} minDSCR {s['min_dscr']:.2f}({s['min_dscr_year']}) DSCR6 {s['dscr_y6']:.2f} mincash {s['min_cash']:>11,.0f} gap {s['funding_gap']:>10,.0f} NPVtv {s['npv_tv']:>11,.0f} eqIRR {s['equity_irr_tv']}")
    for k, s in opts.items():
        print(f"OPT {k[:48]:48s} uses {s['total_uses']:>10,.0f} full {s['fully_funded_uses']:>10,.0f} eq {s['equity']:>10,.0f} gap {s['funding_gap']:>9,.0f} DSCR6 {s['dscr_y6']:.2f} NPVtv {s['npv_tv']:>11,.0f} IRR {s['irr_tv']} first125 {s['first_dscr_above_125']}")
    for k, s in struct.items():
        print(f"{k[:50]:50s} eq {s['equity']:>10,.0f} ({s['equity_share']:.0%}) minDSCR {s['min_dscr']:.2f}({s['min_dscr_year']}) DSCR6 {s['dscr_y6']:.2f} mincash {s['min_cash']:>11,.0f} eqIRR {s['equity_irr_tv']}")
