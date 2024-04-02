## YouTube Video Summarizer with Streamlit

**Creator:** Halleluyah Darasimi Oludele

**Description:**

This Streamlit web app helps you quickly summarize YouTube videos by analyzing their transcripts using Google Generative AI. 

**Features:**

- **Easy to use:** Just enter a YouTube video URL and click submit.
- **Automatic transcript extraction:** The app retrieves the video transcript using the YouTube Transcript API.
- **AI-powered summarization:** The app utilizes Google Generative AI to create a concise summary of the video content based on the transcript.
- **Clear presentation:** The generated summary is displayed within the app for easy viewing.
- **Convenient download:** You can download the summary as a text file for future reference.

**How to Use:**

1. Open the app in your web browser.
2. Paste the URL of the YouTube video you want to summarize.
3. Click the "Submit" button.
4. If a transcript is found, the app will generate a summary and display it in an expandable section.
5. You can download the summary by clicking the "Download Summary" button.

**Requirements:**

- Python 3.11
- Streamlit (`pip install streamlit`)
- youtube-transcript-api (`pip install youtube-transcript-api`)
- google-generativeai (`pip install google-generativeai`)
- A Google Cloud account and API Key ([https://cloud.google.com/ai/apis](https://cloud.google.com/ai/apis))

**Getting Started:**

1. Install the required libraries using `pip`.
2. Set your Google API key in an environment variable named `API_KEY`.
3. Run the app using `streamlit run app.py`.

**Disclaimer:**

This application utilizes third-party libraries and APIs. Their functionality and availability may change over time.

**Please Note:**

- This app relies on the YouTube Transcript API, which may not always provide accurate or complete transcripts. 
- The quality of the summary depends on the quality of the extracted transcript.
- Google Generative AI usage may incur costs depending on your Google Cloud account setup. Refer to the Google Generative AI documentation for details.
