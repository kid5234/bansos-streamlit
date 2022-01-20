from base64 import encode
import base64
import dbm
from git import base
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, engine 
import hashlib
import os

def query(gmail, passhash):
    db_connection_str = 'mysql+pymysql://'+os.environ['db_username']+':'+os.environ['db_password']+'@'+os.environ['db_host']+'/'+os.environ['db_name']
    db_connection = create_engine(db_connection_str)
    query = 'SELECT * FROM admin WHERE Email="{}" AND Password="{}"'.format(gmail, passhash)
    df = pd.read_sql(query, con=db_connection)
    return df

def login_page(obj):
    st.write(" ")
    gmail = st.text_input("Masukkan Email")
    password = st.text_input("Masukkan Password", type='password')
 
    if st.button("Login"):
        if len(gmail) > 0 and len(password) > 0:
            passhash = hashlib.md5(password.encode()).hexdigest()
            data = query(gmail, passhash)
            if len(data)>0:
                st.success("berhasil")
                id = data["Id"]
                username = data["Username"]

                id_str= id.to_string(index=False)
                username_str = username.to_string(index=False)
            
                if 'id_str' and 'username_str' and 'status' not in st.session_state:
                    st.session_state['id_str'] = id_str
                    st.session_state['username_str'] = username_str
                    st.session_state['status'] = "admin"
                
                obj.data = "Informasi"
                st.experimental_rerun()
            else:
                st.error("Data kosong")   
        else:
            st.error("Ada form kosong")
    
            

    

    
    
