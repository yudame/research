# Research Results for Solomon Islands Telecom Series: Ep. 3, Infrastructure Without Capital

This file is for pasting research results from external tools (Claude, Gemini, ChatGPT, Perplexity, Grok, etc.).

---

## Research from Claude

# Satellite vs. Submarine: The Economics of Launching Mobile Networks Across Archipelagos

Partnering with an established infrastructure provider fundamentally transforms the economics of launching mobile networks across dispersed island chains. For Solomon Islands—spanning 1,000+ islands with 85% rural population—infrastructure partnerships can reduce capital requirements by **50-80%** and compress deployment timelines from years to months. The combination of pre-existing fiber connectivity, Starlink satellite backhaul, and shared tower infrastructure eliminates the three traditional barriers that have kept archipelago mobile markets underserved: prohibitive capital costs, geographic complexity, and extended deployment horizons.

This analysis examines the infrastructure economics, technical architecture, and regulatory landscape for mobile network deployment across Solomon Islands, with particular focus on how satellite-first backhaul strategies compare to traditional submarine cable approaches.

---

## The capital equation shifts dramatically with infrastructure partnerships

Launching a greenfield mobile network across Pacific islands typically requires **$50-150 million in CAPEX** for a 100-500 site deployment. This breaks down into spectrum acquisition, tower construction, backhaul infrastructure, core network equipment, and off-grid power systems. The geographic dispersion of archipelago populations multiplies costs that mainland operators take for granted—helicopter deployments, satellite terminals at every site, and hybrid solar-diesel power systems push per-site costs to **$135,000-$337,000**, a 35% premium over global averages.

Infrastructure partnerships fundamentally restructure this capital requirement. Tower sharing alone delivers **30-50% savings** on the largest single cost category. When combined with backhaul leasing (avoiding $5-30 million in satellite or microwave infrastructure) and access to existing fiber connectivity, partnerships can reduce total initial CAPEX by **50-80%**. The Digicel-Telstra Pacific transaction provides a benchmark: Digicel invested over **$850 million** building PNG's mobile network from scratch over 15 years; a partnership-based entrant could achieve comparable coverage for a fraction of that investment.

| Cost Category | Build-from-Scratch | Partnership Model | Savings |
|--------------|-------------------|-------------------|---------|
| Tower infrastructure (100 sites) | $13.5-33.7M | $4-12M (co-location) | 50-70% |
| Backhaul network | $5-30M | Lease-based OPEX | 80-90% |
| Spectrum licensing | $1-20M | Same | 0% |
| Core network | $5-30M | Cloud-native option | 30-50% |
| Power systems | $2-15M | Shared sites | 40-60% |
| **Total Estimated** | **$26-129M** | **$10-50M** | **60-70%** |

Timeline compression proves equally significant. Traditional tower construction in remote Pacific sites takes **6-18 months per site**; co-location on existing infrastructure reduces this to **days or weeks**. The **Solomon Islands National Broadband Infrastructure Project (SINBIP)** exemplifies the opportunity: 161 government-built tower sites available for operator access by 2026 through Solomon Tower Limited, the state-owned enterprise managing this infrastructure on a commercial lease basis.

---

## Starlink transforms the backhaul economics for remote islands

The traditional choice between submarine cables and satellite backhaul has been a false binary—submarine cables offer massive bandwidth at low per-gigabyte costs but require **$6,000-50,000 per kilometer** in capital investment and **3-5 years** from planning to operation. Geostationary satellites provided coverage anywhere but with 500-600ms latency that degraded voice quality and made modern data services unusable. LEO satellite constellations, particularly Starlink, have created a third option that fundamentally changes the calculus for island networks.

**KDDI Japan provides the proof point**: 1,200 mobile towers now use Starlink backhaul across Japan's 6,000+ islands and 16,000+ mountains. KDDI's extensive evaluation confirmed that Starlink "met network technical guidelines for latency, jitter, and uplink/downlink bandwidth" with "customer experience comparable to optical fiber." The service launched commercially in December 2022 on Hatsushima island.

### Technical specifications comparison

| Factor | Starlink (LEO) | Submarine Cable | GEO Satellite | Microwave |
|--------|---------------|-----------------|---------------|-----------|
| **Latency** | 25-60ms (100+ms islands) | 5-10ms per 1,000km | 500-600ms | Near-zero |
| **Bandwidth per site** | 100-350 Mbps | Terabits (shared) | 50-200 Mbps | 1-20 Gbps |
| **CAPEX per site** | $2,500-10,000 | Millions (amortized) | $15,000-50,000 | $5,000-50,000 |
| **Monthly OPEX** | $300-500 | IRU/lease fees | $2,000-10,000 | Spectrum + maintenance |
| **Deployment time** | Days-weeks | 3-5 years | Weeks-months | Weeks-months |
| **Physical vulnerability** | None | High (anchor/fishing) | None | Low |

Starlink's pricing structure for enterprise backhaul applications includes terminal costs of **$2,500-10,000** depending on configuration, with monthly service fees of **$300-500** for business plans. The new 2025 maritime/global pricing adds a $150/month terminal access fee plus **$1-2/GB** for data consumption, creating predictable unit economics for network planning.

The critical caveat for archipelago deployments: Starlink's official documentation explicitly states that "customers in certain remote locations will experience higher latency (e.g., Oceans, Islands, Antarctica)." Real-world latency of **100ms or more** for Pacific island locations must be factored into core network architecture decisions—but this still represents a **5x improvement** over GEO satellite latency.

---

## Hybrid architectures maximize both reach and resilience

