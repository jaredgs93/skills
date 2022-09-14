import ffmpeg
import streamlit as st
import exiftool

def show_metadata(video_url):
    vid = ffmpeg.probe(video_url)
    st.json(vid)