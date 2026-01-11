import yfinance as yfin

ticker = yfin.Ticker("ONGC.NS")
info = ticker.info

data = {
    "Open": info.get("open"),
    "High": info.get("dayHigh"),
    "Low": info.get("dayLow"),
    "Volume": info.get("volume"),
    "Avg. volume": info.get("averageVolume"),
    "Market cap": info.get("marketCap"),
    "P/E ratio": info.get("trailingPE"),
    "EPS": info.get("trailingEps"),
    "Dividend yield": info.get("dividendYield"),
    "52-wk high": info.get("fiftyTwoWeekHigh"),
    "52-wk low": info.get("fiftyTwoWeekLow"),
}

for k, v in data.items():
    print(f"{k:15} : {v}")
