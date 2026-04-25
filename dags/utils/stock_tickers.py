# ---------------------------------------------------------------------------
# S&P 500 CONSTITUENTS
# ---------------------------------------------------------------------------

SP500: list[str] = [
    "A",    "AAPL", "ABBV", "ABNB", "ABT",  "ACGL", "ACN",  "ADBE", "ADI",  "ADM",
    "ADP",  "ADSK", "AEE",  "AEP",  "AES",  "AFL",  "AIG",  "AIZ",  "AJG",  "AKAM",
    "ALB",  "ALGN", "ALL",  "ALLE", "AMAT", "AMCR", "AMD",  "AME",  "AMGN", "AMP",
    "AMT",  "AMZN", "ANET", "AON",  "AOS",  "APA",  "APD",  "APH",  "APO",  "APP",
    "APTV", "ARE",  "ARES", "ATO",  "AVB",  "AVGO", "AVY",  "AWK",  "AXON", "AXP",
    "AZO",  "BA",   "BAC",  "BALL", "BAX",  "BBY",  "BDX",  "BEN",  "BF-B", "BG",
    "BIIB", "BK",   "BKNG", "BKR",  "BLDR", "BLK",  "BMY",  "BR",   "BRK-B","BRO",
    "BSX",  "BX",   "BXP",  "C",    "CAG",  "CAH",  "CARR", "CASY", "CAT",  "CB",
    "CBOE", "CBRE", "CCI",  "CCL",  "CDNS", "CDW",  "CEG",  "CF",   "CFG",  "CHD",
    "CHRW", "CHTR", "CI",   "CIEN", "CINF", "CL",   "CLX",  "CMCSA","CME",  "CMG",
    "CMI",  "CMS",  "CNC",  "CNP",  "COF",  "COHR", "COIN", "COO",  "COP",  "COR",
    "COST", "CPAY", "CPB",  "CPRT", "CPT",  "CRH",  "CRL",  "CRM",  "CRWD", "CSCO",
    "CSGP", "CSX",  "CTAS", "CTRA", "CTSH", "CTVA", "CVNA", "CVS",  "CVX",  "D",
    "DAL",  "DASH", "DD",   "DDOG", "DE",   "DECK", "DELL", "DG",   "DGX",  "DHI",
    "DHR",  "DIS",  "DLR",  "DLTR", "DOC",  "DOV",  "DOW",  "DPZ",  "DRI",  "DTE",
    "DUK",  "DVA",  "DVN",  "DXCM", "EA",   "EBAY", "ECL",  "ED",   "EFX",  "EG",
    "EIX",  "EL",   "ELV",  "EME",  "EMR",  "EOG",  "EPAM", "EQIX", "EQR",  "EQT",
    "ERIE", "ES",   "ESS",  "ETN",  "ETR",  "EVRG", "EW",   "EXC",  "EXE",  "EXPD",
    "EXPE", "EXR",  "F",    "FANG", "FAST", "FCX",  "FDS",  "FDX",  "FE",   "FFIV",
    "FICO", "FIS",  "FISV", "FITB", "FIX",  "FOX",  "FOXA", "FRT",  "FSLR", "FTNT",
    "FTV",  "GD",   "GDDY", "GE",   "GEHC", "GEN",  "GEV",  "GILD", "GIS",  "GL",
    "GLW",  "GM",   "GNRC", "GOOG", "GOOGL","GPC",  "GPN",  "GRMN", "GS",   "GWW",
    "HAL",  "HAS",  "HBAN", "HCA",  "HD",   "HIG",  "HII",  "HLT",  "HON",  "HOOD",
    "HPE",  "HPQ",  "HRL",  "HSIC", "HST",  "HSY",  "HUBB", "HUM",  "HWM",  "IBKR",
    "IBM",  "ICE",  "IDXX", "IEX",  "IFF",  "INCY", "INTC", "INTU", "INVH", "IP",
    "IQV",  "IR",   "IRM",  "ISRG", "IT",   "ITW",  "IVZ",  "J",    "JBHT", "JBL",
    "JCI",  "JKHY", "JNJ",  "JPM",  "KDP",  "KEY",  "KEYS", "KHC",  "KIM",  "KKR",
    "KLAC", "KMB",  "KMI",  "KO",   "KR",   "KVUE", "L",    "LDOS", "LEN",  "LH",
    "LHX",  "LII",  "LIN",  "LITE", "LLY",  "LMT",  "LNT",  "LOW",  "LRCX", "LULU",
    "LUV",  "LVS",  "LW",   "LYB",  "LYV",  "MA",   "MAA",  "MAR",  "MAS",  "MCD",
    "MCHP", "MCK",  "MCO",  "MDLZ", "MDT",  "MET",  "META", "MGM",  "MKC",  "MLM",
    "MMM",  "MNST", "MO",   "MOH",  "MOS",  "MPC",  "MPWR", "MRK",  "MRNA", "MRSH",
    "MS",   "MSCI", "MSFT", "MSI",  "MTB",  "MTD",  "MU",   "NCLH", "NDAQ", "NDSN",
    "NEE",  "NEM",  "NFLX", "NI",   "NKE",  "NOC",  "NOW",  "NRG",  "NSC",  "NTAP",
    "NTRS", "NUE",  "NVDA", "NVR",  "NWS",  "NWSA", "NXPI", "O",    "ODFL", "OKE",
    "OMC",  "ON",   "ORCL", "ORLY", "OTIS", "OXY",  "PANW", "PAYX", "PCAR", "PCG",
    "PEG",  "PEP",  "PFE",  "PFG",  "PG",   "PGR",  "PH",   "PHM",  "PKG",  "PLD",
    "PLTR", "PM",   "PNC",  "PNR",  "PNW",  "PODD", "POOL", "PPG",  "PPL",  "PRU",
    "PSA",  "PSKY", "PSX",  "PTC",  "PWR",  "PYPL", "Q",    "QCOM", "RCL",  "REG",
    "REGN", "RF",   "RJF",  "RL",   "RMD",  "ROK",  "ROL",  "ROP",  "ROST", "RSG",
    "RTX",  "RVTY", "SATS", "SBAC", "SBUX", "SCHW", "SHW",  "SJM",  "SLB",  "SMCI",
    "SNA",  "SNDK", "SNPS", "SO",   "SOLV", "SPG",  "SPGI", "SRE",  "STE",  "STLD",
    "STT",  "STX",  "STZ",  "SW",   "SWK",  "SWKS", "SYF",  "SYK",  "SYY",  "T",
    "TAP",  "TDG",  "TDY",  "TECH", "TEL",  "TER",  "TFC",  "TGT",  "TJX",  "TKO",
    "TMO",  "TMUS", "TPL",  "TPR",  "TRGP", "TRMB", "TROW", "TRV",  "TSCO", "TSLA",
    "TSN",  "TT",   "TTD",  "TTWO", "TXN",  "TXT",  "TYL",  "UAL",  "UBER", "UDR",
    "UHS",  "ULTA", "UNH",  "UNP",  "UPS",  "URI",  "USB",  "V",    "VICI", "VLO",
    "VLTO", "VMC",  "VRSK", "VRSN", "VRT",  "VRTX", "VST",  "VTR",  "VTRS", "VZ",
    "WAB",  "WAT",  "WBD",  "WDAY", "WDC",  "WEC",  "WELL", "WFC",  "WM",   "WMB",
    "WMT",  "WRB",  "WSM",  "WST",  "WTW",  "WY",   "WYNN", "XEL",  "XOM",  "XYL",
    "XYZ",  "YUM",  "ZBH",  "ZBRA", "ZTS",
]

