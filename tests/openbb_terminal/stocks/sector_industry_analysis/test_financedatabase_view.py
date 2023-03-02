# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.sector_industry_analysis import financedatabase_view

# pylint: disable=C0302

GET_STOCKS_DATA_DICT = {
    "CGEO.L": {
        "defaultKeyStatistics": {
            "annualHoldingsTurnover": None,
            "enterpriseToRevenue": None,
            "beta3Year": None,
            "profitMargins": 2.8082001,
            "enterpriseToEbitda": None,
            "52WeekChange": 0.22935784,
            "morningStarRiskRating": None,
            "forwardEps": 2.61,
            "revenueQuarterlyGrowth": None,
            "sharesOutstanding": 46895200,
            "fundInceptionDate": None,
            "annualReportExpenseRatio": None,
            "totalAssets": None,
            "bookValue": None,
            "sharesShort": None,
            "sharesPercentSharesOut": None,
            "fundFamily": None,
            "lastFiscalYearEnd": 1609372800,
            "heldPercentInstitutions": 0.72378,
            "netIncomeToCommon": None,
            "trailingEps": None,
            "lastDividendValue": None,
            "SandP52WeekChange": 0.18828869,
            "priceToBook": None,
            "heldPercentInsiders": 0.23013,
            "nextFiscalYearEnd": 1672444800,
            "yield": None,
            "mostRecentQuarter": 1632960000,
            "shortRatio": None,
            "sharesShortPreviousMonthDate": None,
            "floatShares": 37399430,
            "beta": 1.400947,
            "enterpriseValue": 295083648,
            "priceHint": 2,
            "threeYearAverageReturn": None,
            "lastSplitDate": None,
            "lastSplitFactor": None,
            "legalType": None,
            "lastDividendDate": None,
            "morningStarOverallRating": None,
            "earningsQuarterlyGrowth": -0.423,
            "priceToSalesTrailing12Months": None,
            "dateShortInterest": None,
            "pegRatio": None,
            "ytdReturn": None,
            "forwardPE": None,
            "maxAge": 1,
            "lastCapGain": None,
            "shortPercentOfFloat": None,
            "sharesShortPriorMonth": None,
            "impliedSharesOutstanding": None,
            "category": None,
            "fiveYearAverageReturn": None,
        },
        "details": None,
        "summaryProfile": {
            "zip": "0179",
            "sector": "Industrials",
            "fullTimeEmployees": 20314,
            "longBusinessSummary": "Georgia Capital PLC is a private...",
            "city": "Tbilisi",
            "phone": "995 322 000 000",
            "country": "Georgia",
            "companyOfficers": [],
            "website": "https://www.georgiacapital.ge",
            "maxAge": 86400,
            "address1": "3-5 Tatishvili street",
            "fax": "995 322 000 900",
            "industry": "Conglomerates",
        },
        "recommendationTrend": {
            "trend": [
                {
                    "period": "0m",
                    "strongBuy": 0,
                    "buy": 0,
                    "hold": 0,
                    "sell": 0,
                    "strongSell": 0,
                },
                {
                    "period": "-1m",
                    "strongBuy": 0,
                    "buy": 0,
                    "hold": 0,
                    "sell": 0,
                    "strongSell": 0,
                },
                {
                    "period": "-2m",
                    "strongBuy": 0,
                    "buy": 0,
                    "hold": 0,
                    "sell": 0,
                    "strongSell": 0,
                },
                {
                    "period": "-3m",
                    "strongBuy": 0,
                    "buy": 0,
                    "hold": 0,
                    "sell": 0,
                    "strongSell": 0,
                },
            ],
            "maxAge": 86400,
        },
        "financialsTemplate": {"code": "N", "maxAge": 1},
        "earnings": {
            "maxAge": 86400,
            "earningsChart": {"quarterly": [], "earningsDate": [1637028000]},
            "financialsChart": {
                "yearly": [
                    {"date": 2017, "revenue": 1127170000, "earnings": 70125000},
                    {"date": 2018, "revenue": 1282995000, "earnings": -254000},
                    {"date": 2019, "revenue": 1473437000, "earnings": 569262000},
                    {"date": 2020, "revenue": 339174000, "earnings": 330334000},
                ],
                "quarterly": [
                    {"date": "3Q2020", "revenue": 15281000, "earnings": 398032000},
                    {"date": "1Q2021", "revenue": 164790500, "earnings": 162586000},
                    {"date": "2Q2021", "revenue": 164790500, "earnings": 162586000},
                    {"date": "3Q2021", "revenue": 35720000, "earnings": 229852000},
                ],
            },
            "financialCurrency": "GEL",
        },
        "price": {
            "quoteSourceName": "Delayed Quote",
            "regularMarketOpen": 670,
            "averageDailyVolume3Month": 96855,
            "exchange": "LSE",
            "regularMarketTime": 1642612500,
            "volume24Hr": None,
            "regularMarketDayHigh": 679.54,
            "shortName": "GEORGIA CAPITAL PLC ORD 1P",
            "averageDailyVolume10Day": 171201,
            "longName": "Georgia Capital PLC",
            "regularMarketChange": 2,
            "currencySymbol": "£",
            "regularMarketPreviousClose": 670,
            "preMarketPrice": None,
            "exchangeDataDelayedBy": 20,
            "toCurrency": None,
            "postMarketChange": None,
            "postMarketPrice": None,
            "exchangeName": "LSE",
            "preMarketChange": None,
            "circulatingSupply": None,
            "regularMarketDayLow": 670,
            "priceHint": 2,
            "currency": "GBp",
            "regularMarketPrice": 672,
            "regularMarketVolume": 821749,
            "lastMarket": None,
            "regularMarketSource": "DELAYED",
            "openInterest": None,
            "marketState": "POSTPOST",
            "underlyingSymbol": None,
            "marketCap": 315135744,
            "quoteType": "EQUITY",
            "volumeAllCurrencies": None,
            "strikePrice": None,
            "symbol": "CGEO.L",
            "maxAge": 1,
            "fromCurrency": None,
            "regularMarketChangePercent": 0.0029850744,
        },
        "financialData": {
            "ebitdaMargins": 0,
            "profitMargins": 2.8082001,
            "grossMargins": 0.98942,
            "operatingCashflow": None,
            "revenueGrowth": 1.338,
            "operatingMargins": 0,
            "ebitda": None,
            "targetLowPrice": 42.09,
            "recommendationKey": "strong_buy",
            "grossProfits": 339174000,
            "freeCashflow": None,
            "targetMedianPrice": 44.02,
            "currentPrice": 672,
            "earningsGrowth": None,
            "currentRatio": None,
            "returnOnAssets": None,
            "numberOfAnalystOpinions": 3,
            "targetMeanPrice": 50.32,
            "debtToEquity": None,
            "returnOnEquity": None,
            "targetHighPrice": 64.86,
            "totalCash": None,
            "totalDebt": None,
            "totalRevenue": None,
            "totalCashPerShare": None,
            "financialCurrency": "GEL",
            "maxAge": 86400,
            "revenuePerShare": None,
            "quickRatio": None,
            "recommendationMean": 1.5,
        },
        "quoteType": {
            "exchange": "LSE",
            "shortName": "GEORGIA CAPITAL PLC ORD 1P",
            "longName": "Georgia Capital PLC",
            "exchangeTimezoneName": "Europe/London",
            "exchangeTimezoneShortName": "GMT",
            "isEsgPopulated": False,
            "gmtOffSetMilliseconds": "0",
            "quoteType": "EQUITY",
            "symbol": "CGEO.L",
            "messageBoardId": "finmb_329267401",
            "market": "gb_market",
        },
        "calendarEvents": {
            "maxAge": 1,
            "earnings": {
                "earningsDate": [1637028000],
                "earningsAverage": None,
                "earningsLow": None,
                "earningsHigh": None,
                "revenueAverage": 385000000,
                "revenueLow": 384000000,
                "revenueHigh": 386000000,
            },
            "exDividendDate": None,
            "dividendDate": None,
        },
        "summaryDetail": {
            "previousClose": 670,
            "regularMarketOpen": 670,
            "twoHundredDayAverage": 631.14,
            "trailingAnnualDividendYield": None,
            "payoutRatio": 0,
            "volume24Hr": None,
            "regularMarketDayHigh": 679.54,
            "navPrice": None,
            "averageDailyVolume10Day": 171201,
            "totalAssets": None,
            "regularMarketPreviousClose": 670,
            "fiftyDayAverage": 656.22,
            "trailingAnnualDividendRate": None,
            "open": 670,
            "toCurrency": None,
            "averageVolume10days": 171201,
            "expireDate": None,
            "yield": None,
            "algorithm": None,
            "dividendRate": None,
            "exDividendDate": None,
            "beta": 1.400947,
            "circulatingSupply": None,
            "startDate": None,
            "regularMarketDayLow": 670,
            "priceHint": 2,
            "currency": "GBp",
            "regularMarketVolume": 821749,
            "lastMarket": None,
            "maxSupply": None,
            "openInterest": None,
            "marketCap": 315135744,
            "volumeAllCurrencies": None,
            "strikePrice": None,
            "averageVolume": 96855,
            "priceToSalesTrailing12Months": None,
            "dayLow": 670,
            "ask": 673,
            "ytdReturn": None,
            "askSize": 0,
            "volume": 821749,
            "fiftyTwoWeekHigh": 762,
            "forwardPE": 2.5747128,
            "maxAge": 1,
            "fromCurrency": None,
            "fiveYearAvgDividendYield": None,
            "fiftyTwoWeekLow": 469.5,
            "bid": 672,
            "tradeable": False,
            "dividendYield": None,
            "bidSize": 0,
            "dayHigh": 679.54,
        },
        "symbol": "CGEO.L",
        "esgScores": None,
        "upgradeDowngradeHistory": None,
        "pageViews": None,
    },
    "GRGCF": {
        "defaultKeyStatistics": {
            "annualHoldingsTurnover": None,
            "enterpriseToRevenue": None,
            "beta3Year": None,
            "profitMargins": 2.8082001,
            "enterpriseToEbitda": None,
            "52WeekChange": 0.2445035,
            "morningStarRiskRating": None,
            "forwardEps": None,
            "revenueQuarterlyGrowth": None,
            "sharesOutstanding": 46895200,
            "fundInceptionDate": None,
            "annualReportExpenseRatio": None,
            "totalAssets": None,
            "bookValue": None,
            "sharesShort": None,
            "sharesPercentSharesOut": None,
            "fundFamily": None,
            "lastFiscalYearEnd": 1609372800,
            "heldPercentInstitutions": 0.72378,
            "netIncomeToCommon": None,
            "trailingEps": None,
            "lastDividendValue": None,
            "SandP52WeekChange": 0.18828869,
            "priceToBook": None,
            "heldPercentInsiders": 0.23013,
            "nextFiscalYearEnd": 1672444800,
            "yield": None,
            "mostRecentQuarter": 1632960000,
            "shortRatio": None,
            "sharesShortPreviousMonthDate": None,
            "floatShares": 37399430,
            "beta": 1.400947,
            "enterpriseValue": 396381024,
            "priceHint": 2,
            "threeYearAverageReturn": None,
            "lastSplitDate": None,
            "lastSplitFactor": None,
            "legalType": None,
            "lastDividendDate": None,
            "morningStarOverallRating": None,
            "earningsQuarterlyGrowth": -0.423,
            "priceToSalesTrailing12Months": None,
            "dateShortInterest": None,
            "pegRatio": None,
            "ytdReturn": None,
            "forwardPE": None,
            "maxAge": 1,
            "lastCapGain": None,
            "shortPercentOfFloat": None,
            "sharesShortPriorMonth": None,
            "impliedSharesOutstanding": None,
            "category": None,
            "fiveYearAverageReturn": None,
        },
        "details": None,
        "summaryProfile": {
            "zip": "0179",
            "sector": "Industrials",
            "fullTimeEmployees": 20314,
            "longBusinessSummary": "Georgia Capital PLC is a...",
            "city": "Tbilisi",
            "phone": "995 322 000 000",
            "country": "Georgia",
            "companyOfficers": [],
            "website": "https://www.georgiacapital.ge",
            "maxAge": 86400,
            "address1": "3-5 Tatishvili street",
            "fax": "995 322 000 900",
            "industry": "Conglomerates",
        },
        "recommendationTrend": None,
        "financialsTemplate": {"code": "N", "maxAge": 1},
        "earnings": None,
        "price": {
            "quoteSourceName": "Delayed Quote",
            "regularMarketOpen": 9,
            "averageDailyVolume3Month": 42,
            "exchange": "PNK",
            "regularMarketTime": 1641915989,
            "volume24Hr": None,
            "regularMarketDayHigh": 9,
            "shortName": "GEORGIA CAPITAL PLC",
            "averageDailyVolume10Day": 275,
            "longName": "Georgia Capital PLC",
            "regularMarketChange": 0,
            "currencySymbol": "$",
            "regularMarketPreviousClose": 9,
            "preMarketPrice": None,
            "exchangeDataDelayedBy": 0,
            "toCurrency": None,
            "postMarketChange": None,
            "postMarketPrice": None,
            "exchangeName": "Other OTC",
            "preMarketChange": None,
            "circulatingSupply": None,
            "regularMarketDayLow": 9,
            "priceHint": 2,
            "currency": "USD",
            "regularMarketPrice": 9,
            "regularMarketVolume": 2750,
            "lastMarket": None,
            "regularMarketSource": "DELAYED",
            "openInterest": None,
            "marketState": "POST",
            "underlyingSymbol": None,
            "marketCap": 431985600,
            "quoteType": "EQUITY",
            "volumeAllCurrencies": None,
            "strikePrice": None,
            "symbol": "GRGCF",
            "maxAge": 1,
            "fromCurrency": None,
            "regularMarketChangePercent": 0,
        },
        "financialData": {
            "ebitdaMargins": 0,
            "profitMargins": 2.8082001,
            "grossMargins": 0.98942,
            "operatingCashflow": None,
            "revenueGrowth": 1.338,
            "operatingMargins": 0,
            "ebitda": None,
            "targetLowPrice": None,
            "recommendationKey": "none",
            "grossProfits": 339174000,
            "freeCashflow": None,
            "targetMedianPrice": None,
            "currentPrice": 9,
            "earningsGrowth": None,
            "currentRatio": None,
            "returnOnAssets": None,
            "numberOfAnalystOpinions": None,
            "targetMeanPrice": None,
            "debtToEquity": None,
            "returnOnEquity": None,
            "targetHighPrice": None,
            "totalCash": None,
            "totalDebt": None,
            "totalRevenue": None,
            "totalCashPerShare": None,
            "financialCurrency": "GEL",
            "maxAge": 86400,
            "revenuePerShare": None,
            "quickRatio": None,
            "recommendationMean": None,
        },
        "quoteType": {
            "exchange": "PNK",
            "shortName": "GEORGIA CAPITAL PLC",
            "longName": "Georgia Capital PLC",
            "exchangeTimezoneName": "America/New_York",
            "exchangeTimezoneShortName": "EST",
            "isEsgPopulated": False,
            "gmtOffSetMilliseconds": "-18000000",
            "quoteType": "EQUITY",
            "symbol": "GRGCF",
            "messageBoardId": "finmb_329267401",
            "market": "us_market",
        },
        "calendarEvents": {
            "maxAge": 1,
            "earnings": {
                "earningsDate": [],
                "earningsAverage": None,
                "earningsLow": None,
                "earningsHigh": None,
                "revenueAverage": None,
                "revenueLow": None,
                "revenueHigh": None,
            },
            "exDividendDate": None,
            "dividendDate": None,
        },
        "summaryDetail": {
            "previousClose": 9,
            "regularMarketOpen": 9,
            "twoHundredDayAverage": 8.699631,
            "trailingAnnualDividendYield": None,
            "payoutRatio": 0,
            "volume24Hr": None,
            "regularMarketDayHigh": 9,
            "navPrice": None,
            "averageDailyVolume10Day": 275,
            "totalAssets": None,
            "regularMarketPreviousClose": 9,
            "fiftyDayAverage": 8.928,
            "trailingAnnualDividendRate": None,
            "open": 9,
            "toCurrency": None,
            "averageVolume10days": 275,
            "expireDate": None,
            "yield": None,
            "algorithm": None,
            "dividendRate": None,
            "exDividendDate": None,
            "beta": 1.400947,
            "circulatingSupply": None,
            "startDate": None,
            "regularMarketDayLow": 9,
            "priceHint": 2,
            "currency": "USD",
            "regularMarketVolume": 2750,
            "lastMarket": None,
            "maxSupply": None,
            "openInterest": None,
            "marketCap": 431985600,
            "volumeAllCurrencies": None,
            "strikePrice": None,
            "averageVolume": 42,
            "priceToSalesTrailing12Months": None,
            "dayLow": 9,
            "ask": None,
            "ytdReturn": None,
            "askSize": None,
            "volume": 2750,
            "fiftyTwoWeekHigh": 9.42,
            "forwardPE": None,
            "maxAge": 1,
            "fromCurrency": None,
            "fiveYearAvgDividendYield": None,
            "fiftyTwoWeekLow": 7.2318,
            "bid": None,
            "tradeable": False,
            "dividendYield": None,
            "bidSize": None,
            "dayHigh": 9,
        },
        "symbol": "GRGCF",
        "esgScores": None,
        "upgradeDowngradeHistory": None,
        "pageViews": None,
    },
    "TBCG.L": {
        "defaultKeyStatistics": {
            "annualHoldingsTurnover": None,
            "enterpriseToRevenue": None,
            "beta3Year": None,
            "profitMargins": 0.52791,
            "enterpriseToEbitda": None,
            "52WeekChange": 0.15981734,
            "morningStarRiskRating": None,
            "forwardEps": 13.45,
            "revenueQuarterlyGrowth": None,
            "sharesOutstanding": 55155900,
            "fundInceptionDate": None,
            "annualReportExpenseRatio": None,
            "totalAssets": None,
            "bookValue": None,
            "sharesShort": None,
            "sharesPercentSharesOut": None,
            "fundFamily": None,
            "lastFiscalYearEnd": 1609372800,
            "heldPercentInstitutions": 0.46875,
            "netIncomeToCommon": None,
            "trailingEps": None,
            "lastDividendValue": 34.88,
            "SandP52WeekChange": 0.18828869,
            "priceToBook": None,
            "heldPercentInsiders": 0.23797001,
            "nextFiscalYearEnd": 1672444800,
            "yield": None,
            "mostRecentQuarter": 1632960000,
            "shortRatio": None,
            "sharesShortPreviousMonthDate": None,
            "floatShares": 46661516,
            "beta": 1.283937,
            "enterpriseValue": 828716352,
            "priceHint": 2,
            "threeYearAverageReturn": None,
            "lastSplitDate": None,
            "lastSplitFactor": None,
            "legalType": None,
            "lastDividendDate": 1629331200,
            "morningStarOverallRating": None,
            "earningsQuarterlyGrowth": 0.359,
            "priceToSalesTrailing12Months": None,
            "dateShortInterest": None,
            "pegRatio": 0.99,
            "ytdReturn": None,
            "forwardPE": 114.34944,
            "maxAge": 1,
            "lastCapGain": None,
            "shortPercentOfFloat": None,
            "sharesShortPriorMonth": None,
            "impliedSharesOutstanding": None,
            "category": None,
            "fiveYearAverageReturn": None,
        },
        "details": None,
        "summaryProfile": {
            "zip": "0102",
            "sector": "Financial Services",
            "fullTimeEmployees": 8281,
            "longBusinessSummary": "TBC Bank Group PLC, through its subsidiaries...",
            "city": "Tbilisi",
            "phone": "995 32 227 27 27",
            "country": "Georgia",
            "companyOfficers": [],
            "website": "https://www.tbcbankgroup.com",
            "maxAge": 86400,
            "address1": "7 Marjanishvili Street",
            "fax": "995 32 227 27 74",
            "industry": "Banks—Regional",
        },
        "recommendationTrend": {
            "trend": [
                {
                    "period": "0m",
                    "strongBuy": 0,
                    "buy": 0,
                    "hold": 0,
                    "sell": 0,
                    "strongSell": 0,
                },
                {
                    "period": "-1m",
                    "strongBuy": 5,
                    "buy": 2,
                    "hold": 1,
                    "sell": 0,
                    "strongSell": 0,
                },
                {
                    "period": "-2m",
                    "strongBuy": 5,
                    "buy": 2,
                    "hold": 2,
                    "sell": 0,
                    "strongSell": 0,
                },
                {
                    "period": "-3m",
                    "strongBuy": 5,
                    "buy": 2,
                    "hold": 2,
                    "sell": 0,
                    "strongSell": 0,
                },
            ],
            "maxAge": 86400,
        },
        "financialsTemplate": {"code": "B", "maxAge": 1},
        "earnings": {
            "maxAge": 86400,
            "earningsChart": {
                "quarterly": [{"date": "3Q2021", "actual": 3.71, "estimate": 3.46}],
                "currentQuarterEstimateDate": "4Q",
                "currentQuarterEstimateYear": 2021,
                "earningsDate": [1637233140],
            },
            "financialsChart": {
                "yearly": [
                    {"date": 2017, "revenue": 751745000, "earnings": 354410000},
                    {"date": 2018, "revenue": 925285000, "earnings": 435080000},
                    {"date": 2019, "revenue": 1038407000, "earnings": 537895000},
                    {"date": 2020, "revenue": 800506000, "earnings": 317752000},
                ],
                "quarterly": [
                    {"date": "4Q2020", "revenue": 240660000, "earnings": 99371000},
                    {"date": "1Q2021", "revenue": 293186000, "earnings": 151224000},
                    {"date": "2Q2021", "revenue": 424754000, "earnings": 247945000},
                    {"date": "3Q2021", "revenue": 373891000, "earnings": 204892000},
                ],
            },
            "financialCurrency": "GEL",
        },
        "price": {
            "quoteSourceName": "Delayed Quote",
            "regularMarketOpen": 1536.3,
            "averageDailyVolume3Month": 72253,
            "exchange": "LSE",
            "regularMarketTime": 1642610119,
            "volume24Hr": None,
            "regularMarketDayHigh": 1538,
            "shortName": "TBC BANK GROUP PLC ORD GBP0.01",
            "averageDailyVolume10Day": 31759,
            "longName": "TBC Bank Group PLC",
            "regularMarketChange": 14,
            "currencySymbol": "£",
            "regularMarketPreviousClose": 1524,
            "preMarketPrice": None,
            "exchangeDataDelayedBy": 20,
            "toCurrency": None,
            "postMarketChange": None,
            "postMarketPrice": None,
            "exchangeName": "LSE",
            "preMarketChange": None,
            "circulatingSupply": None,
            "regularMarketDayLow": 1514,
            "priceHint": 2,
            "currency": "GBp",
            "regularMarketPrice": 1538,
            "regularMarketVolume": 33761,
            "lastMarket": None,
            "regularMarketSource": "DELAYED",
            "openInterest": None,
            "marketState": "POSTPOST",
            "underlyingSymbol": None,
            "marketCap": 848297728,
            "quoteType": "EQUITY",
            "volumeAllCurrencies": None,
            "strikePrice": None,
            "symbol": "TBCG.L",
            "maxAge": 1,
            "fromCurrency": None,
            "regularMarketChangePercent": 0.009186352,
        },
        "financialData": {
            "ebitdaMargins": 0,
            "profitMargins": 0.52791,
            "grossMargins": 0,
            "operatingCashflow": None,
            "revenueGrowth": 0.346,
            "operatingMargins": 0,
            "ebitda": None,
            "targetLowPrice": 60.04,
            "recommendationKey": "strong_buy",
            "grossProfits": 800506000,
            "freeCashflow": None,
            "targetMedianPrice": 82.07,
            "currentPrice": 1538,
            "earningsGrowth": None,
            "currentRatio": None,
            "returnOnAssets": 0.03122,
            "numberOfAnalystOpinions": 8,
            "targetMeanPrice": 83.3,
            "debtToEquity": None,
            "returnOnEquity": 0.22670001,
            "targetHighPrice": 112.07,
            "totalCash": None,
            "totalDebt": None,
            "totalRevenue": None,
            "totalCashPerShare": None,
            "financialCurrency": "GEL",
            "maxAge": 86400,
            "revenuePerShare": None,
            "quickRatio": None,
            "recommendationMean": 1.3,
        },
        "quoteType": {
            "exchange": "LSE",
            "shortName": "TBC BANK GROUP PLC ORD GBP0.01",
            "longName": "TBC Bank Group PLC",
            "exchangeTimezoneName": "Europe/London",
            "exchangeTimezoneShortName": "GMT",
            "isEsgPopulated": False,
            "gmtOffSetMilliseconds": "0",
            "quoteType": "EQUITY",
            "symbol": "TBCG.L",
            "messageBoardId": "finmb_32390812",
            "market": "gb_market",
        },
        "calendarEvents": {
            "maxAge": 1,
            "earnings": {
                "earningsDate": [1637233140],
                "earningsAverage": None,
                "earningsLow": None,
                "earningsHigh": None,
                "revenueAverage": 324021000,
                "revenueLow": None,
                "revenueHigh": None,
            },
            "exDividendDate": 1629331200,
            "dividendDate": None,
        },
        "summaryDetail": {
            "previousClose": 1524,
            "regularMarketOpen": 1536.3,
            "twoHundredDayAverage": 1345.83,
            "trailingAnnualDividendYield": None,
            "payoutRatio": 0.1163,
            "volume24Hr": None,
            "regularMarketDayHigh": 1538,
            "navPrice": None,
            "averageDailyVolume10Day": 31759,
            "totalAssets": None,
            "regularMarketPreviousClose": 1524,
            "fiftyDayAverage": 1585.12,
            "trailingAnnualDividendRate": None,
            "open": 1536.3,
            "toCurrency": None,
            "averageVolume10days": 31759,
            "expireDate": None,
            "yield": None,
            "algorithm": None,
            "dividendRate": 0.35,
            "exDividendDate": 1629331200,
            "beta": 1.283937,
            "circulatingSupply": None,
            "startDate": None,
            "regularMarketDayLow": 1514,
            "priceHint": 2,
            "currency": "GBp",
            "regularMarketVolume": 33761,
            "lastMarket": None,
            "maxSupply": None,
            "openInterest": None,
            "marketCap": 848297728,
            "volumeAllCurrencies": None,
            "strikePrice": None,
            "averageVolume": 72253,
            "priceToSalesTrailing12Months": None,
            "dayLow": 1514,
            "ask": 1524,
            "ytdReturn": None,
            "askSize": 0,
            "volume": 33761,
            "fiftyTwoWeekHigh": 1686,
            "forwardPE": 1.1434944,
            "maxAge": 1,
            "fromCurrency": None,
            "fiveYearAvgDividendYield": None,
            "fiftyTwoWeekLow": 965,
            "bid": 1520,
            "tradeable": False,
            "dividendYield": 0.022,
            "bidSize": 0,
            "dayHigh": 1538,
        },
        "symbol": "TBCG.L",
        "esgScores": None,
        "upgradeDowngradeHistory": None,
        "pageViews": None,
    },
}


