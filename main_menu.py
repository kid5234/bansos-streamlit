from numpy import empty
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
    
    if 'status' not in st.session_state:
        status = "guest"
    else:
        status = st.session_state.status

    index = 0

    if obj.data == "Informasi":
        index = 0
    elif obj.data == "Visualisasi":
        index = 1
    elif obj.data == "Unggah":
        index = 2
    elif obj.data == "Unduh":
        index = 3
    elif obj.data == "Tambah Admin":
        index = 4
    elif obj.data == "Login":
        index = 5
    elif obj.data == "Logout":
        index = 6
   
    menu = ["Informasi", "Visualisasi"]

    if status != "admin":
        menu.append("Login")
    
    elif status == "admin":
        str = "Selamat datang "+st.session_state.username_str
        st.sidebar.write(str)
        
        menu.append("Unggah")
        menu.append("Unduh")
        menu.append("Tambah Admin")
        menu.append("Logout")
        st.write(menu)

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
    
    elif choice == "Unggah":
        obj.data = "Unggah"
        index = 2
        st.subheader("Unggah Data Bantuan Sosial - Kota Balikpapan")
        data_processing()

    elif choice == "Unduh":
        obj.data == "Unduh"
        index = 3
        st.subheader("Unduh Data Bantuan Sosial - Kota Balikpapan")
        download_page()

    elif choice == "Tambah Admin":
        obj.data == "Tambah Admin"
        index = 4
        st.subheader("Tambah Admin ")
        regist_page()

    elif choice == "Login":
        obj.data == "Login"
        index = 5
        st.subheader("Login Admin")
        login_page(obj)
    
   
    elif choice == "Logout":
        obj.data == "Logout"
        index = 6
        del st.session_state.id_str
        del st.session_state.username_str
        del st.session_state.status
        information(obj)