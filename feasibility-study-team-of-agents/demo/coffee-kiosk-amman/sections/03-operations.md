# 3. Technical & Operational Study: Specialty Coffee Counter, Amman

*Prepared by the technical-operations-analyst agent, 15 Oct 2026. Currency: JOD. Exchange rates used for imported equipment: the official pegs JOD 0.709 per USD and AED 3.6725 per USD, so 1 AED = JOD 0.1931.*

**Format change from the brief.** The legal section found that Greater Amman Municipality (GAM) is not issuing new licences for street coffee kiosks (04-legal.md). This study therefore plans a **small licensable shop unit of about 25–45 m²** with a walk-up service window and a counter inside. It does not plan a free-standing kiosk. The concept stays the same: specialty espresso, cold brew and bought-in pastries, sold walk-up and through delivery apps.

---

## 3.1 Operating model and capacity

**Service flow.**
1. The customer orders at the counter or the window, or the order arrives through Talabat/Careem.
2. The order is keyed into the POS and paid by card, CliQ or cash.
3. The barista grinds to order on an on-demand grinder, pulls a double shot (18 g dose) on a 2-group machine and steams milk. Cold brew is pre-made in batches and kept chilled.
4. Pastries are either baked off from frozen in a small convection oven or bought in daily, then held in a display chiller.
5. Drinks are handed over in branded cups, or bagged for the delivery rider.

**Opening hours (ASSUMPTION).** 07:00–21:00, 7 days a week, 360 days a year (the market section uses 360). The morning peak (07:30–10:00) serves offices and 8 am lectures. A second peak (13:00–15:00) follows lunch.

**Capacity (Assessment, Medium confidence).**

| Item | Value | Basis |
|---|---|---|
| Machine throughput | about 60 drinks/hour with 2 baristas on a 2-group machine, about 35/hour with one | ASSUMPTION: about 1 min of bar time per milk drink per barista; a 2-group machine can run two drinks at once |
| Practical daily capacity | **400 drinks/day**, so **12,000/month** | ASSUMPTION: about 60 % of the peak rate held across 14 h, after quiet hours |
| Demand, year 1 / 2 / 3 | 117 / 163 / 210 drinks per day | 01-market.md |
| Peak-hour load, year 3 | about 42 drinks/hour | ASSUMPTION: 20 % of daily drinks fall in the busiest hour |
| Pastries | about 29 / 41 / 53 per day | 25 % attach rate (01-market.md) |

Year-1 demand uses about 30 % of capacity, and year 3 about 53 %. The real limit is the **morning peak**. From year 2, two baristas must work the 07:30–10:00 slot. Equipment does not limit revenue in years 1–3. If the site turns out busier than forecast, labour at the peak is the first thing that runs out.

## 3.2 Location and premises

**Recommended area: Al-Jubeiha, on a side street off University Street between the University of Jordan (UJ) north side and Princess Sumaya University (PSUT).** Khalda (Wasfi Al-Tal / Gardens–Bashiti stretch) is the fallback.

Why Jubeiha:
- **Catchment.** The market section's SAM rests on about 24,000 UJ students plus office workers (01-market.md). Jubeiha is within walking distance of UJ and PSUT, and it has clinics, offices and student housing nearby.
- **Competition.** University Street itself already has Starbucks, Costa and Qahwa BLK (02-competition.md). A side-street unit 200–500 m from the main road avoids going head-to-head on rent and on footfall competition, while still catching students on foot. This is an Assessment, and a 500 m competitor count is needed to confirm it.
- **Rent.** Small units in Jubeiha list at about JOD 12/m²/month. Comparable small units in Khalda list at JOD 13–25/m²/month (see below).
- **Licensability.** An enclosed shop unit with a service window is a normal "café/coffee shop" activity for GAM. A street kiosk is not (04-legal.md).

**Requirements.** 25–45 m² on the ground floor with a street frontage for the window. The plot must be zoned commercial. The unit needs single- or three-phase power of at least 10 kW (the espresso machine draws about 4–5 kW at peak; ASSUMPTION, check the machine spec), a water inlet and drain, and space for an AC split unit. Parking or a drop-off point is also needed for delivery riders.

**Rent evidence (OpenSooq, accessed 15 Oct 2026).**

