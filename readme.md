# 📈 Agentic Stock Analysis System
### A Multi-Agent Financial Deliberation Framework
**Author:** Iteoluwa Ibitoye  
**Program:** MS in AI Systems Management, Carnegie Mellon University (Heinz College)

---

## 📌 Project Overview
This system implements a multi-agent orchestration pattern to provide high-fidelity stock analysis. It uses adversarial reasoning to compare different financial philosophies and synthesizes them into a single investment perspective.

### 1. Selected Strategies
This analysis uses two fundamentally different market philosophies to ensure diverse outputs:
* **Momentum Trader:** Focuses on price inertia and trend following. This strategy prioritizes technical indicators like the 20-day and 50-day Moving Averages ($MA_{20}$, $MA_{50}$) to identify "winning" trends.
* **Value Contrarian:** Focuses on mean reversion and overextension. This strategy prioritizes the Relative Strength Index (RSI) and distance from 52-week highs to identify "overbought" or "oversold" conditions.
  
Their findings are then synthesized by a **Chief Evaluator Agent** to identify consensus or conflict.

This project was developed for the CMU Heinz College AIM program to demonstrate **Adversarial AI Reasoning** and **Walk-Forward Validation** in financial decision-support systems.

## 🚀 Key Features
* **Parallel Agent Analysis:** Two distinct trading philosophies (Momentum vs. Value) analyze the same data state without cross-contamination.
* **🥊 Debate Mode (Bonus Extension):** If agents disagree, they enter a second round of deliberation where they must defend their logic or concede to their peer.
* **📊 Historical Backtesting (Bonus Extension):** The system "time-travels" 60 days into the past to test agent predictions against actual real-world price outcomes.
* **JSON-First Architecture:** All inputs and outputs are strictly structured in JSON to ensure system reliability and easy integration with downstream dashboards.

---

### 2. LLM Provider
* **Model:** Llama-3.3-70b-versatile
* **Provider:** **Groq Cloud** (Chosen for high-speed inference and native support for JSON-mode structure).

### 3. 🛠️ Tech Stack
* **Language:** Python 3.13
* **Intelligence:** Llama-3.3-70b (via Groq Cloud) 
* **Financial Data:** Yahoo Finance API (`yfinance`)
* **Environment:** Virtualized Python Environment (`.venv`)
* **Orchestration:**  Custom Python implementation using the Groq SDK for parallel agent calls and sequential evaluation/debate logic. 

---
## ⚙️ Installation & How to Run

### Installation
1.  **Extract the project** or clone the repository.
2.  **Create a virtual environment:**
    ```bash
    python3 -m venv .venv
    ```
3.  **Activate the environment:**
    ```bash
    source .venv/bin/activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the System
1.  **Configure API Key:** Add your Groq API key to a `.env` file: `GROQ_API_KEY=your_key_here`.
2.  **Run Live Analysis:**
    ```bash
    python src/main.py
    ```
    *This will process NVDA, TSLA, JNJ, and GME, run the Evaluator, and initiate Debate Mode if disagreements occur.*
3.  **Run Historical Backtest:**
    ```bash
    python src/backtest.py
    ```
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
