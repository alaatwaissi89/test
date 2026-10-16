# Petra surgical hospital, Wadi Musa (lean, expandable Phase 1: 20 beds)

Feasibility study for a 20-bed specialised surgical hospital with a 24/7 trauma ER, day surgery, endoscopy, general, orthopaedic, gynaecological and paediatric surgery. Owner: Alaa (orthopaedic surgeon). Version 3, 16 Oct 2026.

- `feasibility-study.md` / `.docx`: the report (Arabic, bank format, English executive summary first). Base = lean expandable model (land leased, compact 2,600 m² building with structure for a 3rd floor, refurbished CT, 96 staff).
- `model/ptc_model.py`: 10-year model (construction 2027–28, Y1 = 2029). `python3 ptc_model.py` regenerates `results.json`, `tables.md` and `PTC-financial-model.xlsx` (live formulas, checked against Python). Options A–D compared in `results.json` → `options`.
- `archive-v2-standard-build/`: version 2 (20 beds, land bought, full build: 7.48m funding, IRR 11.7%).
- `model/archive-30bed-trauma-only/`: version 1 (30-bed trauma only, failed).
- `sections/research-notes.md`: sourced findings with URLs. `inputs/`: owner-supplied files. `brief.md`: scope and changes.

Verdict v3: Go with conditions. Full funding 5.82m JOD (CBJ 2.5m + lease 0.5m + equity 2.01m + 0.81m standby), project IRR 16.0% with terminal value, DSCR 1.25 from 2032. Phase 2 (+20 beds, OR 3) about 1.3–1.4m when triggers are met.
