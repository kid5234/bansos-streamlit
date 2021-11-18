from download import *
from data_processing import *
from download_page import *
from visualization_page import *
from information_page import information
import streamlit as st

def main(choice):
    st.sidebar.title("Menu")
    menu = ["Informasi", "Upload Data Bansos", "Visualisasi", "Download Data Bansos"]
    choice = st.sidebar.selectbox("Silahkan pilih:", menu)

    if choice == "Informasi":
        information()

    elif choice == "Upload Data Bansos":
        st.subheader("Upload Data Bansos")
        data_processing()

    elif choice == "Visualisasi":
        st.subheader("Visualisasi Data")
        visualization_page()

    elif choice == "Download Data Bansos":
        st.subheader("Download Data")
        download_page()

    return choice