import yfinance as yf
import pandas as pd

def get_market_data(ticker):
    """Fetches 90 days of data and calculates key indicators."""
    stock = yf.Ticker(ticker)
    df = stock.history(period="90d")
    
    if df.empty:
        return None

    # Calculate Indicators
    current_price = df['Close'].iloc[-1]
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    
    # Simple RSI calculation (Value Contrarian needs this)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    # 52-Week High Logic
    year_data = stock.history(period="1y")
    high_52w = year_data['High'].max()

    return {
        "ticker": ticker,
        "current_price": round(current_price, 2),
        "ma20": round(df['MA20'].iloc[-1], 2),
        "ma50": round(df['MA50'].iloc[-1], 2),
        "rsi": round(rsi.iloc[-1], 2),
        "dist_from_52w_high": round(((high_52w - current_price) / high_52w) * 100, 2),
        "volume_change": round(((df['Volume'].iloc[-1] - df['Volume'].mean()) / df['Volume'].mean()) * 100, 2)
    }