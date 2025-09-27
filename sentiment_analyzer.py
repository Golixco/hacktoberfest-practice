# sentiment_analyzer.py
# Author: Rohan Sonu Bablani (Golixco)
# Simple student-level sentiment analyzer (word-scoring approach).

import re

POSITIVE = {
    "good", "happy", "love", "great", "excellent", "amazing",
    "wonderful", "best", "nice", "fantastic", "awesome" , "Gambare"
}
NEGATIVE = {
    "bad", "sad", "hate", "terrible", "awful", "worst",
    "angry", "poor", "horrible", "disappointing" , "Tatakae"
}

def analyze_sentiment(text: str) -> str:
    words = re.findall(r"\b\w+\b", text.lower())
    score = sum(1 for w in words if w in POSITIVE) - sum(1 for w in words if w in NEGATIVE)

    if score > 0:
        return "Positive 😊"
    if score < 0:
        return "Negative 😞"
    return "Neutral 😐"

def main():
    print("Simple Sentiment Analyzer — type sentences and press Enter.")
    print("Type 'quit' or 'exit' to stop.")
    while True:
        s = input(">>> ").strip()
        if s.lower() in ("quit", "exit"):
            print("Bye — keep learning!")
            break
        print("Sentiment:", analyze_sentiment(s))

if __name__ == "__main__":
    main()
