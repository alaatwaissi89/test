# 08 · Funding & Financing Options: Specialty Coffee Shop Unit, Al-Jubeiha, Amman

*Prepared by the funding-analyst agent, 15 Oct 2026. Currency: JOD. All program statuses were checked on 15 Oct 2026. Every loan figure (instalment, interest, cash to owner, NPV, payback) comes from `tools/fin_model.py`, run on copies of `scenarios/assumptions-prudent.json`. None were computed by hand. The scenario files are in `scenarios/funding/`.*

**Summary.**
- The Prudent plan costs **JOD 44,049**. Against the brief's JOD 40,000 of equity, that leaves a gap of **JOD 4,049**. It rises to about JOD 7–8k if the landlord wants a 12-month rent advance (07-risk R7).
- **Recommended structure (Assessment).** The owner puts in **JOD 28,000** of equity and borrows about **JOD 16,000** as a **bank start-up loan guaranteed by the Jordan Loan Guarantee Corporation (JLGC)**, over 5 years. The best entry points are Bank al Etihad's Business Start-up Loan (up to 12 months' grace) or Housing Bank's Start-ups Business Loan.
- At an assumed 10%, the model gives a repayment of **JOD 341 a month**. Owner NPV is **JOD 28,855**, against JOD 25,803 all-equity. Payback stays at month 37.
- The owner keeps **JOD 12,000 of personal cash in reserve**. The model shows the shop's own cash falling to about JOD 1.1k in month 7. In a −20% volume year it goes to −JOD 4.6k by month 12. That standby is what makes the plan survivable.
- **No grant open today fits a first-time, Amman-based café owner.** JEDCO's start-up grants are suspended, ISSF and Oasis500 fund tech companies, and the German "Leadership in Industry" grants are for manufacturers. USAID enterprise funding ended in 2025.
- Donor money reaches this project only **indirectly**, through EBRD, EIB and KfW lines lent on by banks and JLGC.
- **Confidence:** program terms are High where taken from official pages. Loan pricing is Low: no bank publishes its start-up rate, so 10% is an assumption.

---

## 1. Funding need

| Item | JOD | Source |
|---|---:|---|
| Prudent total startup cost (capex incl. JOD 5,000 key money, pre-opening, 3-month working-capital reserve 11,304) | **44,049** | `model-output-prudent.md` |
| Owner equity in the brief | 40,000 | brief.md (ASSUMPTION) |
| **Base funding gap** | **4,049** | derived |
| Extra cash if the landlord wants 12 months' rent in advance | ≈3,300 | 06-financials §6.1 |
| **Gap including a 12-month rent advance** | **≈7,350** | derived |
| Year-1 EBITDA (Prudent) | −3,475 (positive from month 8) | `model-output-prudent.md` |
| Lowest month-end cash in the business, all-equity | 3,494 (month 7) | derived from the model's monthly rows (§4) |

**Owner profile used (default, label: ASSUMPTION).** A Jordanian individual living in Amman, forming a single-owner LLC, first-time entrepreneur, with no collateral beyond personal guarantees. Some programs apply only if the owner is a **woman**, **under 30 or 35**, based **outside Amman**, a **vocational-training graduate** or a **refugee**. These are marked **Conditional** below.

**What lenders will see (Assessment).**
- A new LLC with no trading history.
- Year 1 is loss-making in the Prudent case.
- The sector is retail food and beverage, which is outside the Central Bank's priority-sector lists.

Banks will therefore lend mainly against **JLGC's guarantee, the owner's personal guarantee and a solid feasibility study**, not against cash flow. Microfinance products for established businesses usually need **12 months of trading**, so they suit a later top-up, not the start.

---

## 2. Programs screened (by category)

Status legend: **Open** = accepting applications now; **Recurring** = standing product or periodic calls; **Closed** = suspended, expired or withdrawn. "n/p" = not published. All checked 15 Oct 2026.

### 2a. Local banks

