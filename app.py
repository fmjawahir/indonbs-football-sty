import streamlit as st
import joblib
import re
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

model_path = 'model.pkl'
model = joblib.load(model_path)

tfidf_vectorizer_path = 'tfidf.pkl'
tfidf_vectorizer = joblib.load(tfidf_vectorizer_path)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words_indo = set(stopwords.words('indonesian'))
    tokens = [word for word in tokens if word not in stop_words_indo]
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

# Streamlit app
st.title("Streamlit App for Sentiment Analysis of Indonesian National Team's Performance Under Shin Tae-yong.")

user_input = st.text_area("Input your text in Bahasa:")

if st.button("Go!"):
    if user_input:
        preprocessed_input = preprocess_text(user_input)
        tfidf_input = tfidf_vectorizer.transform([preprocessed_input])
        prediction = model.predict(tfidf_input)[0]
        sentiment = "Positive" if prediction == 1 else "Negative"
        st.write(f"Predicted Sentiment: {sentiment}")
    else:
        st.write("Please enter text to be analyzed.")