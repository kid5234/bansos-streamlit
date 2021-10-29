from re import template
import streamlit as st
import pandas as pd
import plotly.express as px
from download import *

def data_processing():

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

        st.dataframe(df.head())

        st.write("")

        filename = "tes_download.xlsx"
        download_button_str = download_button(df, filename, f'Unduh disini {filename}', pickle_it=False)
        st.markdown(download_button_str, unsafe_allow_html=True)

        # FILTERING CATEGORY
        st.sidebar.header("Filter berdasarkan: ")
        jenis_kelamin = st.sidebar.multiselect(
            "Pilih Jenis Kelamin:",
            options = df["JENIS_KELAMIN"].unique(),
            default = df["JENIS_KELAMIN"].unique()
        )

        label = st.sidebar.multiselect(
            "Pilih Label Bansos:",
            options = df["LABEL"].unique(),
            default = df["LABEL"].unique()
        )

        df_selection = df.query(
            "JENIS_KELAMIN == @jenis_kelamin & LABEL == @label"
        )

        # DATA VISUALIZATION
        st.title(":bar_chart: eBansos Dashboard")
        st.markdown("tes")

        # Jumlah Data
        total_data = (df_selection["LABEL"] != "" ).sum()
        avg_usia = round(df_selection["USIA"].mean(), 1)
        total_penerima = (df_selection["STATUS"] == "AKTIF").sum()

        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("Jumlah Data:")
            st.subheader(f"{total_data} Jiwa")
        with middle_column:
            st.subheader("Rata-Rata Usia Penerima:")
            st.subheader(f"{avg_usia} Tahun")
        with right_column:
            
            st.subheader("Jumlah Penerima Aktif:")
            st.subheader(f"{total_penerima} Jiwa")

        st.markdown("---")

        label_bansos = (
            df_selection.groupby(by=["LABEL"]).sum()[["USIA"]].sort_values(by="USIA")
        )

        fig_label = px.bar(
            label_bansos,
            x="USIA",
            y=label_bansos.index,
            orientation="h",
            title="<b>Jumlah Penerima berdasarkan Label</b>",
            color_discrete_sequence=["#FFBF86"] * len(label_bansos),
            template = "plotly_white",
        )

        fig_label.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )

        label_bansos2 = (
            df_selection.groupby(by=["LABEL"]).sum()[["USIA"]].sort_values(by="USIA")
        )

        fig_label2 = px.bar(
            label_bansos2,
            x="USIA",
            y=label_bansos2.index,
            title="<b>Jumlah Penerima berdasarkan Label</b>",
            color_discrete_sequence=["#FFBF86"] * len(label_bansos2),
            template = "plotly_white",
        )

        fig_label2.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(tickmode="linear")),
            yaxis=(dict(showgrid=False))
        )

        left_column, right_column = st.columns(2)
        left_column.plotly_chart(fig_label, use_container_width=True)
        right_column.plotly_chart(fig_label2, use_container_width=True)