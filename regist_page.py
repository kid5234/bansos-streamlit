import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import uuid
import re
    
def regist_page():

    @st.cache(allow_output_mutation=True)
    def get_data():
        return []

    st.write(" ")
    #Generate ID
    id = np.random.randint(100,size=(1))

    gmail = st.text_input("Masukkan Email")
    password = st.text_input("Masukkan Password", type='password')
    repassword = st.text_input("Masukkan Ulang Password", type='password')
    
    if st.button("Daftar"):
        get_data().clear() 
        if len(gmail) > 0 and len(password) > 0 and len(repassword) > 0:
            if (repassword == password):   
                get_data().append({"Id": id[0],"Email": gmail, "Password": password, "RePassword": repassword})
                df = pd.DataFrame(get_data())
                if len(df) > 1:
                    st.error("gagal membuat Akun")
                else:
                    st.success("Berhasil membuat Akun")
                    engine = create_engine('mysql://root:@localhost/db_bansos')
                    df.to_sql('admin', con=engine, if_exists='append', index=False)
            else:
                st.error("Password tidak sama")
        else:
            st.error("Ada form kosong")