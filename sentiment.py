from transformers import pipeline
import re
sentiment_model = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

DANGER_TERMS = [
    "kill", "die", "suicide", "murder", "shoot", "stab","bomb", "burn", "blow up", "attack",
    "assault","hurt someone", "beat someone","hang myself", "jump off", "cut myself",
    "end my life", "take my life", "harm myself", "self harm","destroy everything", "burn it all",
    "wipe out","i want to hurt", "i want to kill", "i want to die", "i will kill"
]

STRESS_TERMS = [
    "tired", "exhausted", "burned out","overwhelmed", "stressed", "stress","anxious", "anxiety", 
    "nervous","worried", "panic", "panicking","scared", "afraid", "fear","lonely", "helpless", 
    "hopeless","pressure", "too much", "can't cope","can't handle", "i'm done", "giving up",
    "lost", "confused", "trapped","frustrated", "angry", "upset","depressed", "sad", "crying"
]

def keyword_found(text, key_list):
    for term in key_list:
        if term in text:
            return True
    return False


def analyze_sentiment(text):
    """
    Returns: (label, risk)
      label ∈ {"Positive", "Negative", "Neutral"}
      risk ∈ {"HIGH", "NONE"}
    """
    lowered = text.lower().strip()

    if keyword_found(lowered, DANGER_TERMS):
        return "Negative", "HIGH"

    stress_detected = keyword_found(lowered, STRESS_TERMS)

    try:
        result = sentiment_model(text)[0]
        raw_label = result["label"].upper()
        confidence = float(result["score"])
    except Exception:
        return "Neutral", "NONE"

    if "NEG" in raw_label:
        label = "Negative"
    elif "POS" in raw_label:
        label = "Positive"
    else:
        label = "Neutral"

    if stress_detected and label == "Positive":
        label = "Neutral"
    elif stress_detected and label != "Positive":
        label = "Negative"

    # Neutral decision rule
    if confidence < 0.65:
        return "Neutral", "NONE"

    return label, "NONE"
