from transformers import pipeline

# Load a summarization pipeline (this uses a small, fast model)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def simplify_text(text: str) -> str:
    """
    Simplify/shorten the input text while preserving meaning.
    Returns a summary of the text.
    """
    # Transformers may fail if text is too short or too long, handle exceptions
    try:
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        # fallback to returning original text
        return text

def detect_mood(text: str) -> str:
    """
    Dummy mood detection for demonstration.
    In real scenario, you can use sentiment-analysis models.
    """
    if any(word in text.lower() for word in ["happy", "joy", "excited", "delighted", "smile"]):
        return "Happy"
    if any(word in text.lower() for word in ["sad", "down", "depressed", "unhappy"]):
        return "Sad"
    if any(word in text.lower() for word in ["angry", "mad", "frustrated"]):
        return "Angry"
    return "Neutral"
