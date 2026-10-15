# Jordan data sources for feasibility studies

A catalog of where to find the numbers a Jordan feasibility study needs, by topic. Every agent should check here before searching the open web, and should cite the specific page and release date it used (see `agents/_shared-research-rules.md`).

**Checked:** 15 October 2026. "✓" means the URL loaded on that date. "⚠" means the site exists (it shows up in search results or loads in a normal browser) but automated fetching was blocked, so open it manually or through another page. Freshness is what the page showed on the check date; always re-check for a newer release before using a number.

**Agent key:** MA market-analyst · CA competitor-analyst · LR legal-regulatory-analyst · TO technical-operations-analyst · MK marketing-strategist · FA financial-analyst · RA risk-analyst

**Language tip:** many Jordanian government pages are richer in Arabic (`/AR/` or `/ar/` paths) than in English. Search in Arabic too, e.g. دائرة الإحصاءات العامة، مسح نفقات ودخل الأسرة، رخص المهن.

---

## 1. Start here: the core official sources

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| Department of Statistics (DoS), home ✓ | https://dosweb.dos.gov.jo/ | National statistics office: population, prices, labour, trade, GDP, surveys, censuses | Updated Oct 2026 | Yes | Web, PDF, XLSX | All |
| DoS JorInfo Data Bank (PxWeb) ✓ | https://jorinfo.dos.gov.jo/Databank/pxweb/en/ | Queryable tables: population, national accounts, poverty, gender, agriculture, environment | Varies by table | Yes | PxWeb tables, export | MA, FA |
| DoS Jordan Statistical Yearbook 2024 ✓ | https://dosweb.dos.gov.jo/product/jordan-statistical-yearbook-2024/ | 23 chapters of demographic, social, economic and agricultural tables (preliminary) | 2024 edition | Yes | XLSX and PDF per chapter | MA, FA |
| DoS Jordan in Figures 2024 ✓ | https://dosweb.dos.gov.jo/product/jordan-in-figures-2024/ | Short reference of headline indicators | 2024 edition | Yes | PDF | MA |
| Central Bank of Jordan (CBJ) ✓ | https://www.cbj.gov.jo/Default/EN/ | Policy and deposit interest rates, exchange rates, SME credit, financial soundness | Updated Oct 2026 | Yes | Web, PDF, XLSX | FA, RA |
| CBJ Statistical Database ⚠ | https://statisticaldb.cbj.gov.jo/ | Time series: money, credit by sector, interest rates, balance of payments | Ongoing | Yes | Database export | FA, RA |
| CBJ Annual Statistical Bulletin ✓ | https://www.cbj.gov.jo/En/List/Annual_Statistical_Bulletin | Long annual series tables | Page updated Sep 2026 | Yes | XLSX | FA |
| Open Government Data Portal ✓ | https://opendata.gov.jo/ | 3,768 datasets from 157 agencies (economy, business, government) | Ongoing | Yes | Mixed (CSV, XLSX, PDF) | All |
| Petra, Jordan News Agency ✓ | https://petra.gov.jo/ | Fastest place to see new DoS, CCD and ministry releases (CPI, unemployment, company registrations) | Daily | Yes | News | All |

## 2. Demographics and population

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| DoS Population ✓ | https://dosweb.dos.gov.jo/population/population-2/ | Population estimates and projections 2015–2050 by governorate, district, locality, urban/rural, sex, age | Estimates to 2025 | Yes | PDF, XLS, interactive | MA, MK |
| DoS Population and Housing Census 2015 ✓ | https://dosweb.dos.gov.jo/censuses/population_housing/census2015/ | Last full census: households, housing units, nationality | 2015 | Yes | PDF, XLSX | MA |
| DoS DHS 2023 (Population and Family Health Survey) ✓ | https://dosweb.dos.gov.jo/product/dhs2023_en/ | Household composition, fertility, health, assets | 2023 | Yes | PDF | MA |
| UN World Population Prospects ✓ | https://population.un.org/wpp/ | Independent population estimates and projections by age | Check latest revision | Yes | CSV, XLSX | MA |
| UNHCR Jordan data portal ✓ | https://data.unhcr.org/en/country/jor | Registered refugees by nationality and governorate (a real share of local demand in some areas) | 30 Sep 2026 | Yes | Web, CSV | MA, RA |
| WorldPop ✓ | https://hub.worldpop.org/geodata/listing?id=29 | 100 m gridded population counts, for catchment-area estimates around a site | 2000–2020 | Yes | GeoTIFF | MA, TO |
| HDX Jordan ✓ | https://data.humdata.org/group/jor | ~155 datasets: admin boundaries, population, food prices, facilities | Ongoing | Yes | CSV, SHP, XLSX | MA, TO |