The optimal backhaul strategy for archipelago networks combines multiple technologies based on geography and traffic density. The **Coral Sea Cable System** (4,700km, **40 Tbps capacity**) provides high-bandwidth, low-latency connectivity to main population centers in Solomon Islands and PNG. From these anchor points, a hybrid architecture extends coverage across dispersed islands.

**Recommended architecture pattern:**
- **Main trunk**: Submarine cable (Coral Sea Cable) to Honiara gateway
- **Inter-island distribution**: Microwave links for islands within 50km with line-of-sight (Digicel demonstrated 189km microwave link in Tonga)
- **Remote islands**: Starlink terminals for sites beyond microwave range
- **Disaster redundancy**: Satellite backup for all fiber-connected sites

Solomon Islands already benefits from improved international connectivity. The Coral Sea Cable reduced wholesale capacity costs by up to **80%** compared to pre-cable satellite-only connectivity. The Solomon Islands Domestic Network (SIDN) extends 730km of submarine cable to connect Honiara with Auki, Noro, and Taro. Our Telekom uses this combination of cable and continued satellite for remote sites.

For a new entrant partnering with an infrastructure provider like SATSOL that already has fiber access and Starlink capability, the backhaul problem essentially disappears from the capital stack. Instead of $20-30 million in backhaul infrastructure investment, the operator pays predictable monthly fees per site while maintaining geographic flexibility to add coverage incrementally.

---

## SINBIP creates 161 ready-to-use tower sites by 2026

The Solomon Islands National Broadband Infrastructure Project represents a transformational opportunity for mobile operators. Funded through a **CNY 448.9 million (~$66-100 million)** concessional loan from Exim Bank of China at 1.0% interest over 20 years, SINBIP will deliver 161 3G/4G-capable tower sites with microwave and VSAT backhaul connections by 2026.

**Current deployment status (September 2024):**
- **Phase 1**: 14 sites operational (13 Guadalcanal + 1 Russell Islands VSAT site)
- **Phase 2**: Choiseul and Western Provinces deployment commenced
- **Phase 3**: Malaita, Makira, Temotu, Renbel targeted for Q1 2025

Solomon Tower Limited (STL), a new state-owned enterprise, will own and manage this infrastructure. The government explicitly designed a **public-private partnership model** enabling infrastructure sharing with all operators—Solomon Telekom, bmobile, ISPs, and new entrants. STL will negotiate commercial lease terms with operators; revenues service the Exim Bank loan.

Tower specifications include solar power systems at most sites, reducing operator OPEX significantly compared to diesel-dependent alternatives. Sites use 1.8-meter VSAT dishes where microwave backhaul isn't feasible, providing baseline connectivity that operators can supplement or replace with higher-bandwidth alternatives.

---

## The regulatory framework favors new entrants

Solomon Islands' telecommunications regulatory environment presents surprisingly low barriers to entry compared to many markets. The Telecommunications Commission Solomon Islands (TCSI) operates as an independent statutory authority, and critically, **does not charge operators for radio spectrum use**. The Commission explicitly encourages competition by "maintaining one form of service licence which authorises all manner of telecommunications services, and it does not charge operators for the use of radio-spectrum."

**Licensing pathway:**
- **Class Licence**: Standard form application, 45-day processing if criteria satisfied
- **Individual Licence**: Competitive selection process when number restricted
- **Spectrum assignment**: Administrative allocation (not auction) with no ongoing fees

Current spectrum allocations show availability for additional operators. Our Telekom holds 700 MHz (Band 28), 850 MHz, 900 MHz, 1800 MHz (Band 3), and 2100 MHz for various service layers. BMobile operates on 900 MHz, 1800 MHz, and 2100 MHz but has not deployed 4G. Starlink received a license in 2024 after regulatory review, demonstrating the path for new connectivity providers.

**Land access complexity** represents the primary regulatory challenge. Approximately **87% of Solomon Islands land is customary land**, managed by local indigenous groups rather than formal government title systems. Tower siting requires community consent through direct negotiation with landowners—a process that can extend from months to years depending on community dynamics. Environmental approval under the Environment Regulations 2008 requires Environmental Impact Statements for significant developments.

---

## Climate resilience justifies satellite-first architecture

Pacific island telecommunications face existential climate risks that mainland networks rarely encounter. The January 2022 Tonga volcanic eruption and tsunami demonstrated the fragility of submarine cable infrastructure in catastrophic events. The 827km cable connecting Tonga to Fiji wasn't merely cut—an **80km section was shredded into multiple pieces**, moved 5km by undersea blast forces, and buried under sediment.

**Tonga communication impact:**
- International connectivity: **38-day complete outage**
- Domestic cable restoration: **18 months**
- Cable repair ship transit: 8+ days from Port Moresby (4,200km away)
- Daily ship costs: **$35,000-50,000**
- Total damage estimate: **$90.4 million** (World Bank GRADE assessment)

Cyclone impacts across the Pacific provide additional data points:

| Event | Total Damage | Telecom Impact |
|-------|-------------|----------------|
| Cyclone Winston (Fiji 2016) | $1.4 billion | 80% lost power, island communications severed |
| Cyclone Pam (Vanuatu 2015) | $449 million | One tower operational in Port Vila post-cyclone |
| Cyclone Harold (2020) | Multi-country | Communications destroyed across 7+ islands |

Satellite backhaul provides inherent resilience that terrestrial and submarine infrastructure cannot match. With no ground-based single points of failure, Starlink service can continue operating through events that sever cables or destroy towers—provided the terminal and power system survive. This resilience has real-world validation: Starlink deployed over 800 emergency kits across 120+ missions following Florida hurricanes, California wildfires, and the Maui disasters.