| Listing | Area | Rent | JOD/m²/month |
|---|---|---|---|
| Khalda, shop 33 m² (posted 03-10-2026) [R1] | 33 m² | 10,000/yr | 25.3 |
| Khalda, shop at Arab Bank signal (19-09-2026) [R2] | 70 m² | 11,000/yr | 13.1 |
| Khalda, main road near Bashiti signals (04-10-2026) [R3] | 90 m² | 8,500/yr | 7.9 |
| Khalda, Wasfi Al-Tal complex (Gardens) [R4] | 110 m² | 8,000/yr | 6.1 |
| Jubeiha, shop (02-10-2026) [R5] | 48 m² | 580/month | 12.1 |
| Jubeiha, on University St, 45 m² + 42 m² mezzanine [R6] | 45 m² ground | 6,500 (period not stated; read as annual) | 12.0 (ground floor only) |
| Gardens, retail (Bayut) [R7] | 80 m² | 35,000/yr | 36.5 (prime main-road showroom; outlier) |

Small units carry a much higher rent per m², and main-road frontage on Wasfi Al-Tal is far above side streets. **Value used: JOD 550/month (JOD 6,600/year) for a 30–45 m² Jubeiha side-street unit.** That is within the 48 m² listing at 580/month [R5] and the University St listing at about 542/month [R6]. *Confidence: Medium.* Landlords in Amman often ask for the year's rent up front or in two instalments, and some units carry key money (*khilw*, one Jubeiha listing mentions it [R8]). Both are cash-flow items for the finance agent, and key money is excluded from capex here.

**Fit-out.** Counter and back bar, plumbing, electrical upgrade, flooring, lighting, a service window, menu boards and signage. This is an ASSUMPTION of about JOD 250–300/m² for a light café fit-out of a shell unit, and no Amman fit-out quotes could be found online. **Value used: JOD 7,500** plus JOD 800 signage and JOD 600 AC. *Confidence: Low. Get 3 contractor quotes.*

## 3.3 Equipment

| # | Item | Qty | Unit price (JOD) | Total (JOD) | Life (yrs) | Source / basis |
|---|---|---|---|---|---|---|
| 1 | Espresso machine, 2-group volumetric (Nuova Simonelli Appia Life Compact 2GR or equal) | 1 | 3,150 | 3,150 | 7 | AED 13,020 in UAE [E1] = JOD 2,514, plus 25 % freight, customs and GST (ASSUMPTION). Cross-check: Appia Life 2GR USD 8,805 in the USA [E2]. Used Expobar JOD 1,000 and Bezzera JOD 1,500 in Jordan [E3], an option to save about JOD 1,800 |
| 2 | On-demand espresso grinder, 75 mm flat burr (Eureka Atom 75 or equal) | 2 | 1,080 | 2,160 | 5 | AED 4,463 [E4] = JOD 862, plus 25 % landed. Two grinders: house blend and decaf/single origin |
| 3 | Water filter/softener system | 1 | 250 | 250 | 5 | ASSUMPTION |
| 4 | Cold-brew and batch-brew kit | 1 | 300 | 300 | 5 | ASSUMPTION |
| 5 | Under-counter fridges (2) and pastry display chiller | 1 set | 1,800 | 1,800 | 7 | ASSUMPTION |
| 6 | Ice machine, small (about 30 kg/day) | 1 | 600 | 600 | 5 | ASSUMPTION |
| 7 | Commercial blender | 1 | 300 | 300 | 3 | Used Abdin commercial blender JOD 150 in Amman [E3]. New taken at about 2×, ASSUMPTION |
| 8 | Small convection oven (bake-off) | 1 | 400 | 400 | 5 | ASSUMPTION |
| 9 | POS hardware (tablet, receipt printer, cash drawer, card terminal) | 1 | 600 | 600 | 4 | ASSUMPTION |
| 10 | Smallwares (pitchers, scales, tampers, knock box, shakers) | lot | 500 | 500 | 3 | ASSUMPTION |
| 11 | Fit-out (counter, plumbing, electrics, floor, window) | lot | 7,500 | 7,500 | 5 | ASSUMPTION, see 3.2 |
| 12 | AC split unit | 1 | 600 | 600 | 7 | ASSUMPTION |
| 13 | Signage and menu boards | lot | 800 | 800 | 5 | ASSUMPTION |
| 14 | Contingency (about 10 %) | — | 1,900 | 1,900 | 5 | ASSUMPTION |
| | **Total capex** | | | **20,860** | | |

