import streamlit as st
from data_processing import *
import streamlit.components.v1 as components

def visualization_page():
    html_temp = "<div class='tableauPlaceholder' id='viz1636791329623' style='position: relative'><noscript><a href='#'><img alt='Dashboard Fix ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ba&#47;bansos2_public&#47;DashboardFix&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='bansos2_public&#47;DashboardFix' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ba&#47;bansos2_public&#47;DashboardFix&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1636791329623');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='2277px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    components.html(html_temp, width=1000, height=1500)


# import streamlit as st
# import pandas as pd
# from matplotlib.figure import Figure
# from main import *
# from data_processing import *

# def visualization_page():

    # st.markdown("tes")
    # df = pd.read_excel("dataset/data_bansos_2021-11-11.xlsx")
    # # FILTERING CATEGORY
    # st.sidebar.header("Filter berdasarkan: ")
    # jenis_kelamin = st.sidebar.multiselect(
    #     "Pilih Jenis Kelamin:",
    #     options = df["JENIS_KELAMIN"].unique(),
    #     default = df["JENIS_KELAMIN"].unique()
    # )

    # label = st.sidebar.multiselect(
    #     "Pilih Label Bansos:",
    #     options = df["LABEL"].unique(),
    #     default = df["LABEL"].unique()
    # )

    # df_selection = df.query(
    #     "JENIS_KELAMIN == @jenis_kelamin & LABEL == @label"
    # )

    # # DATA VISUALIZATION
    # st.title(":bar_chart: eBansos Dashboard")
    # st.markdown("tes")

    # # Jumlah Data
    # total_data = (df_selection["LABEL"] != "" ).sum()
    # avg_usia = round(df_selection["USIA"].mean(), 1)
    # total_penerima = (df_selection["STATUS"] == "AKTIF").sum()

    # left_column, middle_column, right_column = st.columns(3)
    # with left_column:
    #     st.subheader("Jumlah Data:")
    #     st.subheader(f"{total_data} Jiwa")
    # with middle_column:
    #     st.subheader("Rata-Rata Usia Penerima:")
    #     st.subheader(f"{avg_usia} Tahun")
    # with right_column:
        
    #     st.subheader("Jumlah Penerima Aktif:")
    #     st.subheader(f"{total_penerima} Jiwa")

    # st.markdown("---")

    # label_bansos = (
    #     df_selection.groupby(by=["LABEL"]).sum()[["LABEL"]].sort_values(by="LABEL")
    # )

    # fig_label = px.bar(
    #     label_bansos,
    #     x="USIA",
    #     y=label_bansos.index,
    #     orientation="h",
    #     title="<b>Jumlah Penerima berdasarkan Label</b>",
    #     color_discrete_sequence=["#FFBF86"] * len(label_bansos),
    #     template = "plotly_white",
    # )

    # fig_label.update_layout(
    #     plot_bgcolor="rgba(0,0,0,0)",
    #     xaxis=(dict(showgrid=False))
    # )

    # st.plotly_chart(fig_label)