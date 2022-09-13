import ffmpeg
import streamlit as st

root_folder = '/Users/jaredguerrero/Documents/Doctorado UCLM/Proyectos SMILE/video/'
video = 'Sujeto10.mp4'
ruta_video = root_folder+video
j = ffmpeg.probe(ruta_video)
st.json(j)
