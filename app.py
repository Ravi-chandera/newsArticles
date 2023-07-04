import streamlit as st
import requests
import json

# API Key for News API (Replace 'YOUR_API_KEY' with your actual API key)
API_KEY = 'f19f20641485460d81e4ca953abf54f3'

def fetch_articles(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

# Streamlit app code
st.title("News Articles")

# Get user input
keyword = st.text_input("Enter a keyword")

# Check if keyword is provided
if keyword:
    # Fetch news articles
    data = fetch_articles(keyword)
    
    # Display the JSON response
    st.subheader(f"Showing JSON response for '{keyword}':")
    st.json(data["totalResults"])
else:
    st.write("Enter a keyword to search for news articles.")
