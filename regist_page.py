from venv import create
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import hashlib
import os
    
def regist_page():

    @st.cache(allow_output_mutation=True)
    def get_data():
        return []

    st.write(" ")
    #Generate ID
    id = np.random.randint(100,size=(1))
    username = st.text_input("Masukkan Username")
    gmail = st.text_input("Masukkan Email")
    password = st.text_input("Masukkan Password", type='password')
    repassword = st.text_input("Masukkan Ulang Password", type='password')
    
    if st.button("Daftar"):
        get_data().clear() 
        if len(username)>0 and len(gmail) > 0 and len(password) > 0 and len(repassword) > 0:
            if (repassword == password):   
                md5 = hashlib.md5(password.encode()).hexdigest()
                get_data().append({"Username":username, "Email": gmail, "Password": md5})
                df = pd.DataFrame(get_data())
                if len(df) > 1:
                    st.error("gagal membuat Akun")
                else:
                    st.success("Berhasil membuat Akun")
                    engine = create_engine('mysql+pymysql://'+os.environ['db_username']+':'+os.environ['db_password']+'@'+os.environ['db_host']+'/'+os.environ['db_name'])
                    df.to_sql('admin', con=engine, if_exists='append', index=False)
            else:
                st.error("Password tidak sama")
        else:
            st.error("Ada form kosong")
