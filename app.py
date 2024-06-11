# install streamlit
import streamlit as st
import pickle
import time

st.title("Twitter Sentiment Analysis")

# Load Mode 
model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

tweet = st.text_input("Enter your text")

sumbit = st.button('predicts')

if sumbit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction time taken: ', round(end-start ,2),'second')
    print(prediction[0])
    st.write("Predicted Sentiment is : ",prediction[0])

 