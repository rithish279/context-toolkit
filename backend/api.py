from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from dotenv import load_dotenv
from groq import Groq

from strategies import get_all_strategies
from utils import TokenCounter

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
token_counter = TokenCounter()

def ask_ai(context_messages, question):
    
    messages = []
    
    for msg in context_messages:
        if msg.startswith("User:"):
            messages.append({
                "role": "user",
                "content": msg.replace("User:", "").strip()
            })
        elif not msg.startswith("[..."):  # Skip summary placeholders
            messages.append({
                "role": "user",
                "content": msg
            })
    
    # Add the question if not already in messages
    if not messages or messages[-1]["content"] != question:
        messages.append({
            "role": "user",
            "content": question
        })
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
@app.route('/analyze', methods=['POST'])
def analyze():

    try:
        data = request.json
        conversation = data.get('conversation', [])
        question = data.get('question', conversation[-1] if conversation else "")

        if not conversation:
            return jsonify({"error": "No conversation provided"}), 400
        
        strategies = get_all_strategies()
        results = {}

        for strategy in strategies:
            result = strategy.apply(conversation)
            kept_messages = result["kept_messages"]
            metadata = result["metadata"]

            tokens_used = token_counter.count_messages(kept_messages)

            ai_response = ask_ai(kept_messages, question)

             # Format result for frontend
            strategy_key = strategy.name.lower().replace(" ", "_")
            results[strategy_key] = {
                "name": strategy.name,
                "description": metadata.get("description", ""),
                "tokensUsed": tokens_used,
                "keptCount": len(kept_messages),
                "totalCount": len(conversation),
                "keptMessages": kept_messages,
                "response": ai_response,
                "color": metadata.get("color", "#999")
            }
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "API is running"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
