# Positive Language Rewriter for YouTube Comments

A simple web app that fetches YouTube comments and helps rewrite negative or harsh comments into positive, friendly language. Built with Python and Streamlit.

---

## What It Does

- You enter a YouTube video link.
- The app fetches some comments from that video.
- You select a comment to analyze.
- The app tells you if the comment is Positive, Negative, or Neutral.
- If Negative or Neutral, it can rewrite the comment to sound more positive.
- Shows two rewritten versions: one with simple word changes, and one with AI-powered paraphrasing.

---

## How to Run This App (For Beginners)

### Step 1: Install Python

Make sure Python is installed on your computer (version 3.7 or higher). You can download it here:  
[https://python.org/downloads](https://python.org/downloads)

### Step 2: Get the Project Code

Get the project folder with these files:  
- `app.py`  
- `rewriter.py`  
- `requirements.txt`  
- (optional) `README.md`

You can get it by downloading from GitHub (if available), or ask your friend to send you the folder.

### Step 3: Open the Project in VS Code

- Open **Visual Studio Code (VS Code)**.
- Open the project folder in VS Code (`File → Open Folder`).

### Step 4: Set Up a Virtual Environment

- Open the terminal in VS Code (`Terminal → New Terminal`).
- Run this command to create a virtual environment:
  - On Windows:
    ```
    python -m venv .venv
    ```
  - On Mac/Linux:
    ```
    python3 -m venv .venv
    ```
- Activate the virtual environment:
  - On Windows:
    ```
    .venv\Scripts\activate
    ```
  - On Mac/Linux:
    ```
    source .venv/bin/activate
    ```

### Step 5: Install Required Packages

Run this command to install all necessary Python packages:


If you get errors about missing packages like `sentencepiece` or `torch`, install them manually:


### Step 6: Get a YouTube Data API Key

To fetch comments from YouTube, you need an API key:

1. Go to [Google Cloud Console](https://console.cloud.google.com).
2. Create a new Project.
3. Enable the **YouTube Data API v3** for your project.
4. Go to **Credentials**, then **Create API key**.
5. Copy the generated API key (a long string).

### Step 7: Add Your API Key in `app.py`

- Open `app.py` in VS Code.
- Find this line:


- Replace `"YOUR_YOUTUBE_API_KEY"` with your actual API key inside quotes. For example:


- Save the file.

### Step 8: Run Your App

In the terminal (with the virtual environment activated), run:


This will open your web browser with the app interface.

### Step 9: Use the App

- Enter a YouTube video URL (e.g., `https://www.youtube.com/watch?v=VIDEO_ID`).
- Wait while comments load.
- Select a comment from the dropdown.
- See the sentiment detected (Positive / Negative / Neutral).
- If Negative or Neutral, click the rewrite button to see positive rewrites.
- Enjoy!

---

## Tips for Success

- Always activate the virtual environment before running the app.
- Keep your API key secret—don’t share it publicly.
- If an error appears, read it carefully and ask for help if needed.
- Take your time; small errors are normal when starting.

---

## Files Explanation

- **app.py** — The main app interface and logic.
- **rewriter.py** — Code that detects sentiment and rewrites messages.
- **requirements.txt** — List of Python packages needed.

---

## Need Help?

Feel free to ask the project owner or look for help online—there are many beginner-friendly Python and Streamlit tutorials available.

---

Thank you for trying out this app! Have fun spreading positivity online! 😊