# ---------------------------------------------------------------------------
# GICS SECTORS
# ---------------------------------------------------------------------------

GICS_SECTORS = {
    # ── Information Technology  (target: ~85, already adequate) ─────────────
    "Information Technology": {
        "Software & Services": [
            # Top 40 by market cap — populate from screener
            "MSFT", "AAPL", "GOOGL", "META", "CRM", "NOW", "ORCL", "SAP",
            "ADBE", "INTU", "SNOW", "PLTR", "UBER", "ABNB", "SHOP", "WDAY",
            "TEAM", "DDOG", "ZS", "OKTA", "MDB", "NET", "HUBS", "BILL",
            "TWLO", "GTLB", "PATH", "APPF", "PCTY", "PAYC",
            "SSNLF", "CDNS", "SNPS", "SNPS", "PTC",
            "VEEV", "CSGP",             # Niche / upstart additions
            "CWAN",   # Clearwater Analytics — institutional investment data
            "IBTA",   # Ibotta — performance marketing SaaS
            "SOUN",   # SoundHound — voice AI
            "AI",     # C3.ai — enterprise AI
            "BBAI",   # BigBear.ai — decision intelligence
        ],
        "Technology Hardware & Equipment": [
            # Top 25 by market cap
            "AAPL", "DELL", "HPQ", "HPE", "STX", "WDC", "NTAP", "PSTG",
            "CSCO", "ANET", "CIEN", "LITE", "VIAV", "COHU",
            "GLW",   # already in watchlist — optical/fiber infrastructure
            "VRT",   # already in watchlist — data center power
            "SMCI",  "WOLF", "AMKR", "ONTO",
            "ARLO",  "SONO",             # Niche additions
            "NTGR",   # Netgear — SMB networking
            "LSCC",   # Lattice Semiconductor — low-power FPGAs
        ],
        "Semiconductors & Equipment": [
            # Top 20 by market cap
            "NVDA", "TSM",  "ASML", "AVGO", "AMD",  "QCOM", "TXN",  "INTC",
            "AMAT", "LRCX", "KLAC", "MU",   "MRVL", "ON",   "STM",
            "MPWR", "SWKS", "QRVO", "MCHP", "ADI",
            # Niche / upstart additions
            "AMBA",   # Ambarella — edge AI vision chips
            "CEVA",   # CEVA — semiconductor IP licensing
            "FORM",   # FormFactor — wafer probe cards
            "ACLS",   # Axcelis — ion implant equipment
            "IONQ",   # IonQ — quantum computing hardware
        ],
    },
    # ── Health Care  (target: 60, adequate) ─────────────────────────────────
    "Health Care": {
        "Pharmaceuticals, Biotech & Life Sciences": [
            # Top 35 by market cap
            "LLY",  "JNJ",  "NVO",  "ABBV", "MRK",  "AZN",  "PFE",  "BMY",
            "AMGN", "GILD", "VRTX", "REGN", "BIIB", "MRNA",             "ALNY", "IONS", "RARE", "KYMR",  # BLUE delisted; KYMR = Kymera RNA degradation
            "NBIX", "ACAD", "INCY", "BMRN", "SRPT",
            "NTLA", "BEAM", "EDIT", "CRSP", "RXRX",
            "ILMN", "A",    "TMO",  "IDXX", "SDGR",
            # Niche / upstart additions
            "ROIV", "ARWR",  # RNA therapeutics
            # base editing cardiovascular
            "MDGL",              # NASH/metabolic liver disease
            "HRMY",              # rare neurological diseases
        ],
        "Health Care Equipment & Services": [
            # Top 25 by market cap
            "UNH", "CVS", "MCK", "CAH", "CI",  "HUM", "ELV",
            "MDT", "ABT", "BSX", "SYK", "EW",  "ZBH",             "ISRG","DXCM","PODD","NEOG","NVCR",
            "RMD", "PHG", "GMED","LMAT","STVN",
            # Niche additions
            # Accolade — health navigation/advocacy platform
            "HIMS",   # Hims & Hers — telehealth consumer
            "DOCS",   # Doximity — physician network SaaS
            "OMCL",   # Omnicell — pharmacy automation
            "TNDM",   # Tandem Diabetes — insulin delivery devices
        ],
    },
    # ── Financials  (target: 55, adequate) ──────────────────────────────────
    "Financials": {
        "Banks": [
            # Top 20 by market cap
            "JPM", "BAC", "WFC", "C",   "GS",  "MS",  "USB", "PNC",
            "TFC", "COF", "FITB","KEY", "RF",  "HBAN","CFG",
            "MTB", "ZION","FITB", "WAL", "SBCF",
            # Niche additions — regional stress indicators
            "BANC",   # PacWest — regional bank sentiment proxy
            "FLG",   # NY Community Bancorp — CRE exposure bellwether
            "OZK",    # Bank OZK — construction/CRE lending
        ],
        "Diversified Financials": [
            # Top 20 by market cap — ensure market infrastructure is represented
            "BRK-B","BLK", "SCHW","AXP", "SPGI","MCO", "CME", "ICE",
            "CBOE", "NDAQ","MSCI","FDS", "MKTX","LPLA","RJF",
            "BEN",  "IVZ", "TROW","AMG", "VOYA",
            # Niche / upstart additions
            "FIG",    # Figma — already in watchlist (alt asset mgmt proxy)
            "HOOD",   # Robinhood — retail investor sentiment proxy
            "COIN",   # Coinbase — crypto market infrastructure
            "MSTR",   # MicroStrategy — Bitcoin treasury proxy
            "SFM",    # Sprouts — atypical but useful consumer spend proxy
        ],
        "Insurance": [
            # Top 15 by market cap
            "BRK-B","MET", "PRU", "AFL", "AIG", "CB",  "TRV", "ALL",
            "PGR",  "HIG", "LNC", "GL",  "RLI", "KNSL","WRB",
            # Niche additions
            "ROOT",   # Root Insurance — usage-based auto, insurtech proxy
            "LMND",   # Lemonade — AI-native insurance
            "RYAN",   # Ryan Specialty — specialty wholesale insurance
        ],
    },
    # ── Consumer Discretionary  (target: 60, adequate) ──────────────────────
    "Consumer Discretionary": {
        "Retailing": [
            # Top 20 by market cap
            "AMZN","TSLA","HD",  "TGT", "LOW", "TJX", "ROST","BURL",
            "ORLY","AZO", "DG",  "DLTR","W",   "ETSY","EBAY",
            "RH",  "WSM", "BBWI","ARKO",
        ],
        "Consumer Services": [
            # Top 15 by market cap
            "MCD", "SBUX","YUM", "CMG", "DPZ", "DNUT","JACK","WEN",
            "HLT", "MAR", "H",   "IHG", "WH",  "TNL", "VCNX",
            # Niche additions
            "EAT",   # Dine Brands — casual dining health check
            "CAKE",   # Cheesecake Factory — mid-market consumer spend
            "BROS",   # Dutch Bros — high-growth QSR
        ],
        "Consumer Durables & Apparel": [
            # Top 15 by market cap
            "NKE", "LULU","PVH", "RL",  "VFC", "VFC", "UA",  "CROX",
            "BOOT","DECK","WWW", "COLM","ONON","BIRK",
            # Niche additions
            "SFIX",   # Stitch Fix — personalized fashion, AI demand signal
            "RENT",   # Rent the Runway — sharing economy consumer health
        ],
        "Automobiles & Components": [
            # Top 10 by market cap
            "TSLA","GM",  "F",   "TM",  "HMC", "RIVN","LCID",            "STLA","RACE",
            # Niche / international additions
            "1211.HK",  # BYD — China EV + battery, essential
            "POWR",     # Powerschool — supply chain adjacent; swap if needed
            "LEA",      # Lear Corp — auto components, EV seat/electrical
            "APTV",     # Aptiv — auto electrical architecture
            "BWA",      # BorgWarner — EV drivetrain components
        ],
    },
    # ── Industrials  (target: 50, bump Capital Goods) ───────────────────────
    "Industrials": {
        "Capital Goods": [
            # Top 30 by market cap (bumped from 20)
            "GE",  "HON", "MMM", "RTX", "LMT", "NOC", "GD",  "BA",
            "CAT", "DE",  "ETN", "EMR", "ROK", "PH",  "ITW",
            "DOV", "FTV", "GNRC","CARR","OTIS",
            "HII", "TDG", "AXON","HEI", "TXT",
            "KTOS","AVAV","RKLB","LUNR","RDW",
            # Niche defense / space upstarts
            "ASTS",   # AST SpaceMobile — satellite broadband
            "SPCE",   # Virgin Galactic — space tourism proxy
            # European defense (Yahoo Finance ADR/OTC or direct)
            "RHM.DE",   # Rheinmetall — European defense bellwether (corrected Yahoo suffix)
            "BA.L",     # BAE Systems
            "AIR.PA",   # Airbus
        ],
        "Transportation": [
            # Top 20 by market cap (bumped from 15)
            "UNP", "CSX", "NSC", "CP",  "CNI", "UPS", "FDX", "XPO",
            "ODFL","SAIA","JBHT","CHRW","EXPD","GXO", "DHLGY",
            "DAL", "UAL", "AAL", "LUV", "ALK",
            # Shipping / freight cycle indicators
            "ZIM",    # ZIM Integrated Shipping — spot rate proxy
            "MATX",   # Matson — transpacific trade health
            "SBLK",   # Star Bulk — dry bulk commodities
            "STNG",   # Golden Ocean — iron ore / coal shipping
        ],
        "Commercial & Professional Services": [
            # Top 20 by market cap (bumped from 10)
            "CTAS","RSG", "WM",  "VRRM","ACN", "EPAM","GLOB","EXLS",
            "TASK","WEX", "BR",  "VRSK","MCO", "TRI",
            "IHS", "SFCO","KD",  "DXC",
        ],
    },
    # ── Communication Services  (target: 50, bump both groups) ─────────────
    "Communication Services": {
        "Media & Entertainment": [
            # Top 30 by market cap (bumped from 20)
            "GOOGL","META","NFLX","DIS", "CMCSA","WBD","FOX",
            "FOXA","NYT", "SPOT","SIRI","IHRT", "FWONA",
            "RBLX","U",   "EA",  "TTWO",            "LYV", "MSGE", "MSGS","IMAX","AMC",
            # Upstarts / niche
            "SNAP",   # Snapchat — gen-Z attention proxy
            "PINS",   # Pinterest — social commerce signal
            "RDDT",   # Reddit — community media upstart
            "MTCH",   # Match Group — digital relationship economy
            "DUOL",   # Duolingo — EdTech / digital content adjacent
        ],
        "Telecommunication Services": [
            # Top 20 by market cap (bumped from 10)
            "VZ",  "T",   "TMUS","LUMN","CABO","SHEN",            "TDS", "OOMA","ORANY","TEF.MC", "DTEGY","BCE","TU",
            "ERIC",   # Ericsson ADR — acquired Vonage, global telecom infrastructure
        ],
    },
    # ── Consumer Staples  (target: 50, bump all groups) ─────────────────────
    "Consumer Staples": {
        "Food, Beverage & Tobacco": [
            # Top 30 by market cap (bumped from 20)
            "PEP", "KO",  "PM",  "MO",  "MDLZ","GIS", "CAG",
            "CPB", "SJM", "HRL", "MKC", "INGR","STKL","CALM",
            "TAP", "SAM", "BUD", "STZ", "MNST",
            "CELH","KDP",  "FIZZ","REED","COKE",
            # Niche / emerging consumer brands
            "HAIN",   # Hain Celestial — organic/natural foods
            "SMPL",   # Simply Good Foods — low-carb / keto trend
            "NOMD",   # Nomad Foods — European frozen foods
            "DNUT",   # Krispy Kreme — consumer indulgence proxy
            "BROS",   # Dutch Bros — already in services; cross-tag
        ],
        "Food & Staples Retailing": [
            # Top 20 by market cap (bumped from 10)
            "WMT", "COST","KR",  "SYY", "USFD","PFGC","USFD","CHEF",
            "ACI", "CASY","WINN","ANDE","CVGW","UNFI","GO",
            "PSMT","INGR","ANDE","MFG", "SFM",
        ],
        "Household & Personal Products": [
            # Top 20 by market cap (bumped from 10)
            "PG",  "CL",  "EL",  "KMB", "CHD", "ENR", "SPB", "CLX",
            "COTY","RCUS","HNST","CURV","NUS", "USPH",
            "SKIN","ATER","PRPL",
            # Upstarts
            "HNST",   # Honest Company — already in watchlist, clean label
            "ELF",    # ELF Beauty — indie beauty growth story
            "SKIN",   # BeautyHealth — Hydrafacial, med-aesthetics trend
        ],
    },
    # ── Energy  (target: 50, large bump) ────────────────────────────────────
    "Energy": {
        "Energy": [
            # Top 20 by market cap (oil & gas majors + midstream)
            "XOM", "CVX", "COP", "EOG", "SLB", "OXY", "DVN",
            "MPC", "PSX", "VLO", "FANG","CTRA","APA",
            "HAL", "BKR", "NOV", "PTEN","WHD",
            # Midstream / pipeline infrastructure
            "ET",  "EPD", "MPLX", "WMB", "KMI", "TRGP","OKE", "PAA",
            # Clean energy / energy transition
            "ENPH","SEDG","RUN", "FSLR","ARRY","NEE", "BEP", "CWEN",
            # Nuclear
            "CEG",    # Constellation Energy — largest US nuclear operator
            "VST",    # Vistra — nuclear + power gen
            "CCJ",    # Cameco — already in watchlist, uranium miner
            "SMR",    # NuScale Power — small modular reactor upstart
            "OKLO",   # Oklo — advanced fission upstart
            # Energy storage / hydrogen
            "PLUG",   # Plug Power — hydrogen fuel cells
            "BLDP",   # Ballard Power Systems — fuel cells
            "BE",     # Bloom Energy — solid oxide fuel cells
        ],
    },
    # ── Real Estate  (target: 50, large bump + REIT sub-tagging) ────────────
    "Real Estate": {
        "Real Estate (REITs)": [
            # Data center REITs — behave like tech
            "EQIX","DLR", "AMT", "CCI", "SBAC","IRM",
            # Industrial / logistics REITs
            "PLD", "STAG","EGP", "REXR","FR",
            # Residential REITs
            "AVB", "EQR", "MAA", "UDR", "CPT", "NHI", "NNN",
            # Retail REITs
            "SPG", "O",   "VICI","GLPI","WPC", "EPRT","IVT",   # RPAI → InvenTrust Properties
            # Healthcare REITs
            "WELL","VTR", "OHI", "SBRA","HR",
            # Office REITs (stress indicator)
            "BXP", "SLG", "HIW", "PDM",             # Mortgage REITs (rate sensitivity proxy)
            "AGNC","NLY", "TWO", "RITM","RWT",
        ],
        "Real Estate Management & Development": [
            # Top 15 by market cap
            "CBRE","JLL", "CWK", "MMI", "NMRK","OPEN","Z",   "RKT",  "EXPI","COMP","RC",  "FOR", "AIV", "IRT", "NXRT",
        ],
    },
    # ── Materials  (target: 50, large bump) ─────────────────────────────────
    "Materials": {
        "Materials": [
            # Diversified miners / metals
            "BHP", "RIO", "VALE","FCX", "AA",  "NUE", "STLD",
            "CMC", "CLF", "ATI", "MP",  "CTRA","KALU","KALU",
            # Gold & precious metals miners
            "NEM", "AEM", "GOLD","KGC", "AGI",  "WPM", "PAAS","CDE",
            # Specialty chemicals
            "LIN", "APD", "ECL", "SHW", "PPG", "RPM", "EMN", "CE",
            "DD",  "DOW", "LYB", "HUN", "OLN", "CC",  "TROX",
            # Agriculture inputs (fertilizers)
            "MOS", "NTR", "CF",  "ICL", "NTR",
            # Rare earths / critical minerals (strategic)
            "MP",     # MP Materials — only US rare earth mine
            "UUUU",   # Energy Fuels — rare earth + uranium
            "ALTX",   # Altus Minerals
        ],
    },
    # ── Utilities  (target: 50, large bump) ─────────────────────────────────
    "Utilities": {
        "Utilities": [
            # Electric utilities
            "NEE", "DUK", "SO",  "D",   "AEP", "EXC", "SRE", "PCG",
            "ED",  "ETR", "PPL", "XEL", "WEC", "CMS", "AES",
            "NI",  "LNT", "EVRG","PNW", "AVA",
            # Gas utilities
            "SR",  "NFG", "OGS", "NWN",
            # Water utilities
            "AWK", "WTRG", "HTO",  "YORW","MSEX",  # HTO = H2O America (formerly SJW renamed)
            # Renewable / clean utilities
            "AES", "BEP", "CWEN","BEPC",  # TERP acquired by Brookfield → BEPC
            # Transmission / grid infrastructure
            "AEE", "FE",  "EIX", "IDA", "OTTR",
            # International utility ADRs (rate/inflation proxy)
            "ENIC", "ENIC","ENIC","PAM",
        ],
    },
}

