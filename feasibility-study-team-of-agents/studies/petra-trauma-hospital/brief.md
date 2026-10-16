# Project brief: Petra Trauma Hospital (30 beds), Wadi Musa, Ma'an governorate

Prepared 16 Oct 2026 by the orchestrator from the owner's one-line request:
"اعمل لي دراسة جدوى متكاملة لمشروع مستشفى صغير بقدرة ٣٠ سرير في محافظة معان البتراء، مستشفى إصابات trauma center".
The intake form was not filled; everything below marked ASSUMPTION is a default the owner must confirm.

## Concept
A private 30-bed trauma and orthopaedic hospital ("trauma center") in Wadi Musa (Petra district, Ma'an governorate, Jordan), serving:
1. Road traffic accidents on the Desert Highway (Highway 15), King's Highway and the Wadi Musa / Petra roads.
2. Tourist injuries at Petra (falls, fractures, heat illness, animal-ride accidents) and trekking routes (Jordan Trail, Little Petra, Wadi Rum transfers). Paying via travel insurance / assistance companies and cash.
3. Local population of Petra district and southern Ma'an (orthopaedic elective and trauma surgery, emergency care), paying via private insurance, MoH/RMS referral contracts, and cash.

## Scale and services (ASSUMPTION, owner to confirm)
- 30 inpatient beds: 22 surgical / orthopaedic ward beds (mix of private and semi-private rooms), 6 ICU/HDU beds, 2 isolation/monitored beds.
- 24/7 emergency department with ~8 bays incl. 1 resuscitation bay; helipad-ready roof or ground pad (optional).
- 2 operating theatres (one orthopaedic/trauma, one general/emergency) + recovery.
- Imaging: digital X-ray, CT (64-slice minimum), ultrasound, C-arm in theatre; MRI deferred to phase 2.
- Laboratory, blood bank storage, pharmacy, CSSD, physiotherapy and rehabilitation.
- Owner is an orthopaedic surgeon and will be medical director / lead surgeon.

## Location and premises (ASSUMPTION)
- Wadi Musa, Petra district, Ma'an governorate. Site not yet chosen.
- Base case: new purpose-built building of ~4,000–5,000 m² on land the owner or family provides (land cost excluded from capex but shown as owner's in-kind equity at a market value to be verified). Alternative: lease/convert an existing building (e.g. hotel) — evaluate briefly.

## Money and timing (ASSUMPTION)
- Currency: JOD. Owner's available cash unknown; assume owner equity of 25–30% of total cost (incl. land in kind) and the rest from debt/partners. Funding analyst to find best-fit programmes.
- Timeline: licensing and design 2027, construction and fit-out 2027–2028, opening ~Q1 2029 (Year 1 = 2029). Agents may propose a more realistic timeline with evidence.

## Owner profile
- Jordanian orthopaedic surgeon (exact age, gender, governorate of residence to be confirmed). Assume Jordanian national, from/with family links to Wadi Musa (the project's other study, Abu Ghazi Village, is a Wadi Musa family project).

## Output
- Final report in Arabic with English executive summary, bank format. Every figure tagged [SOURCE], [ASSUMPTION] or [VERIFY].
- Folder: studies/petra-trauma-hospital/ (sections/ for agent sections, model/ for the model).

## Update 16 Oct 2026, 07:21 (owner message + 2 attachments)
Owner: "استعن بالملفات المرفقة لاستكمال الدراسة، لا يوجد سوى الأرض، وأريد سبل التمويل والمنح" — only the land exists; wants financing routes AND grants.
Inputs in inputs/ (see /mnt/project-files/.notes/inputs.md for a summary):
1. ennab-2025-ayadi-shafiya-hospital-study.pdf: earlier 80-bed general hospital study on the same project. Owner company: Al-Anbat for Medical Services LLC (الأنباط للخدمات العلاجية والطبية ذ.م.م), CR 74183. LAND: Wadi Musa, basin Mukhaimer (15), plot 684, 6 dunums 813 m² (6,813 m²), valued JOD 420,000 + 35,000 conversion/registration fees [SOURCE: Ennab 2025]. Its cost lines (building 298 JOD/m², salaries, equipment) look far below market: use as owner input to cross-check, not as evidence.
2. private-hospital-licensing-guide-jordan-2026.pdf: licensing compliance guide dated 26 Sep 2026.
Revised defaults: land = plot 684 (owner in-kind equity ~JOD 455k [VERIFY: DLS valuation]); the company already exists (LLC); new build on that plot; nothing else exists (no design, no permits).

## Correction 16 Oct 2026, 07:25 (owner)
"الأرض ليست محددة بعد، استخدم الدراسة المرفقة للمساعدة فقط" — the land is NOT yet chosen; the Ennab study is reference only.
So: plot 684 is NOT the project site. Base case = buy a plot in Wadi Musa (size per the GFA need, typically 3–5 dunums) at a researched market price per dunum; land cost is in capex and is part of the owner's equity contribution. Sensitivity: owner/family land contributed in kind. The company Al-Anbat LLC is from the reference study; ownership of this project's entity is still to be confirmed by the owner.

## Scope change 07:45 (owner, 16 Oct 2026)
Owner: "Modify the project to be for the smallest allowed hospital and it's not only for trauma: one-day surgical procedures, the most common surgeries, general surgery, small paediatric ward, gynaecological ward."
- New base: 20-bed SPECIALISED SURGICAL hospital (licensing minimum for specialised = 20 beds; general = 40 beds with surgery, OB/GYN, internal medicine, paediatrics). Beds: surgical/ortho/trauma 9, gynaecology 4, paediatrics 4, ICU 2 + 1 isolation. Day-surgery unit (6 trolleys, not licensed beds), 2 ORs, endoscopy room, 24/7 ER (6 bays), CT.
- [VERIFY at the MoH coordination meeting] that a multi-surgical-specialty hospital with gyn and paediatric wards can be licensed as "specialised". If MoH says it is a general hospital, the minimum is 40 beds with internal medicine and obstetrics (modelled as a fallback scenario).
- The earlier 30-bed trauma-only model is kept for reference only (it failed: NPV with TV -2.9m).

## Version 3, 08:04 (owner): "best model of hospital with the least amount of money, could be upgraded in future"
Base switched to the lean expandable Phase 1: land on long lease (18k/yr), 2,600 m² at 600/m² + 120k expansion provision (3rd floor, OR-3 shell, spare MRI room), refurbished CT, reagent-rental lab, cloud HIS, housekeeping outsourced, 96 staff, CBJ 2.5m + lease 0.5m. Version 2 archived.


## Owner profile change (16 Oct 2026, 18:21)
The owner / medical director is a physician in general, not an orthopaedic surgeon. Financial assumptions are unchanged (open-staff model, director salary 5,000/month), but surgical volume now depends on contracting resident orthopaedic and general surgeons; added as condition 6 and in risk 5.
