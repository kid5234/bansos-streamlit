import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, engine 


def query(gmail, password):
    rootpassword=""
    db_connection_str = 'mysql+pymysql://root:'+rootpassword+'@localhost/db_bansos'
    db_connection = create_engine(db_connection_str)
    query = 'SELECT * FROM admin WHERE Email="{}" AND Password="{}"'.format(gmail, password)
    df = pd.read_sql(query, con=db_connection)
    return df

def get_data(id, gmail):
    return id, gmail


def login_page():
    st.write(" ")

    gmail = st.text_input("Masukkan Email")
    password = st.text_input("Masukkan Password", type='password')
    repassword = st.text_input("Masukkan Ulang Password", type='password')

    if st.button("Login"):
        if len(gmail) > 0 and len(password) > 0 and len(repassword) > 0:
            if (repassword == password):   
                data = query(gmail, password)
                if len(data)>0:
                    st.success("berhasil")
                    id = data["Id"]
                    gmail = data["Email"]

                    id_str= id.to_string(index=False)
                    gmail_str = gmail.to_string(index=False)
                    
                    get_data(id_str, gmail_str)
                else:
                    st.error("Data kosong")
            else:
                st.error("Password tidak sama")
        else:
            st.error("Ada form kosong")
    

    
    
