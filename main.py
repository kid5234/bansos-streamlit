from pandas.core.dtypes import base
from download import *
from data_processing import *
from information_page import *
from download_page import *
from search import *
import streamlit as st
import pandas as pd
import seaborn as sns

def main():
    st.sidebar.title("Menu")
    menu = ["Informasi", "Data Bansos", "Visualisasi", "Download"]
    choice = st.sidebar.selectbox("Silahkan pilih:", menu)

    if choice == "Informasi":
        information()

    elif choice == "Data Bansos":
        st.subheader("Upload Data Bansos")
        # DATA PROCESSING
        data_processing()

    elif choice == "Visualisasi":
        st.subheader("Visualisasi Data")
        visualization_page()

    elif choice == "Download":
        st.subheader("Download Data")
        download_page()

        # DATA VISUALIZATION
        # vis(filename)
