# golixco_chatbot.py
# Author: Rohan Sonu Bablani (Golixco)
# Small rule-based chatbot (AIML-ish) using regex patterns.
# Student-level project for learning regex-based dialogue systems.

import re
import random
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("conversation.log")

# --- simple spam detector (student-level, word-scoring) ---
SPAM_WORDS = {"free", "click", "buy", "subscribe", "visit", "win", "prize", "discount"}
SPAM_THRESHOLD = 1  # >=1 spam words -> flagged

def is_spam(text: str) -> bool:
    words = set(re.findall(r"\b\w+\b", text.lower()))
    hits = sum(1 for w in words if w in SPAM_WORDS)
    return hits >= SPAM_THRESHOLD

# --- end spam detector ---


# small pattern -> responses list (feels like AIML categories)
PATTERNS = [
    (r'\bhi\b|\bhello\b|\bhey\b', [
        "Hey — I'm Golixco. How can I help you today?",
        "Hello! Golixco here. What's up?",
        "Hi! Need any help with Python / AIML homework?"
    ]),
    (r'\bhow are you\b|\bhow r u\b', [
        "I am a bot, but I'm doing fine — thanks for asking!",
        "Running smoothly. Ready to help you learn :)"
    ]),
    (r'\b(name|who are you)\b', [
        "I'm Golixco, a small student-built chatbot. Nice to meet you!",
        "Call me Golixco — I was made as a fun AIML-style project."
    ]),
    (r'\bpython\b|\bprogramming\b|\bcode\b', [
        "I like Python. Want a small code example or help with a bug?",
        "Programming tip: break problems into small functions."
    ]),
    (r'\b(hacktoberfest|hacktober)\b', [
        "Nice — Hacktoberfest is a great way to start contributing.",
        "Make small quality PRs. Docs and beginner bugs are excellent."
    ]),
    (r'\b(joke|tell me a joke)\b', [
        "Why do programmers prefer dark mode? Because light attracts bugs. 😄",
        "I'd tell you a UDP joke, but you might not get it. 😅"
    ]),
    (r'\b(thanks|thank you)\b', [
        "You're welcome! Happy hacking :)",
        "No problem — glad to help."
    ]),
    (r'\b(help|what can you do)\b', [
        "I can answer simple questions, show examples, and save this chat to conversation.log.",
        "Ask me about Python, GitHub, or say 'demo' to see a short example."
    ]),
    (r'\bdemo\b|\bexample\b', [
        "Demo: print('Hello from Golixco') — try running simple examples yourself.",
        "Example command: python3 golixco_chatbot.py (then chat)."
    ]),
        (r'\bok\b|\ball good\b|\bchill\b', [
        "Cool — glad everything's fine. Want a study tip?",
        "Alright — if you need help, say 'help' or ask about Python."
    ]),
    (r'\bstudy\b|\bcourse\b|\bwhat (should|to) study\b', [
        "Study tip: practice small projects and read code daily.",
        "If you're in AIML, try implementing Naive Bayes or a small chatbot — hands-on helps the most."
    ]),
# fallback handled separately
]

FALLBACKS = [
    "Sorry — I didn't get that. Could you say it differently?",
    "Hmm, I don't know that yet. Try asking about Python, Hacktoberfest, or say 'help'.",
    "I'm learning — that question is new to me. Try a simpler phrase."
]

def match_response(text: str) -> str:
    t = text.lower()
    for pattern, responses in PATTERNS:
        if re.search(pattern, t):
            return random.choice(responses)
    return random.choice(FALLBACKS)

def save_line(user: str, bot: str):
    ts = datetime.now().isoformat()
    try:
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(f"{ts}\tUSER: {user}\n{ts}\tGOLIXCO: {bot}\n")
    except Exception:
        pass  # logging must not crash the chat

def intro():
    print("Golixco — small AIML-ish chatbot (student project). Type 'quit' to exit.")
    print("Try: hello, how are you, python, hacktoberfest, joke, demo, help")

def main():
    intro()
    while True:
        try:
            text = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye — keep learning!")
            break
        if not text:
            continue
        if text.lower() in ("quit", "exit", "bye"):
            print("Golixco: Bye — good luck with Hacktoberfest!")
            save_line(text, "Bye — good luck with Hacktoberfest!")
            break
        
        # quick spam check (student-level)
        if is_spam(text):
            reply = "I think this might be spam — I can't help with that. If this is a mistake, try rephrasing."
            print("Golixco:", reply)
            save_line(text, reply)
            continue
response = match_response(text)
        print("Golixco:", response)
        save_line(text, response)

if __name__ == "__main__":
    main()
