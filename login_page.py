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

def login_page(obj):
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
                    username = data["Username"]

                    id_str= id.to_string(index=False)
                    username_str = username.to_string(index=False)
                
                    if 'id_str' and 'username_str' and 'status' not in st.session_state:
                        st.session_state['id_str'] = id_str
                        st.session_state['username_str'] = username_str
                        st.session_state['status'] = "admin"
                else:
                    st.error("Data kosong")
            else:
                st.error("Password tidak sama")
        else:
            st.error("Ada form kosong")
    

    
    
