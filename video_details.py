#import ffmpeg
import streamlit as st
import os
import sys
#sys.path.append('ffmpeg/')

#st.json({'Exists':os.path.exists('ffmpeg/')})
root_folder = 'videos/'
video = 'Sujeto35.mp4'
ruta_video = root_folder+video

#j = ffmpeg.probe(ruta_video)
#st.json(j)

video_file = open(ruta_video, 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

import subprocess

list_files = subprocess.run(["ls", "-l"])
"The exit code was: %d" % list_files.returncode