# ---------------------------------------------------------------------------
# MACRO SIGNALS
# ---------------------------------------------------------------------------

MACRO_SIGNALS = {
    "volatility": [
        "^VIX",      # CBOE Equity Volatility Index
        "^MOVE",     # ICE BofA Bond Volatility Index (via Yahoo as ^MOVE or proxy)
        "^VXN",      # Nasdaq-100 Volatility
        "VIXY",      # Russell 2000 Volatility
    ],
    "rates_and_yields": [
        "^IRX",      # 13-week T-bill yield
        "^FVX",      # 5-year treasury yield
        "^TNX",      # 10-year treasury yield
        "^TYX",      # 30-year treasury yield
        "TLT",       # iShares 20+ Year Treasury Bond ETF (liquid rate proxy)
        "HYG",       # iShares iBoxx High Yield Corporate Bond ETF (credit spread)
        "LQD",       # iShares Investment Grade Corporate Bond ETF
        "TIP",       # iShares TIPS ETF (inflation expectations)
    ],
    "currencies": [
        "DX-Y.NYB",  # US Dollar Index
        "EURUSD=X",  # EUR/USD
        "JPY=X",     # USD/JPY
        "GBPUSD=X",  # GBP/USD
        "CNY=X",     # USD/CNY (China FX policy signal)
        "AUDUSD=X",  # AUD/USD (commodity currency proxy)
    ],
    "commodities": [
        "CL=F",      # WTI Crude Oil Futures
        "BZ=F",      # Brent Crude Futures
        "NG=F",      # Natural Gas Futures
        "GC=F",      # Gold Futures
        "SI=F",      # Silver Futures
        "HG=F",      # Copper Futures (global growth bellwether)
        "ZW=F",      # Wheat Futures (food inflation)
        "ZC=F",      # Corn Futures
        "ZS=F",      # Soybean Futures
    ],
    "crypto": [
        "BTC-USD",   # Bitcoin (risk appetite proxy)
        "ETH-USD",   # Ethereum (DeFi/on-chain activity)
    ],
    "broad_indices": [
        "^GSPC",     # S&P 500
        "^NDX",      # Nasdaq-100
        "^DJI",      # Dow Jones Industrial Average
        "^RUT",      # Russell 2000 (small cap health)
        "^FTSE",     # FTSE 100 (UK)
        "^GDAXI",    # DAX (Germany)
        "^N225",     # Nikkei 225 (Japan)
        "^HSI",      # Hang Seng (Hong Kong/China proxy)
        "^STOXX50E", # Euro Stoxx 50
    ],
}

