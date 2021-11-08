from pandas.core.dtypes import base
from download import *
from data_processing import *
from search import *
from visualization import *
import streamlit as st
import pandas as pd
import seaborn as sns

def main():
    st.sidebar.title("Menu")
    menu = ["Informasi", "Data Bansos"]
    choice = st.sidebar.selectbox("Silahkan pilih:", menu)

    if choice == "Informasi":
        st.subheader("Informasi")
        information()

    elif choice == "Data Bansos":
        # DATA PROCESSING
        data_processing()

        # DATA VISUALIZATION
        # vis(filename) 

def side_bar_menu():
    st.sidebar.title("Tentang E-Bansos")
    st.sidebar.info(".......")

def information():
    st.markdown("Disini masuk isi konten")
    st.write("disini juga, tapi belum ditata")

