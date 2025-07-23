import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration
from googleapiclient.discovery import build
import re
from rewriter import rewrite_sentence

st.title("🌟 Positive Language Rewriter for YouTube Comments")

# Input for YouTube video URL
video_url = st.text_input("🎥 Enter YouTube Video URL")

# Cache model loading to avoid reloading every time
@st.cache_resource
def load_model():
    model = T5ForConditionalGeneration.from_pretrained("ramsrigouthamg/t5_paraphraser")
    tokenizer = T5Tokenizer.from_pretrained("ramsrigouthamg/t5_paraphraser")
    return model, tokenizer

model, tokenizer = load_model()

def paraphrase(text):
    input_text = "paraphrase: " + text + " </s>"
    encoding = tokenizer.encode_plus(input_text, return_tensors="pt")
    output = model.generate(
        input_ids=encoding["input_ids"],
        attention_mask=encoding["attention_mask"],
        max_length=60,
        num_beams=5,
        early_stopping=True
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Function to fetch YouTube comments using API key
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

# Your YouTube Data API key here:
API_KEY = "AIzaSyCu_hzuexqxmRXCTIV0qNi0ZKS8TElFk4Q"  # <-- Replace this with your actual key

comments = []
if video_url:
    try:
        comments = get_youtube_comments(video_url, API_KEY)
        if not comments:
            st.warning("No comments found for this video.")
    except Exception as e:
        st.error(f"Error fetching comments: {e}")

if comments:
    selected_comment = st.selectbox("💬 Select a comment to rewrite:", comments)
else:
    selected_comment = None

if st.button("🔁 Rewrite Comment"):
    if selected_comment:
        # Use your rewrite_sentence for simple word replacements
        rewritten_basic = rewrite_sentence(selected_comment)
        
        # Paraphrase advanced rewriting
        rewritten_advanced = paraphrase(selected_comment)

        st.subheader("✅ Rewritten Comment (Basic):")
        st.success(rewritten_basic)

        st.subheader("✅ Rewritten Comment (Advanced - Paraphrased):")
        st.success(rewritten_advanced)
    else:
        st.warning("Please select a comment to rewrite.")