# ---------------------------------------------------------------------------
# COUNTRY / REGIONAL ETFs
# ---------------------------------------------------------------------------

COUNTRY_ETFS = {
    "developed_markets": [
        "EWJ",   # Japan
        "EWG",   # Germany
        "EWU",   # United Kingdom
        "EWQ",   # France
        "EWI",   # Italy
        "EWP",   # Spain
        "EWL",   # Switzerland
        "EWC",   # Canada
        "EWA",   # Australia
        "EWS",   # Singapore
    ],
    "emerging_markets": [
        "EWZ",   # Brazil
        "EWY",   # South Korea
        "EWT",   # Taiwan
        "INDA",  # India
        "FXI",   # China large cap
        "KWEB",  # China internet (tech subset of FXI)
        "EWW",   # Mexico
        "EZA",   # South Africa
        "EWH",   # Hong Kong
        "THD",   # Thailand
    ],
    "regional_blocs": [
        "VEA",   # Developed markets ex-US (broad)
        "VWO",   # Emerging markets (broad)
        "EEM",   # iShares Emerging Markets (alternative to VWO)
        "EFA",   # iShares EAFE (Europe, Australasia, Far East)
        "IEMG",  # iShares Core EM
    ],
}

# ---------------------------------------------------------------------------
# PERSONAL WATCHLIST
# ---------------------------------------------------------------------------

