#import ffmpeg
import streamlit as st
import os
root_folder = '/videos/'
video = 'Sujeto35.mp4'
ruta_video = root_folder+video
"""j = ffmpeg.probe(ruta_video)
st.json(j)"""


files = [f for f in os.listdir('.')]
files
