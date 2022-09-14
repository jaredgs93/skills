import ffmpeg

#Remover comentarios
#from videoprops import get_video_properties
import streamlit as st

def show_metadata(video_url):
    print(video_url)

    #Remover comentarios
    #props = get_video_properties(video_url)
    #print(props)
    #st.json(props)
    metadata = ffmpeg.probe("videos/VID_20190610_205528543.mp4")
    st.json(metadata)
    #print(metadata)