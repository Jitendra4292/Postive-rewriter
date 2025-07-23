from textblob import TextBlob

def detect_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity < 0:
        return "Negative"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Positive"

def rewrite_sentence(text):
    negative_words = {
        "hate": "dislike",
        "angry": "upset",
        "sad": "a bit down",
        "worst": "not good",
        "useless": "less effective",
        "annoying": "a little frustrating",
        "stupid": "confusing",
        "boring": "not very exciting"
    }

    words = text.split()
    new_words = [negative_words.get(word.lower(), word) for word in words]
    rewritten_text = " ".join(new_words)
    return rewritten_text