## 3. Household income, spending and buying power

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| DoS Household Expenditure and Income Survey (HEIS) ✓ | https://dosweb.dos.gov.jo/economic/expenditures-income/ | Average household income and spending by item and governorate, CPI weights, poverty indicators | Latest published round 2017/18 (page lists 2017); a newer round has been in preparation, check for it | Yes | PDF, XLSX | MA, MK, FA |
| DoS Poverty statistics ✓ | https://dosweb.dos.gov.jo/population/poverty/ | Poverty lines, gaps, Gini | 2010 tables (old; World Bank has newer estimates) | Yes | XLSX, interactive | MA, RA |
| DoS Energy in Homes survey ✓ | https://dosweb.dos.gov.jo/economic/energy-in-homes/ | Household energy use and spending | 2008 (old) | Yes | PDF | TO, MA |
| DoS Agricultural food budget ✓ | https://dosweb.dos.gov.jo/agriculture/food-budget/ | Food balance sheets | 2009 (old) | Yes | PDF, XLSX | MA |
| Numbeo, Amman cost of living ✓ | https://www.numbeo.com/cost-of-living/in/Amman | Crowd-sourced consumer prices (meal, cappuccino, rent, net salary) | Updated 13 Oct 2026 | Yes | Web | MA, CA, MK (sanity check only, low confidence) |
| Arab Barometer, Jordan ✓ | https://www.arabbarometer.org/countries/jordan/ | Public-opinion surveys: economic sentiment, finances, attitudes | 2025 wave | Yes (registration for microdata) | PDF, SPSS/Stata | MA, MK, RA |
| ERF Data Portal, JLMPS 2025 ✓ | https://erfdataportal.com/index.php/catalog/320 | Jordan Labor Market Panel Survey 2025: income, employment, households | 2025 | Free for research with licence | Microdata | MA, FA |

**Gap:** there is no recent official city- or neighbourhood-level income series. For a district, combine HEIS governorate averages with DoS population and CPI, and label the result as derived.

## 4. Prices and inflation

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| DoS Price indices ✓ | https://dosweb.dos.gov.jo/economic/price-indices/ | CPI (with item groups), producer, wholesale and industrial price indices | Sep 2026 | Yes | XLSX | FA, MA |
| DoS Agricultural prices ✓ | https://dosweb.dos.gov.jo/agriculture/agricultural-prices/ | Central market, wholesale and farm-gate crop prices, input prices | Monthly; latest listed Feb 2026 | Yes | Web tables, XLSX | TO, FA |
| Jordan News, Central Market daily prices ✓ | https://www.jordannews.jo/Section-112/Economy/Vegetable-and-Fruit-Prices-Today-40562 | Daily Amman central market produce prices (in piasters/kg) | Daily articles | Yes | News | TO |
| Ministry of Energy, fuel prices ✓ | https://www.memr.gov.jo/ | Local fuel prices by type, energy balance, energy statistics | Page updated Oct 2026 | Yes | Web, PDF | TO, FA |
| Energy and Minerals Regulatory Commission ✓ | https://www.emrc.gov.jo/ | Electricity tariffs and monthly fuel price adjustment | Oct 2026 | Yes | PDF | TO, FA |
| Trading Economics, Jordan ✓ | https://tradingeconomics.com/jordan/indicators | Quick dashboard of inflation, unemployment, rates (secondary; cite the original) | Aug 2026 readings | Partly free | Web | FA |

