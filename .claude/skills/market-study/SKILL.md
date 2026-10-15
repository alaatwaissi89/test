---
name: market-study
description: Run a sourced market and competition study (TAM/SAM/SOM, growth, customer segments, competitor map, price benchmark, gaps, positioning) for a business idea in a specific location. Use when the user wants only the market study part of a feasibility study, or a quick market check before a full study.
---

# Market & Competition Study

Produce a decision-ready market study for one business idea in one location. Run two research tracks in parallel (spawn two agents if you can), then merge.

## Rules
1. No invented numbers: each figure has publisher, title, year and URL, or is labelled `ASSUMPTION: reasoning`.
2. Local data first (country, city, local currency); global data only as flagged context. Prefer the last 3 years.
3. Triangulate decision-driving numbers: two sources, or a source plus a bottom-up check; give the range and the value used.
4. Tag findings High / Medium / Low confidence; label opinions "Assessment".

## Track A: Market
1. Define the market (category, geography, B2C/B2B).
2. Size it top-down (industry reports, statistics office, import/trade data) and bottom-up (target customers × purchase frequency × average spend). Reconcile into TAM → SAM → SOM for years 1–3, showing the share assumptions.
3. Growth rate with source; drivers and trends (demographics, income, behaviour, seasonality).
4. 2–4 customer segments with size, needs and willingness to pay.
5. Demand evidence: search interest, marketplace/app activity, reviews of similar businesses.

## Track B: Competition
1. Direct and indirect competitors from maps listings, directories, delivery apps, marketplaces, websites and news.
2. Table of the top 5–10: offer, price points (with source and date checked), size, ratings and review count, strengths and weaknesses taken from reviews.
3. Price benchmark: min / median / max for the core product.
4. Five forces, each Low / Medium / High with evidence; barriers to entry.
5. Gaps: recurring review complaints, unserved segments or areas, price gaps → recommended positioning and launch price.

## Output
One Markdown document: Summary (attractiveness 1–5, recommended positioning and price, SOM) · Market size table · Growth and trends · Segments · Competitor table · Price benchmark · Five forces · Gaps and positioning · Key numbers (YAML: tam, sam, som_year1..3, cagr, avg_spend, price_min/median/max, competitor_count) · Numbered sources · Open questions for the owner (site footfall, budget, anything only they know).

Publish it as a document for the user and lead your reply with the verdict and the 3 numbers that matter most.
