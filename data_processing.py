from re import template
import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
from download import *
from datetime import date

def data_processing():

    # DATA PROCESSING
    data_file = st.file_uploader("Upload File Excel", type=["xlsx"])
    
    if data_file is not None:
        df = pd.read_excel(data_file)
        df['NIK_CAPIL'] = df['NIK_CAPIL'].astype(str)
        df['NO_KK_CAPIL'] = df['NO_KK_CAPIL'].astype(str)
        df['NIK_CAPIL'] = df['NIK_CAPIL'].str.split(".").str[0]
        df['NO_KK_CAPIL'] = df['NO_KK_CAPIL'].str.split(".").str[0]
        df['USIA'] = df['USIA'].astype('Int64')
        st.dataframe(df)

        st.write("")

        tempLabel = []

        for x in range(0, len(df['NAMA'])):
            if df['NIK'].loc[x] != '' and df['NO_KK'].loc[x] != '' and df['NAMA'].loc[x] != '' and df['NIK_CAPIL'].loc[x] != ''and df['NO_KK_CAPIL'].loc[x] != '' and df['NAMA_LGKP_CAPIL'].loc[x] != '' and df['OPD_PENGAMPU'].loc[x] != '' and df['DOMISILI'].loc[x] == 'Dalam Daerah' and df['KET_NIK'].loc[x] == 'NIK SAMA' and df['KET_NAMA'].loc[x] == 'NAMA SAMA' and df['KET_KK_NIK'].loc[x] == 'KK AMAN' and df['JENIS_KELAMIN'].loc[x] == 'L':
                tempLabel.append('SANGAT LAYAK DAPAT BANSOS')
            elif df['NIK'].loc[x] != '' and df['NO_KK'].loc[x] != '' and df['NAMA'].loc[x] != '' and df['NIK_CAPIL'].loc[x] != '' and df['NO_KK_CAPIL'].loc[x] != '' and df['NAMA_LGKP_CAPIL'].loc[x] != '' and df['OPD_PENGAMPU'].loc[x] != '' and df['DOMISILI'].loc[x] == 'Dalam Daerah' and df['KET_NIK'].loc[x] == 'NIK SAMA' and df['KET_NAMA'].loc[x] == 'NAMA SAMA' and df['KET_KK_NIK'].loc[x] == 'KK AMAN':
                tempLabel.append('LAYAK DAPAT BANSOS')
            else:
                tempLabel.append('TIDAK LAYAK DAPAT BANSOS')

        df.insert(19, "LABEL", tempLabel)

        date_now = []
        today = date.today()

        for i in range(0, len(df['NIK'])):
            date_now.append(today)

        df.insert(20, "DATE", date_now)

        st.dataframe(df.head())

        #AUTO SAVE INTO LOCAL DIRECTORY
        savetodir = "dataset/data_bansos_"+today.strftime("%Y-%m-%d")+".xlsx"
        df.to_excel(savetodir, sheet_name="databansos")

        # IMPORT DATAFRAME INTO MySQL
        engine = create_engine('mysql://root:@localhost/db_bansos')
        df.to_sql('bansos', con=engine, if_exists='append', index=False)

        filename = "bansos_download_"+today.strftime("%Y-%m-%d")+".xlsx"
        download_button_str = download_button(df, filename, f'Unduh disini {filename}', pickle_it=False)
        st.markdown(download_button_str, unsafe_allow_html=True)