| Program · provider | Type | Amount | Rate / cost | Tenor · grace | Collateral / own share | Eligibility | Fit | Status | Src |
|---|---|---|---|---|---|---|---|---|---|
| Business Start-up Loan · Bank al Etihad | Loan | up to JOD 250,000; finances up to 80% of fixed assets | n/p | up to 60 mo · up to 12 mo grace | "minimal collateral"; asset and life insurance on main shareholder | Jordan-registered company operating < 5 years; needs feasibility study with cash flows, vocational licence, registration certificate | **Yes**. Grace covers the loss months. Note the 80%-of-fixed-assets cap (capex here is 26,860, so about 21.5k at most, derived) | Open | [B1] |
| Start-ups Business Loan Program · Housing Bank (HBTF) | Loan | up to JOD 500,000 | overnight interbank + bank margin | up to 6 yrs · n/p | **≥20% own contribution**; JLGC guarantee plus any collateral the bank asks for | Start-up SMEs operating ≤ 5 yrs; services incl. tourism eligible; fixed assets and working capital | **Yes** | Open | [B2] |
| SME lending (Quick Loan, POS loan, EIB facility) · Arab Bank | Loan | Quick Loan up to 30k; POS loan up to 100k | n/p | ≤36 mo | POS loan sized on card turnover | No start-up product listed | **Partial**. POS loan suits year 2, once there is card history | Recurring | [B3] |
| Capital Start · Capital Bank | Loan / package | n/p | n/p | n/p | n/p | SMEs | **Unknown**. No terms published; ask | Recurring | [B4] |
| Murabaha under JLGC "Guarantees for Employment" · Jordan Islamic Bank; also Islamic International Arab Bank | Islamic financing + guarantee | n/p | n/p (Sharia-compliant profit rate) | n/p | JLGC guarantee, KfW-funded | SMEs creating jobs for Jordanians (signed 24 Aug 2026) | **Yes/Partial**. The shop creates 3 jobs; terms TBC | Open (new) | [B5][B6] |
| CBJ financing programs via commercial banks (e.g. Jordan Kuwait Bank) | Concessional loan | n/p | "competitive" | n/p | n/p | Industry, tourism, agriculture, energy, transport, consulting, technical education | **No**. A retail café is not in these sectors | Recurring | [B7] |

Market pricing reference: the CBJ weighted-average rate on loans and advances was **7.95%** at end-Dec 2025 (8.14% on overdrafts). The CBJ policy rate is **5.75%** [C1]. No bank publishes its start-up loan rate.

**ASSUMPTION: 10% all-in for a guaranteed start-up loan.** This is the 7.95% average plus about 1 point for small-business risk and about 1 point for JLGC's fee, which banks normally pass on (JLGC does not publish its fee). It is tested at 12%. **Confidence: Low.**

### 2b. Microfinance and specialised lenders

| Program · provider | Type | Amount | Rate / cost | Tenor | Eligibility | Fit | Status | Src |
|---|---|---|---|---|---|---|---|---|
| Tamkeen Finance · Tamweelcom | Loan | JOD 300–3,000 | **31.8% declining** (≈18% flat) + 1% fee | 6–36 mo, no grace | Start-ups and home-based firms allowed ("age of project 0 or more") | **Partial**. Fast and open to start-ups, but small and expensive | Recurring | [M1] |
| Licensed Businesses loan · Tamweelcom | Loan | JOD 3,001–75,000 | 20.5–26.7% declining (11.4–15% flat) + 1% fee | 3–48 mo | Licensed business **operating ≥ 1 year** | **No at launch**. Yes for a year-2 top-up | Recurring | [M2] |
| Microfund for Women | Loan | small (Kiva avg loan ≈ US$1,017) | portfolio yield ≈ 30% | n/p | Women | **Conditional** (woman owner) | Recurring | [M3] |
| Vitas Jordan, FINCA, Ahli Microfinance, National Microfinance Bank | Loan | n/p | n/p | n/p | Micro and small businesses | **Partial**. Terms not retrieved; expect MFI pricing like the above | Recurring | [M4] |
| Development & Employment Fund (DEF) | Loan (incl. Islamic) | H1 2026: JOD 8.55m over 971 loans (≈8.8k average, derived); 2026 target JOD 27m | n/p | n/p | Jordanians; 38% of H1 loans went to women; all governorates | **Partial**. Plausible for 5–15k, but official terms not retrieved. Confidence Low | Open | [M5] |
| DEF × Ministry of Labour interest-free loans | Qard hasan | JOD 1,000–3,000 | **0%** | ≤60 mo, 3 mo grace | Jordanian, **age 18–45**, VTC graduate, home-based vocational project | **No/Conditional**. Home-based vocational only | Open (2026 allocation) | [M6] |

