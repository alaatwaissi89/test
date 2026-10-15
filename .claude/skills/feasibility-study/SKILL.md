---
name: feasibility-study
description: Run a full, sourced feasibility study (market, competition, operations, legal, marketing, financials, risk, final report) for any business idea using a team of specialist agents. Use when the user gives a business or project idea and asks for a feasibility study, دراسة جدوى, business plan viability, or "is this idea worth it".
---

# Feasibility Study Team

You are the **orchestrator** of a team of specialist agents. Given a business idea, you produce a complete, decision-ready feasibility study in which every number is sourced or clearly labelled as an assumption.

## Research rules (paste into every agent brief)
1. No invented numbers. Every figure has a source (publisher, title, year, URL) or is labelled `ASSUMPTION: reasoning`.
2. Local first: the project's own country, city and currency. Global data only as flagged context.
3. Prefer data from the last 3 years; older data shows its year and any adjustment.
4. Decision-driving numbers (market size, price, volume, capex, main costs) need 2 independent sources or a source plus a bottom-up check. Give the range, the value used, and why.
5. Tag key findings High / Medium / Low confidence. Label opinions "Assessment".
6. For Jordan, check `jordan-data-sources.md` in the team folder first for trusted sources by topic.
7. Each section ends with `## Sources`, a `## Key numbers` YAML block for the next agents, and `## Open questions for the owner`.

## Step 0: Intake
If the user gives a filled Business Idea Intake Form (`feasibility-study-team-of-agents/templates/business-idea-intake.md` in the team folder, or its Google Doc copy in their Drive folder), build the brief from it: owner answers are facts (cite as "owner"), and their quotes and prices take priority over researched estimates. Pass section 6 (owner profile) to the funding analyst and section 5 (money) to the financial analyst. If the user gives only a one-line idea, offer the form, but don't wait for it.
Write `brief.md`: concept, country/city, target customers, scale, currency, available capital, timeline, owner experience. Ask the user once for what is missing that changes the answer (location and budget matter most). If they don't answer, choose defaults, mark them `ASSUMPTION`, and continue. Write the report in the user's language.

## Step 1 (parallel): spawn 3 agents with the brief
**Market analyst → `sections/01-market.md`.** Define the market; size it top-down (reports, statistics office) and bottom-up (target customers × frequency × spend) and reconcile into TAM/SAM/SOM; growth rate and trends; 2–4 customer segments with willingness to pay; demand evidence. Key numbers: tam, sam, som_year1..3, cagr, avg_spend, purchase_frequency, target_customers.

**Competitor analyst → `sections/02-competition.md`.** Direct and indirect competitors from maps listings, directories, delivery apps, marketplaces, websites, news. Table of top 5–10: offer, price points (source + date), size, ratings, strengths/weaknesses from reviews. Price benchmark (min/median/max), five forces with evidence, gaps, recommended positioning. Key numbers: competitor_count, price_min, price_median, price_max.

**Legal & regulatory analyst → `sections/04-legal.md`.** Official sources first. Legal entity options and minimum capital; licences and permits (authority, fee, time); corporate tax, VAT; minimum wage and social security rates; standards and compliance; red flags. Note it is research, not legal advice. Key numbers: corporate_tax_rate, vat_rate, social_security_employer_rate, setup_fees_total, months_to_license.

## Step 2 (parallel): spawn 2 agents with the brief + step 1 key numbers
**Technical & operations analyst → `sections/03-operations.md`.** Operating model and daily capacity; location with rent from 3+ current listings; itemised equipment with sourced prices and useful life; staffing with salaries from minimum wage, surveys or job listings plus employer contributions; unit cost of goods from supplier prices; utilities and running costs; launch timeline. Key numbers: capex_items, fixed_opex_monthly, cogs_per_unit, max_units_per_month, headcount, payroll_monthly, months_to_launch.

**Marketing strategist → `sections/05-marketing.md`.** Positioning against the gaps; price per product justified against the benchmark; channels with local cost benchmarks and platform commissions; 90-day launch plan; marketing budget; sales ramp for months 1–12 and years 2–5 built from capacity, SOM and conversion, with reasoning. Key numbers: price_per_unit, units_month1..12, units_year1..5, marketing_monthly_y1, marketing_pct_revenue_later, channel_commission_pct.

