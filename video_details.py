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
    metadata = {}
    metadata['height'] = cv2video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    metadata['width']  = cv2video.get(cv2.CAP_PROP_FRAME_WIDTH) 
    metadata['frame_rate'] = cv2video.get(cv2.CAP_PROP_FPS)
    metadata['fourcc'] = cv2video.get(cv2.CAP_PROP_FOURCC)
    metadata['frame_count'] = cv2video.get(cv2.CAP_PROP_FRAME_COUNT)
    metadata['format'] = cv2video.get(cv2.CAP_PROP_FORMAT)
    metadata['brightness'] = cv2video.get(cv2.CAP_PROP_BRIGHTNESS)
    metadata['contrast'] = cv2video.get(cv2.CAP_PROP_CONTRAST)
    metadata['saturation'] = cv2video.get(cv2.CAP_PROP_SATURATION)
    metadata['hue'] = cv2video.get(cv2.CAP_PROP_HUE)
    metadata['image_gain'] = cv2video.get(cv2.CAP_PROP_GAIN)
    #st.text ("Video Dimension: height:{} width:{}".format( height, width))
    st.json(metadata)
    #print(metadata)