## 5. Macro economy and sector statistics

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| DoS Quarterly GDP ✓ | https://dosweb.dos.gov.jo/nationalaccount/quarterly-estimates/ | GDP current and constant prices, growth by economic activity | Q2 2026 | Yes | Tables, XLSX | MA, FA |
| DoS Industry and Energy ✓ | https://dosweb.dos.gov.jo/industry/industry-and-energy/ | Industrial survey: output, employment, costs by industry | 2015 (old) | Yes | PDF, XLSX | MA, TO |
| DoS Services survey ✓ | https://dosweb.dos.gov.jo/industry/services/ | Services sector output and costs | 2015 (old) | Yes | PDF | MA, FA |
| DoS Internal trade survey ✓ | https://dosweb.dos.gov.jo/industry/internal-trade/ | Wholesale and retail: output, compensation, value added | Latest year shown 2015 (old) | Yes | PDF | MA, FA |
| DoS Economic Establishments Census ✓ | https://dosweb.dos.gov.jo/censuses/establish-census/ | Every establishment: activity, location, employment size, revenue, capital | 2018 | Yes | PDF | CA, MA |
| DoS Building licences ✓ | https://dosweb.dos.gov.jo/economic/building-licenses/ | Monthly building permits, licensed areas, new housing units | Monthly | Yes | Press release, tables | MA, RA |
| DoS Construction ✓ | https://dosweb.dos.gov.jo/industry/construction/ | Construction sector survey and costs | 2015 (old) | Yes | PDF | TO |
| DoS Domestic tourism ✓ | https://dosweb.dos.gov.jo/economic/domestic-tourism/ | Domestic trips, spending, length of stay | 2012 (old) | Yes | PDF | MA |
| Ministry of Tourism and Antiquities ✓ | https://www.mota.gov.jo/ | Quarterly tourism report and studies (statistics page was under maintenance on check date) | See page | Yes | PDF | MA |
| Ministry of Finance ✓ | https://www.mof.gov.jo/ | Monthly General Government Finance Bulletin, budget, public debt | Aug 2026 bulletin | Yes | PDF, XLSX | FA, RA |
| Telecommunications Regulatory Commission ✓ | https://www.trc.gov.jo/ | Quarterly telecom indicators (subscriptions, internet) | Q2 2026 | Yes | PDF | MK, MA |
| Amman Stock Exchange ✓ | https://www.ase.com.jo/ | Listed company disclosures and quarterly reports, sector indices (margins and benchmarks for listed peers) | Daily | Yes for bulletins | Web, PDF | CA, FA |
| Jordan Strategy Forum ✓ | https://jsf.org/ | Economic outlook, Investor Confidence Index, SME reports | Oct 2026 | Yes | PDF | MA, RA |
| Economic and Social Council ✓ | https://www.esc.jo/ | State of the Country reports, annual report | 2025 report | Yes | PDF | RA |

## 6. External trade (imports, exports, tariffs)

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| DoS External trade ✓ | https://dosweb.dos.gov.jo/economic/externaltrade/ | Imports, exports, re-exports by commodity and country | Monthly; Oct 2026 release | Yes | Web tables, XLSX | MA, TO |
| Jordan Customs ✓ | https://www.customs.gov.jo/ | Integrated tariff lookup (duty by HS code), procedures, annual reports | Updated Oct 2026 | Yes | Web | LR, TO, FA |
| UN Comtrade ✓ | https://comtradeplus.un.org/ | Detailed trade flows by HS code and partner | Ongoing | Free tier, registration | CSV, API | MA |
| World Bank WITS ✓ | https://wits.worldbank.org/CountryProfile/en/JOR | Trade and tariff profile | 2023 | Yes | Web, CSV | MA |
| ITC Trade Map ✓ | https://www.trademap.org/ | Import/export statistics by product and market | Ongoing | Free registration | Web, XLSX | MA |
| ITC Market Access Map ✓ | https://www.macmap.org/ | Tariffs and non-tariff measures for a product in any market (for export plans) | Ongoing | Yes | Web | LR, MA |
| OEC Jordan profile ✓ | https://oec.world/en/profile/country/jor | Visual trade profile, top products and partners | 2022 | Yes | Web | MA |

