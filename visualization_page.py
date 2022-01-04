from typing import Text
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import MySQLdb


def visualization_page():
    # html_temp = "<div class='tableauPlaceholder' id='viz1638766654954' style='position: relative'><noscript><a href='#'><img alt='DStreamlit ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ba&#47;BansosRevisi&#47;DStreamlit&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='BansosRevisi&#47;DStreamlit' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ba&#47;BansosRevisi&#47;DStreamlit&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1638766654954');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='1827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='1827px';} else { vizElement.style.width='100%';vizElement.style.height='3327px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    # components.html(html_temp, width=1000, height=1500)
    
    # try:
    #     conn = create_engine('mysql://root:@localhost/db_bansos')
    # except Exception as error:
    #     print("Error while connecting to MySQL", error)

    # all_bansos = pd.read_sql_query('select * from bansos', conn)
    # all_kecamatan = pd.read_sql_query('select * from kecamatan', conn)
    # all_kelurahan = pd.read_sql_query('select * from kelurahan', conn)

    # st.write("Total Data: ", all_bansos.shape[0])
    # st.write("Total Penerima: ", all_bansos["KET_KK_NIK" == "KK AMAN"].sum())
    # st.write("Total Ditolak: ", )

    conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="db_bansos")
    cursorBansos = conn.cursor()
    cursorBansos.execute('select bansos.nik, bansos.no_kk, bansos.nama, bansos.nik_capil, bansos.no_kk_capil, bansos.nama_lgkp_capil, bansos.status, bansos.kategori, bansos.opd_pengampu, bansos.tahap, bansos.alamat_capil, bansos.kelurahan_capil, bansos.kecamatan_capil, bansos.domisili, bansos.ket_nik, bansos.jenis_kelamin, bansos.ket_nama, bansos.ket_kk_nik, bansos.usia, bansos.label, bansos.date, kelurahan.latitude, kelurahan.longitude  from bansos left join kelurahan on bansos.kelurahan_capil = kelurahan.kelurahan_capil');
    # 'select * from bansos left join kelurahan on bansos.kelurahan_capil = kelurahan.kelurahan_capil'
    rows = cursorBansos.fetchall()
    
    df = pd.DataFrame( [[ij for ij in i] for i in rows] )
    df.rename(columns={0: 'NIK',
                       1: 'NO_KK',
                       2: 'NAMA',
                       3: 'NIK_CAPIL',
                       4: 'NO_KK_CAPIL',
                       5: 'NAMA_LGKP_CAPIL',
                       6: 'STATUS',
                       7: 'KATEGORI',
                       8: 'OPD_PENGAMPU',
                       9: 'TAHAP',
                       10: 'ALAMAT_CAPIL',
                       11: 'KELURAHAN_CAPIL',
                       12: 'KECAMATAN_CAPIL',
                       13: 'DOMISILI',
                       14: 'KET_NIK',
                       15: 'JENIS_KELAMIN',
                       16: 'KET_NAMA',
                       17: 'KET_KK_NIK',
                       18: 'USIA',
                       19: 'LABEL',
                       20: 'DATE',
                       21: 'LATITUDE',
                       22: 'LONGITUDE',}, inplace=True);


    # FILTERING CATEGORY
    st.subheader("Filter berdasarkan: ")

    # ROW FILTER DATE
    row1_1, row1_2, row1_3 = st.columns((1,1,1))

    with row1_1:
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        start_date = st.date_input('Start date', today)

    with row1_2:
        end_date = st.date_input('End date', tomorrow)

    with row1_3:
        if start_date < end_date:
            st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
        else:
            st.error('Error: End date must fall after start date.')

    # ROW FILTER GENERAL
    row2_1, row2_2, row2_3, row2_4 = st.columns((1,1,1,1))
    
    with row2_1:
        with st.expander("LABEL"):
            label = st.multiselect(
                "Pilih Label Bansos:",
                options = df["LABEL"].unique(),
                default = df["LABEL"].unique()
            )

        with st.expander("OPD PENGAMPU"):
            opd_pengampu = st.multiselect(
                "Pilih OPD Pengampu Bansos:",
                options = df["OPD_PENGAMPU"].unique(),
                default = df["OPD_PENGAMPU"].unique()
            )

    with row2_2:
        with st.expander("STATUS"):
            status = st.multiselect(
                "Pilih Status Bansos:",
                options = df["STATUS"].unique(),
                default = df["STATUS"].unique()
            )

        with st.expander("KATEGORI"):
            kategori = st.multiselect(
                "Pilih Kategori Bansos:",
                options = df["KATEGORI"].unique(),
                default = df["KATEGORI"].unique()
            )
        
    with row2_3:
        with st.expander("JENIS KELAMIN"):
            jenis_kelamin = st.multiselect(
                "Pilih Jenis Kelamin:",
                options = df["JENIS_KELAMIN"].unique(),
                default = df["JENIS_KELAMIN"].unique()
            )

        with st.expander("TAHAP"):
            tahap = st.multiselect(
                "Pilih Tahap Bansos:",
                options = df["TAHAP"].unique(),
                default = df["TAHAP"].unique()
            )
    
    with row2_4:
        with st.expander("KECAMATAN_CAPIL"):
            kecamatan_capil = st.multiselect(
                "Pilih Kecamatan:",
                options = df["KECAMATAN_CAPIL"].unique(),
                default = df["KECAMATAN_CAPIL"].unique()
            )

        with st.expander("KELURAHAN_CAPIL"):
            kelurahan_capil = st.multiselect(
                "Pilih Kelurahan:",
                options = df["KELURAHAN_CAPIL"].unique(),
                default = df["KELURAHAN_CAPIL"].unique()
            )

    df_selection = df.query(
        "KECAMATAN_CAPIL == @kecamatan_capil & KELURAHAN_CAPIL == @kelurahan_capil & JENIS_KELAMIN == @jenis_kelamin & LABEL == @label & STATUS == @status & OPD_PENGAMPU == @opd_pengampu & TAHAP == @tahap"
    )

    # Jumlah Data
    total_data = (df_selection["LABEL"] != "" ).sum()
    total_diterima = (df_selection["LABEL"] != "TIDAK LAYAK DAPAT BANSOS").sum()
    total_ditolak = (df_selection["LABEL"] == "TIDAK LAYAK DAPAT BANSOS").sum()

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Total Data:")
        st.subheader(f"{total_data} Jiwa")
    with middle_column:
        st.subheader("Total Diterima:")
        st.subheader(f"{total_diterima} Jiwa")
    with right_column:
        st.subheader("Total Ditolak:")
        st.subheader(f"{total_ditolak} Jiwa")

    st.write("")
    st.markdown("Maps Kecamatan")
   
    dfKelurahan = df_selection[['KELURAHAN_CAPIL', 'LATITUDE', 'LONGITUDE']]
    dfKelurahan = dfKelurahan.value_counts().reset_index()
    dfKelurahan.columns = ['KELURAHAN_CAPIL', 'lat', 'lon', 'count']
    dfKelurahan['text'] = dfKelurahan['KELURAHAN_CAPIL']
    figKelurahan = px.scatter_geo(dfKelurahan, lat='lat', lon='lon', size='count', text=dfKelurahan['text'])
    
    st.plotly_chart(figKelurahan, use_container_width=True)

    row_OPD, row_tahap = st.columns(2)
    with row_OPD:
        dfOPD = df_selection[['OPD_PENGAMPU']]
        dfOPD = dfOPD.fillna('Tidak ada OPD')
        dfOPD = dfOPD.value_counts().reset_index()
        dfOPD.columns = ['OPD_PENGAMPU', 'count']
        figOPD = px.bar(dfOPD, x='OPD_PENGAMPU',
                        y='count', color='count',
                        title='Persebaran Data berdasarkan OPD Pengampu')
        st.plotly_chart(figOPD, use_container_width=True)

    with row_tahap:
        dfTahap = df_selection[['TAHAP']]
        dfTahap = dfTahap.fillna('Tidak Terdeteksi')
        dfTahap = dfTahap.value_counts().reset_index()
        dfTahap.columns = ['TAHAP', 'count']
        figTahap = px.pie(dfTahap, values='count', names='TAHAP', title='Persebaran Data berdasarkan Tahap', hole=0.4)
        st.plotly_chart(figTahap, use_container_width=True)

    
    row_gender_label, row_kategori = st.columns(2)
    with row_gender_label:
        # GENDER
        dfGender = df_selection[['JENIS_KELAMIN']]
        dfGender = dfGender.fillna('Tidak Terdeteksi')
        dfGender = dfGender.value_counts().reset_index()
        dfGender.columns = ['JENIS_KELAMIN', 'count']
        parentGender = []
        for i in range(len(dfGender['JENIS_KELAMIN'].unique())):
            parentGender.append("")
        figGender = px.treemap(dfGender, names=dfGender['JENIS_KELAMIN'].unique(), parents=parentGender, values='count', title='Persebaran Data berdasarkan Jenis Kelamin')
        st.plotly_chart(figGender, use_container_width=True)

    with row_kategori:
        # LABEL
        dfLabel = df_selection[['LABEL']]
        dfLabel = dfLabel.fillna('Tidak Terdeteksi')
        dfLabel = dfLabel.value_counts().reset_index()
        dfLabel.columns = ['LABEL', 'count']
        parentLabel = []
        for i in range(len(dfLabel['LABEL'].unique())):
            parentLabel.append("")
        figLabel = px.treemap(dfLabel, names=dfLabel['LABEL'].unique(), parents=parentLabel, values='count', title='Persebaran Data berdasarkan Label')
        st.plotly_chart(figLabel, use_container_width=True)
    
    # PIVOT TABLE KATEGORI
    dfKategori = df_selection[['KATEGORI', 'LABEL']]
    dfKategori = dfKategori.fillna('Tidak ada KATEGORI')
    dfKategori = dfKategori.value_counts().reset_index()
    dfKategori.columns = ['KATEGORI', 'LABEL', 'JUMLAH']
    dfKategori = pd.pivot_table(data = dfKategori, index=['KATEGORI'], columns=['LABEL'], values=['JUMLAH'])
    st.dataframe(dfKategori)

    
    # STATUS
    dfStatus = df_selection[['STATUS']]
    dfStatus = dfStatus.fillna('Tidak Terdeteksi')
    dfStatus = dfStatus.value_counts().reset_index()
    dfStatus.columns = ['STATUS', 'count']
    figStatus = px.bar(dfStatus, x='count',
                    y='STATUS', color='STATUS', orientation='h',
                    title='Persebaran Data berdasarkan Status')
    st.plotly_chart(figStatus, use_container_width=True)


    # USIA DAN GENDER
    dfUsia = df_selection[['USIA', 'JENIS_KELAMIN']]
    # dfUsia = dfUsia.fillna('Tidak Terdeteksi')
    dfUsia = dfUsia.value_counts().reset_index()
    dfUsia.columns = ['USIA', 'JENIS KELAMIN', 'JUMLAH']
    dfUsia = dfUsia.sort_values(by = 'USIA')
    # st.dataframe(dfUsia)
    figUsia = px.line(dfUsia, x='USIA', y='JUMLAH', color='JENIS KELAMIN', symbol="JENIS KELAMIN")
    st.plotly_chart(figUsia, use_container_width=True)



