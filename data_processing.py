from re import template
import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
from download import *
from datetime import date
import MySQLdb
   
def data_processing():

    # Layout 2
    st.write(
        """
        Sebelum mengunggah data bantuan sosial, alangkah baiknya perlu diperhatikan beberapa syarat dan ketentuan setiap kategori data pada file yang akan diunggah. Syarat dan Ketentuan Dataset yang akan diunggah adalah sebagai berikut:
        """
    )
    st.markdown("1. Tipe File Excel")
    st.markdown("2. Berisi kolom-kolom data sesuai dengan list keterangan data bansos")
    st.markdown("3. Data telah bersih dari anomali, kesalahan kata, dll")
    st.markdown("4. ...")
    st.markdown("##### ** Keterangan Data Bansos dalam E - Bansos: **")

    row2_1, row2_2 = st.columns((1,1))

    with row2_1:
        with st.expander("NIK"):
            st.write("Nomor NIK dari setiap penerima bantuan sosial.")
            
        with st.expander("NO KK"):
            st.write("Nomor Kartu Keluarga dari setiap penerima bantuan sosial.")
        
        with st.expander("NIK CAPIL"):
            st.write("Nomor NIK dari setiap penerima bantuan sosial yang sesuai dengan database dari capil.")
        
        with st.expander("NO KK CAPIL"):
            st.write("Nomor Kartu Keluarga dari setiap penerima bantuan sosial yang sesuai dengan database dari capil.")
        
        with st.expander("NAMA"):
            st.write("Nama lengkap penerima bantuan sosial")
        
        with st.expander("NAMA LENGKAP CAPIL"):
            st.write("Nama lengkap penerima bantuan sosial yang sesuai dengan database dari capil")
        
        with st.expander("KATEGORI"):
            st.write("Kategori pekerjan tiap penerima bantuan sosial")
        
        with st.expander("STATUS"):
            st.write("Status keberadaan tiap penerima bantuan sosial")
        
        with st.expander("OPD PENGAMPU"):
            st.write("Organisasi Perangkat Daerah yang memberikan anggaran kepada penerima bansos, diantaranya ialah:")
            st.write("1. Dinas Sosial")
            st.write("2. DISNAKER")
            st.write("3. DISHUB")
            st.write("4. DKUMKMP")
            st.write("5. DPOP")
        
        with st.expander("TAHAP"):
            st.write("Tahap pengajuan bantuan sosial yang terdiri dari beberapa kategori, seperti:")
            st.write("1. Tahap 1")
            st.write("2. Tahap 2 Aju Iya")
            st.write("3. Tahap 2 Aju Tidak")            
            st.write("4. Tidak")

    with row2_2:
        with st.expander("ALAMAT CAPIL"):
            st.write("Alamat lengkap penerima bantuan sosial di Balikpapan yang sesuai dengan database dari capil")

        with st.expander("KELURAHAN CAPIL"):
            st.write("Data kelurahan penerima bantuan sosial di Balikpapan yang sesuai dengan database dari capil, seperti:")
            st.write("1. Baru Ilir")
            st.write("2. Baru Tengah")
            st.write("3. Baru Ulu")
            st.write("4. Batu Ampar")
            st.write("5. Damai")
            st.write("6. Damai Bahagia")
            st.write("7. Damai Baru")
            st.write("8. Graha Indah")
            st.write("9. Gunung Bahagia")
            st.write("10. Gunung Samarinda")
            st.write("11. Gunung Samarinda Baru")
            st.write("12. Gunung Sari Ilir")
            st.write("13. Gunung Sari Ulu")
            st.write("14. Karang Jati")
            st.write("15. Karang Joang")
            st.write("16. Karang Rejo")
            st.write("17. Kariangau")
            st.write("18. Klandasan Ilir")
            st.write("19. Lamaru")
            st.write("20. Manggar")
            st.write("21. Manggar Baru")
            st.write("22. Marga Sari")
            st.write("23. Margo Mulyo")
            st.write("24. Mekar Sari")
            st.write("25. Muara Rapak")
            st.write("26. Prapatan")
            st.write("27. Sepinggan")
            st.write("28. Sepinggan Baru")
            st.write("29. Sepinggan Raya")
            st.write("30. Sumber Rejo")
            st.write("31. Sungai Nangka")
            st.write("32. Telaga Sari")
            st.write("33. Teritip")
        
        with st.expander("KECAMATAN CAPIL"):
            st.write("Data kecamatan penerima bantuan sosial di Balikpapan yang sesuai dengan database dari capil")
            st.write("1. Balikpapan Barat")
            st.write("2. Balikpapan Kota")
            st.write("3. Balikpapan Selatan")
            st.write("4. Balikpapan Tengah")
            st.write("5. Balikpapan Timur")
            st.write("6. Balikpapan Utara")
        
        with st.expander("DOMISILI"):
            st.write("")
        
        with st.expander("KETERANGAN NIK"):
            st.write("")
        
        with st.expander("JENIS KELAMIN"):
            st.write("Gender tiap penerima bansos")
        
        with st.expander("KETERANGAN NAMA"):
            st.write("")
        
        with st.expander("KETERANGAN NIK DAN KK"):
            st.write("")
        
        with st.expander("USIA"):
            st.write("Rentang usia tiap penerima bansos")
        
        with st.expander("LABEL PENERIMA"):
            st.write("Kategori penerima bansos yang terdiri dari:")
            st.write("1. SANGAT LAYAK")
            st.write("2. LAYAK")
            st.write("3. TIDAK LAYAK")

    st.markdown("""<hr style="height:1px;border:none;color:#bbbbbb;background-color:#bbbbbb;" /> """, unsafe_allow_html=True)

    # DATA PROCESSING
    data_file = st.file_uploader("Upload File Excel", type=["xlsx"])
    
    if data_file is not None:
        # file_details = {"filename":data_file.name, "filetype":data_file.type, "filesize":data_file.size}
        # st.write(file_details)
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

        filename = "tes_download.xlsx"
        download_button_str = download_button(df, filename, f'Unduh disini {filename}', pickle_it=False)
        st.markdown(download_button_str, unsafe_allow_html=True)
        
        return df
        