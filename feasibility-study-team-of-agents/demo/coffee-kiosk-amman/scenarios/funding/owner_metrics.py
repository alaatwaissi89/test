# Uses fin_model's own functions; derived metrics only (payment, owner NPV, lowest cash balance)
import sys, json
sys.path.insert(0, "/mnt/project-files/feasibility-study-team-of-agents/tools")
import fin_model as fm
for f in sys.argv[1:]:
    a = json.load(open(f)); r = fm.run(a); fin = a["financing"]
    pay = fm.loan_payment(fin["loan_amount"], fin["loan_rate"], fin["loan_years"])
    n = int(round(fin["loan_years"] * 12)) if fin["loan_amount"] else 0
    eq = [-r["equity"]] + [s["equity_cf"] for s in r["annual"]]
    cash = r["wc"]; low = (cash, 0)
    for row in r["rows"]:
        cash += row["ebitda"] - r["annual"][row["year"]-1]["tax"]/12 - (pay if row["month"] <= n else 0)
        if cash < low[0]: low = (cash, row["month"])
    tot_int = sum(s["interest"] for s in r["annual"])
    print(f"{f}: payment={pay:,.0f}/mo x{n}; total interest={tot_int:,.0f}; owner NPV@16%={fm.npv(r['rate'], eq):,.0f}; owner IRR={(fm.irr(eq) or 0)*100:.1f}%; "
          f"lowest business cash={low[0]:,.0f} (month {low[1]}); owner cash kept outside vs 40k budget={40000-r['equity']:,.0f}")
