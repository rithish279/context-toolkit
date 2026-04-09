'''Do different context strategies produce different answers??'''

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation = [
    "User: Hi, I'm Alex",
    "User: I love pepperoni pizza",
    "User: I'm allergic to peanuts",
    "User: What's the weather?",
    "User: What movie should I watch?",
    "User: What should I order for dinner?",
]

def strategy_recent_only(chat, keep_last=2):
    # keep last two messages
    return chat[-keep_last:]

def strategy_important_only(chat):
    
    important = []
    keywords = ["name", "love", "allergy", "allergic"]

    for msg in chat:
        if any(k in msg.lower() for k in keywords):
            important.append(msg)

    if chat[-1] not in important:

        important.append(chat[-1])
    return important

def ask_ai(context, question):

    messages = []
    for msg in context:
        if msg.startswith("User"):

            messages.append({"role": "user", "content": msg[5:].strip()})
    messages.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=100
    )
    return response.choices[0].message.content

question = "What should I order for dinner?"

print("=" * 60)
print("STRATEGY 1: Recent Only (last 2 messages)")
context1 = strategy_recent_only(conversation)
print(f"Context: {context1}")
print(f"AI says: {ask_ai(context1, question)}")

print("\n" + "=" * 60)
print("STRATEGY 2: Important Only")
context2 = strategy_important_only(conversation)
print(f"Context: {context2}")
print(f"AI says: {ask_ai(context2, question)}")