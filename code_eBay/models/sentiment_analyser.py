from transformers import pipeline
import numpy as np

# Load multilingual sentiment analysis pipeline (supports German)
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def average_sentiment(feedback):
    """
    Compute the average sentiment score from a list of feedback entries.
    Each entry is a list of [timestamp, text].

    Returns a float between 1 (worst) and 5 (best), or None if no feedback.
    """
    if not feedback or len(feedback) == 0:
        return 0

    # Extract only the feedback texts
    texts = [entry[1] for entry in feedback if len(entry) == 2 and entry[1].strip()]
    
    if not texts:
        return 0

    # Run sentiment analysis
    results = sentiment_pipeline(texts)

    # Convert labels (e.g., '4 stars') to numeric
    scores = [int(result['label'].split()[0]) for result in results]
    avg_score=round(float(np.mean(scores)), 2)
    normalzed_score=(avg_score-3)/2
    return normalzed_score
