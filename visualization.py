import streamlit as st
import pandas as pd
from matplotlib.figure import Figure
from main import *
from data_processing import *

def viz():
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
        df_selection.groupby(by=["LABEL"]).sum()[["LABEL"]].sort_values(by="LABEL")
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

    st.plotly_chart(fig_label)