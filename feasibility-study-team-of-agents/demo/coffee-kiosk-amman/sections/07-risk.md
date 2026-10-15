# 07 · Risk Assessment: Specialty Coffee Shop Unit, Al-Jubeiha, Amman

*Prepared by the risk-analyst agent, 15 Oct 2026. Currency: JOD. All scenario figures come from `tools/fin_model.py`. The Prudent scenario file is `assumptions-prudent.json`, kept in the session scratchpad and not in the study folder.*

**Bottom line (Assessment).** The base case is not a sound planning figure. Its 30–34% net margin is two to three times the café benchmark of 10–15% (06-financials §6.8). We built a **Prudent** scenario that combines six realistic adjustments. In it the project is still viable but thin:

- **NPV JOD 25,803** and IRR 31.1%.
- **Payback in month 37.**
- **Year-1 net loss of JOD 15,352.**
- **Startup cost of JOD 44,049**, which is above the JOD 40,000 budget.

Two assumptions decide the project, and a licence ruling comes before both:
1. **Licensing.** Licensing is a yes/no question. A refusal after the lease is signed loses about half the capital.
2. **Volume.** In the Prudent case, NPV reaches zero if volume is **32% below plan**.
3. **Price.** In the Prudent case, NPV reaches zero if price is **9% below plan**.

All three can be tested for under about JOD 1,500 before any money is committed.

---

## 1. Risk register

Likelihood (L) and impact (I) are scored 1–5, and the score is L × I. All scores are **Assessment**. The register is ranked by deal-breaker status first and score second.

