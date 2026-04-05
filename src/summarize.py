import json
import os

def generate_summary():
    output_dir = 'outputs'
    # 1. Setup the structure required by the assignment
    summary = {
        "strategies": ["Momentum Trader", "Value Contrarian"],
        "stocks_analyzed": [],
        "total_agreements": 0,
        "total_disagreements": 0,
        "results": [] # This is the section we're fixing!
    }

    # 2. Get all JSON files except the summary itself
    files = [f for f in os.listdir(output_dir) if f.endswith('.json') and f != 'summary.json']

    for file in files:
        path = os.path.join(output_dir, file)
        with open(path, 'r') as f:
            try:
                data = json.load(f)
                
                # Extract the key pieces of info
                ticker = data.get("ticker")
                a_decision = data.get("strategy_a", {}).get("decision")
                b_decision = data.get("strategy_b", {}).get("decision")
                agree = data.get("evaluator", {}).get("agents_agree", False)

                # 3. Populate the 'results' list
                summary["stocks_analyzed"].append(ticker)
                summary["results"].append({
                    "ticker": ticker,
                    "a_decision": a_decision,
                    "b_decision": b_decision,
                    "agree": agree
                })

                # 4. Update the counters
                if agree:
                    summary["total_agreements"] += 1
                else:
                    summary["total_disagreements"] += 1

            except Exception as e:
                print(f"Error reading {file}: {e}")

    # 5. Write the final aggregated file
    with open(os.path.join(output_dir, 'summary.json'), 'w') as f:
        json.dump(summary, f, indent=4)
    
    print(f"✅ summary.json generated with {len(summary['results'])} stocks in the results section.")

if __name__ == "__main__":
    generate_summary()