**World Bank analysis** confirms that investing in resilient telecommunications infrastructure delivers a **4:1 return**—$4 in avoided losses and accelerated recovery for every $1 invested in hardening. For island networks, this translates to cyclone-rated tower designs (wind ratings of 200-320+ km/h), reinforced equipment shelters, and backup power systems with **48-72 hours of autonomy** for critical sites.

---

## Low-band spectrum enables economically viable rural coverage

Network architecture decisions fundamentally shape deployment economics across dispersed island populations. Solomon Islands' 85% rural population living across 1,000+ islands requires coverage-focused spectrum strategy rather than capacity-first approaches suited to dense urban markets.

**700 MHz spectrum delivers transformational coverage economics.** A single 700 MHz cell site provides **5-10km coverage radius** compared to 2-3km for 1800 MHz—reducing required site counts by approximately **50%** and coverage costs by **70%** versus 2100 MHz deployments. The APT700 band harmonization across Asia-Pacific provides equipment ecosystem scale benefits.

**Coverage comparison by frequency:**

| Frequency | Typical Rural Radius | Sites for Equivalent Coverage | Relative Cost |
|-----------|---------------------|------------------------------|---------------|
| 700 MHz | 5-10 km | 1x baseline | 1.0x |
| 1800 MHz | 2-3 km | 2-3x | 2.0x |
| 2100 MHz | 2-3 km | 2-3x | 2.3x |
| 2600 MHz | 1 km | 4-5x | 3.5x |

For archipelago deployment, the recommended spectrum strategy prioritizes 700 MHz as the coverage layer across all sites, with 1800 MHz capacity supplements only in population centers like Honiara. This approach minimizes site count—the primary cost driver—while providing adequate capacity for rural population densities.

**Core network architecture** must accommodate satellite backhaul latency. Cloud-native architectures offer CAPEX advantages (OPEX model versus upfront investment) but add latency to already-elevated satellite paths. The optimal approach deploys edge User Plane Functions (UPF) at regional hubs, processing local traffic without backhauling to distant cloud cores. This hybrid architecture—cloud-native control plane with distributed user plane—balances cost efficiency with latency management.

---

## Open RAN and infrastructure sharing compound cost advantages

Beyond partnership-based tower and backhaul access, additional architectural choices can further reduce total cost of ownership. **Open RAN deployments** deliver **25-30% TCO reduction** compared to traditional integrated RAN solutions, with particular benefits for cost-constrained island deployments. Multi-vendor flexibility reduces supply chain risk, while lower-cost radio units from emerging vendors (NuRAN, Parallel Wireless) suit minimum-viable rural site configurations.

**Rural site specifications for cost-optimized deployment:**

| Component | Specification | Power Draw |
|-----------|--------------|------------|
| Radio unit (700 MHz, single-sector) | 150-500W | - |
| Baseband processing | Centralized or local | 100-300W |
| Satellite terminal (Starlink) | Standard business | 100-200W |
| Total site power | 350-1,000W | - |
| Solar array sizing | 4-8 kW | - |
| Battery capacity (3-day autonomy) | 25-75 kWh | - |
| **Estimated CAPEX** | **$25,000-50,000** (excluding tower) | - |

**Infrastructure sharing regulations** in Solomon Islands currently operate on voluntary commercial terms rather than mandated access pricing. TCSI supports sharing arrangements that improve rural coverage but hasn't implemented mandatory frameworks. The SINBIP/Solomon Tower Limited model provides de facto open access for government-funded sites, while private tower sharing requires bilateral negotiation.

For a new entrant, the combination of SINBIP tower access, partnership-based backhaul, cloud-native core, Open RAN, and low-band spectrum focus could enable network launch at **$15-30 million initial CAPEX**—an order of magnitude below traditional greenfield deployments.

---

## Market opportunity and competitive dynamics

Solomon Islands' mobile market remains a duopoly with significant competitive gaps. **Our Telekom** (wholly owned by Solomon Islands National Provident Fund since 2014) operates as the dominant provider with 2G/3G/4G coverage across all nine provinces. **bmobile-Vodafone** (Telikom PNG subsidiary) covers only four provinces with 2G/3G service—no 4G deployment. Combined mobile penetration remains low relative to regional benchmarks, with high data costs repeatedly noted as a concern by the telecommunications commissioner.

A partnership-enabled entrant leveraging existing infrastructure could differentiate on:
- **Coverage**: Faster rural deployment via SINBIP and partnership sites
- **Price**: Lower cost structure enables competitive pricing
- **Technology**: 4G/LTE service outside main centers
- **Resilience**: Satellite-first backhaul maintains service through disasters

The population of approximately **823,000** (60% under age 25) represents a modest but growing market. Geographic dispersion means per-subscriber infrastructure costs exceed mainland markets, but partnership models that eliminate fixed infrastructure investment shift economics toward sustainable unit economics.

---

## Conclusion: Partnership-first strategy unlocks archipelago markets

The infrastructure economics for launching mobile networks across archipelagos have fundamentally shifted. Traditional approaches requiring $100+ million in capital investment and multi-year deployment timelines face a new alternative: partnership-based models that leverage existing fiber, satellite, and tower infrastructure to achieve equivalent coverage for **$15-30 million** in initial capital and deployment timelines measured in months rather than years.

The technical architecture for this approach combines **Starlink satellite backhaul** (100-350 Mbps, days to deploy) for remote sites with fiber connectivity (via partnerships accessing Coral Sea Cable) for main population centers. **Low-band 700 MHz spectrum** reduces required site counts by 50% compared to mid-band approaches. **Open RAN** and **cloud-native core networks** further compress both capital and operating costs.

For Solomon Islands specifically, the convergence of SINBIP's 161 government-funded tower sites, TCSI's zero-fee spectrum licensing, and infrastructure partnerships with established providers creates a window for market entry that didn't exist even five years ago. The regulatory framework presents no structural barriers; customary land complexity for tower siting represents the primary operational challenge.

