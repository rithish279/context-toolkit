import os
from dotenv import load_dotenv
from groq import Groq

from strategies import get_all_strategies
from utils import TokenCounter

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
token_counter = TokenCounter()

# Test conversation
conversation = [
    "User: Hi, I'm Alex",
    "User: I love pepperoni pizza",
    "User: I'm allergic to peanuts",
    "User: What's the weather?",
    "User: What movie should I watch?",
    "User: What should I order for dinner?",
]

question = "What should I order for dinner?"

def ask_ai(context, question):
    """Send context to LLM and get response"""
    messages = []
    for msg in context:
        if msg.startswith("User:"):
            messages.append({"role": "user", "content": msg[5:].strip()})
    messages.append({"role": "user", "content": question})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=150
    )
    return response.choices[0].message.content

def show_forgotten(full_conversation, kept_messages):
    """Show which messages were forgotten"""
    forgotten = [msg for msg in full_conversation if msg not in kept_messages]
    if forgotten:
        return f"FORGOTTEN ({len(forgotten)}): {forgotten[:3]}..."
    return "All important info kept"

def main():
    print("\n" + "="*70)
    print("AI CONTEXT MANAGEMENT TOOLKIT - Phase 2")
    print("="*70)
    
    print(f"\nFull conversation: {len(conversation)} messages")
    for i, msg in enumerate(conversation):
        print(f"   {i+1}. {msg}")
    
    print(f"\nQuestion: {question}")
    print("="*70)
    
    # Run all strategies
    strategies = get_all_strategies()
    
    for strategy in strategies:
        print(f"\nSTRATEGY: {strategy.name}")
        
        # Apply strategy
        result = strategy.apply(conversation)
        kept = result["kept_messages"]
        metadata = result["metadata"]
        
        # Calculate metrics
        token_count = token_counter.count_messages(kept)
        
        # Get AI response
        response = ask_ai(kept, question)
        
        # Display results
        print(f"   Description: {metadata['description']}")
        print(f"   Tokens used: {token_count}")
        print(f"   Messages kept: {len(kept)}/{metadata.get('total_messages', len(conversation))}")
        print(f"   {show_forgotten(conversation, kept)}")
        print(f"   Context given to AI: {kept}")
        print(f"   AI Response: {response}")
        print("-"*50)

if __name__ == "__main__":
    main()