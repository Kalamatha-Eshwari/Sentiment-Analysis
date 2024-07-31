import streamlit as st
import pickle
from textblob import TextBlob

# Load the model from the pickle file
def load_model():
    try:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please check the file path.")
        return None

# Initialize the model
model = load_model()

# Streamlit UI
st.set_page_config(page_title="Sentiment Analysis", layout='centered')

st.title("Sentiment Analysis App")

# Text input for user
user_input = st.text_area("Enter the text you want to analyze:", "")

def analyze_sentiment(text):
    """Perform sentiment analysis on the input text using the loaded model."""
    if model:
        blob = TextBlob(text)  # Using TextBlob for simplicity
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            sentiment_label = "Positive 😊"
        elif sentiment < 0:
            sentiment_label = "Negative 😡"
        else:
            sentiment_label = "Neutral 😐"
        return sentiment_label, sentiment
    else:
        return "Model not loaded", 0

if st.button("Analyze Sentiment"):
    if user_input:
        # Analyze sentiment
        sentiment_label, sentiment_score = analyze_sentiment(user_input)
        st.subheader("Analysis Result:")
        st.write(f"**Sentiment:** {sentiment_label}")
        st.write(f"**Score:** {sentiment_score:.2f}")
    else:
        st.error("Please enter some text.")

