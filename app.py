import streamlit as st
from main import *

st.set_page_config(page_title="E-Bansos",
                   page_icon=":moneybag:",
                   layout="wide",
)

main()
side_bar_menu()

# # ---- HIDE STREAMLIT STYLE ----
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)