import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration
from googleapiclient.discovery import build
import re

# Import from your rewriter.py
from rewriter import rewrite_sentence, detect_sentiment

st.title("🌟 Positive Language Rewriter for YouTube Comments")

video_url = st.text_input("🎥 Enter YouTube Video URL")

@st.cache_resource
def load_model():
    model = T5ForConditionalGeneration.from_pretrained("ramsrigouthamg/t5_paraphraser")
    tokenizer = T5Tokenizer.from_pretrained("ramsrigouthamg/t5_paraphraser")
    return model, tokenizer
model, tokenizer = load_model()

def paraphrase(text):
    input_text = "paraphrase this sentence with positive tone: " + text + " </s>"
    encoding = tokenizer.encode_plus(input_text, return_tensors="pt")
    output = model.generate(
        input_ids=encoding["input_ids"],
        attention_mask=encoding["attention_mask"],
        max_length=60,
        num_beams=5,
        early_stopping=True
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

def get_youtube_comments(video_url, api_key, max_comments=20):
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", video_url)
    if not video_id_match:
        return []
    video_id = video_id_match.group(1)
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_comments,
        textFormat="plainText"
    )
    response = request.execute()
    for item in response.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)
    return comments

API_KEY = "AIzaSyCu_hzuexqxmRXCTIV0qNi0ZKS8TElFk4Q"  # <-- Use your real API key here

comments = []
if video_url:
    try:
        comments = get_youtube_comments(video_url, API_KEY)
        if not comments:
            st.warning("No comments found for this video.")
    except Exception as e:
        st.error(f"Error fetching comments: {e}")

selected_comment = st.selectbox("💬 Select a comment to analyze & rewrite:", comments) if comments else None

if selected_comment:
    sentiment = detect_sentiment(selected_comment)
    st.markdown(f"**Sentiment:** :{'smile:' if sentiment=='Positive' else 'cry:' if sentiment=='Negative' else 'neutral_face:'} {sentiment}")

    if sentiment == "Negative":
        if st.button("🔁 Rewrite to Positive"):
            rewritten_basic = rewrite_sentence(selected_comment)
            rewritten_advanced = paraphrase(selected_comment)
            st.subheader("✅ Rewritten Comment (Basic):")
            st.success(rewritten_basic)
            st.subheader("✅ Rewritten Comment (Advanced - AI):")
            st.success(rewritten_advanced)
    elif sentiment == "Neutral":
        st.info("This comment seems neutral. You can still rewrite if you want.")
        if st.button("🔁 Rewrite Anyway"):
            rewritten_basic = rewrite_sentence(selected_comment)
            rewritten_advanced = paraphrase(selected_comment)
            st.subheader("✅ Rewritten Comment (Basic):")
            st.success(rewritten_basic)
            st.subheader("✅ Rewritten Comment (Advanced - AI):")
            st.success(rewritten_advanced)
    else:  # Positive
        st.success("This comment is already positive! 🎉 No rewrite needed.")

else:
    st.warning("Please select a comment to analyze.")

