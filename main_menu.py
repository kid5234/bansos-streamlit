from download import *
from data_processing import *
from download_page import *
from visualization_page import *
from information_page import information
import streamlit as st

def main(obj = ""):
    st.sidebar.title("Menu")
    index = 0

    if obj.data == "Informasi":
        index = 0
    elif obj.data == "Unggah":
        index = 1
    elif obj.data == "Visualisasi":
        index = 2
    elif obj.data == "Unduh":
        index = 3
    menu = ["Informasi", "Unggah", "Visualisasi", "Unduh"]
    choice = st.sidebar.selectbox("Silahkan pilih:", menu, index)
    
    if choice == "Informasi":
        obj.data = "Informasi"
        index = 0
        information(obj)

    elif choice == "Unggah":
        obj.data = "Unggah"
        index = 1
        st.subheader("Unggah Data Bantuan Sosial - Kota Balikpapan")
        data_processing()

    elif choice == "Visualisasi":
        obj.data = "Visualisasi"
        index = 2
        st.subheader("Visualisasi Data Bantuan Sosial - Kota Balikpapan")
        visualization_page()

    elif choice == "Unduh":
        obj.data == "Unduh"
        index = 3
        st.subheader("Unduh Data Bantuan Sosial - Kota Balikpapan")
        download_page()
    