| # | Risk | Cat. | L | I | Score | Early warning sign | Mitigation | Owner |
|---|---|---|---|---|---|---|---|---|
| R1 | **The chosen unit cannot be licensed for prepared coffee.** GAM issues no new licences for street coffee sales and says a cafeteria licence does not cover coffee. It counts about 3,700 kiosks and has closed 145 outlets in 2026 (04-legal). The 2023 hot-beverage regulation adds conditions: a commercial zone (not local-commercial inside a residential block), at least 100 m from squares, intersections, traffic lights and bridge or tunnel ramps, the whole shop used for the activity, no staff serving outside the shop, and a JOD 500 deposit [L1][L2] | Legal | 4 | 5 | **20** | GAM will not confirm the activity class in writing, the plot is in a residential block, or a traffic light is less than 100 m away | Run the pre-lease licence test in §4, K1. Write a licence condition into the lease. Do not pay key money or start fit-out before the licence is approved in principle | Owner + lawyer |
| R2 | **Volume falls short of plan** (117 / 163 / 210 drinks a day in years 1–3, from the SOM; Low confidence, 01-market) | Market | 4 | 4 | **16** | Footfall counts below about 1,500 passers-by in the 7–10 am window. Pop-up sales below 60 drinks a day | Footfall count plus a pop-up or pass pre-sale (§4, K2). Office-box B2B sales. Keep the opening crew flexible | Owner |
| R3 | **Labour is understated.** Two staff at the 48 h/week legal cap give 96 h, but the shop is open 98 h a week and needs about 130 person-hours once the peaks are double-staffed (§3) | Operational | 5 | 3 | **15** | The owner is working the bar more than 40 h a week, or overtime appears in month 1 | Budget a third barista from year 1 (included in Prudent) | Owner |
| R4 | **Seasonal dips are not modelled.** UJ teaching stops 22 Jun–12 Jul and 30 Aug–4 Oct, and only the summer semester runs in between [S1]. Daytime takeaway falls in Ramadan, although evening café trade rises [S2] | Market | 5 | 3 | **15** | (Certain to happen) | Plan the cash for it (included in Prudent). Run an evening Ramadan menu and push office B2B sales in summer | Owner |
| R5 | **Price pressure.** Qahwa BLK sells a latte at JOD 2.00, against our blended ticket of JOD 2.45 (02-competition) | Competition | 3 | 4 | **12** | Pass and box share above 12% of drinks, or the average ticket below JOD 2.35 | Cap discounts. Compete on quality rather than price (§4, K3) | Owner |
| R6 | **A competitor opens close by.** Barriers to entry are low (02-competition) | Competition | 4 | 3 | **12** | A new coffee permit or fit-out within 300 m | Build loyalty through passes and lock in B2B accounts in the first 6 months | Owner |
| R7 | **Funding gap.** Prudent startup is JOD 44,049 against a JOD 40,000 budget. A 12-month rent advance adds about JOD 3,300 | Financial | 4 | 3 | **12** | The landlord asks for key money or a full year in advance | Negotiate a 6-month advance. Buy a used espresso machine (saves about JOD 1,800, 03-operations). Keep a JOD 5–8k standby | Owner |
| R8 | **The head barista leaves,** and the owner has no café experience | Operational | 3 | 4 | **12** | Quality complaints, or the barista is hard to reach | Pay a retention bonus at 12 months, document the recipes, cross-train the second barista | Owner |
| R9 | **Fines or closures for operating violations.** The 2023 draft sets 3-, 7- and 30-day closures for serving outside the shop or delivering to the street [L1] | Legal | 3 | 3 | 9 | GAM warning notices | Serve through the window only, with no service to kerbside cars. Train staff on the rule | Owner |
| R10 | **Licensing or fit-out delay** (licensing estimate 2–3 months, Low confidence, 04-legal) | Operational | 3 | 3 | 9 | No GAM inspection date by month 2 | Seek a rent-free fit-out period. Agree a fixed-price fit-out contract | Owner |
| R11 | **COGS inflation** (imported beans, milk) | Financial | 3 | 3 | 9 | Supplier price lists rise more than 10% | Fix bean prices for 6–12 months. Exchange-rate risk is low because the JOD is pegged to the USD (03-operations) | Owner |
| R12 | **Delivery-app dependence and commission rises** (25% all-in, 05-marketing) | Market | 3 | 2 | 6 | Delivery share above 25% of sales | Add a pickup pre-order channel. Price app menus higher | Owner |
| R13 | **Food-safety finding** from JFDA or GAM (04-legal) | Legal | 2 | 4 | 8 | Inspection remarks | Run a HACCP-style checklist and keep health certificates current | Head barista |
| R14 | **Macro shock** (regional conflict, weaker consumer spending) | Macro | 2 | 4 | 8 | Footfall drops across Amman | Keep fixed costs low and avoid a long lease without a break clause | Owner |
| R15 | **Equipment downtime** (single machine) | Operational | 2 | 3 | 6 | Repeated faults | Service contract with the local agent, and keep a spare-parts kit | Head barista |

## 2. Heat map summary

| Likelihood ↓ / Impact → | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| **5** | | R3, R4 | | |
| **4** | | R6, R7 | R2 | **R1** |
| **3** | R12 | R9, R10, R11 | R5, R8 | |
| **2** | | R15 | R13, R14 | |

The red zone (score 15 or more) holds licensing (R1), volume (R2), labour (R3) and seasonality (R4). R3 and R4 are near-certain, so they belong in the plan rather than in the risk list, and the Prudent case includes them. R1 and R2 are genuine uncertainties, and both can be tested before money is committed. **Confidence in the register: Medium.**

## 3. Scenario analysis

### 3a. How the Prudent case is built (each step added on top of the one before)

