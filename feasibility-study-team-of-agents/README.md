# Feasibility Study Team of Agents

A team of AI agents that turns a business idea into a full, sourced feasibility study (دراسة جدوى): market study, competition, technical and operational study, legal and regulatory study, marketing plan, financial model, risk assessment and a final report with a clear Go / No-go verdict.

## How to use it
Give Claude your idea, for example: *"Feasibility study for a specialty coffee kiosk in Amman, budget 40,000 JOD."* The `feasibility-study` skill runs the team. Include the location and your budget if you can; the team asks once for anything important that is missing.

## The team
| Agent | Produces |
|---|---|
| `orchestrator` | Project brief, task dispatch, quality gate, final delivery |
| `market-analyst` | Market size (TAM/SAM/SOM), growth, segments, demand evidence |
| `competitor-analyst` | Competitor map, price benchmark, five forces, gaps |
| `legal-regulatory-analyst` | Legal form, licences, taxes, labour rules, compliance |
| `technical-operations-analyst` | Location, equipment, staffing, suppliers, capex and opex |
| `marketing-strategist` | Positioning, pricing, channels, sales forecast |
| `financial-analyst` | Assumptions file, model run, 5-year financials, NPV/IRR/payback |
| `risk-analyst` | Risk register, scenarios, killer assumptions |
| `report-writer` | The final study document |

Workflow: intake → (market, competition, legal in parallel) → (operations, marketing in parallel) → financials → risk → quality gate → report.

## Accuracy rules
Every number carries a source with URL or is labelled as an assumption with its reasoning; key numbers are triangulated; financials are computed only by `tools/fin_model.py`, never by hand. See `agents/_shared-research-rules.md`.

## Folder contents
- `agents/` agent definitions (Claude Code subagent format)
- `skills/feasibility-study/SKILL.md` the orchestrator skill
- `tools/fin_model.py` the financial model (5-year P&L, cash flow, break-even, NPV, IRR, payback, sensitivity, Excel export)
- `templates/` assumptions template and report outline
- `demo/` a complete sample study

These are research tools, not professional financial or legal advice; confirm licensing and tax points with a local accountant or lawyer before investing.