## Step 3: Financial analyst → `sections/06-financials.md`
Never compute financials by hand. Fill `assumptions.json` (schema below) from the key numbers, add sourced discount rate (policy rate + risk premium), inflation, and loan terms if any. Run `python3 tools/fin_model.py assumptions.json financial-model.xlsx` (the model ships in the feasibility-study-team-of-agents folder / repo; if it is not present, recreate it from the `feasibility-financial-model` skill). Prices go in net of VAT; salaries go in gross (the model adds employer contributions once). Sanity-check margins against an industry benchmark and break-even against capacity; if net margin is far above the benchmark or the owner is unpaid, also run a prudent scenario (owner salary, realistic staffing, seasonality, lower volume, higher costs) on a copy of the assumptions and use it as the planning case. Fix assumptions and rerun, never edit outputs. Write startup costs, funding, 5-year P&L, cash flow, break-even, NPV, IRR, payback, ROI, sensitivity, and a plain-language reading.

## Step 3b: Funding analyst → `sections/08-funding.md`
Find and match financing for this project, official provider pages first: local banks and Islamic financing; microfinance and specialised lenders; central bank programs and loan guarantees; government support programs and grants; international and foreign donor programs (development banks, aid agencies, Arab funds, EU/UN programs); equity, accelerators, crowdfunding, supplier credit and leasing. For every program: provider, type, amount, rate/cost, tenor and grace, collateral, eligibility, fit with this project (Yes / Partial / No and why), how to apply, status (open / recurring / closed, date checked), source URL. Shortlist the 5–8 best fits; build 2–3 funding structures covering the startup cost and run each through the model by setting `financing` in a copy of `assumptions.json`; give an application roadmap. Ask for owner details that change eligibility (age, gender, nationality, governorate). For Jordan, use `jordan-data-sources.md` in the team folder if present. Key numbers: funding_gap, recommended_structure, loan_amount, loan_rate, loan_years, grant_amount, monthly_debt_service.

## Step 4: Risk analyst → `sections/07-risk.md`
Risk register of 10–15 risks (market, competition, operations, finance, legal, macro) with likelihood × impact, early warning sign, mitigation. Pessimistic / base / optimistic scenarios from the model's sensitivity table. The 2–3 killer assumptions and a cheap way to test each before investing.

## Step 5: Quality gate (you)
Check every decision-driving number has a source or labelled assumption; numbers agree across sections (price, staff count vs payroll, capex totals); location and currency consistent. Return failing sections to their agent with the exact fix; at most 2 rounds.

## Step 6: Report writer → `feasibility-study.md`
Cover · Executive summary (verdict Go / Go with conditions / No-go with reason; startup cost; recommended funding structure; break-even; NPV/IRR/payback; top 3 risks; top 3 conditions) · Project description · Market · Competition · Marketing & sales · Technical & operations · Legal · Financials · Funding · Risk · Conclusions and next steps · Appendices: assumptions table, numbered sources, open questions. No new numbers; keep source references; report conflicts instead of picking one. Publish as a document for the user.

## Reply to the user
Verdict, the 3 numbers that matter (startup cost, break-even month, NPV or IRR), top 3 risks, and the questions only they can answer, with a link to the full report.

## assumptions.json schema
```json
{
  "project": "", "currency": "JOD",
  "capex": [{"name": "", "amount": 0, "life_years": 5, "source": ""}],
  "pre_opening_costs": [{"name": "", "amount": 0, "source": ""}],
  "working_capital_months": 3,
  "revenue_streams": [{"name": "", "price": 0, "unit_cost": 0,
    "units_month_y1": [12 numbers], "units_year": [ignored, y2, y3, y4, y5]}],
  "price_growth": 0.0, "channel_commission_pct": 0.0,
  "fixed_opex_monthly": [{"name": "", "amount": 0, "source": ""}],
  "opex_inflation": 0.0,
  "payroll": [{"role": "", "count_by_year": [1,1,1,1,1], "monthly_salary": 0}],
  "employer_contribution_rate": 0.0, "salary_growth": 0.0,
  "marketing": {"monthly_y1": 0, "pct_revenue_after_y1": 0.03},
  "corporate_tax_rate": 0.0,
  "financing": {"loan_amount": 0, "loan_rate": 0.0, "loan_years": 5},
  "discount_rate": 0.12, "residual_value_pct": 0.0
}
```
