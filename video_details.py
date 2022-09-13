#import ffmpeg
import streamlit as st
import os
root_folder = 'videos/'
video = 'Sujeto35.mp4'
ruta_video = root_folder+video
st.json({'ruta_existente':os.path.exists(ruta_video)})

video_file = open('ruta_video', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
