import yfinance as yf
import json
import os
import pandas as pd
from strategies import run_strategy

def calculate_historical_signals(df_subset):
    """Calculates TA signals for a specific point in time."""
    current_price = df_subset['Close'].iloc[-1]
    ma20 = df_subset['Close'].rolling(window=20).mean().iloc[-1]
    ma50 = df_subset['Close'].rolling(window=50).mean().iloc[-1]
    
    # RSI Calculation for the subset
    delta = df_subset['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    high_52w = df_subset['High'].max()
    dist_from_52w = ((high_52w - current_price) / high_52w) * 100

    return {
        "current_price": round(current_price, 2),
        "ma20": round(ma20, 2),
        "ma50": round(ma50, 2),
        "rsi": round(rsi.iloc[-1], 2),
        "dist_from_52w_high": round(dist_from_52w, 2),
        "volume_change": 0 # Placeholder for backtest
    }

def run_historical_test():
    tickers = ["NVDA", "TSLA", "JNJ", "GME"]
    backtest_results = []

    for ticker in tickers:
        print(f"⏳ Backtesting {ticker} (Calculating signals for T-60 days)...")
        stock = yf.Ticker(ticker)
        full_hist = stock.history(period="2y") # Get extra data for 52-week high accuracy
        
        # 1. Create the 'Past' view (Data ending exactly 60 days ago)
        # We assume 252 trading days in a year; 60 days ago is ~42 trading days
        past_df = full_hist.iloc[:-42] 
        historical_data = calculate_historical_signals(past_df)
        
        # 2. Get the 'Future' outcome (What happened from then until today)
        price_then = historical_data['current_price']
        price_now = full_hist['Close'].iloc[-1]
        price_diff_pct = ((price_now - price_then) / price_then) * 100

        # 3. Run Strategies on 'Past' data
        strat_a = run_strategy("momentum_trader", historical_data)
        strat_b = run_strategy("value_contrarian", historical_data)

        # 4. Professional Scoring Logic
        def evaluate(decision, change):
            if decision == "BUY" and change > 3: return "✅ PROFIT"
            if decision == "SELL" and change < -3: return "✅ AVOIDED LOSS"
            if decision == "HOLD" and abs(change) < 3: return "✅ CORRECT NEUTRAL"
            return "❌ MISSED/WRONG"

        backtest_results.append({
            "ticker": ticker,
            "decision_date": str(past_df.index[-1].date()),
            "signals_at_time": historical_data,
            "momentum_move": strat_a['decision'],
            "value_move": strat_b['decision'],
            "price_then": price_then,
            "price_now": round(price_now, 2),
            "outcome_60d": f"{round(price_diff_pct, 2)}%",
            "momentum_score": evaluate(strat_a['decision'], price_diff_pct),
            "value_score": evaluate(strat_b['decision'], price_diff_pct)
        })

    with open("outputs/backtest.json", "w") as f:
        json.dump(backtest_results, f, indent=4)
    print("✅ Backtest complete! Check outputs/backtest.json for the 'Truth' scores.")

if __name__ == "__main__":
    run_historical_test()