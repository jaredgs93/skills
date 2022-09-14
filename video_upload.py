import streamlit as st
import video_details
import os
os.system("apt")
#URL prueba: https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4

st.set_page_config(page_title="Carga de video")

url_video = st.text_input('URL del video', '')
send_video = st.button('Cargar video')
if send_video:
    #try:
        video_details.show_metadata(url_video)
    #except:
        #st.warning('URL no válida. Intentar de nuevo.', icon="⚠️")