Climate resilience provides strategic justification for satellite-first architecture beyond pure economics. When submarine cables take 38 days to 18 months to repair after catastrophic events, satellite backhaul transitions from cost-optimization strategy to business continuity requirement. The **4:1 return on resilience investment** documented by World Bank analysis applies directly to network architecture decisions.

Infrastructure investors, development finance institutions, and telecom operators evaluating Pacific island opportunities should recognize that the partnership model—accessing existing fiber, Starlink backhaul, and shared tower infrastructure—transforms archipelago deployments from marginal investment cases into commercially viable opportunities with manageable risk profiles.

## Key Sources from Research

**Infrastructure Economics & Case Studies**
- [Digicel Papua New Guinea deployment](https://restofworld.org/2021/papua-new-guinea-calling/) - $850M+ investment over 15 years for comprehensive PNG network
- [GSMA Mobile Backhaul Overview](https://www.gsma.com/solutions-and-impact/technologies/networks/gsma_resources/mobile-backhaul-an-overview/) - Technical standards and deployment approaches

**Starlink Cellular Backhaul Validation**
- [KDDI Japan Starlink deployment](https://news.kddi.com/kddi/corporate/english/newsrelease/2022/12/01/6415.html) - 1,200 towers using Starlink across Japanese islands
- [KDDI deployment analysis](https://www.telecomsinfrastructure.com/2023/01/kddi-plans-to-improve-rural.html?m=0) - Technical validation and performance metrics

**Solomon Islands Infrastructure**
- [SINBIP government announcement](https://solomons.gov.sb/solomon-tower-limited-delivered-14-mobile-tower-sites-under-the-solomon-islands-national-broadband-infrastructure-project-sinbip/) - 161 tower sites project details
- [SINBIP progress update](https://www.sibconline.com.sb/proposed-161-towers-project-progresses/) - Phase deployment status
- [Coral Sea Cable System](https://www.submarinenetworks.com/en/systems/asia-australia/coral-sea) - 4,700km, 40 Tbps capacity specifications

**Regulatory Framework**
- [TCSI website](https://www.tcsi.org.sb/) - Telecommunications Commission of Solomon Islands
- [TCSI licensing process](https://www.tcsi.org.sb/apply-for-a-licence) - Application procedures and requirements
- [TCSI spectrum policy](https://www.tcsi.org.sb/index.php/library/annual-reports/62-2013-annual-report/file) - Zero-fee spectrum allocation approach
- [Starlink Solomon Islands license](https://developingtelecoms.com/telecom-technology/satellite-communications-networks/17241-starlink-clear-to-operate-in-solomon-islands-after-receiving-licence.html) - 2024 regulatory approval

**Climate Resilience Case Studies**
- [Tonga volcanic eruption cable damage](https://news.berkeley.edu/2024/05/09/submarine-communications-cables/) - 80km section destroyed, 38-day outage
- [Tonga cable repair timeline](https://www.voanews.com/a/volcano-damage-to-tonga-undersea-cable-worse-than-expected-/6443686.html) - 18-month domestic restoration
- [Cloudflare Tonga analysis](https://blog.cloudflare.com/internet-is-back-in-tonga-after-38-days-of-outage/) - Internet restoration timeline
- [World Bank Tonga assessment](https://thedocs.worldbank.org/en/doc/b69af83e486aa652d4232276ad698c7b-0070062022/original/GRADE-Report-Tonga-Volcanic-Eruption.pdf) - $90.4M total damage
- [World Bank resilience guide 2024](https://documents1.worldbank.org/curated/en/099121724111526960/pdf/P1785971617dfc0361b79b10ed943988d67.pdf) - 4:1 ROI on resilience investment

**Emergency Response & Disaster Recovery**
- [Starlink emergency response](https://starlink.com/emergency-response) - Deployment capabilities
- [D4H emergency communications analysis](https://www.d4h.com/blog/improving-emergency-management-communications-with-starlink-satellite-internet) - Disaster recovery use cases

---

## Research from Perplexity

<!-- Paste Perplexity research results here -->

---

## Research from Gemini

Infrastructure Economics and Technical Architecture for Archipelagic Mobile Network Deployment: The Solomon Islands ContextI. Executive Summary and Strategic MandateThe deployment of modern mobile telecommunications infrastructure across the Solomon Islands archipelago is fundamentally constrained by challenging geographic dispersal, high environmental vulnerability, and an unfavorable density-to-cost ratio. To bridge the digital divide and achieve the national goal of increasing connectivity to over 80% of the population 1, the reliance on traditional, competitive, capital-intensive models is proving economically unsustainable. More than half the population in the Pacific Islands remains unconnected to mobile internet, highlighting a significant investment gap that market forces alone cannot close by 2030.2This report establishes that the only financially viable and strategically resilient approach for the Solomon Islands is the implementation of a Hybrid Infrastructure Strategy. This strategy is anchored by the State-Owned Infrastructure Sharing Model (the Solomon Islands National Broadband Infrastructure Project, SINBIP) and relies on a technical architecture that mandatorily integrates Low Earth Orbit (LEO) satellite backhaul for resilience and coverage efficiency, complementing existing or planned submarine fiber capacity. This combination effectively externalizes massive network CAPEX, accelerates deployment timelines, and guarantees essential connectivity continuity in the face of frequent and severe natural disasters.31.1 Strategic Findings SynthesisThe SINBIP infrastructure sharing model is confirmed as the principal financial lever, allowing Mobile Network Operators (MNOs) to convert approximately 40% of their potential passive infrastructure capital expenditures (CAPEX) into manageable operational expenditures (OPEX).5 This capital conversion liberates resources for core network investment and service innovation.Technically, the archipelagic deployment requires the highly efficient coverage propagation provided by low-band spectrum (e.g., 700/800 MHz).6 For backhaul, the reliance on submarine cable provides necessary bulk capacity and ultra-low latency for major centers, but its extreme vulnerability mandates the adoption of LEO satellite backhaul as a non-negotiable resilience overlay for all remote tower sites.1.2 Key RecommendationsMandate Hybrid Backhaul: Require all MNOs utilizing the SINBIP sites to integrate LEO satellite backhaul as the critical secondary link, prioritizing network resilience over marginal OPEX savings.Optimize Spectrum Utilization: Expedite the allocation of low-band spectrum (700/800 MHz) by the Telecommunications Commission Solomon Islands (TCSI) to maximize coverage per tower site and ensure cost-effective rollout across the 161 planned STL locations.6Capitalize Universal Access Fund: Formally allocate Universal Access Special Fund revenue to subsidize the OPEX associated with satellite backhaul capacity for the most remote, commercially marginal tower sites, linking regulatory fees directly to the achievement of universal service targets.7II. Infrastructure Economics and Archipelagic Context2.1 Geographic and Economic Drivers of High CAPEXThe fundamental economic challenge in the Solomon Islands arises from the extreme geographical dispersal of population centers across numerous islands. Achieving comprehensive mobile coverage across such an archipelagic region necessitates the construction of multiple, widely separated transmission points.9 This dispersion drastically inflates the network CAPEX per subscriber relative to high-density or continental deployments.Furthermore, the region is highly exposed to catastrophic natural hazards, including tropical cyclones, floods, and seismic events.4 This necessitates significant investment in infrastructure hardening, redundancy, and robust power systems—all of which increase the baseline CAPEX. The economic rationale for resilience planning is underscored by historical data; it is predicted that a 1-in-100-year cyclone event in the capital cities of Pacific Island nations could result in economic losses amounting to as much as 60% of GDP.4 Therefore, network infrastructure investment must incorporate high durability and backup capability, raising the initial cost burden for operators and regulators alike.2.2 Technical Foundation: The Criticality of Low-Band SpectrumAchieving broad, cost-effective coverage in a geographically challenging area like the Solomon Islands hinges on spectrum efficiency. Modern mobile networks utilize a mix of frequencies, but low-band spectrum (sub-1 GHz, typically 700 MHz and 800 MHz) remains critical for connectivity in rural and remote communities.6The physical characteristics of low-band frequencies allow a single low-band site to cover approximately three times the area of a site using mid-band spectrum.6 In the context of the ambitious national coverage project (SINBIP), where tower construction is costly and logistically challenging, minimizing the number of base station sites required to meet the coverage mandates (such as the 81% population coverage obligation previously set for bemobile 14) is paramount. By deploying 4G/5G services across these lower frequencies, MNOs can realize substantial reductions in both CAPEX (fewer towers needed) and OPEX (reduced power and maintenance costs).6 This technical optimization provides an essential leverage point for making the commercial rollout to geographically challenging areas profitable. While MNOs like Solomon Telekom and Bemobile have been allocated GSM spectrum 15, the specific modern allocations for 4G/5G (e.g., 700 MHz, 800 MHz, 2.6 GHz 16) are detailed in the TCSI's National Radio Frequency Spectrum Plan.182.3 The Role of the Telecommunications Commission (TCSI)The regulatory framework is essential for transforming investment capacity. The TCSI is mandated with the responsibility for spectrum allocation, licensing, and setting annual fees for the use of particular spectrum bands.7 Crucially, the annual fees collected for spectrum rights are required by Regulation to be paid into the Universal Access Special Fund.7This regulatory mechanism provides a direct means of subsidizing service delivery in commercially marginal areas. Since backhaul connectivity for the most remote islands is often the highest variable cost (OPEX), the Universal Access Fund should be strategically deployed to offset the operating costs of high-cost backhaul solutions, such as LEO satellite capacity, for the low-density tower sites managed by the State-Owned Enterprise, STL. This action formalizes the link between regulatory revenue and the national objective of universal service provision.III. Backhaul Comparative Analysis: TCO and Resilience ModelingThe strategic decision on backhaul technology must balance cost, capacity, and resilience, especially in a high-risk operational environment.3.1 Submarine Fiber-Optic Cable (The High-Capacity Anchor)Submarine fiber-optic cables offer the highest possible capacity and lowest latency, making them indispensable for international trunk routes and major population centers. However, this technology involves enormous capital outlay. Projects spanning major oceanic routes, such as trans-Pacific links, can cost up to $400 million.19 Key cost components include the fiber cable itself, which ranges from $6,000 to $20,000 per kilometer, dependent on armoring and fiber pair count, and repeaters, which cost approximately $200,000 each and must be installed every 60–80 kilometers.19Contemporary funding models show a dramatic shift in ownership, with content providers (Google, Meta, etc.) now consuming 75% of international bandwidth and leading most new cable constructions, rather than traditional telco consortiums.19 For archipelagic MNOs, this means purchasing leased capacity, transforming a massive CAPEX challenge into a substantial long-term capacity OPEX commitment.The critical vulnerability of fiber backhaul in the Pacific cannot be overstated. The 2022 Tonga volcano eruption demonstrated how a single physical break, caused by seismic activity or anchor drag, can instantly sever all connectivity to the outside world, resulting in a communications blackout lasting weeks or months while repairs are organized.20 This single point of failure risk mandates that fiber connectivity be augmented by a fully redundant system for resilience purposes.3.2 Emerging LEO Satellite Backhaul (The Resilience Overlay)Low Earth Orbit (LEO) satellite constellations, such as those provided by Starlink, offer a technically viable and operationally superior solution for resilience and rapid rural deployment compared to older satellite generations. LEO systems provide high throughput (individual customers receive speeds in the hundreds of Mbps 21) and achieve low latency, typically between 20–50 milliseconds on land, with potential future improvements below 20ms using inter-satellite laser crosslinks.22 This performance profile is adequate for modern 4G and 5G cellular backhaul requirements.23The financial model of LEO systems involves lower CAPEX for ground terminals, relying primarily on variable OPEX through monthly service plans.24 Commercial plans designed for enterprise and mobile backhaul provide service level agreements (SLAs) with 99.9% availability, and priority data can be scaled up to 5TB per month.24 This pay-as-you-grow model allows MNOs to deploy connectivity rapidly across the remote SINBIP sites, significantly reducing TTM relative to fixed infrastructure.26The most profound benefit of LEO backhaul is its role in disaster recovery. Following the Tonga cable break, existing satellite infrastructure allowed service restoration within days.3 The inherent distribution of connectivity across thousands of satellites provides immediate redundancy that fiber cannot match.27 Furthermore, capabilities like Starlink's "Direct to Cell" provide a crucial layer of coverage by acting as a cellphone tower in space, eliminating dead zones for standard LTE phones in emergencies or remote areas.28 For the Solomon Islands, LEO capacity represents the strategic marginal cost solution for the outer islands, providing necessary redundancy and enabling immediate, cost-effective coverage expansion.Table III.1 provides a comparative summary of the critical TCO factors:Table III.1: Comparative TCO Factors for Archipelagic BackhaulParameterSubmarine Fiber-Optic CableLEO Satellite BackhaulStrategic Implication for SINBIPPrimary Cost TypeHigh CAPEX 19High Variable OPEX 24Hybrid model minimizes CAPEX risk while ensuring operational flexibility.Capacity ScalabilityMassive (Multiple Tbps) 19High (100s of Mbps per terminal) 21Fiber for trunk routes (Honiara); LEO for rural tower aggregation.Latency (Typical)Ultra-Low (sub-10ms)Low (20–50ms) 22LEO latency is sufficient for 4G/5G mobile services.Resilience to FailureVery Low (Single point of failure) 20High (Distributed network) 3LEO is essential for mandated disaster preparedness and service continuity.Deployment TimelineSlow (3-5 years) 19Rapid (Weeks/Months) 26LEO enables immediate expansion across remote STL towers.IV. Financial Modeling: The Impact of Infrastructure Partnerships (SINBIP Case Study)4.1 The SINBIP Structure and MandateThe Solomon Islands National Broadband Infrastructure Project (SINBIP) is fundamentally a state-led infrastructure sharing initiative designed to circumvent the archipelagic CAPEX problem. The project involves the construction of up to 161 new mobile towers, executed through a contract with China Harbour Engineering SI Company Limited and Huawei Technologies.9The Government established Solomon Islands Tower Company Ltd (STL), a State-Owned Enterprise (SOE), to own and manage these infrastructure assets.1 STL’s core mandate is to manage the sites and provide a "clear level playing" field for all operators, including STCL and bemobile, by offering tower space on a lease basis under a "win-win commercial arrangement".1 The project has already activated 57 towers, vastly improving connectivity in provinces such as Western, Isabel, and Guadalcanal.9 STL anticipates that this expansion will extend network coverage to an additional 200,000 people, increasing nationwide mobile access to over 80%.14.2 Financial Transformation: CAPEX Reduction and ReinvestmentThe mandatory infrastructure sharing model transforms the financial structure for MNOs by converting prohibitive, non-core Capital Expenditure (CAPEX) into predictable Operating Expenditure (OPEX) in the form of site lease payments to STL.5 This conversion is the single most effective financial lever available to MNOs operating in the Solomon Islands.Network operators stand to save as much as 40% of capital expenditures by sharing passive infrastructure, particularly antenna sites required for 4G and 5G deployment.5 By shedding the massive upfront investment required to build, acquire land for, and harden the 161 remote towers, MNOs are able to improve their balance sheets and profitability.The capital conserved through this model can be strategically redirected to core network functions, such as modernizing the Core Network, investing in new spectrum acquisition from TCSI, and accelerating Time-to-Market (TTM) for new services.26 This accelerated investment enhances competition and improves service quality, benefiting the consumers reached by the SINBIP expansion.4.3 The TowerCo Operational Challenge for STLThe success and long-term viability of the SINBIP model hinge on STL’s ability to operate efficiently and achieve cost leadership. As a TowerCo, STL’s cost structure will be dominated by four key components: Rent (50–60%), Maintenance (8–12%), Labor (10–20%), and Power (10–15%).31To ensure commercial sustainability, STL must focus intensely on optimizing these costs. Strategies employed by major global TowerCos, such as Ground Lease Buyouts (GLBOs), where the company acquires ownership or long-term rights-of-use (RoU) for tower sites, should be adopted.31 Given its SOE status, STL can leverage governmental support to secure favorable, long-term land access, thus capitalizing the largest operational cost component. Furthermore, managing the 10–15% power OPEX is critical for remote sites, requiring investment in efficient, resilient power solutions (e.g., hybrid solar/battery systems) to control expenses and ensure operational effectiveness, thereby maintaining the "unmatchable prices" required to attract and retain MNO tenants.31Table IV.1: Financial Impact of the SINBIP Sharing ModelMetricTraditional MNO Build ModelSINBIP/STL Sharing ModelValue Delivered to MNOsPassive Infrastructure Cost100% CAPEX (Construction, Land Acquisition)Lease/Rental OPEX (Paid to STL) 1CAPEX reduction up to 40%.5Risk ExposureHigh (Weather damage, property disputes)Medium (Managed and mitigated by STL)Risk pooling and centralized resilience planning.Focus of InvestmentInfrastructure construction and maintenanceCore network, service platforms, customer acquisition 30Improved profitability and accelerated launch of new services.26Coverage Mandate FulfillmentChallenging, high risk of performance penalties 14Accelerated, leveraged by STL's state mandate 9Enables rapid expansion toward 80%+ population coverage.1V. Technical Architecture and Resilient Deployment StrategyThe technical design for the Solomon Islands must be focused on achieving a high degree of disaster resilience, capable of maintaining communications during and immediately after extreme weather events, which are increasingly common.125.1 Hybrid Backhaul Implementation StrategyThe optimal architecture is built on redundancy through hybrid transmission, ensuring no single point of failure can disrupt national communications.The primary backhaul must be anchored by high-capacity submarine fiber connectivity, serving the bulk data requirements of urban centers. However, this capacity must be actively backed up by LEO Satellite Systems deployed as the mandatory secondary and tertiary backhaul layer.LEO backhaul must serve two distinct roles:Remote Aggregation: Connecting all remote SINBIP tower sites where the cost of fixed fiber or terrestrial microwave links is prohibitive. LEO systems provide the necessary capacity (100s of Mbps 21) and acceptable latency (20–50ms 22) for these dispersed sites.Core Network Resilience: Providing immediate disaster recovery support for core network nodes and cable landing stations. The integration of portable satellite assets should be formalized within national disaster protocols.27 As the SOE asset manager, STL should maintain pre-positioned, deployable LEO terminals and integrated backup power to rapidly restore communication services post-cyclone or post-seismic event, transforming telecommunications infrastructure into a tool for recovery, as demonstrated in the Tonga case study.35.2 Passive Infrastructure Hardening and Power SystemsAll newly constructed and existing passive infrastructure must adhere to stringent hardening standards against extreme weather events.32 Physical cabling for fixed broadband and local area networks must be rigorously protected using conduit and lockable enclosures to prevent accidental or environmental damage.33The single most critical element for maintaining network continuity in archipelagic deployments is power resilience. Cyclones frequently lead to widespread power grid failure. Therefore, every SINBIP tower site must be equipped with robust, self-sufficient backup power systems (e.g., diesel generators supplemented by solar/battery hybrids) to ensure continuous operation.32 This proactive investment in backup power is essential to control the TowerCo's high OPEX component and guarantee that the telecommunications system can function during the critical rescue and recovery phases of a disaster.5.3 Modernizing the Core NetworkThe shift to the shared passive infrastructure model creates an imperative and an opportunity for MNOs to modernize their operational systems. MNOs should utilize their conserved capital to transition to flexible, software-driven core architectures.Adopting a Cloud-Native Core architecture offers substantial benefits in an archipelagic environment. By decoupling software functions from underlying hardware and using virtualized roaming gateways 34, operators gain greater operational efficiency and flexibility. This approach minimizes the technical complexity and physical footprint required on remote islands, allowing network functions to be managed centrally. A cloud-native core is ideally suited for managing a distributed network that relies heavily on resilient, high-latency satellite backhaul links for its remote segments.VI. Conclusion and Strategic RecommendationsThe path to achieving nationwide digital inclusion in the Solomon Islands is defined by strategic partnerships and technological duality. The SINBIP infrastructure sharing model provides the necessary economic foundation by shielding MNOs from excessive archipelagic CAPEX, shifting the risk and investment burden to the SOE, STL. However, this commercial viability must be structurally supported by a resilient backhaul framework. Exclusive reliance on high-capacity fiber is a catastrophic vulnerability in the Pacific context; therefore, the Hybrid Backhaul Strategy—fiber for trunk routes and LEO satellite for remote site aggregation and resilience—is non-negotiable for national security and service continuity.The Government and regulators must continue to leverage their instruments, such as the Universal Access Special Fund and spectrum management policies, to ensure the commercial sustainability of the most challenging network segments.Actionable Policy and Investment RecommendationsFormalize LEO Integration and DR Protocol: TCSI must formally introduce regulations mandating that MNOs and STL incorporate LEO satellite connectivity with commercial service level agreements (SLAs) for disaster recovery and as the primary backhaul for the most geographically isolated SINBIP sites.Accelerate Low-Band Allocation: The TCSI should rapidly finalize the allocation and licensing of low-band spectrum (700/800 MHz) to MNOs to maximize the coverage footprint of the new STL towers and achieve the national coverage target efficiently, preventing the deepening of the digital divide in rural areas.6Finance Marginal Connectivity OPEX: The Ministry of Finance and Treasury, in coordination with TCSI, should establish a mechanism to utilize the Universal Access Special Fund revenue to strategically subsidize the OPEX required for maintaining LEO satellite backhaul capacity for the geographically challenging sites, thereby guaranteeing the commercial sustainability of universal access goals.Strengthen STL Financial Structure: STL must execute strategies to secure long-term lease control over its land portfolio and invest strategically in cost-saving measures, particularly high-efficiency hybrid power systems, to maintain operational cost leadership and maximize tower tenancy.

The analysis drew upon strategic reports, industry technical specifications, and regulatory filings from leading global and regional organizations. Here is a list of the primary sources used:

| Source URL | Topic/Focus of Reference |
|---|---|
| [https://www.ifc.org/content/dam/ifc/doc/mgrt/emcompass-note-79-digital-infrastructure-sharing.pdf](https://www.ifc.org/content/dam/ifc/doc/mgrt/emcompass-note-79-digital-infrastructure-sharing.pdf) | Quantifiable CAPEX savings (up to 40%) achieved through passive infrastructure sharing models. |
| [https://www.eetimes.com/why-low-band-spectrum-remains-the-backbone-of-mobile-networks/](https://www.eetimes.com/why-low-band-spectrum-remains-the-backbone-of-mobile-networks/) | The technical and economic rationale for using low-band spectrum (700/800 MHz) for cost-effective, wide-area rural mobile coverage. |
| [https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-investment-gaps-pacific-islands](https://www.google.com/search?q=https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-investment-gaps-pacific-islands) | Analysis of the investment gap in the Pacific Islands and the challenge of connecting more than half the population to mobile internet. |
| [https://starlink.com/updates/network-update](https://starlink.com/updates/network-update) | Current performance metrics of LEO satellite systems, including high download speeds (100s of Mbps) and low latency capabilities. |
| [https://solomons.gov.sb/solomon-tower-limited-delivered-14-mobile-tower-sites-under-the-solomon-islands-national-broadband-infrastructure-project-sinbip/](https://solomons.gov.sb/solomon-tower-limited-delivered-14-mobile-tower-sites-under-the-solomon-islands-national-broadband-infrastructure-project-sinbip/) | Official mandate and coverage objectives of the Solomon Islands Tower Company (STL) and the SINBIP project. |
| [https://tcsi.org.sb/index.php/resources/spectrum-management/spectrum-allocation](https://tcsi.org.sb/index.php/resources/spectrum-management/spectrum-allocation) | Details on the Telecommunications Commission Solomon Islands (TCSI) role in spectrum allocation and the requirement to pay annual fees into the Universal Access Special Fund. |
| [https://blog.telegeography.com/the-economics-of-submarine-cables](https://blog.telegeography.com/the-economics-of-submarine-cables) | Economics of large submarine cable systems, including CAPEX estimates ($250M–$400M) and the shift in construction ownership to content providers. |
| [https://www.dcceew.gov.au/sites/default/files/documents/infrastructure-report.pdf](https://www.dcceew.gov.au/sites/default/files/documents/infrastructure-report.pdf) | Prediction of potential economic losses (up to 60% of GDP) for Pacific Island nations due to a major cyclone event, emphasizing the need for infrastructure resilience. |
| [https://www.alixpartners.com/insights/102ktwo/how-towercos-can-drive-value-in-a-difficult-economic-climate/](https://www.alixpartners.com/insights/102ktwo/how-towercos-can-drive-value-in-a-difficult-economic-climate/) | Breakdown of a typical TowerCo's cost structure, highlighting Rent and Power as the major operational expenditure (OPEX) drivers. |
| [https://www.itu.int/dms\_pub/itu-d/opb/gen/D-GEN-INVEST.CON-2020-PDF-E.pdf](https://www.itu.int/dms_pub/itu-d/opb/gen/D-GEN-INVEST.CON-2020-PDF-E.pdf) | General findings regarding the higher OPEX and CAPEX required for remote rural areas and small island developing states. |
| [https://www.ses.com/blog/efficient-disaster-recovery-and-network-resiliency-when-satellite-spectrum-vital](https://www.ses.com/blog/efficient-disaster-recovery-and-network-resiliency-when-satellite-spectrum-vital) | Case study on the rapid restoration of communications in Tonga after the volcanic eruption using existing satellite infrastructure. |
| [https://starlink.com/business/direct-to-cell](https://starlink.com/business/direct-to-cell) | Technical overview of LEO satellite capabilities, including Direct to Cell services that act as a "cell tower in space" for emergency or remote connectivity. |
| [https://www.preventionweb.net/news/tonga-volcanic-eruption-has-revealed-vulnerabilities-our-global-telecommunication-system](https://www.preventionweb.net/news/tonga-volcanic-eruption-has-revealed-vulnerabilities-our-global-telecommunication-system) | Detailed assessment of Tonga's reliance on a single submarine cable and the severity of the communications outage following the 2022 volcanic eruption. |
| [https://www.gsacom.com/paper/low-band-spectrum-for-lte-and-5g-may-2021/](https://www.google.com/search?q=https://www.gsacom.com/paper/low-band-spectrum-for-lte-and-5g-may-2021/) | Global status of low-band spectrum (sub-1 GHz) deployment for 4G/5G, affirming its critical role in coverage expansion. |
| [https://arxiv.org/html/2508.09839v1](https://arxiv.org/html/2508.09839v1) | Technical data on Starlink performance, including median downlink throughput (152 Mbps) and round-trip time (44 ms). |
| [https://www.dhs.gov/sites/default/files/2024-09/2024aepphasellimpactsofextremeweatherevents.pdf](https://www.dhs.gov/sites/default/files/2024-09/2024aepphasellimpactsofextremeweatherevents.pdf) | Analysis of how extreme weather events disrupt telecommunications and the need for resilient fiber-optic and mobile network infrastructure. |
| [https://solomons.gov.sb/proposed-161-towers-project-progressed/](https://solomons.gov.sb/proposed-161-towers-project-progressed/) | Confirmation of the SINBIP project funding via concessional loan and the plan to connect the new system to the incumbent Solomon Telekom core network. |
| [https://www.ifc.org/content/dam/ifc/doc/mgrt/emcompass-note-79-digital-infrastructure-sharing.pdf](https://www.ifc.org/content/dam/ifc/doc/mgrt/emcompass-note-79-digital-infrastructure-sharing.pdf) | Quantifiable CAPEX savings (up to 40%) achieved through passive infrastructure sharing models. |

---

## Notes

- Research conducted: TBD
- Tools used: [List tools used]
- Raw outputs saved here for reference and verification
