import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_strategy(strategy_name, market_data):
    """Calls the LLM with a specific strategy prompt."""
    
    # Load the specific prompt from your prompts folder
    prompt_path = f"prompts/{strategy_name.lower().replace(' ', '_')}.txt"
    with open(prompt_path, "r") as f:
        system_prompt = f.read()

    # The actual AI call
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Analyze this data: {json.dumps(market_data)}"}
        ],
        response_format={"type": "json_object"} # Forces the AI to give us JSON
    )
    
    return json.loads(response.choices[0].message.content)

def run_debate(strategy_name, original_decision, peer_justification, market_data):
    """Allows an agent to respond to the opposing strategy's reasoning."""
    with open("prompts/debate.txt", "r") as f:
        system_prompt = f.read()

    user_content = (
        f"You are the {strategy_name}. Your original decision was {original_decision}. "
        f"Your peer says: '{peer_justification}'. "
        f"Based on this and the data {json.dumps(market_data)}, do you change your mind?"
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)