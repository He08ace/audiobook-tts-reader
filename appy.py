import streamlit as st
import requests
import tempfile

# Your ElevenLabs API key
API_KEY = "sk_050fb6eb08fe227c482661ca4036baba9194716d2f737788"
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # You can change to "Bella", "Antoni", etc.

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

# ✅ FIXED FUNCTION STARTS HERE
def get_audio_from_elevenlabs(text, voice_id="Rachel"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            fp.write(response.content)
            return fp.name
    else:
        st.error("⚠️ Failed to generate audio. Check your API key or quota.")
        return None

# Play Button
if st.button("🔊 Play with ElevenLabs Voice"):
    audio_file_path = get_audio_from_elevenlabs(text, VOICE_ID)
    if audio_file_path:
        st.audio(audio_file_path, format="audio/mp3")
