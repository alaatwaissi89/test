# Shared research rules (every agent follows these)

1. **No invented numbers.** Every figure (market size, price, wage, rent, growth rate, tax rate, cost) carries a source: publisher, title, year, URL. If no source exists, label it `ASSUMPTION` and state the reasoning (e.g. "derived: 3 suppliers quoted 2.1–2.6 JOD/kg, midpoint used").
2. **Local first.** Use data for the project's actual country/city and currency. Global figures only as context, and flagged as such.
3. **Recency.** Prefer data from the last 3 years. Older data is marked with its year and adjusted (inflation, growth) with the adjustment shown.
4. **Triangulate.** Any number that drives the decision (market size, price, volume, capex, main opex lines) needs at least 2 independent sources or a source plus a bottom-up check. Report the range, then the value used and why.
5. **Confidence.** Tag every key finding High / Medium / Low confidence.
6. **Separate fact from judgement.** Facts cite sources; opinions are labelled "Assessment".
7. **Output format.** Write your section as Markdown to the path the orchestrator gives you, ending with a `## Sources` list and a `## Key numbers handed to other agents` block (YAML) so the next agent can use them without re-reading prose.
8. **Gaps.** End with `## Open questions for the owner`: anything only the client can answer (budget, location, licences already held).