## 7. Company registration, licensing and standards

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| Companies Control Department (CCD) ✓ | https://www.ccd.gov.jo/ | Company types, registration steps and fees, forms, monthly registration statistics (Arabic news section) | Oct 2026 | Yes | Web, PDF | LR, CA |
| CCD company search ✓ | https://portal.ccd.gov.jo/search/by-name.aspx | Look up registered companies by name (also by number and partner) | Live | Yes | Web | CA, LR |
| Ministry of Industry, Trade and Supply ✓ | https://www.mit.gov.jo/ | Trade names, sole proprietorships and their statistics, price controls, trade agreements | May 2026 | Yes | Web | LR, CA |
| Greater Amman Municipality ✓ | https://www.ammancity.gov.jo/ | Vocational (craft) licences, building licences, zoning, GIS (Amman only) | Live | Yes | Web | LR, TO |
| Jordan Food and Drug Administration ✓ | https://www.jfda.jo/ | Food and drug establishment licensing, registration, guides | See page | Yes | Web, PDF | LR, TO |
| Jordan Standards and Metrology Organization ✓ | https://www.jsmo.gov.jo/ | Technical regulations, standards catalogue, quality mark and Halal certification | Oct 2026 | Catalogue free; standards may be sold | Web, PDF | LR, TO |
| Amman Chamber of Commerce ✓ | https://www.ammanchamber.org.jo/ | Member directory with company search, studies, certificates of origin | Oct 2026 | Yes | Web | CA, LR |
| Jordan Chamber of Commerce ✓ | https://www.jocc.org.jo/ | Trade and services studies, statistical newsletters | Sep 2026 | Yes | PDF | MA, CA |
| Jordan Chamber of Industry ✓ | https://www.jci.org.jo/ | Industrial directory, sector studies and statistics | Oct 2026 | Yes | Web, PDF | CA, MA, TO |
| Amman Chamber of Industry ⚠ | https://www.aci.org.jo/ | Industrial directory and studies (server error on check date) | | Yes | Web | CA |
| Legislation and Opinion Bureau ⚠ | https://www.lob.gov.jo/ | Official texts of laws and regulations (page loads but content is script-rendered; use the Arabic site in a browser) | Live | Yes | Web, PDF | LR |

## 8. Investment incentives, tax and special zones

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| Ministry of Investment ✓ | https://moin.gov.jo/ | Investment Environment Law and regulations, licensing guide, investment map of opportunities, PPP tenders | Oct 2026 | Yes | Web, PDF | LR, FA |
| UNCTAD Investment Laws Navigator, Investment Environment Law 2022 ✓ | https://investmentpolicy.unctad.org/investment-laws/laws/391/investment-environment-law | English summary and download of the 2022 law: incentives, development zones, investor rights | 2022 law | Yes | Web, PDF | LR |
| Income and Sales Tax Department ✓ | https://www.istd.gov.jo/ | Income tax and sales tax laws, sales tax tables, instructions, forms | 2026 | Yes | Web, PDF | LR, FA |
| Aqaba Special Economic Zone Authority ✓ | https://www.aseza.jo/ | Aqaba zone incentives (5% income tax on net project income, customs exemptions), single-window licensing | Oct 2026 | Yes | Web | LR, FA |
| Jordan Enterprise Development Corporation ✓ | https://www.jedco.gov.jo/ | SME grants, financing programmes, export support, studies | Oct 2026 | Yes | Web | FA, LR |
| Jordan Investment Commission site ✓ | https://www.jic.gov.jo/ | Older investment promotion site; prefer Ministry of Investment | | Yes | Web | LR |

