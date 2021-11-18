from download import *
from data_processing import *
from download_page import *
from visualization_page import *
from information_page import information
import streamlit as st

def main(obj = ""):
    st.sidebar.title("Menu")
    index = 0
    # st.write(obj.data)
    if obj.data == "Informasi":
        index = 0
    elif obj.data == "Data Bansos":
        index = 1
    elif obj.data == "Visualisasi":
        index = 2
    elif obj.data == "Download":
        index = 3
    menu = ["Informasi", "Data Bansos", "Visualisasi", "Download"]
    choice = st.sidebar.selectbox("Silahkan pilih:", menu, index)
    
    if choice == "Informasi":
        obj.data = "Informasi"
        index = 0
        information(obj)

    elif choice == "Data Bansos":
        obj.data = "Data Bansos"
        index = 1
        st.subheader("Upload Data Bansos")
        data_processing()

    elif choice == "Visualisasi":
        obj.data = "Visualisasi"
        index = 2
        st.subheader("Visualisasi Data")
        visualization_page()

    elif choice == "Download":
        obj.data == "Download"
        index = 3
        st.subheader("Download Data")
        download_page()
    
