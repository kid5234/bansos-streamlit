from download import *
from data_processing import *
from download_page import *
from visualization_page import *
from information_page import information
from regist_page import *
from login_page import *
import streamlit as st

def main(obj = ""):
    st.sidebar.title("Menu")
    
    # data = get_data()
    
    status = "admin"
    nama = "iqbal"

    index = 0

    if obj.data == "Informasi":
        index = 0
    elif obj.data == "Visualisasi":
        index = 1
    elif obj.data == "Login":
        index = 2
    elif obj.data == "Registrasi":
        index = 3
    elif obj.data == "Unggah":
        index = 4
    elif obj.data == "Unduh":
        index = 5
   
    if status != "admin":
        st.sidebar.write("bukan admin")
        menu = ["Informasi", "Visualisasi", "Login", "Registrasi"]
        choice = st.sidebar.selectbox("Silahkan pilih:", menu, index)
    
    elif status == "admin":
        str = "admin "+nama
        st.sidebar.write(str)

        menu = ["Informasi", "Visualisasi", "Login", "Registrasi"]
        menu.append("Unggah")
        menu.append("Unduh")
        choice = st.sidebar.selectbox("Silahkan pilih:", menu, index)
    
    
    if choice == "Informasi":
        obj.data = "Informasi"
        index = 0
        information(obj)

    elif choice == "Visualisasi":
        obj.data = "Visualisasi"
        index = 1
        st.subheader("Visualisasi Data Bantuan Sosial - Kota Balikpapan")
        visualization_page()

    elif choice == "Login":
        obj.data == "Login"
        index = 2
        st.subheader("Login Admin")
        login_page()
    
    elif choice == "Registrasi":
        obj.data == "Registrasi"
        index = 3
        st.subheader("Registrasi Admin ")
        regist_page()
    
    elif choice == "Unggah":
        obj.data = "Unggah"
        index = 4
        st.subheader("Unggah Data Bantuan Sosial - Kota Balikpapan")
        data_processing()
    elif choice == "Unduh":
        obj.data == "Unduh"
        index = 5
        st.subheader("Unduh Data Bantuan Sosial - Kota Balikpapan")
        download_page()
