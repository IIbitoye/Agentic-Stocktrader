import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_evaluator(strat_a_output, strat_b_output):
    """Synthesizes the two strategy outputs into a consensus or conflict analysis."""
    
    with open("prompts/evaluator.txt", "r") as f:
        system_prompt = f.read()

    combined_input = {
        "strategy_a": strat_a_output,
        "strategy_b": strat_b_output
    }

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"COMPARE THESE REPORTS: {json.dumps(combined_input)}"}
        ],
        response_format={"type": "json_object"}
    )
    
    return json.loads(response.choices[0].message.content)