WATCHLIST = [
    # Original watchlist
    "SPOT",    # Spotify — audio streaming economy
    "VRT",     # Vertiv — data center power infrastructure
    "GLW",     # Corning — fiber/optical infrastructure
    "CCJ",     # Cameco — uranium, nuclear energy cycle
    "BABA",    # Alibaba — China consumer + tech proxy
    "INTU",    # Intuit — SMB financial health proxy
    "HNST",    # Honest Company — clean label consumer
    "GLD",     # SPDR Gold ETF
    "SLV",     # iShares Silver ETF
    "FCX",     # Freeport-McMoRan — copper, leading macro indicator
    "ASML",    # ASML — semiconductor equipment monopoly
    "NVO",     # Novo Nordisk — GLP-1/obesity drug cycle
    "TSM",     # TSMC — global semiconductor capacity proxy
    "FIG",     # Figma / alt-asset management placeholder
    "WTTR",    # Select Water Solutions — oilfield water services
    "IIIN",    # Insteel Industries — steel wire products, construction
    "EVTC",    # EVERTEC — LatAm payment processing
    "WLDN",    # Willdan Group — energy efficiency services
 
    # Additions agreed in review
    "CRWD",    # CrowdStrike — cybersecurity bellwether
    "PANW",    # Palo Alto Networks — enterprise security spend
    "ZS",      # Zscaler — cloud-native security
    "CEG",     # Constellation Energy — nuclear power
    "VST",     # Vistra — power generation + nuclear
    "SMR",     # NuScale — small modular reactor
    "VALE",    # Vale — iron ore, Brazil macro
    "LLY",     # Eli Lilly — GLP-1 cycle anchor
    "INFY",    # Infosys — India IT services
    "ZIM",     # ZIM Shipping — global trade / spot freight rates
    "ELF",     # ELF Beauty — indie beauty growth
]

