import streamlit as st
import pickle
import re

model = pickle.load(open("models/model.pkl","rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl","rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]','',text)
    return text

st.title("Fake News Detection")

news = st.text_area("Enter news text")

if st.button("Predict"):

    news = clean_text(news)

    vec = vectorizer.transform([news])

    pred = model.predict(vec)

    if pred[0] == 1:
        st.success("Real News")
    else:
        st.error("Fake News")