@pytest.mark.vcr(record_mode="none")
@pytest.mark.parametrize(
    "raw",
    [True, False],
)
def test_display_bars_financials(mocker, raw):
    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    # MOCK GET_STOCKS_DATA
    target = "openbb_terminal.stocks.sector_industry_analysis.financedatabase_model.get_stocks_data"
    mocker.patch(target=target, return_value=GET_STOCKS_DATA_DICT)

    financedatabase_view.display_bars_financials(
        finance_key="defaultKeyStatistics",
        finance_metric="profitMargins",
        country="Georgia",
        sector=None,
        industry=None,
        marketcap="",
        exclude_exchanges=False,
        limit=10,
        export="",
        raw=raw,
        already_loaded_stocks_data=None,
    )


@pytest.mark.vcr
def test_display_bars_financials_load_data(mocker):
    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    # MOCK GET_STOCKS_DATA
    target = "openbb_terminal.stocks.sector_industry_analysis.financedatabase_model.get_stocks_data"
    mocker.patch(target=target, return_value=GET_STOCKS_DATA_DICT)

    financedatabase_view.display_bars_financials(
        finance_key="defaultKeyStatistics",
        finance_metric="operatingCashflow",
        country="Georgia",
        sector="Industrials",
        industry="Conglomerates",
        marketcap="",
        exclude_exchanges=True,
        limit=10,
        export="",
        raw=False,
        already_loaded_stocks_data=GET_STOCKS_DATA_DICT,
    )