def _flatten() -> list[str]:
    """
    Build the full deduplicated universe. Called once at module import.
 
    Deduplication is intentional — tickers appear in multiple source lists
    (e.g. FCX is in SP500, GICS Materials, and WATCHLIST) but should only
    be fetched once per pipeline run.  Using a set here is the guarantee.
    """
    seen: set[str] = set()
    tickers: set[str] = set()
 
    for t in SP500:
        seen.add(t.upper())
    for sector in GICS_SECTORS.values():
        for ig_tickers in sector.values():
            for t in ig_tickers:
                seen.add(t.upper())
    for cat_tickers in MACRO_SIGNALS.values():
        for t in cat_tickers:
            seen.add(t.upper())
    for region_tickers in COUNTRY_ETFS.values():
        for t in region_tickers:
            seen.add(t.upper())
    for t in WATCHLIST:
        seen.add(t.upper())
 
    tickers = seen
    return sorted(tickers)
 
 
ALL_TICKERS: list[str] = _flatten()
 
# Sanity check at import time — raises immediately if deduplication breaks.
assert len(ALL_TICKERS) == len(set(ALL_TICKERS)), (
    f"ALL_TICKERS contains duplicates — this is a bug in _flatten(). "
    f"Expected {len(set(ALL_TICKERS))} unique, got {len(ALL_TICKERS)} total."
)