*Confidence: Medium for the machine and grinders (two price points each). Low for fit-out and the smaller items.* Using second-hand machines from OpenSooq [E3] could cut capex by about JOD 2,500. The trade-off is no warranty and more risk of downtime.

## 3.4 Staffing

**Organisation.** The owner works as manager: purchasing, cash, marketing and cover on days off, unpaid in this model (ASSUMPTION; the finance agent should decide whether to add an owner's draw). Under the owner are a head barista and a barista. A part-time barista joins in year 2 and becomes full-time in year 3. The owner has no café experience (brief), so an experienced head barista is essential.

**Rota (year 1).** A morning shift 07:00–15:00 and an evening shift 13:00–21:00 overlap over the lunch peak. Each employee works 6 × 8 h = 48 h a week, which is the legal maximum (04-legal.md). The owner covers the two days off.

| Role | Monthly gross (JOD) | Evidence | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|
| Head barista (3+ yrs experience) | 500 | Job ad near UJ, 3 yrs experience, JOD 500 [W1]. 7th Circle café from JOD 550 [W2] | 1 | 1 | 1 |
| Barista | 380 | Rabieh café JOD 400 [W3]. Junior starting pay JOD 350–400 (Reddit, self-reported) [W4]. Minimum wage JOD 290 (04-legal.md) | 1 | 1 | 2 |
| Part-time barista (about 24 h/week, morning peak) | 180 | ASSUMPTION: 24 h × 4.33 weeks × about JOD 1.70/h, at or slightly above the hourly minimum of JOD 1.67 [W5] | 0 | 1 | 0 |
| **Gross payroll** | | | **880** | **1,060** | **1,260** |
| Employer social security 14.25 % (04-legal.md) | | | 125 | 151 | 180 |
| **Total employer cost / month** | | | **1,005** | **1,211** | **1,440** |

*Confidence: Medium (3 job listings plus the statutory minimum).*

## 3.5 Inputs and unit cost

| Input | Price used | Evidence |
|---|---|---|
| Specialty espresso beans | **JOD 18/kg** (wholesale) | Retail: Bunna espresso blend 250 g JD 9, up to JD 24 for the 1 kg option [I1][I2]. Dimitri's 250 g JOD 5.78–8.25, which is JOD 23–33/kg (02-competition.md). DejaBrew espresso blend JD 9.5 per bag [I3]. Wholesale taken as about 25 % below the JOD 24/kg retail price (ASSUMPTION; Bunna runs a B2B channel [I4]) |
| Fresh milk | **JOD 1.10/L** | Hammoudeh fresh pasteurised milk 1 L JOD 1.25, full-fat 4×1 L JOD 3.70 (JOD 0.93/L) [I5]. Numbeo Amman JOD 1.16 (range 0.95–1.50) [I6] |
| 12 oz paper cup | JOD 0.03–0.06 | Jordan-made 12 oz cup, 50 for JOD 1.32 = JOD 0.026 each [I7]. Double-wall cups cost more (ASSUMPTION 0.06) |
| Lid, sleeve, napkin, stirrer or straw | JOD 0.04 | ASSUMPTION |
| Frozen croissant (bake-off) | about JOD 0.33 each | 200 × 30 g croissants for AED 345 (UAE wholesale) [I8] = JOD 0.33. No Jordan wholesale price list was found online |

**Cost of goods per drink (12 oz).**

| Drink type | Mix | Beans | Milk | Packaging | Other | Cost |
|---|---|---|---|---|---|---|
| Milk drink (latte, cappuccino, flat white, Spanish latte) | 70 % | 18 g = 0.324 | 220 ml = 0.242 | 0.100 | — | 0.666 |
| Black (espresso, americano) | 20 % | 0.324 | — | 0.100 | water 0.010 | 0.434 |
| Cold brew | 10 % | 25 g = 0.450 | — | 0.100 | ice 0.020 | 0.570 |
| **Weighted** | | | | | | **0.610** |
| Syrups, sugar, cocoa (25 % of drinks × 0.06, plus 0.01) | | | | | | 0.025 |
| Waste and spillage (5 %) | | | | | | 0.032 |
| **COGS per drink used** | | | | | | **JOD 0.67** |

At the market section's JOD 2.75 average price, COGS is 24 % of the GST-inclusive price, or about 28 % of the net-of-GST price (JOD 2.37). That is a normal ratio for specialty coffee (Assessment).

**COGS per pastry: JOD 0.60.** This is an ASSUMPTION blending bake-off croissants (about JOD 0.33 [I8], plus fillings and a bag, about 0.45) with bought-in cookies and cakes from a local bakery (about 0.70), plus 10 % waste. At JOD 1.50 per pastry (01-market.md), COGS is 40 % of price. *Confidence: Low. Get 2 bakery quotes.*

Delivery-app commissions and card fees are variable selling costs. They are left to the finance agent.

## 3.6 Running costs (fixed, monthly)

| Item | JOD/month | Basis |
|---|---|---|
| Rent | 550 | See 3.2 [R5][R6] |
| Electricity | 175 | About 1,380 kWh/month × JOD 0.120/kWh. The commercial tariff is 120 fils/kWh for 1–2,000 kWh/month [U1]. Business price JOD 0.120/kWh [U2]. Load (ASSUMPTION): machine 21, AC 12, fridges 6, lights/POS 4, oven 2, grinders 1 = about 46 kWh/day. Includes about JOD 10 of bill fees |
| Water and sewage | 25 | ASSUMPTION (Miyahuna commercial tariff not checked) |
| Internet | 30 | Numbeo broadband JOD 22.72 (19–30) [I6]. A business line costs a little more |
| POS / back-office software | 30 | A Jordan POS alternative to Foodics starts at USD 35/month (= JOD 25) [U3] |
| Insurance (property, contents, liability) | 25 | ASSUMPTION, JOD 300/yr |
| Maintenance and machine servicing | 40 | ASSUMPTION |
| Cleaning and chemicals | 30 | ASSUMPTION |
| Local marketing (social media, sampling) | 150 | ASSUMPTION |
| Bookkeeping / accountant | 50 | ASSUMPTION |
| **Total fixed opex excluding payroll** | **1,105** | |

Annual licence renewals and professional fees are covered in 04-legal.md.

## 3.7 Implementation timeline

| Month | Activity |
|---|---|
| 0–1 | Site search, footfall counts, written confirmation from GAM of the activity class and zoning (04-legal.md critical risk). Sign the lease |
| 1–3 | Company registration and licensing, about 2.5 months (04-legal.md). Order the espresso machine and grinders (4–6 weeks lead time, ASSUMPTION) |
| 2–4 | Fit-out, 6–8 weeks (ASSUMPTION). Hire the head barista by month 3 |
| 4–5 | Install equipment, dial in the beans, train staff, soft opening of 1–2 weeks |
| **5** | **Grand opening** |

Months to launch: **5**, within the brief's 4–6 month window. Licensing and fit-out are the critical path, and they can overlap only once the lease is signed.

---

## Key numbers handed to other agents

```yaml
currency: JOD
premises:
  format: "enclosed shop unit with walk-up window (not a street kiosk)"
  area: "Al-Jubeiha side street off University St, near UJ and PSUT; fallback Khalda"
  size_m2: 35
  rent_monthly: 550
  rent_paid_in_advance_months: 6        # ASSUMPTION, common Amman practice; working-capital item
capex_items:
  - {name: espresso_machine_2group, amount: 3150, life_years: 7}
  - {name: espresso_grinders_x2, amount: 2160, life_years: 5}
  - {name: water_filtration, amount: 250, life_years: 5}
  - {name: coldbrew_batchbrew_kit, amount: 300, life_years: 5}
  - {name: refrigeration_and_display, amount: 1800, life_years: 7}
  - {name: ice_machine, amount: 600, life_years: 5}
  - {name: blender, amount: 300, life_years: 3}
  - {name: convection_oven, amount: 400, life_years: 5}
  - {name: pos_hardware, amount: 600, life_years: 4}
  - {name: smallwares, amount: 500, life_years: 3}
  - {name: fit_out, amount: 7500, life_years: 5}
  - {name: air_conditioning, amount: 600, life_years: 7}
  - {name: signage_menu_boards, amount: 800, life_years: 5}
  - {name: contingency, amount: 1900, life_years: 5}
capex_total: 20860
fixed_opex_monthly:
  - {name: rent, amount: 550}
  - {name: electricity, amount: 175}
  - {name: water, amount: 25}
  - {name: internet, amount: 30}
  - {name: pos_software, amount: 30}
  - {name: insurance, amount: 25}
  - {name: maintenance, amount: 40}
  - {name: cleaning_supplies, amount: 30}
  - {name: marketing, amount: 150}
  - {name: bookkeeping, amount: 50}
fixed_opex_monthly_total: 1105          # excludes payroll
cogs_per_unit:
  drink: 0.67                            # weighted 70% milk / 20% black / 10% cold brew, incl. packaging and 5% waste
  pastry: 0.60                           # ASSUMPTION, Low confidence
input_prices:
  beans_per_kg: 18
  milk_per_litre: 1.10
  electricity_per_kwh: 0.120
max_units_per_month: 12000               # drinks; 400/day practical capacity
max_drinks_per_day: 400
peak_hour_capacity_drinks: 60            # 2 baristas, 2-group machine
operating_hours_per_day: 14
operating_days_per_year: 360
payroll_by_role:                         # gross JOD/month per person
  - {role: head_barista, salary: 500, headcount: {y1: 1, y2: 1, y3: 1}}
  - {role: barista, salary: 380, headcount: {y1: 1, y2: 1, y3: 2}}
  - {role: part_time_barista, salary: 180, headcount: {y1: 0, y2: 1, y3: 0}}
  - {role: owner_manager, salary: 0, headcount: {y1: 1, y2: 1, y3: 1}}   # unpaid, ASSUMPTION
employer_social_security_rate: 0.1425
headcount: {y1: 2, y2: 3, y3: 3}         # paid staff, excluding owner
payroll_monthly:                          # incl. employer social security
  y1: 1005
  y2: 1211
  y3: 1440
months_to_launch: 5
confidence: {capex: Medium-Low, rent: Medium, payroll: Medium, cogs_drink: Medium, cogs_pastry: Low, utilities: Medium}
```

## Sources

- [R1] OpenSooq, Khalda shop 33 m², JOD 10,000/yr, 03-10-2026. https://jo.opensooq.com/ar/search/288067584
- [R2] OpenSooq, Khalda shop 70 m², Arab Bank signal, JOD 11,000/yr, 19-09-2026. https://jo.opensooq.com/ar/search/287382614
- [R3] OpenSooq, Khalda shop 90 m², near Bashiti signals, JOD 8,500/yr, 04-10-2026. https://jo.opensooq.com/ar/search/288133308
- [R4] OpenSooq, Khalda shop 110 m², Wasfi Al-Tal (Gardens), JOD 8,000/yr, Oct 2026. https://jo.opensooq.com/ar/search/287774306
- [R5] OpenSooq, Jubeiha shop 48 m², JOD 580/month, 02-10-2026. https://jo.opensooq.com/ar/search/288038042
- [R6] OpenSooq, Jubeiha shops for rent (category page; University St 45 m² + 42 m² mezzanine, JOD 6,500), accessed 15 Oct 2026. https://jo.opensooq.com/ar/%D8%B9%D9%85%D8%A7%D9%86/%D8%A7%D9%84%D8%AC%D8%A8%D9%8A%D9%87%D8%A9/%D8%B9%D9%82%D8%A7%D8%B1%D8%A7%D8%AA/%D9%85%D8%AD%D9%84%D8%A7%D8%AA-%D9%84%D9%84%D8%A7%D9%8A%D8%AC%D8%A7%D8%B1
- [R7] Bayut Jordan, Shops for rent in Khalda (Gardens retail 80 m², JOD 35,000/yr), accessed 15 Oct 2026. https://www.bayut.jo/en/amman/shops-for-rent-in-khalda/
- [R8] OpenSooq, Jubeiha shop between UJ and PSUT, with key money (*khilw*), 16-09-2026. https://jo.opensooq.com/ar/search/287247976
- [E1] BeanBurds (UAE), Nuova Simonelli Appia Life Compact 2 Group, AED 13,020, accessed 15 Oct 2026. https://beanburds.com/products/nuova-simonelli-appia-life-compact-2-group-volumetric-black
- [E2] Coffeeionado (USA), Nuova Simonelli Appia Life 2 Group, USD 8,805, accessed 15 Oct 2026. https://www.coffeeionado.com/products/nuova-simonelli-appia-life-2-group
- [E3] OpenSooq Jordan, Coffee and beverage equipment (used Expobar JOD 1,000; Bezzera JOD 1,500; Abdin blender JOD 150), Oct 2026. https://jo.opensooq.com/en/businesses-industrial/coffee-and-beverage-equipment
- [E4] Jebelz (UAE), Eureka Atom Speciality 75 grinder, AED 4,463, accessed 15 Oct 2026. https://jebelz.com/ae_en/eureka-atom-speciality-75-flat-steel-burr-espresso-grinder-white.html
- [I1] Bunna Roastery (Amman), Espresso Blend (250 g / 500 g / 1 kg; 250 g JD 9), accessed 15 Oct 2026. https://bunna-jo.com/product/espresso-blend
- [I2] Bunna Roastery, shop listing (Espresso Blend JD 9–24), accessed 15 Oct 2026. https://bunna-jo.com/shop
- [I3] DejaBrew Roastery (Amman), shop (Espresso Blend JD 9.5), accessed 15 Oct 2026. https://www.dejabrew-jo.com/shop/
- [I4] Bunna Roastery, B2B page. https://bunna-jo.com/b2b
- [I5] Hammoudeh Dairy online store, milk prices, accessed 15 Oct 2026. https://onlinestore.hammoudehdairy.com/product-category/dairy/milk/
- [I6] Numbeo, Cost of Living in Amman (milk, utilities, internet), updated 13 Oct 2026. https://www.numbeo.com/cost-of-living/in/Amman?displayCurrency=JOD
- [I7] Jafar Shop (Jordan), 12 oz paper cups, 50 pcs, JOD 1.32. https://www.jafarshop.com/products/%D9%83%D8%A7%D8%B3%D8%A7%D8%AA-%D9%88%D8%B1%D9%82%D9%8A%D8%A9-12-%D8%A7%D9%88%D9%86%D8%B5-50-%D9%83%D8%A7%D8%B3%D8%A9-rz
- [I8] Grand Bake (UAE), frozen croissant carton 30 g × 200, AED 345 (context; not a Jordan price). https://www.grandbake.com/collections/croissant-cartoon
- [W1] Facebook group "Ask Barista Jo": vacancy for 2 baristas, 3+ yrs experience, café near UJ, JOD 500. https://www.facebook.com/groups/279140666575214/
- [W2] Wzzff, barista vacancy, café at 7th Circle, Amman, from JOD 550. https://wzzff.com/job/1764599-q
- [W3] Wazaf.net, barista vacancy, Rabieh café, JOD 400. https://wazaf.net/job-ads-1704111/
- [W4] Reddit r/jordan, "Average barista salary" (self-reported JOD 350–400 starting). https://www.reddit.com/r/jordan/comments/12f8rm8/average_barista_salary/
- [W5] Wage.is, Jordan salary and minimum wage (JD 1.67/hour), Feb 2026. https://wage.is/jordan/
- [U1] NEPCO, Electricity tariff schedule (commercial: 120 fils/kWh for 1–2,000 kWh/month, 152 fils above, from 01/04/2022). https://www.nepco.com.jo/assets/doc/tariff.pdf
- [U2] GlobalPetrolPrices, Jordan electricity prices, March 2026 (business JOD 0.120/kWh). https://www.globalpetrolprices.com/Jordan/electricity_prices/
- [U3] Managely, "Best Foodics alternative in Jordan" (from USD 35/month). https://managely.cloud/en/best-foodics-alternative-in-jordan
- Step-1 sections: 01-market.md, 02-competition.md, 04-legal.md (demand, prices, wages, social security, licensing).

## Open questions for the owner

1. **Site.** Can you shortlist 2–3 actual units in Jubeiha (side streets near UJ/PSUT) or Khalda? We need GAM's written confirmation of the activity class for each unit before signing a lease.
2. **Key money and advance rent.** Will you accept a unit that asks for *khilw* or a full year's rent up front? This changes the cash needed at start.
3. **New or used machine.** A new 2-group machine with a warranty (about JOD 3,150 landed) or a used one from OpenSooq (JOD 1,000–1,500)? Ask the Jordan agents of Nuova Simonelli, La Marzocco and Wega for local quotes. The landed price used here is estimated from UAE prices.
4. **Bean supplier.** Ask Bunna, Dimitri's and Nebo for wholesale terms on 10–15 kg/month. The JOD 18/kg used here is an estimate.
5. **Pastry route.** Bake-off frozen pastry (needs the oven, lower cost) or daily delivery from a local bakery (no oven, higher cost)? Get 2 quotes.
6. **Owner's role.** Will you work in the shop full-time without salary? If not, the model needs a third full-time barista from year 1, about JOD 434/month more.
7. **Fit-out.** Get 3 contractor quotes on a shell unit. The JOD 7,500 used here is the least certain capex line.