| Step | Adjustment and basis | NPV (16%) | IRR | Payback | Y1 net profit | Startup |
|---|---|---:|---:|---:|---:|---:|
| Base | As in 06-financials (owner unpaid) | 146,444 | 112.6% | m15 | 15,862 | 35,690 |
| + Owner salary | JOD 600 gross a month (06-financials scenario) | 123,160 | 92.9% | m18 | 9,363 | 37,747 |
| + Third barista from year 1 | Barista ×2 in all years (JOD 380, 03-operations), with the year-2 part-timer dropped. Coverage arithmetic: the shop is open 14 h × 7 = 98 h a week. Double-staffing the 07:30–10:00 and 13:00–15:00 peaks adds about 31.5 h, so about 130 person-hours are needed a week. Two staff at the 48 h legal cap (04-legal) give 96 h before 14 days of annual leave each. Three give 144 h | 117,280 | 84.9% | m19 | 5,247 | 39,049 |
| + Seasonality | Year-1 month 1 is taken as March 2027 (opening in month 5, 03-operations). **ASSUMPTION** factors: Jun −10% (UJ exams end 22 Jun), Jul and Aug −25% (summer semester only, 12 Jul–30 Aug), Sep −30% (no classes until 4 Oct) [S1]. These are derived as about 40% student share of the catchment (01-market) × about 65% fewer students on campus. Ramadan is about Feb 2028 (month 12), **ASSUMPTION** −20%: daytime takeaway falls, and evening café trade partly offsets it [S2]. Years 2–5 are reduced by 9% to match | 94,184 | 72.3% | m23 | 418 | 39,049 |
| + Volume −20% | Orchestrator stress. SOM confidence is Low | 46,233 | 44.7% | m31 | −10,795 | 39,049 |
| + Unit cost +15% | Pastry COGS is Low confidence, and bean wholesale price is an estimate (03-operations) | 30,296 | 35.2% | m35 | −14,352 | 39,049 |
| **+ Key money JOD 5,000 = PRUDENT** | OpenSooq Oct 2026 asks: JOD 5,000 for a shop in Umm Al-Summaq [K1] and JOD 6,900 for a counter booth in Majdi Mall, University St [K2]. A Jubeiha listing between UJ and PSUT asks for *khilw* (29,999 shown, for 120 m², ambiguous) [K3]. A 7th Circle unit asks for JOD 150k (prime, an outlier) [K4]. The low end of the small-unit range is used, amortised over 5 years | **25,803** | **31.1%** | **m37** | **−15,352** | **44,049** |

The three adjustments that cost the most NPV are volume −20% (about JOD 48k), seasonality (about JOD 23k) and owner salary (about JOD 23k).

### 3b. Scenario summary

| Scenario | NPV | IRR | Payback | Year-1 net profit | Note |
|---|---:|---:|---:|---:|---|
| Optimistic (base volume +20%, owner unpaid) | 197,061 | 141.9% | m12 | 25,774 | Model sensitivity. **Not credible**, because it builds on an already optimistic base |
| Optimistic with owner salary | 173,777 | 120.7% | m14 | 19,275 | Owner-salary sensitivity |
| Base (owner unpaid) | 146,444 | 112.6% | m15 | 15,862 | 06-financials |
| **Prudent (recommended planning case)** | **25,803** | **31.1%** | **m37** | **−15,352** | EBITDA turns positive in month 8 (the October semester start). Net margin −21% in year 1, 11% in year 2, 18–20% in years 3–5 |
| Prudent + price −10% | −4,040 | 13.5% | m50 | −22,253 | Model sensitivity on the Prudent file |
| Prudent + volume −20% (64% of plan) | −9,448 | 10.1% | m54 | −23,700 | |
| Prudent pessimistic (+ volume −20% and cost +15% again) | **−24,358** | 0.3% | >60 | −26,973 | Worst case tested |

**Reading the scenarios (Assessment).**
- The Prudent margin of 18–20% from year 3 is still above the 10–15% benchmark. It should therefore be read as a central case, not a floor.
- The model does not carry the year-1 loss forward against later tax. If carry-forward is allowed, the Prudent NPV would be about JOD 3k higher.
- If the owner really works about 40 h a week on the bar, the third barista can be dropped, which adds about JOD 5.9k of NPV.
- **Licence refusal is not in the model.** If GAM refuses after the lease and fit-out, the loss is roughly:
  - 6 months' rent: JOD 3,300
  - key money: JOD 5,000
  - non-recoverable fit-out, signage and AC: JOD 8,900
  - fees: JOD 2,250
  - a 30% loss on resale of JOD 10,060 of equipment: about JOD 3,000 (**ASSUMPTION**)

  That totals **about JOD 22,500**, more than half the capital. If the refusal comes after the lease but before fit-out, the loss is about JOD 9,000. If the test is run before the lease, it costs a few hundred JOD.

