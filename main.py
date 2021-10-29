from pandas.core.dtypes import base
from download import *
from data_processing import *
from search import *
from visualization import *
import streamlit as st
import pandas as pd
import seaborn as sns
import io

import os
import base64
import json
import pickle
import uuid
import re

st.set_page_config(page_title="E-Bansos",
                   page_icon=":moneybag:",
                   layout="wide",
)

def main():
    menu = ["Informasi", "Data Bansos"]
    choice = st.sidebar.selectbox("Menu", menu, key = "menu")

    if choice == "Informasi":
        st.subheader("Informasi")
    
    elif choice == "Data Bansos":
        # DATA PROCESSING
        data_processing()
        # if st.button("Visualisasi"):
        #     viz()

        # SEARCHING
        # st.subheader("Pencarian")
        # local_css("style.css")
        # search = st.text_input("", "Search...")
        # button_clicked = st.button("OK")
        # st.subheader("Dataset")

        # DATA VISUALIZATION
        # vis(filename) 

main()

# # ---- HIDE STREAMLIT STYLE ----
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)