## 9. Labour, wages and social security

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| DoS Employment and unemployment ✓ | https://dosweb.dos.gov.jo/labourforce/employment-and-unemployment/ | Quarterly unemployment and participation by sex, age, education, governorate | Q2 2026 | Yes | PDF, tables | MA, TO, RA |
| DoS Employment in establishments ✓ | https://dosweb.dos.gov.jo/economic/employment-in-establishment/ | Wages, bonuses and compensation by occupation and sector, working hours | Latest year shown 2015 (old; inflate with CPI) | Yes | XLSX | TO, FA |
| DoS Job creation survey ✓ | https://dosweb.dos.gov.jo/labourforce/job-creation/ | Net new jobs by sector | 2013 (old) | Yes | PDF | MA |
| Ministry of Labour ✓ | https://www.mol.gov.jo/ | Labour law, minimum wage decisions, work permits for non-Jordanians, annual reports | Oct 2026 | Yes | Web, PDF | LR, TO, FA |
| Social Security Corporation ✓ | https://www.ssc.gov.jo/ | Social security law, contribution rules, publications | Aug 2026 | Yes | Web, PDF | LR, FA |
| ILOSTAT country profiles ✓ | https://ilostat.ilo.org/data/country-profiles/ | Internationally comparable labour indicators for Jordan | Ongoing | Yes | Web, CSV | MA |
| Bayt.com Jordan ✓ | https://www.bayt.com/en/jordan/ | Live job ads (advertised salaries where shown; no salary database on the page) | Live | Yes | Web | TO |
| Salary Explorer, Jordan ⚠ | https://www.salaryexplorer.com/average-salary-wage-comparison-jordan-c108 | Self-reported salary estimates by job (low confidence) | | Yes | Web | TO |
| Akhtaboot ⚠ | https://www.akhtaboot.com/ | Jordan job board | Live | Yes | Web | TO |

## 10. Real estate and rents

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| Department of Lands and Survey ✓ | https://www.dls.gov.jo/ | Monthly real-estate trading reports, real estate indicators, administrative land/apartment values, licensed agents and valuers | Sep 2026 report | Yes | PDF, Web | TO, FA, MA |
| OpenSooq Jordan ✓ | https://jo.opensooq.com/ | Classified listings: shops, offices, apartments and land for rent or sale, used equipment, jobs | Live | Yes | Web | TO, FA (collect 5+ comparable listings; asking prices, not achieved rents) |
| Global Property Guide, Jordan rental yields ✓ | https://www.globalpropertyguide.com/middle-east/jordan/rental-yields | Gross rental yields for Amman | Dec 2017 (old) | Paid | Web | FA (context only) |

**Tip:** for a specific shop location, the strongest evidence is 3–5 OpenSooq listings in the same street or district plus one call to a local agent; record listing date and URL.

## 11. Consumers, digital and marketing

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| DataReportal, Digital 2026 Jordan ✓ | https://datareportal.com/reports/digital-2026-jordan | Internet and social media users, ad reach by platform (Facebook, Instagram, TikTok, Snapchat, YouTube, LinkedIn) | Nov 2025 (data Oct 2025) | Yes | Web, slides | MK |
| TRC telecom indicators ✓ | https://www.trc.gov.jo/ | Mobile and internet subscriptions | Q2 2026 | Yes | PDF | MK |
| Google Trends, Jordan ⚠ | https://trends.google.com/trends/explore?geo=JO | Search interest over time for products, brands, competitors | Live | Yes | Web, CSV | MK, MA |
| Talabat Jordan ✓ | https://www.talabat.com/jordan | Restaurant and grocery delivery: competitor menus, prices, ratings (open per restaurant) | Live | Yes | Web/app | CA, MK |
| OpenStreetMap, Jordan ✓ | https://www.openstreetmap.org/relation/184818 | Map data for mapping competitors, footfall generators and roads around a site | Live | Yes (open licence) | Web, OSM export | CA, TO |
| GEM Jordan National Report 2024/25 ✓ | https://gemconsortium.org/report/51666 | Entrepreneurship activity, business discontinuation reasons, financing | 2025 | Yes (download) | PDF | RA, MA |
| GEM Jordan country profile ✓ | https://www.gemconsortium.org/country-profile/175 | Headline entrepreneurship indicators | 2025 | Yes | Web | RA |

