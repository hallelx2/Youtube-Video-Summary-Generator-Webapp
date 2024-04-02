from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import random
import string
import os


GOOGLE_API_KEY = os.environ['API_KEY']
genai.configure(api_key=GOOGLE_API_KEY)

def get_video_id(url):
    id = url[-11::]
    return id

def get_transcript(id):
    transcript_json = YouTubeTranscriptApi.get_transcript(id)
    transcript = ""
    for text in transcript_json:
        transcript += text['text']

    return transcript

def get_video_summary(transcript):
    prompt  = f"Give me a summary of what was discussed in this youtube video with transcript: {transcript}"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def create_random_filename():
    # Generate a random filename with a .txt extension
    chars = string.ascii_lowercase + string.digits
    random_filename = "".join(random.choice(chars) for _ in range(10)) + ".txt"

    
    while os.path.exists(random_filename):
        random_filename = create_random_filename() 

    return random_filename

def generate_response_text(response):
    random_filename = create_random_filename()
    with open(random_filename, "w") as file:
        file.write(response)


def main():
    link = "https://youtu.be/mgQMPlrJw7I"
    id = get_video_id(link)
    transcript = get_transcript(id)
    response = get_video_summary(transcript)
    generate_response_text(response)
    print(response)

if __name__=='__main__':
    main()