def get_batches(batch_size: int = 100) -> list[list[str]]:
    """
    Split ALL_TICKERS into chunks of `batch_size` for pipeline ingestion.
 
    Returns a list of lists, each containing at most `batch_size` tickers.
    The final batch may be smaller. Tickers are uppercase and sorted.
    """
    if batch_size < 1:
        raise ValueError(f"batch_size must be >= 1, got {batch_size}")
    return [ALL_TICKERS[i : i + batch_size] for i in range(0, len(ALL_TICKERS), batch_size)]
 

def get_category(ticker: str) -> dict:
    """
    Return all category buckets a ticker belongs to across the universe.
 
    Returns a dict:
        {
            "ticker": "NVDA",
            "buckets": [
                {"type": "sp500"},
                {"type": "gics", "sector": "Information Technology", "industry_group": "Semiconductors & Equipment"},
                {"type": "watchlist"},
            ]
        }
 
    A ticker may appear in multiple buckets (e.g. FCX is in Materials GICS,
    Energy watchlist, and S&P 500 simultaneously).  This is intentional —
    cross-sector membership is analytically meaningful.
    """
    t = ticker.upper()
    result: dict = {"ticker": t, "buckets": []}
 
    if t in (s.upper() for s in SP500):
        result["buckets"].append({"type": "sp500"})
 
    for sector, igs in GICS_SECTORS.items():
        for ig, tickers in igs.items():
            if t in (x.upper() for x in tickers):
                result["buckets"].append({
                    "type": "gics",
                    "sector": sector,
                    "industry_group": ig,
                })
 
    for cat, tickers in MACRO_SIGNALS.items():
        if t in (x.upper() for x in tickers):
            result["buckets"].append({"type": "macro_signal", "category": cat})
 
    for region, tickers in COUNTRY_ETFS.items():
        if t in (x.upper() for x in tickers):
            result["buckets"].append({"type": "country_etf", "region": region})
 
    if t in (x.upper() for x in WATCHLIST):
        result["buckets"].append({"type": "watchlist"})
 
    return result

