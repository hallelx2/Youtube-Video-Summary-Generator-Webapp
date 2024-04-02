import streamlit as st
from script import get_transcript, get_video_id, get_video_summary

st.set_page_config(page_title="Youtube Summary generator")

st.title('Youtube Transcript Web App')

def main():
    link = st.text_input('Input the link to the youtube video')
    if link:
        if st.button('Get Summary'):
            id = get_video_id(link)
            transcript = get_transcript(id)
            response = get_video_summary(transcript)
            st.write('# Here is the Concise summary of the video on the youtube platform')
            st.write(response)
    else:
        st.write('You need to provide the link to the youtube video')

if __name__ == "__main__":
    main()