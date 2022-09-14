import ffmpeg

#Remover comentarios
#from videoprops import get_video_properties
import streamlit as st
import cv2


def show_metadata(video_url):
    print(video_url)

    #Remover comentarios
    #props = get_video_properties(video_url)
    #print(props)
    #st.json(props)
    
    #metadata = ffmpeg.probe(video_url)
    #st.json(metadata)

    cv2video = cv2.VideoCapture(video_url)
    height = cv2video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = cv2video.get(cv2.CAP_PROP_FRAME_WIDTH) 
    st.text ("Video Dimension: height:{} width:{}".format( height, width))
    #print(metadata)