def universe_summary() -> dict:
    """
    Return a structured summary of the universe — useful for DAG logging,
    metadata tables, or a dbt seed audit row.
 
    Example output:
        {
            "total_tickers": 852,
            "sp500": 503,
            "gics": {"Information Technology": 96, ...},
            "macro_signals": {"volatility": 4, "rates_and_yields": 8, ...},
            "country_etfs": {"developed_markets": 10, ...},
            "watchlist": 29,
        }
    """
    return {
        "total_tickers": len(ALL_TICKERS),
        "sp500": len(set(t.upper() for t in SP500)),
        "gics": {
            sector: sum(len(v) for v in igs.values())
            for sector, igs in GICS_SECTORS.items()
        },
        "macro_signals": {
            cat: len(tickers) for cat, tickers in MACRO_SIGNALS.items()
        },
        "country_etfs": {
            region: len(tickers) for region, tickers in COUNTRY_ETFS.items()
        },
        "watchlist": len(WATCHLIST),
    }

if __name__ == "__main__":
    import argparse
    import json
 
    parser = argparse.ArgumentParser(description="Ticker universe utility")
    parser.add_argument("--batches",  type=int, metavar="N",
                        help="Print batches of size N (default 100)")
    parser.add_argument("--lookup",   type=str, metavar="TICKER",
                        help="Look up category membership for a ticker")
    parser.add_argument("--summary",  action="store_true",
                        help="Print universe summary as JSON")
    parser.add_argument("--overlap",  action="store_true",
                        help="Show tickers that appear in multiple source lists")
    args = parser.parse_args()
 
    if args.lookup:
        print(json.dumps(get_category(args.lookup), indent=2))
 
    elif args.batches is not None:
        batches = get_batches(args.batches)
        print(f"# {len(batches)} batches of up to {args.batches} tickers")
        print(f"batches = {json.dumps(batches, indent=4)}")
 
    else:
        # Default: human-readable summary
        summary = universe_summary()
        print(f"Total unique tickers : {summary['total_tickers']}")
        print(f"S&P 500 constituents : {summary['sp500']}")
        print("\nGICS breakdown:")
        for sector, count in summary["gics"].items():
            print(f"  {sector:<45} {count:>4}")
        print("\nMacro signals:")
        for cat, count in summary["macro_signals"].items():
            print(f"  {cat:<30} {count:>4}")
        print("\nCountry ETFs:")
        for region, count in summary["country_etfs"].items():
            print(f"  {region:<30} {count:>4}")
        print(f"\nWatchlist            : {summary['watchlist']}")
        print("  (all deduplicated in ALL_TICKERS — each fetched exactly once)")
        print(f"\nBatch preview (size=100): {len(get_batches(100))} batches")
