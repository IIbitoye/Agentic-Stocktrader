import json
import os
from datetime import datetime
from market_data import get_market_data
from strategies import run_strategy, run_debate  # 1. Update this import
from evaluator import run_evaluator
from summarize import generate_summary

def main():
    tickers = ["NVDA", "TSLA", "JNJ", "GME"]
    
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    for ticker in tickers:
        print(f"🚀 Processing {ticker}...")
        data = get_market_data(ticker)
        if not data: continue
        
        # 1. Parallel execution
        strat_a = run_strategy("momentum_trader", data)
        strat_b = run_strategy("value_contrarian", data)
        
        # 2. Evaluation Step
        evaluation = run_evaluator(strat_a, strat_b)

        # --- DEBATE LOGIC FITS HERE ---
        debate_results = None
        # Use .get() to avoid errors if 'agents_agree' is missing
        if not evaluation.get('agents_agree', True): 
            print(f"   - 🥊 Disagreement found! Starting Debate Mode...")
            # We pass the opposing justifications to each agent
            debate_a = run_debate("Momentum Trader", strat_a['decision'], strat_b['justification'], data)
            debate_b = run_debate("Value Contrarian", strat_b['decision'], strat_a['justification'], data)
            
            debate_results = {
                "momentum_rebuttal": debate_a,
                "value_rebuttal": debate_b
            }
        
        # 3. Final Output Structure
        output = {
            "ticker": ticker,
            "run_date": str(datetime.now().date()),
            "market_data_summary": data,
            "strategy_a": strat_a,
            "strategy_b": strat_b,
            "evaluator": evaluation,
            "debate_results": debate_results # 2. Add this key!
        }
        
        # 4. Save to outputs/
        with open(f"outputs/{ticker}.json", "w") as f:
            json.dump(output, f, indent=4)
        print(f"✅ Saved {ticker}.json with evaluation and debate status.")

    # 5. Final Reporting
    print("\n--- All stocks processed. Generating Final Summary ---")
    generate_summary()

if __name__ == "__main__":
    main()