**Gap:** there is no free, current Jordan consumer panel. Euromonitor, NielsenIQ and Statista sell category data; otherwise run a short primary survey or customer interviews and label the results as primary research.

## 12. International datasets and country reports

| Source | URL | What it has | Freshness | Free | Format | Agents |
|---|---|---|---|---|---|---|
| World Bank Open Data, Jordan ✓ | https://data.worldbank.org/country/jordan | World Development Indicators: GDP, income, population, poverty, business | To 2025 | Yes | CSV, XLSX, API | MA, FA |
| World Bank Jordan Economic Monitor ✓ | https://www.worldbank.org/en/country/jordan/publication/jordan-economic-monitor-home | Twice-yearly macro analysis and outlook | Latest listed: Summer 2024 | Yes | PDF | MA, RA |
| World Bank Microdata Library, Jordan ✓ | https://microdata.worldbank.org/index.php/catalog?country%5B%5D=JOR | Survey microdata, incl. Enterprise Surveys 2019 and COVID follow-ups | 2019–2024 | Free / licensed | Microdata | MA, FA |
| World Bank Enterprise Surveys, Jordan ✓ | https://www.enterprisesurveys.org/en/data/exploreeconomies/2019/jordan | Firm-level obstacles: finance, permits, electricity, informality | 2019 | Yes | Web, microdata | RA, LR |
| World Bank B-READY ✓ | https://www.worldbank.org/en/businessready | Business environment assessment (successor to Doing Business); check whether Jordan is in the covered list | 2025 report | Yes | PDF, data | LR, RA |
| IMF Jordan ✓ | https://www.imf.org/en/Countries/JOR | Article IV and programme reports with macro forecasts | Latest listed Dec 2024 | Yes | PDF | FA, RA |
| IMF DataMapper, Jordan ✓ | https://www.imf.org/external/datamapper/profile/JOR | WEO forecasts: GDP growth, inflation, unemployment | Twice a year | Yes | Web, CSV | FA, RA |
| US trade.gov Country Commercial Guide ✓ | https://www.trade.gov/country-commercial-guides/jordan-market-overview | Market overview, leading sectors, trade barriers | Feb 2026 | Yes | Web | MA, LR |
| FAOSTAT ✓ | https://www.fao.org/faostat/en/ | Food production, trade, consumer food prices | Ongoing | Yes | CSV, API | MA, TO |

## 13. Known freshness problems (adjust before using)

| Data | Latest available | What to do |
|---|---|---|
| Household income and spending (HEIS) | 2017/18 | Inflate with DoS CPI to today, say so, and check whether a newer round has been released |
| Wages by occupation (employment in establishments) | 2015 | Inflate with CPI; triangulate with job ads and MoL minimum wage |
| Establishment census | 2018 | Use for structure (counts by activity and area), then check current competitors on the ground and in the CCD/chamber directories |
| Internal trade, industry, services and construction surveys | 2015 | Use only for ratios (margins, cost structure), flagged as old |
| Household energy survey, food balance, job creation | 2008, 2009, 2013 | Context only |
| Domestic tourism survey | 2012 | Context only |
| DoS poverty tables | 2010 | Use World Bank estimates instead |

## Not yet checked

Paid or login-only sources that may be worth it for larger studies: Euromonitor, NielsenIQ, Statista, CEIC, Fitch Solutions, Meta Ads Manager audience estimates (free with an ad account, good for sizing a reachable audience in a city).
