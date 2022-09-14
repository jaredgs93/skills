#import ffmpeg
from videoprops import get_video_properties
import streamlit as st

def show_metadata(video_url):
    #vid = ffmpeg.probe(video_url)
    #st.json(vid)
    props = get_video_properties(video_url)
    print(props)
    st.json(props)
    