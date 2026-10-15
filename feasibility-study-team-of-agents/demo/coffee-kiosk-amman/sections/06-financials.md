# 06 · Financial Study: Specialty Coffee Shop Unit, Al-Jubeiha, Amman

*Prepared by the financial-analyst agent, 15 Oct 2026. Currency: JOD. Every figure below was produced by `tools/fin_model.py` from `assumptions.json`; nothing was computed by hand. Full output: `model-output.md`; workbook: `financial-model.xlsx`.*

**Summary.** The unit needs **JOD 35,690** to open: JOD 20,860 equipment and fit-out, JOD 6,885 pre-opening costs and a JOD 7,945 working-capital reserve. That fits inside the brief's JOD 40,000 equity budget, with no loan. On the team's volumes, the shop covers its monthly cash costs from **month 2**, earns back the startup cost by **month 15**, and has a 5-year **NPV of JOD 146,444 at 16%** (IRR 112.6%). Year-1 revenue is **JOD 100,081 net of GST**.

**The base case is optimistic, and it should be read that way (Assessment).** Its net margin of 30–34% from year 2 is two to three times the café benchmark of 10–15%. That gap comes from four things: an unpaid owner, a two-person crew working 14 hours a day, low side-street rent, and no seasonal dip. If the owner takes a notional JOD 600 a month, NPV falls to **JOD 123,160** (IRR 92.9%, payback month 18). Even the harshest case run (owner salary, volume −20% and unit cost +15% together) keeps NPV positive at **JOD 54,877**. The project stays viable under every stress tested. The bigger risks are the licence, key money and the volume forecast, and the model cannot capture those.

---

## 6.1 How the inputs were built

| Input | Value used | Treatment and source |
|---|---|---|
| Drink price | **JOD 2.112 net** | The marketing ticket of JOD 2.45 **includes 16% GST** (05-marketing, 04-legal). The model needs prices net of sales tax, so 2.45 / 1.16 = 2.112 |
| Pastry price | **JOD 1.509 net** | JOD 1.75 incl. GST / 1.16 |
| Drink volume | 1,650 → 4,650 per month in year 1 (40,950 for the year); then 58,680 / 75,600 / 79,200 / 82,440 | 05-marketing ramp, built on 01-market SOM |
| Pastry volume | 0.22 per drink (9,009 in year 1 → 18,137 in year 5) | 05-marketing |
| Unit cost | Drink JOD 0.67, pastry JOD 0.60 | 03-operations 3.5. Indexed to inflation each year |
| Price growth | 2% a year | ASSUMPTION. Slightly below CPI; marketing held prices flat and left indexation open |
| Channel commission and card fees | **4.5% of all revenue** | See the arithmetic below |
| Payroll | Head barista 500, barista 380, part-timer 180 (gross). Headcount y1: 1+1; y2: 1+1+0.5 PT; y3–5: 1+2 | 03-operations 3.4. Owner unpaid in the base case |
| Employer social security | 14.25%, applied **once** by the model | 04-legal. Operations' totals (1,005 / 1,211 / 1,440) already include SS, so the model is given the **gross** salaries to avoid counting SS twice |
| Fixed opex | JOD 985 a month | Operations' JOD 1,105 **minus** its JOD 150 local-marketing line, which the separate marketing budget already covers. **Plus** an ASSUMPTION of JOD 30 a month for licence renewals and health certificates, whose amounts 04-legal could not retrieve |
| Marketing | JOD 658 a month in year 1 (year-1 total JOD 7,890), then 3% of revenue | 05-marketing |
| Inflation (opex, unit costs) | 2.5% | Jordan DoS: CPI +2.26% Jan–Sep 2026 and +2.73% Sep y/y (QNA, 12 Oct 2026). Midpoint used. Wages are also indexed at 2.5% (ASSUMPTION) |
| Corporate tax | 21% | 20% CIT + 1% national contribution, LLC (04-legal, PwC 2026) |
| Discount rate | **16%** | CBJ main policy rate 5.75% (held 30 Jul 2026, Jordan News) **plus an ASSUMPTION** of a 10% premium for a small, unlisted, first-time-owner food business = 15.75%, rounded to 16%. Cross-check: the Jordan average bank lending rate is 8.24% (CEIC, Jan 2025). Equity in a start-up should clear that by a wide margin |
| Financing | None | Brief: equity funded |
| Residual value | 0 | ASSUMPTION, conservative. The working-capital reserve is recovered in year 5 |

