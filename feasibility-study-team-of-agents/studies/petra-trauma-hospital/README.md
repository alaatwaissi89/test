# Petra surgical hospital (20 beds), Wadi Musa

Feasibility study for a 20-bed specialised surgical hospital with a 24/7 trauma ER, day surgery, general, orthopaedic, gynaecological and paediatric surgery. Owner: Alaa (orthopaedic surgeon). Prepared 16 Oct 2026 with the feasibility-study team workflow.

- `feasibility-study.md` / `.docx`: the report (Arabic, bank format, English executive summary first).
- `model/ptc_model.py`: 10-year model (construction 2027–28, Y1 = 2029). Run `python3 ptc_model.py` to regenerate `results.json`, `tables.md` and `PTC-financial-model.xlsx` (live formulas; matches Python).
- `model/archive-30bed-trauma-only/`: the first 30-bed trauma-only version, dropped after the owner changed the scope (it failed: NPV −2.9m).
- `sections/research-notes.md`: all sourced findings with URLs.
- `inputs/`: owner-supplied files (reference study Ennab 2025, MoH licensing guide 2026).
- `brief.md`: scope, defaults and changes.

Verdict: Go with conditions (thin). Base: JOD 7.48m fully funded, project IRR 11.7% with terminal value, DSCR ≥1.25 from 2033. Key condition: MoH must accept a 20-bed multi-surgical hospital as "specialised".
