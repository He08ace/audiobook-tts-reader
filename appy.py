import streamlit as st
from gtts import gTTS
import tempfile

# Audiobook Chapters
chapters = {
    "Introduction": "Welcome to your audiobook. This is the introduction.",
    "Chapter 1: The Journey Begins": "Once upon a time, in a village far away, a young dreamer set out on an adventure.",
    "Chapter 2: The First Challenge": "The path ahead was steep, but courage lit the way.",
    "Chapter 3: Lessons Learned": "Every mistake taught the dreamer something valuable.",
}

st.set_page_config(page_title="Audiobook TTS Reader", layout="wide")

st.title("📖 Audiobook Reader with TTS")
st.caption("Powered by Google Text-to-Speech (gTTS)")

selected_chapter = st.selectbox("Choose a chapter to read and listen:", list(chapters.keys()))
text = chapters[selected_chapter]

st.subheader(selected_chapter)
st.write(text)

if st.button("🔊 Play Audio"):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format='audio/mp3')
  
