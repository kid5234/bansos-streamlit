from pandas.core.dtypes import base
from download import *
from data_processing import *
from information_page import *
from download_page import *
from search import *
from visualization import *
import streamlit as st
import pandas as pd
import seaborn as sns

def main():
    st.sidebar.title("Menu")
    menu = ["Informasi", "Data Bansos", "Download"]
    choice = st.sidebar.selectbox("Silahkan pilih:", menu)

    if choice == "Informasi":
        st.subheader("Informasi")
        information()

    elif choice == "Data Bansos":
        st.subheader("Upload Data Bansos")
        # DATA PROCESSING
        data_processing()
    elif choice == "Download":
        st.subheader("Download Data")
        download_page()

        # DATA VISUALIZATION
        # vis(filename) 

def side_bar_menu():
    st.sidebar.title("Tentang E-Bansos")
    st.sidebar.info("...")