**Channel commission arithmetic.** The model applies a single commission rate to all revenue, so the two variable selling costs are blended into one rate:
- **Delivery apps:** 15% of sales go through Talabat/Careem, at 25% all-in commission. 0.15 × 0.25 = **3.75% of revenue**. This follows 05-marketing, which applies the commission to pastries ordered through the apps as well as drinks. If pastries were exempt, the rate would be slightly lower, so 3.75% is a little conservative.
- **Card fees on walk-up sales:** 85% of sales are walk-up. ASSUMPTION: 60% of those are paid by card. ASSUMPTION: 1.5% merchant discount rate. Jordanian banks do not publish their MDR (Jordan Islamic Bank's POS page states only a "competitive" rate); Careem's 1.5–3% processing fee (Menuviel 2026) is context. 0.85 × 0.60 × 0.015 = **0.77% of revenue**. CliQ and cash transfers are treated as free.
- **Total: 3.75% + 0.77% = 4.52%, used as 4.5%.**

**Rent paid 6 months in advance.** The lease is signed around month 1 and the shop opens in month 5 (03-operations 3.7). The first six-month advance therefore covers:
- about **4 months of fit-out and licensing**, when there is no revenue. That rent is a real pre-opening cost, entered as **JOD 2,200** (4 × 550) in `pre_opening_costs`;
- **2 operating months**, which the model already charges in fixed opex for months 1–2. Paying that rent early is a cash-timing difference, not an extra cost, and the 3-month working-capital reserve (JOD 7,945) covers it.

This avoids charging the same JOD 1,100 twice. If the landlord asks for a **full year in advance**, about JOD 3,300 more cash is needed at opening. That still fits inside the JOD 40,000 budget.

**Key money (*khilw*) is excluded.** It is an ASSUMPTION that the chosen unit carries none. One Jubeiha listing mentions key money (03-operations [R8]). It is a **risk**: it would add directly to the startup cost and would not be depreciable. Every JOD 1,000 of key money lowers NPV by about JOD 1,000.

## 6.2 Startup cost and funding

| Item | JOD |
|---|---:|
| Equipment and fit-out (capex, 14 items incl. 10% contingency; 03-operations 3.3) | 20,860 |
| Government registrations, licences, certificates (04-legal, ASSUMPTION) | 1,500 |
| Lawyer / accountant / licensing agent (04-legal, midpoint of 500–1,000) | 750 |
| Pre-opening marketing (05-marketing) | 710 |
| Rent during fit-out and licensing (4 × 550) | 2,200 |
| Pre-opening hiring and training: head barista 1.5 months + barista 0.5 month, incl. SS (ASSUMPTION) | 1,075 |
| Opening inventory and dial-in (about 2 weeks of COGS, ASSUMPTION) | 650 |
| Working-capital reserve (3 months of year-1 fixed costs, payroll and marketing) | 7,945 |
| **Total startup cost** | **35,690** |
| Equity | 35,690 |
| Loan | 0 |

That leaves about **JOD 4,300 of headroom** under the brief's JOD 40,000. It is enough for a 12-month rent advance, but not for key money of more than about JOD 1,000 on top of that.

## 6.3 Income statement (5 years, JOD, net of GST)

| Line | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---:|---:|---:|---:|---:|
| Units sold (drinks + pastries) | 49,959 | 71,590 | 92,232 | 96,624 | 100,577 |
| Revenue | 100,081 | 146,282 | 192,229 | 205,411 | 218,091 |
| Cost of goods | 32,842 | 48,238 | 63,701 | 68,402 | 72,981 |
| Channel commissions and card fees | 4,504 | 6,583 | 8,650 | 9,243 | 9,814 |
| Payroll (incl. employer SS) | 12,065 | 14,896 | 18,149 | 18,603 | 19,068 |
| Fixed operating costs | 11,820 | 12,115 | 12,418 | 12,729 | 13,047 |
| Marketing | 7,896 | 4,388 | 5,767 | 6,162 | 6,543 |
| **EBITDA** | **30,955** | **60,061** | **83,544** | **90,271** | **96,638** |
| Pre-opening costs expensed | 6,885 | 0 | 0 | 0 | 0 |
| Depreciation | 3,992 | 3,992 | 3,992 | 3,992 | 3,992 |
| Profit before tax | 20,078 | 56,069 | 79,552 | 86,279 | 92,646 |
| Tax (21%) | 4,216 | 11,775 | 16,706 | 18,119 | 19,456 |
| **Net profit** | **15,862** | **44,295** | **62,846** | **68,161** | **73,191** |
| Net margin | 15.8% | 30.3% | 32.7% | 33.2% | 33.6% |

## 6.4 Cash flow

| JOD | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---:|---:|---:|---:|---:|---:|
| Project free cash flow | −35,690 | 26,738 | 48,286 | 66,838 | 72,152 | 85,127 |
| Cumulative | −35,690 | −8,952 | 39,334 | 106,172 | 178,325 | 263,452 |

Year 5 includes recovery of the JOD 7,945 working-capital reserve. Month 1 is the only month with negative EBITDA (−121). Cash stays positive after the startup outlay, so no financing is needed. Year-1 tax is approximated in the model, and the owner should keep the reserve untouched until about month 6.

## 6.5 Key indicators

| Indicator | Base case (owner unpaid) | Owner salary scenario (JOD 600/month) |
|---|---:|---:|
| Total startup cost | 35,690 | 37,747 |
| NPV (5 yrs, 16%) | **146,444** | **123,160** |
| IRR (5 yrs) | **112.6%** | **92.9%** |
| Payback | **month 15 (1.2 yrs)** | month 18 (1.5 yrs) |
| First month with positive EBITDA | **2** | 3 |
| Break-even volume, year 1 (units/month) | 2,109 vs plan average 4,163 | 2,655 |
| Contribution margin per unit, year 1 | JOD 1.26 | JOD 1.26 |
| Year-1 net profit | 15,862 | 9,363 |
| Year-3 net profit | 62,846 | 56,019 |
| 5-year ROI on startup cost | 740.7% | 609.8% |

**Owner salary scenario.** This is a copy of `assumptions.json`, kept outside the study folder. Its only change is an owner-manager line at **JOD 600 gross a month**. That figure is an ASSUMPTION: a manager's premium over the head barista's JOD 500 (03-operations [W1]), with employer SS applied. The scenario's working-capital reserve rises with payroll, which is why its startup cost is higher. The scenario is a fairer measure of the business's own return, because in the base case part of the "profit" is really the owner's unpaid wage.

## 6.6 Break-even

- **By month:** EBITDA turns positive in **month 2** (month 3 with an owner salary).
- **By volume:** break-even is **2,109 units a month** in year 1. The model's units are drinks and pastries combined. At 0.22 pastries per drink, that is about **1,730 drinks a month, or about 58 drinks a day** (about 73 a day with an owner salary). This is a unit conversion of the model's output.
- **Against capacity:** operations puts practical capacity at **400 drinks a day**. Break-even therefore needs about **14% of capacity**, and the plan averages 114 drinks a day in year 1 (29%). Break-even is plausible and well inside capacity. The month-1 plan of 55 drinks a day sits almost exactly at break-even, which is consistent with month 1 being the only loss month.

## 6.7 Sensitivity (from the model)

| Scenario | NPV base | IRR | Payback month | Y1 net profit | NPV with owner salary |
|---|---:|---:|---:|---:|---:|
| Base case | 146,444 | 112.6% | 15 | 15,862 | 123,160 |
| Price −10% (≈ JOD 2.20 GST-incl. ticket, the low case marketing asked for) | 107,114 | 89.3% | 18 | 8,311 | 83,830 |
| Volume −20% | 95,828 | 82.3% | 19 | 5,950 | 72,418 |
| Volume +20% | 197,061 | 141.9% | 12 | 25,774 | 173,777 |
| Unit cost +15% | 125,411 | 100.4% | 16 | 11,970 | 102,127 |
| Fixed costs & payroll +15% | 134,973 | 103.3% | 16 | 13,031 | 108,196 |
| Capex +20% | 142,821 | 102.8% | 16 | 15,231 | 119,537 |
| **Pessimistic (volume −20%, cost +15%)** | **79,001** | 71.9% | 21 | 2,836 | **54,877** (Y1 loss −4,636) |

Price and volume drive the result. A 10% price cut costs about JOD 39,000 of NPV, and a 20% volume shortfall about JOD 51,000. Capex barely matters: +20% costs about JOD 3,600. With an owner salary, a 20% volume shortfall pushes year 1 slightly into loss (−695), but the 5-year NPV stays strongly positive.

## 6.8 Sanity checks against benchmarks

| Metric | This model (Y1 → Y5) | Benchmark | Reading |
|---|---|---|---|
| Gross margin (revenue − COGS) | 67.2% → 66.5% | 65–75% healthy (Bellwether Coffee, May 2026). 60.1–60.5% average for US coffee shops (BizBuySell, 2020–21) | **In range.** Confidence: Medium |
| Net margin | 15.8% (Y1), 30–34% (Y2–5) | 10–15% healthy, 5–15% typical (Bellwether). 7–9% pre-tax average (BizBuySell) | **Well above benchmark.** Treat as optimistic |
| Payroll / revenue | 12.1% → 8.7% (20.3% → 12.9% with owner salary) | No local benchmark sourced | Very lean (Assessment) |
| Rent / revenue | about 6.6% → 3.3% | No local benchmark sourced | Low because the unit is a side-street shop |

**Why the net margin is so high (Assessment).** The gross margin is normal, so the gap sits below gross profit:
1. **Unpaid owner.** The owner works as manager and covers baristas' days off for free. Adding JOD 600 a month removes about 4–6 points of margin.
2. **Lean crew.** Two staff cover 98 opening hours a week in year 1, so a single barista works alone for much of the day (operations: about 35 drinks an hour with one). Benchmarks reflect larger cafés with seating and more staff.
3. **Low fixed costs.** JOD 550 rent for a 35 m² side-street unit.
4. **Volumes are untested and flat across the year.** The ramp assumes 30 trading days every month. A university-area shop will see dips in Ramadan daytime and the summer break (05-marketing open question 6). None of that is modelled.

For decision-making, the **owner-salary scenario combined with the pessimistic case (NPV JOD 54,877)** is the prudent planning figure. Even there, the startup cost is recovered within about 27 months.

## 6.9 What the numbers mean (Assessment)

- **Affordable and self-funding.** JOD 35,690 fits the budget, no loan is needed, and the business should cover its running costs from month 2.
- **The financial case is strong on paper, and the non-financial risks decide it.** The deciding risk is GAM licensing (04-legal: no new licences for street coffee sales). A refusal or delay after signing a lease and starting fit-out would cost rent and the fit-out spend before any revenue. Key money, a 12-month rent advance or a fit-out overrun would also eat the JOD 4,300 of headroom quickly.
- **Volume is the number to validate.** Do a footfall count and test sales (for example, at a pop-up or a university event) before signing. A 20% volume miss still leaves NPV positive, but year 1 goes to about break-even once an owner salary is counted.
- **Protect the price.** Pass and office-box discounts that push the blended ticket toward JOD 2.20 cost about JOD 39,000 of NPV. Keep the passes capped at around 12% of drinks, as marketing proposes.
- **Confidence: Medium–Low overall.** Capex and costs are Medium. Volume and price are Medium–Low, because they rest on SOM assumptions. Pastry COGS, fit-out and licence fees are Low.

## Sources

- Central Bank of Jordan decision reported by Jordan News, "Central Bank of Jordan Keeps Main Interest Rate Unchanged at 5.75%", 30 Jul 2026. https://www.jordannews.jo/Section-112/Economy/Central-Bank-of-Jordan-Keeps-Main-Interest-Rate-Unchanged-at-5-75-53662
- Qatar News Agency (citing Jordan Department of Statistics), "Jordan's inflation rises 2.26 percent since start of 2026", 12 Oct 2026. https://qna.org.qa/en/News-Area/News/2026-10/12/jordans-inflation-rises-226-percent-since-start-of-2026
- Jordan Times (DoS), "Jordan's inflation rises by 2.03% in H1 of 2026". https://jordantimes.com/news/business/jordans-inflation-reaches-203-in-h1-of-2026-dos
- CEIC Data, Jordan Bank Lending Rate (8.24%, Jan 2025). https://www.ceicdata.com/en/indicator/jordan/bank-lending-rate
- Bellwether Coffee, "Coffee Shop Profit Margins: What to Expect and How to Improve Them", 3 May 2026 (publisher's own benchmarks; global context). https://bellwethercoffee.com/blog/coffee-shop-profit-margins
- BizBuySell, "Coffee Shops and Cafes: Revenue and Profit Benchmarks" (US averages 2020–2021; global context). https://www.bizbuysell.com/learning-center/revenue-profit-benchmarks/coffee-shops-and-cafes
- Jordan Islamic Bank, Point of Sale service (MDR not published). https://www.jordanislamicbank.com/en/point-of-sale-service-pos
- Menuviel, "Careem Fees and Commissions for Restaurants" (1.5–3% payment processing; via 05-marketing). https://blog.menuviel.com/careem-fees-and-commissions-for-restaurants/
- Internal: 01-market.md, 03-operations.md (capex, opex, payroll, COGS, capacity, timeline), 04-legal.md (GST 16%, CIT 21%, SS 14.25%, setup fees), 05-marketing.md (prices, volumes, commission, marketing budget).
- Model files: `assumptions.json`, `model-output.md`, `financial-model.xlsx` (this folder).

## Key numbers handed to other agents

```yaml
currency: JOD
total_startup_cost: 35690          # capex 20,860 + pre-opening 6,885 + working capital 7,945; equity funded
breakeven_month: 2                  # first month with positive EBITDA
breakeven_units_month_y1: 2109      # drinks + pastries; ~58 drinks/day vs 400/day capacity
npv: 146444                         # 5 yrs at 16%
irr: 1.126
payback_years: 1.2                  # month 15
year1_revenue: 100081               # net of 16% GST
year3_net_profit: 62846
worst_case_npv: 79001               # pessimistic: volume -20%, unit cost +15%
owner_salary_scenario:              # owner-manager JOD 600/month gross
  npv: 123160
  irr: 0.929
  payback_month: 18
  worst_case_npv: 54877
gross_margin_y1: 0.672
net_margin_y1: 0.158
net_margin_y3: 0.327
discount_rate: 0.16                 # CBJ 5.75% + 10% small-business premium (ASSUMPTION)
channel_commission_blended: 0.045   # 3.75% delivery + 0.77% card fees
key_money: excluded                 # risk
confidence_overall: Medium-Low
```

## Open questions for the owner

1. **Your salary.** Will you draw a salary? The base case assumes not. At JOD 600 a month, NPV falls by about JOD 23,000.
2. **Key money and rent advance.** Is any *khilw* asked on your shortlisted units? Will the landlord accept 6 months in advance? The budget headroom is only about JOD 4,300.
3. **Card terms.** Ask your bank for its merchant discount rate. The 1.5% used here is an assumption.
4. **Seasonality.** Will you trade normally through Ramadan and the university summer break? The model assumes a flat 30 trading days a month.
5. **Legal form.** An LLC is assumed (21% tax). A sole proprietorship is taxed at personal rates of 5–25% and changes the after-tax figures.
6. **Licence before lease.** Can GAM's written confirmation of the activity class be obtained before you sign? Pre-opening rent and fit-out are spent before revenue starts.
