import os
os.system("static_ffmpeg -version")
os.system("static_ffprobe -version")

import streamlit as st
import requests
import video_details


#URL prueba: https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4
#import os

#os.system("static_ffmpeg -version")
#os.system("static_ffprobe -version")

st.set_page_config(page_title="Carga de video")

url_video = st.text_input('URL del video', '')
send_video = st.button('Cargar video')
if send_video:
    #try:
        #file_name = 'trial_video.mp4' 
        #resp = requests.get(url_video) # making requests to server

        #with open(file_name, "wb") as f: # opening a file handler to create new file 
        #    f.write(resp.content)
        video_details.show_metadata(url_video)
        

    #except Exception as e:
    #    st.warning('URL no válida. Intentar de nuevo.', icon="⚠️")
    #    print(e)
