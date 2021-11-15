import base64
from pandas.core.indexes import base
import streamlit as st
import os
import base64


from download import download_button

def download_page():
    st.write(" ")
    
    col1, col2, col3 = st.columns(3)
    dir = os.listdir('dataset/')
    
    for file in dir:
        col1.write(file[0:11])
        col2.write(file[12:22])

        b64 = base64.b64encode(file.encode()).decode()
        href = f'<a href="data:file/xlsx;base64,{b64}">Download {file}</a>'
        
        col3.markdown(href, unsafe_allow_html=True)