@pytest.mark.vcr
@pytest.mark.parametrize(
    "mktcap, raw",
    [
        ("", True),
        ("", False),
        ("Small Cap", False),
    ],
)
def test_display_companies_per_sector_in_country(mktcap, mocker, raw):
    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    financedatabase_view.display_companies_per_sector_in_country(
        country="Georgia",
        mktcap=mktcap,
        exclude_exchanges=False,
        export="",
        raw=raw,
        max_sectors_to_display=15,
        min_pct_to_display_sector=0.015,
    )


@pytest.mark.vcr
@pytest.mark.parametrize(
    "exclude_exchanges, raw",
    [
        (True, True),
        (False, True),
        (True, False),
    ],
)
def test_display_companies_per_industry_in_sector(exclude_exchanges, mocker, raw):
    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    financedatabase_view.display_companies_per_industry_in_sector(
        sector="Conglomerates",
        mktcap="Mid",
        exclude_exchanges=exclude_exchanges,
        export="",
        raw=raw,
        max_industries_to_display=15,
        min_pct_to_display_industry=0.015,
    )


@pytest.mark.default_cassette("test_display_companies_per_country_in_sector")
@pytest.mark.vcr
@pytest.mark.parametrize(
    "exclude_exchanges, raw",
    [
        (True, True),
        (False, True),
        (True, False),
    ],
)
def test_display_companies_per_country_in_sector(exclude_exchanges, mocker, raw):
    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    financedatabase_view.display_companies_per_country_in_sector(
        sector="Conglomerates",
        mktcap="Mid",
        exclude_exchanges=exclude_exchanges,
        export="",
        raw=raw,
        max_countries_to_display=15,
        min_pct_to_display_country=0.015,
    )


@pytest.mark.default_cassette("test_display_companies_per_country_in_industry")
@pytest.mark.vcr
@pytest.mark.parametrize(
    "exclude_exchanges, raw",
    [
        (True, True),
        (False, True),
        (False, False),
    ],
)
def test_display_companies_per_country_in_industry(exclude_exchanges, mocker, raw):
    # MOCK EXPORT_DATA
    mocker.patch(target="openbb_terminal.stocks.options.yfinance_view.export_data")

    financedatabase_view.display_companies_per_country_in_industry(
        industry="Uranium",
        mktcap="Mid",
        exclude_exchanges=exclude_exchanges,
        export="",
        raw=raw,
        max_countries_to_display=15,
        min_pct_to_display_country=0.015,
    )
