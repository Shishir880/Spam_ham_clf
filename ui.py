import streamlit as st
import requests

st.title("Spam Detector App")
st.write("Enter a message to check if it's Spam or Ham")

user_input = st.text_area("Enter text here:")
if st.button("Predict"):
    if user_input:
        api_url = "http://127.0.0.1:5000/predict"
        response = requests.post(api_url, json={"text": user_input})
        if response.status_code == 200:
            result = response.json().get("prediction", "Error")
            st.write(f"### Prediction: {result}")
        else:
            st.error("Error in API response")
    else:
        st.warning("Please enter some text to predict.")