## 4. Killer assumptions and how to test them

| # | Killer assumption | Threshold that makes it negative (Prudent cost base) | Cheap test before investing | Cost and time |
|---|---|---|---|---|
| **K1** | **The specific unit can be licensed** as a main-profession coffee shop with window service | This is a yes/no outcome. A "no" after the lease costs about JOD 9k–22.5k | **Pre-lease licence test:** (1) Get the plot's zoning certificate (مخطط موقع تنظيمي) from GAM and check it against the 2023 regulation: a commercial zone that is not local-commercial inside a residential block, and at least 100 m from traffic lights, intersections and squares [L1]. Measure the distances on site. (2) Through a licensing agent, get GAM's written preliminary approval (موافقة مبدئية) for the profession class "preparing and selling hot beverages" or "café" at that address. (3) Sign only a lease with a condition precedent: rent and key money are refunded if the licence is refused within 90 days. Screen 3 units at once | About JOD 300–600 in agent fees (**ASSUMPTION**), 2–4 weeks |
| **K2** | **Volume reaches about 100 drinks a day in year 2 and about 130 in year 3** | Prudent NPV is zero at **68% of plan volume**, including seasonality. That is about 101 drinks a day in year 2 and 130 in year 3, against a plan of 163 and 210 | (1) A footfall count at each shortlisted unit: 2 semester weekdays, 7–10 am and 1–4 pm, counting passers-by and current coffee carriers (01-market). (2) A 2-week pop-up or a sampling stand at a licensed partner site, such as an office lobby or a campus event, to measure drinks per hour. (3) Pre-sell 20-drink passes (JOD 40, 05-marketing) on Instagram, refundable if the shop does not open. Target: 100 passes, worth JOD 4,000, in 3 weeks | About JOD 500–900 (**ASSUMPTION**: counter staff, beans, cups, a JOD 200 ad boost), 3–4 weeks |
| **K3** | **The blended ticket holds at about JOD 2.45** (GST-inclusive) next to Qahwa BLK at JOD 2.00 | Prudent NPV is zero at **−8.6%**, which is a ticket of about **JOD 2.24** | Use the pop-up in K2 to test prices: alternate the latte at 2.50 and 2.25 over different days and record conversion and attach rate. Run an intercept survey of 100 students and office workers (Van Westendorp-style willingness to pay) | Runs with K2, plus about JOD 100 |

The other assumptions matter, but none decides the project alone. Unit cost +15% costs about JOD 16–18k of NPV, and capex +20% costs about JOD 4.7k (Prudent waterfall and sensitivity). The supplier quotes (beans, pastry) and three fit-out quotes that 03-operations already lists will settle these.

## Key numbers handed to other agents

```yaml
currency: JOD
top_risks:
  - {id: R1, name: "GAM licence refused / unit not licensable", score: 20, deal_breaker: true}
  - {id: R2, name: "Volume below plan", score: 16}
  - {id: R3, name: "Two-person crew cannot cover 98 h/week under 48 h cap", score: 15, in_prudent: true}
  - {id: R4, name: "Summer break and Ramadan dips", score: 15, in_prudent: true}
  - {id: R5, name: "Price pressure vs Qahwa BLK JOD 2.00 latte", score: 12}
prudent_scenario:
  npv: 25803
  irr: 0.311
  payback_month: 37
  year1_net_profit: -15352
  startup_cost: 44049          # exceeds JOD 40,000 budget
  first_positive_ebitda_month: 8
  adjustments: [owner_salary_600, third_barista_y1, seasonality_y1_months_4_7_12_and_minus9pct_y2_5, volume_minus20, unit_cost_plus15, key_money_5000]
base_npv: 146444
optimistic_npv: 197061          # base volume +20%; not credible
worst_case_npv: -24358          # prudent + volume -20% + unit cost +15%
breakeven_thresholds_prudent:
  volume_vs_plan: 0.68          # NPV=0
  price_change: -0.086          # NPV=0, ticket ~JOD 2.24 incl. GST
licence_refusal_loss: {after_fitout: 22500, after_lease_before_fitout: 9000}
probability_view: "Assessment: if K1 passes, NPV>0 is more likely than not (Prudent +25.8k, 32% volume headroom); without K1 the project should not proceed"
confidence_overall: Medium-Low
```

