import streamlit as st
from main import *

st.set_page_config(page_title="E-Bansos",
                   page_icon=":moneybag:",
                   layout="wide",
)

st.sidebar.image("images/logo_kampus_merdeka.png", width=None, use_column_width=True)

main()

with st.sidebar.expander("Credits"):
        """
        Platform ini adalah hasil kerja tim kami:
        - [Abdul Ghofur Rais Kumar](https://www.linkedin.com/in/abdul-ghofur-rais-kumar/)
        - [Elok Rina Rahayu](https://www.instagram.com/jea_xinn/)
        - [Fitri Andriyani]()
        - [M. Iqbal Al-Haswan Bisyoe](https://github.com/IQBALE)
        - [Devanis Dwi Sutrisno](https://www.linkedin.com/in/devanis-dwi-sutrisno/)
        
        ### **Contacts**
        [![](https://img.shields.io/badge/GitHub-Follow-informational)](https://github.com/devanisdwi/bansos-streamlit)
        [![](https://img.shields.io/badge/Open-Issue-informational)](mailto:devanisdwis@gmail.com)
        [![MAIL Badge](https://img.shields.io/badge/-devanisdwis@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:devanisdwis@gmail.com)](mailto:devanisdwis@gmail.com)
        
        ##### @ Cosmic Team, 2021

        """

# # ---- HIDE STREAMLIT STYLE ----
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)