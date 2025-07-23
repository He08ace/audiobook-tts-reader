import streamlit as st
import requests
import tempfile

# Your ElevenLabs API key
API_KEY = "sk_079e3e853ca2e92309cef079e2a3adbb36d55c845cc36712"
VOICE_ID = "Rachel"  # You can change to "Bella", "Antoni", etc.

# Audiobook Chapters
chapters = {
    "Introduction": "Welcome to your audiobook. This is the introduction.",
    "Chapter 1: The Journey Begins": "Once upon a time, in a village far away, a young dreamer set out on an adventure.",
    "Chapter 2: The First Challenge": "The path ahead was steep, but courage lit the way.",
    "Chapter 3: Lessons Learned": "Every mistake taught the dreamer something valuable.",
}

# Streamlit Layout
st.set_page_config(page_title="Audiobook Reader", layout="wide")
st.title("📖 Audiobook TTS Reader")
st.caption("Now powered by ElevenLabs Voice AI")

# Chapter Selector
selected_chapter = st.selectbox("Choose a chapter", list(chapters.keys()))
text = chapters[selected_chapter]

# Display Selected Text
st.subheader(selected_chapter)
st.write(text)

# Function to Get Audio
def get_audio_