## Sources

- [L1] Zad Jordan, "Draft hot-beverages regulation bans delivery" (draft *Regulation for licensing the preparation and sale of hot beverages within GAM, 2023*, published by the Legislation and Opinion Bureau), 12 Jun 2023. https://www.jordanzad.com/index.php?page=article&id=554691. **Whether the draft was enacted unchanged is not verified (Medium confidence).**
- [L2] Legislation and Opinion Bureau, draft regulation page. https://www.lob.gov.jo/?v=1.16&lang=ar#!/DraftDetails?DraftID=10649
- GAM, "No New licenses for cafeterias Selling Coffee for Drivers and Pedestrians", and Jordan News, 30 Aug 2026 (3,700 kiosks, 309 violations, 145 closures), both via 04-legal.
- [S1] University of Jordan Registration Unit, University Calendar (2nd-semester exams 9–22 Jun 2026; summer semester 12 Jul–30 Aug 2026; 1st semester 2026/27 begins 4 Oct 2026), accessed 15 Oct 2026. https://registration.ju.edu.jo/en/english/Lists/UniversityCalendar/All_Events.aspx
- [S2] Jordan Times, "Restaurants lag behind cafés, sweet shops in Ramadan sales", 29 Mar 2023 (cafés see customer numbers roughly double in Ramadan, mainly after iftar). https://jordantimes.com/news/local/restaurants%C2%A0lag-behind-caf%C3%A9s-sweet-shops-ramadan-sales
- [K1] OpenSooq, "Shop for rent with key money 5,000", Umm Al-Summaq, 11 Oct 2026. https://jo.opensooq.com/ar/search/288479030
- [K2] OpenSooq, counter booth inside Majdi Mall, University St, key money JOD 6,900, Oct 2026. https://jo.opensooq.com/ar/search/288616478
- [K3] OpenSooq, Jubeiha shop between UJ and PSUT, with key money (JOD 29,999 shown, 120 m²), 16 Sep 2026. https://jo.opensooq.com/ar/search/287247976
- [K4] Eureka Jo, 7th Circle 75 m² shop, key money JOD 150k (search excerpt). https://eurekajo.com/Realestates/Search/NorthShuna-Kuraymah/Commercial/Rent
- Facebook group "Commercial Jordan", Jubeiha shop with "small key money", rent JOD 600 (amount not stated). https://www.facebook.com/groups/commercialjordan/posts/2611955959178098/
- Internal: 01-market, 02-competition, 03-operations, 04-legal, 05-marketing, 06-financials. Model runs: `model-output.md`, owner-salary scenario, Prudent scenario (`assumptions-prudent.json` and `model-output-prudent.md`, kept in the session scratchpad).

## Open questions for the owner

1. Will you work the bar about 40 h a week yourself? If so, the third barista can be dropped (+JOD 5.9k NPV).
2. Can you fund about JOD 44–48k? Prudent startup plus a possible 12-month rent advance exceeds the JOD 40k budget.
3. Will landlords accept a licence condition precedent in the lease? Units whose landlords refuse should be dropped.
4. Will you trade through Ramadan daytime and the summer break, or close or shorten hours? Shorter hours would cut payroll in those months.
5. Do you have access to a licensed site, such as an office lobby or campus event, for a 2-week pop-up test?