### 2c. Central Bank of Jordan programs

| Program | Type | Terms | Fit | Status | Src |
|---|---|---|---|---|---|
| **CBJ Program Guarantee for Financing Micro & Small Companies** (managed by JLGC; offered through banks, Islamic banks and MFIs) | Guarantee on a bank/MFI loan | **85% cover, loan up to JOD 25,000, up to 42 months** | **Yes**. Covers the recommended JOD 16k. The short tenor raises the instalment (§4) | Recurring (listed in JLGC's current programs and 2024 annual report) | [G1][G2] |
| CBJ start-up guarantee program via JLGC | Guarantee | Launched for start-ups; terms not on the announcement | **Yes**, through the bank | Recurring | [G3] |
| CBJ refinancing for "vital economic sectors" (JD 1.4bn) | Cheap refinancing to banks | **1.0% (Amman) / 0.5% (governorates)**, fixed for 10 years; 10 sectors | **No**. Retail F&B is not one of the sectors; a "tourist restaurant" classification is not realistic for a takeaway unit. Confidence Medium | Open | [C1][B7] |
| CBJ/MoPIC micro soft-financing window (2021) | Subsidised MFI loans | ≤ JOD 25k, borrower paid ≤ 5% (cost cap 9%), 85% JLGC | Would fit, but it was a 2021 allocation. No 2026 renewal found | **Closed / not confirmed** | [C2] |
| CBJ–IBRD programme via Housing Bank | Loan | LIBOR + 5.3–5.8% | LIBOR has been discontinued, so this is a legacy page | **Closed (legacy)** | [C3] |

### 2d. Government programs and guarantees

| Program · provider | Type | Terms | Fit | Status | Src |
|---|---|---|---|---|---|
| **JLGC Small Startups Program** | Guarantee | **85%**, loan ≤ JOD 500k, ≤ 96 months (also "Inhad for self-employment" variant, ≤ 250k, 84 mo) | **Yes**. The main route for the recommended loan | Open | [G1][G2] |
| JLGC Entrepreneurship Financing Program | Guarantee | 80%, ≤ JOD 75k, ≤ 96 mo | **Yes** (alternative) | Open | [G1] |
| JLGC SME / Micro Loan Guarantees; "Kafala" Islamic (trade) | Guarantee | 70%; SME ≤ 250k/72 mo; micro ≤ 15k/36 mo | **Yes** (lower cover) | Open | [G1] |
| JLGC **Guarantee for Employment** (funded by Germany/KfW) | Guarantee | Linked to new jobs for Jordanians. Partner banks so far: Bank al Etihad, Jordan Islamic Bank, IIAB | **Yes/Partial**. Terms on sme.jlgc.com | Open (launched H1 2026) | [G4][G5] |
| JEDCO "Tamkeen" grants | Grant ≤ JOD 50k | SMEs in services, tourism and creative sectors | Would partly fit an *operating* SME | **Closed** (deadline 30 Nov 2024) | [J1] |
| JEDCO grants/loans for new ventures and incubators | Grant/loan | — | — | **Closed** ("stopped for now") | [J2] |
| ISSF 2.0 (World Bank US$50m) | Equity / fund-of-funds | Tech: ICT, fintech, health, green, AI | **No** | Open | [W1] |
| "Leadership in Industry" (Germany €35m, MoITS / Industrial Development Fund) | Grant ≤ 25k micro, 70% (80% women-led) | **Industrial** MSMEs only | **No**; **Conditional** only if a roastery or manufacturing arm is added | Open (launched 28 Jun 2026) | [W2] |
| Investment Environment Law incentives | Tax/customs | — | **No**. 04-legal found no sector incentive for an Amman retail kiosk | — | 04-legal |

### 2e. International and foreign funders (all indirect, through local banks)

| Funder | Channel to this project | Fit | Status | Src |
|---|---|---|---|---|
| **EBRD** | US$25m subordinated loan to **Bank al Etihad** (9 Jul 2026), 40% for MSMEs incl. women- and youth-led. US$75m MSME credit line to **Housing Bank** (Apr 2025), focused on cities **outside Amman** | **Yes**, via those banks' start-up loans. Stronger fit if Conditional: woman, youth, or outside Amman | Open | [E1][E2] |
| **EIB** | Regional SME facility through Arab Bank; EIB lines to Tamweelcom and Microfund for Women | **Partial** (indirect) | Recurring | [B3][E3] |
| **KfW / German government** | Funds JLGC's Guarantee for Employment; "Leadership in Industry" grants | **Yes** (guarantee) / No (grants) | Open | [G4][W2] |
| **World Bank / IFC** | ISSF (tech equity); IFC investments in Tamweelcom | **No** direct / Partial via MFI | Open | [W1][M2] |
| **USAID** | Former SME and guarantee programs | **No** | **Closed**: USAID's Jordan programming was dismantled in 2025 | [U1] |
| **Arab Fund (AFESD), Kuwait Fund, OPEC Fund, Saudi Fund** | Sovereign soft loans to government; Arab Fund lines to Arab Bank (2014/2017) | **No direct window found** for a private café. Confidence Medium | n/a | [B3][A1] |
| **GIZ, ILO, UNDP, EU (incl. refugee/host-community livelihoods grants)** | Periodic small grant calls via NGOs | **Conditional** (refugee, host-community governorate, women or youth). No open call for an Amman first-time café owner was found in this search. Confidence Low (calls are irregular) | Recurring, not open now | — |

### 2f. Non-debt options

| Option | Terms / evidence | Fit | Status |
|---|---|---|---|
| Accelerators (Oasis500, Flat6Labs, ZINC) | Oasis500 makes seed investments in **tech and creative** start-ups [N1] | **No** for a single café unit | Recurring |
| Equipment leasing (Ejara Leasing serves SMEs; also Etihad Leasing, Al-Kawthar (Islamic), Tamallak, Specialized Leasing) [N2] | Terms n/p. Could finance the espresso machine and grinders (JOD 5,310 capex) | **Partial**. Ask for quotes | Recurring |
| Supplier credit (roaster or equipment dealer instalments) | ASSUMPTION: 3–6 months' credit on beans; dealer instalments on the machine | **Yes**. Ask during supplier quotes (03-operations) | — |
| Pre-sold drink passes | 07-risk K2: 100 × JOD 40 passes = JOD 4,000 in 3 weeks, refundable | **Yes**. Tests demand and funds opening stock | — |
| Family or a minority partner | Equity, no cost of debt; an LLC allows a second shareholder (04-legal) | **Yes** | — |
| Kiva (crowdfunded via Microfund for Women) [M3] | Small loans | **Conditional** (woman) | Recurring |

---

## 3. Shortlist (ranked by cost and likelihood of approval)

| # | Option | Amount for this project | Rate / cost | Why |
|---|---|---:|---|---|
| 1 | **Bank al Etihad Business Start-up Loan + JLGC guarantee** (Small Startups 85%, or Guarantee for Employment) | **≈ JOD 16,000** | ASSUMPTION ≈10% all-in (market average 7.95%); 60 months, **up to 12 months' grace** | Built for companies under 5 years old. The grace period covers the loss months. EBRD has just topped up its MSME lending |
| 2 | **Housing Bank Start-ups Business Loan + JLGC** | ≈ JOD 16,000 | Interbank + margin (≈10% ASSUMPTION); ≤ 6 yrs | Requires 20% own contribution, which is easily met (28k of 44k). Strongest EBRD backing, but its new line targets areas outside Amman |
| 3 | **CBJ Micro & Small Companies guarantee (85%, ≤ JOD 25k, ≤ 42 months)** via any participating bank or MFI | ≈ JOD 16,000 | Bank rate (≈10% ASSUMPTION) | Highest cover for a small ticket. 42 months means higher instalments: JOD 454 vs 341 a month |
| 4 | **Islamic murabaha under JLGC Guarantee for Employment** (Jordan Islamic Bank / IIAB) | ≈ JOD 16,000 | Profit rate n/p | Sharia-compliant alternative, KfW-backed, rewards the 3 jobs created |
| 5 | **Equipment lease or supplier instalments** for the espresso machine and grinders | ≈ JOD 5,300 | n/p (ask) | Cuts the bank ticket and is secured on the asset itself |
| 6 | Tamweelcom Tamkeen Finance (top-up only) | ≤ JOD 3,000 | 31.8% declining | Open to start-ups and fast, but the most expensive option; emergency use only |
| 7 | Pre-sold passes / family partner | JOD 4,000+ | 0% | Non-debt; also validates demand (07-risk K2) |

Conditional upgrades:
- **Woman owner:** Microfund for Women, EBRD and Bank al Etihad's women-led MSME allocation, and the 80% cover on German industrial grants (industrial only).
- **Age 18–45 and a VTC graduate:** DEF qard hasan, 0%, but home-based projects only.
- **Outside Amman:** the EBRD–Housing Bank line, and CBJ refinancing at 0.5% for eligible sectors.
- **Refugee or host community:** NGO livelihoods grants when calls open.

---

## 4. Funding structures run through the model

Method:
- Each structure is a copy of `assumptions-prudent.json` with only `financing` changed. The model was rerun with `python3 tools/fin_model.py <copy>.json`.
- The monthly instalment comes from the model's own `loan_payment()`.
- **Owner NPV** is the model's `npv()` at 16% applied to its "Cash to owner after loan service" row.
- **Lowest business cash** starts from the working-capital reserve. It then adds the model's monthly EBITDA, subtracts the model's monthly tax accrual and subtracts the instalment.
- **"Owner cash kept outside"** is JOD 40,000 minus the equity put in.

Scripts and outputs:
- Scenario files: `scenarios/funding/S*.json`, with outputs in the matching `.md` files.
- Derived-metrics script: `scenarios/funding/owner_metrics.py`.

**Limitation:** the model has **no grace period**, so repayments start in month 1. A 12-month grace period (Bank al Etihad) would improve year-1 cash beyond what is shown here.

| | S0 All equity | S1 Close the gap | **S2 Keep a reserve (recommended)** | S2b S2 at 12% | S2c CBJ program, 42 mo | S3 Microfinance |
|---|---:|---:|---:|---:|---:|---:|
| Equity | 44,049 | 40,000 | **28,000** | 28,000 | 28,000 | 34,049 |
| Loan | 0 | 4,049 | **16,049** | 16,049 | 16,049 | 10,000 |
| Rate · term | — | 10% · 5 y | **10% · 5 y** | 12% · 5 y | 10% · 42 mo | 20.5% · 4 y |
| Monthly debt service | 0 | 86 | **341** | 357 | 454 | 307 |
| Total interest | 0 | 1,113 | **4,411** | 5,371 | 3,038 | 4,735 |
| Cash to owner Y0 | −44,049 | −40,000 | **−28,000** | −28,000 | −28,000 | −34,049 |
| Cash to owner Y1 | −3,475 | −4,508 | **−7,567** | −7,759 | −8,929 | −7,159 |
| Cash to owner Y2 | 16,743 | 15,775 | **12,906** | 12,769 | 11,500 | 13,371 |
| Cash to owner Y3 | 30,205 | 29,221 | **26,305** | 26,156 | 24,864 | 26,728 |
| Cash to owner Y5 | 47,561 | 46,540 | **43,514** | 43,333 | 47,561 | 47,561 |
| Year-1 net profit | −15,352 | −15,727 | **−16,840** | −17,144 | −16,775 | −17,239 |
| Project NPV (model) | 25,803 | 25,904 | **26,204** | 26,294 | 26,040 | 26,211 |
| **Owner NPV @16%** | 25,803 | 26,573 | **28,855** | 28,316 | 28,335 | 25,903 |
| Owner IRR | 31.1% | 32.5% | **38.1%** | 37.7% | 36.8% | 33.4% |
| Payback (project) | m37 | m37 | **m37** | m37 | m37 | m37 |
| Lowest business cash (month) | 3,494 (m7) | 2,892 (m7) | **1,107 (m7)** | 995 (m7) | 313 (m7) | 1,345 (m7) |
| Owner cash kept outside (vs 40k) | **−4,049 (over budget)** | 0 | **12,000** | 12,000 | 12,000 | 5,951 |
| **Total liquidity at the low point** (business + owner standby) | −555 | 2,892 | **13,107** | 12,995 | 12,313 | 7,296 |

Notes:
- Total liquidity is derived (sum of the two rows above).
- Project NPV rises slightly with debt because the model deducts interest before tax.

**Stress test of S2 (Prudent + volume −20%).**
- Owner NPV **−6,396**, project NPV −9,047, payback month 53.
- Business cash bottoms at **−4,611 in month 12**.
- The owner's JOD 12,000 standby covers that shortfall and still leaves about JOD 7.4k (derived).
- Under all-equity, the same shortfall would have to be met from cash the owner does not have, since the budget is already exceeded.

**Reading (Assessment).**
1. **S1 closes the gap cheaply** (JOD 86 a month), but leaves the owner with no cash outside the business. Banks rarely bother with a JOD 4k start-up ticket, so S1 is better done through supplier credit or a lease than through a bank.
2. **S2 is the best balance.** It raises owner NPV by about JOD 3k and keeps JOD 12k liquid with the owner, which is the cushion that matters given the GAM licensing risk and seasonal dips (07-risk R1 and R4). The JOD 341 instalment is about 4–5% of planned monthly revenue in months 8–12, and less after that. That comparison is Assessment against the model's monthly revenue.
3. **S2c (the CBJ 42-month program)** costs less interest but leaves only JOD 313 in the business at month 7. Use it only if the bank pairs it with a grace period, or if the 85% CBJ cover is the only guarantee offered.
4. **S3 (microfinance)** is the costliest per dinar, and the larger Tamweelcom product needs 12 months of trading anyway. Keep it as a year-2 option.
5. Debt does not fix the project's real risk. If volume misses by 20%, every structure loses value. Licensing (K1) and demand (K2) tests come **before** any loan application.

---

## 5. Application roadmap

| Step | When (month vs lease) | Action | Documents |
|---|---|---|---|
| 1 | M−2 | Pass the pre-lease licence test (07-risk K1) and demand test (K2). **Do not apply for debt before both pass** | GAM zoning certificate, preliminary approval |
| 2 | M−2 | Ask 3 banks for indicative terms: Bank al Etihad, Housing Bank, and Jordan Islamic Bank or IIAB. Ask for: rate, JLGC program used (Small Startups 85% vs CBJ micro 85% vs Guarantee for Employment), JLGC fee, **12-month grace**, collateral and personal guarantee | ID, this feasibility study with 5-year cash flows (06/07), CV showing barista hire plan |
| 3 | M−2 | Ask the equipment dealer and roaster for instalment and credit terms; get a lease quote (Ejara, Etihad Leasing) for the espresso machine and grinders | Supplier quotes (03-operations) |
| 4 | M−1 | Register the LLC (04-legal). Banks need a registration certificate under 3 months old and, for Bank al Etihad, a **vocational licence**. That means the GAM licence path must be in progress first | Memorandum of association, registration certificate, Chamber of Commerce membership |
| 5 | M0 | Submit the formal application. The bank applies to JLGC via sme.jlgc.com. **ASSUMPTION:** 3–6 weeks to decision | Signed lease (with licence condition precedent), vocational licence or GAM approval, fit-out quotes, insurance on assets, life insurance on owner |
| 6 | M0–M1 | Disbursement against equipment invoices and fit-out; keep the JOD 12k standby in a separate personal account | Invoices, proof of 28k equity injection |
| 7 | M12+ | Once trading, consider a Tamweelcom or Arab Bank POS loan only if expansion is needed | 12 months' statements, POS turnover |

Timing risk: a bank loan needs the licence, and the licence needs the lease. Negotiate a lease with a 90-day licence condition (07-risk K1). Fund fit-out deposits from equity until the loan disburses.

---

## Key numbers handed to other agents

```yaml
currency: JOD
date_checked: 2026-10-15
total_startup_cost_prudent: 44049
equity_budget: 40000
funding_gap: 4049                  # ~7350 with a 12-month rent advance
recommended_structure: "Equity 28,000 + JLGC-guaranteed bank start-up loan (Bank al Etihad or Housing Bank), owner keeps 12,000 standby"
equity_in: 28000
loan_amount: 16049
loan_rate: 0.10                    # ASSUMPTION: CBJ avg 7.95% (Dec 2025) + SME premium + JLGC fee; tested at 12%
loan_years: 5
grace_months_available: 12         # Bank al Etihad; not modelled
guarantee: "JLGC Small Startups 85% (<=500k, <=96 mo) or CBJ Micro&Small 85% (<=25k, <=42 mo)"
grant_amount: 0                    # no open grant fits an Amman first-time cafe owner
monthly_debt_service: 341          # model loan_payment(); 357 at 12%; 454 on a 42-month CBJ tenor
total_interest_5y: 4411
owner_npv_16pct: 28855             # vs 25,803 all-equity
project_npv: 26204
payback_month: 37
lowest_business_cash: 1107         # month 7; owner standby 12,000 outside the business
stress_volume_minus20: {owner_npv: -6396, lowest_business_cash: -4611, month: 12}
confidence: {program_terms: High, loan_pricing: Low, grant_availability: Medium}
```

## Sources

- [B1] Bank al Etihad, "Business Start-up Loan" (product page, checked 15 Oct 2026). https://www.bankaletihad.com/business/business-loans/business-start-up-loan
- [B2] Housing Bank, "Start-ups Business Loan Program" (checked 15 Oct 2026). https://hbtf.com/en/corporate/credit-programs/start-ups-business-loan-program
- [B3] Arab Bank, "SME Lending Solutions" (checked 15 Oct 2026). https://www.arabbank.com.jo/mainmenu/home/SMEs_Banking/sme-lending-solutions
- [B4] Capital Bank, "Capital Start" (no terms published). https://capitalbank.jo/en/institutional/sme/banking-programs/capital-start
- [B5] Jordan Islamic Bank, "Agreement… to launch the Guarantees for Employment program", 3 Sep 2026. https://www.jordanislamicbank.com/en/news/an-agreement-between-jordan-islamic-bank-and-loan-guarantee-to-launch-the-guarantees-for-employment-program-2
- [B6] JLGC news, "JLGC and Islamic International Arab Bank sign Kafala agreement for Guarantees for Employment". https://www.jlgc.com/en/news/jlgc-and-islamic-international-arab-bank-sign-kafala-agreement-for-guarantees-for-employment
- [B7] Jordan Kuwait Bank, "CBJ Financing Programs" (sector list). https://jkb01jo2022.dev2.dot.jo/en/midsize-business/cbj-financing-programs (staging mirror of the bank's site; Medium confidence)
- [C1] Central Bank of Jordan, "Recent Monetary & Economic Developments in Jordan", January 2026 (rates at end-Dec 2025; refinancing program). https://www.cbj.gov.jo/ebv4.0/root_storage/en/eb_list_page/january_2026-0.pdf
- [C2] Jordan Times, "CBJ, Planning Ministry launch JD21m soft financing programme for micro businesses", 21 Dec 2021. https://jordantimes.com/node/349545
- [C3] Housing Bank, "First Central Bank Program in cooperation with IBRD" (legacy page). https://hbtf01jo2026.dev2.dot.jo/en/first-central-bank-program-in-cooperation-with-international-bank-for-reconstruction-and-development
- [G1] JLGC, "Loan Guarantee Programs" (coverage, ceilings, tenors; checked 15 Oct 2026). https://jlgc.com/en/service/programs/loan-guarantee-programs
- [G2] JLGC, Annual Report 2024 (31st). https://www.jlgc.com/uploads/2025/06/jlgc-31-annual-report-2024-en.pdf
- [G3] JLGC news, "The Central Bank of Jordan launched new program for startups guarantee managed by JLGC". https://jlgc.com/en/news/the-central-bank-of-jordan-launched-new-program-for-startups-guarantee-managed-by-jlgc
- [G4] Jordan News, "JLGC Revenue Rises to JOD 34.2 Million in H1 2026", 3 Aug 2026. https://www.jordannews.jo/Section-33/Trade-Industry/JLGC-Revenue-Rises-to-JOD-34-2-Million-in-H1-2026-53778
- [G5] JLGC news, "JLGC and Bank al Etihad sign agreement to expand business financing and link it to job creation", 9 Sep 2026. https://jlgc.com/en/news/jlgc-and-bank-al-etihad-sign-agreement-to-expand-business-financing-and-link-it-to-job-creation
- [M1] Tamweelcom, "Tamkeen Finance". https://tmw01jo2022.dev2.dot.jo/en/loan/business/tamkeen-finance (staging mirror of tamweelcom.jo; Medium confidence)
- [M2] Tamweelcom, "Licensed Businesses". https://tmw01jo2022.dev2.dot.jo/en/loan/business/licensed-businesses (as above)
- [M3] Kiva, Microfund for Women partner page. https://kiva.org/partners/550
- [M4] UN-ESCWA SME portal, "Vitas Jordan". https://smeportal.unescwa.org/financing/vitas-jordan
- [M5] Jordan News, "Development and Employment Fund: 8.5 Million Dinars in Financing for the First Half of 2026", 11 Jul 2026. https://www.jordannews.jo/Section-33/Trade-Industry/Development-and-Employment-Fund-8-5-Million-Dinars-in-Financing-for-the-First-Half-of-2026-52939 (news only; Low confidence on terms)
- [M6] Jordan News, "Agreement to Grant Interest-Free Loans to Vocational Training Graduates", 4 Apr 2026. https://www.jordannews.jo/Section-109/News/Agreement-to-Grant-Interest-Free-Loans-to-Vocational-Training-Graduates-50301
- [J1] JEDCO, "Tamkeen Program Supporting SMEs in Jordan". https://jedco.gov.jo/En/NewsDetails/Tamkeen_Program_Supporting_Small_and_Medium_Enterprises_in_Jordan
- [J2] JEDCO Services Guide, "Grants or Loans for New Ventures / Business Incubators (Stopped for Now)". https://jedco.gov.jo/EN/ListDetails/Services_Guide/39/6
- [W1] World Bank, ISSF 2.0 factsheet, Apr 2025. https://thedocs.worldbank.org/en/doc/8d85a1355064cab2cd727d7484f20df3-0280012025/original/wb-jo-ISSF2-Factsheet-en-FINAL07042025.pdf
- [W2] Petra, "Jordan launches €35 million programme to boost industrial competitiveness, support small businesses", 28 Jun 2026. https://www.petra.gov.jo/en/news/jordan-launches-35-million-programme-to-boost-industrial-competitiveness-support-small-businesses
- [E1] EBRD, "EBRD to expand green and inclusive finance in Jordan" (Bank al Etihad), 9 Jul 2026. https://www.ebrd.com/home/news-and-events/news/2026/ebrd-to-expand-green-and-inclusive-finance-in-jordan.html
- [E2] EBRD, "EBRD partners with Jordan's HBTF to enhance small businesses", 6 Apr 2025. https://www.ebrd.com/home/news-and-events/news/2025/ebrd-partners-with-jordan-s-hbtf-to-enhance-small-businesses.html
- [E3] EIB project 20210090 (Tamweelcom). https://www.eib.org/en/projects/all/20210090
- [U1] International Growth Centre, "Setbacks and opportunities in the wake of USAID's Jordan withdrawal", 23 Sep 2025. https://www.theigc.org/publications/setbacks-opportunities-wake-usaids-jordan-withdrawal
- [A1] Ministry of Planning, "Gov't, AFESD sign soft loan agreement worth $100m". https://mop.gov.jo/En/NewsDetails/Gov%E2%80%99t_AFESD_sign_soft_loan_agreement_worth_100m
- [N1] KAFD, Oasis500 project page. https://kafd.jo/en/ProjectCoDesc.aspx?pid=7
- [N2] Jordan Financial Services directory, "Leasing Companies". https://www.jordanfinancialservices.com/2024/company-category/leasing-companies
- Internal: 04-legal.md, 06-financials.md, 07-risk.md, `scenarios/assumptions-prudent.json`, `scenarios/model-output-prudent.md`, `tools/fin_model.py`.

## Open questions for the owner

1. **Profile.** Are you a woman, aged 18–35 (or 18–45 with a VTC certificate), resident outside Amman, or a refugee? Each opens conditional programs (§3).
2. **Cash and collateral.** Can you commit JOD 28k now and hold JOD 12k aside? Can you offer a personal guarantee or a salaried co-guarantor? Do you own property?
3. **Islamic or conventional** financing preference?
4. **Bank relationship.** Where do you bank today? An existing relationship speeds approval and may improve pricing.
5. **Grace period.** Will you push for 12 months' grace? It matters most in the Prudent case, where EBITDA is negative until month 8.
6. **Partner.** Would you accept a family member or a minority partner (LLC) instead of debt?
7. **Equipment.** Would you lease, or buy used (about JOD 1,800 saved, 07-risk R7)? Either reduces the loan.
