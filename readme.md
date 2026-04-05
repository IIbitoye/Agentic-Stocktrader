# 📈 Agentic Stock Analysis System
### A Multi-Agent Financial Deliberation Framework
**Author:** Iteoluwa Ibitoye  
**Program:** MS in AI Systems Management, Carnegie Mellon University (Heinz College)

---

## 📌 Project Overview
This system utilizes a **Multi-Agent Orchestration** pattern to perform technical stock analysis. Unlike a single-prompt analysis, this project employs two specialized agents—a **Momentum Trader** and a **Value Contrarian**—who analyze market data independently. Their findings are then synthesized by a **Chief Evaluator Agent** to identify consensus or conflict.

This project was developed for the CMU Heinz College AIM program to demonstrate **Adversarial AI Reasoning** and **Walk-Forward Validation** in financial decision-support systems.

---

## 🚀 Key Features
* **Parallel Agent Analysis:** Two distinct trading philosophies (Momentum vs. Value) analyze the same data state without cross-contamination.
* **🥊 Debate Mode (Bonus Extension):** If agents disagree, they enter a second round of deliberation where they must defend their logic or concede to their peer.
* **📊 Historical Backtesting (Bonus Extension):** The system "time-travels" 60 days into the past to test agent predictions against actual real-world price outcomes.
* **JSON-First Architecture:** All inputs and outputs are strictly structured in JSON to ensure system reliability and easy integration with downstream dashboards.

---

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Intelligence:** Llama-3.3-70b (via Groq Cloud)
* **Financial Data:** Yahoo Finance API (`yfinance`)
* **Environment:** Virtualized Python Environment (`.venv`)

---

## 📂 File Structure
```text
stocktrader_iibitoye/
├── src/
│   ├── main.py          # Master Orchestrator (Data -> Agents -> Evaluator -> Debate)
│   ├── market_data.py   # Technical Analysis Engine (Calculates RSI, MA20, MA50)
│   ├── strategies.py    # Logic for individual Strategy Agents and Debate Mode
│   ├── evaluator.py     # Synthesis logic for the Chief Evaluator
│   ├── summarize.py     # Macro-reporting tool for the full portfolio
│   └── backtest.py      # Historical performance validation script
├── prompts/             # System instructions (Momentum, Value, Evaluator, Debate)
├── outputs/             # Generated JSON reports and summary.json
├── .env                 # API Keys (Protected/Not Uploaded)
└── requirements.txt     # Project Dependencies