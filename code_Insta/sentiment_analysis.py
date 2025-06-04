import joblib
import nltk
import re
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load the trained model pipeline
model = joblib.load("models/random_forest_model.pkl")  

# Text preprocessing function (same as training)
def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove URLs, mentions, hashtags, numbers, and punctuation
    text = re.sub(r"http\S+|www\S+|@\w+|#\w+|\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

# Prediction function
def predict_sentiment(comment):
    processed = preprocess_text(comment)
    prediction = model.predict([processed])
    return prediction[0]

