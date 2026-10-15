# Abu Ghazi Village, Wadi Musa: feasibility study

Bank-format study (Arabic, English executive summary) for the Abu Ghazi Village heritage and commercial complex in Wadi Musa, Petra. Prepared 15 Oct 2026 with the feasibility-study team. JOD; Year 1 = March 2027 to February 2028.

| File | What it is |
|---|---|
| `feasibility-study.md` / `.docx` | The full study (also a Google Doc in the Drive folder `studies/abu-ghazi-village`) |
| `model/agv_model.py` | Study model: 10 years, grace-period debt, funding, gallery and stress scenarios. Run `python3 model/agv_model.py` |
| `model/AGV-financial-model.xlsx` | Excel model with live formulas (Inputs, Debt, CashFlow) plus scenario tables |
| `model/tables.md`, `model/results.json` | Model outputs used in the study |

Recommended structure: JOD 165,000 under the CBJ economic-sectors programme (tourism, outside Amman, floor 3.25%), 12 months' grace then 108 payments of JOD 1,764.15, plus JOD 20,000 owner cash. Year-2 DSCR 1.53. Gallery Phase 1 as a separate conditional JOD 50,000 tranche.

## Note for the team folder
The team's `tools/fin_model.py` is a 5-year model with no grace period and no rent lines, so it could not run this project. `model/agv_model.py` is a study-specific model. Adding grace periods, multiple facilities, a 10-year horizon and DSCR to the shared tool would let future bank-format studies use it directly.
