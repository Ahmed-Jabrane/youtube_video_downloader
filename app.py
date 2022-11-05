import streamlit as st
from pytube import YouTube
from streamlit_player import st_player
import moviepy.editor as mp


st.set_page_config(page_title="Youtube Video Downloader", page_icon="📹", layout="centered")

st.title("📹 Youtube Video Downloader")

st.sidebar.title("")

st.sidebar.write(
    f"This is open source project in Python using [Streamlit](https://streamlit.io/) to download and convert videos from Youtube."
)

st.sidebar.write(f"If you want to use the code or contribute, you can download it from [here](https://docs.streamlit.io/knowledge-base/tutorials/databases/public-gsheet).")

st.sidebar.markdown('![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ahmed-Jabrane)')


form = st.form(key="annotation")

with form:
    cols = st.columns((1, 1))
    url = cols[0].text_input('Enter the video url')
    convert_to = cols[1].selectbox("Convert to:", ["MP4", "MP3"], index=0 )
    submitted = st.form_submit_button(label="Convert")


if submitted:

    yt = YouTube(url)
    # Embed a youtube video
    st_player(url)
    SAVE_PATH = "." 
    tt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)

    st.success("Thanks! The video was downloaded.")

    if convert_to == "MP3":
        clip = mp.VideoFileClip(tt).subclip(0,20)
        clip.audio.write_audiofile(tt.replace('.mp4','.mp3'))
        st.balloons()
    else:
        st.balloons()
    
    


    
