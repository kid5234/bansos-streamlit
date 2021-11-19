import base64
from pandas.core.indexes import base
import streamlit as st
import os
import pandas as pd
from download import *
import pandas as pd
from download import download_button
    
def download_page():
    st.write(" ")
    head1, head2, head3 = st.columns(3)
    col1, col2, col3 = st.columns(3)
    
    path = "dataset/"
    os.chdir(path)
    
    head1.markdown("Nama File")
    head2.markdown("Tanggal")
    head3.markdown("Aksi")

    for file in os.listdir():
        
    # Check whether file is in text format or not
       
        custom_css = f"""  
        <style>
            #box{{
                margin: 10px 0px 40px;
            }}
        </style>
        """
        customcol1 = custom_css+f'<p id=box>{file[0:11]}</p>'
        customcol2 = custom_css+f'<p id=box>{file[12:22]}</p>'

        col1.markdown(customcol1, unsafe_allow_html=True)
        col2.markdown(customcol2, unsafe_allow_html=True)
        
        if file.endswith(".xlsx"):
            df = pd.read_excel(file)

            download_button_str = download_button(df, file, f'Unduh File', pickle_it=False)
            col3.markdown(download_button_str, unsafe_allow_html=True)
            
            
    return os.chdir('../')     
            