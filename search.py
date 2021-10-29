import streamlit as st
from data_processing import *

def local_css(search):
    with open(filename) as f:
        st.markdown("hm")

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)
