import streamlit as st
import requests
import base64
from streamlit_lottie import st_lottie
from visualization_page import *

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_bansos = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_3P0UlV.json')

lottie_kriteria = load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_0ivllrpx.json')

lottie_problematika = load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_2zo0udtb.json')

lottie_peranan = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_kdivdeom.json')

def information(obj):
    # Layout 1
    row1_1, row1_2 = st.columns((3,2))

    with row1_1:
        st.subheader("Selamat Datang di Platform")
        st.image("images/logo_pandu_detail.png")
        st.write(
            """
            Platform ini merupakan upaya Pemerintah Kota Balikpapan dalam rangka
            menciptakan transparansi, akuntabilitas dan integrasi pelayanan dalam
            pengelolaan bantuan sosial yang bersumber dari Anggaran Pendapatan dan
            Belanja Daerah Kota Balikpapan.

            Sekarang, seluruh lapisan masyarakat dapat melihat daftar penerima yang berhak mendapatkan bansos di Kota Balikpapan:
            """
        )

        if st.button("Lihat Penerima Bantuan Sosial"):
            obj.data = "Visualisasi"
            st.experimental_rerun()

    with row1_2:
        global lottie_bansos
        st_lottie(lottie_bansos, speed=1, height=400, key="awal_bansos")

    # ALUR BANSOS
    st.image("images/alur_bansos.png")

    st.markdown("""<hr style="height:1px;border:none;color:#bbbbbb;background-color:#bbbbbb;" /> """, unsafe_allow_html=True)

    # Layout 3
    row3_1, row3_2 = st.columns((0.2,0.5))

    with row3_1:
        global lottie_kriteria
        st_lottie(lottie_kriteria, speed=0.35, height=200, key="kriteria")

    with row3_2:
        st.subheader("Kriteria Penerima Bantuan Sosial")
        st.markdown(
            """
            1. Diutamakan kepala keluarga
            2. Prioritas awal bagi masyarakat berjenis kelamin laki - laki (tidak menutup kemungkinan untuk perempuan)
            3. Berdomisili di wilayah Kota Balikpapan
            4. Memiliki kelengkapan data yang sesuai dengan database capil
            5. Hanya 1 orang yang bisa mendaftar setiap keluarga
            """
        )

    st.markdown("""<hr style="height:1px;border:none;color:#bbbbbb;background-color:#bbbbbb;" /> """, unsafe_allow_html=True)

    # Layout 4
    row4_1, row4_2 = st.columns((0.8,0.5))

    with row4_1:
        st.subheader("Problematika Data Bansos di Kota Balikpapan")
        st.write(
            """
            1. Data penerima bantuan sosial tidak akurat.
            2. Sumber daya pendukung dalam penyaluran bantuan sosial belum mampu beradaptasi dengan situasi pandemi COVID-19.
            3. Penyaluran bantuan sosial berpotensi terjadinya korupsi.
            4. Pengawasan dalam penyaluran bantuan sosial masih tergolong lemah. 
            """
        )

    with row4_2:
        global lottie_problematika
        st_lottie(lottie_problematika, speed=0.35, height=200, key="problematika")

    st.markdown("""<hr style="height:1px;border:none;color:#bbbbbb;background-color:#bbbbbb;" /> """, unsafe_allow_html=True)

    # Layout 5
    row5_1, row5_2 = st.columns((0.2,0.5))

    with row5_1:
        global lottie_peranan
        st_lottie(lottie_peranan, speed=0.35, height=200, key="peranan")

    with row5_2:
        st.subheader("Peranan Data dalam Penanganan Bansos")
        st.write(
            """
            1. Sebagai pertanggungjawaban dari realisasi sebuah program kerja pemerintah karena bansos berasal dari anggaran APBN.
            2. Sebagai bentuk transparansi dari pemerintah ke masyarakat dalam penyaluran bantuan sosial.
            3. Sebagai bahan evaluasi agar pemerintah kedepannya lebih baik lagi dalam menyelesaikan permasalahan terkait penyaluran bantuan sosial serta mencari solusi bersama dalam menghadapi kendala-kendala yang ada. 
            """
        )

    st.markdown("""<hr style="height:1px;border:none;color:#bbbbbb;background-color:#bbbbbb;" /> """, unsafe_allow_html=True)

    # Layout 6
    row6_1, row6_2, row6_3 = st.columns((2, 0.1, 0.1))

    with row6_1:
        st.subheader("Kesimpulan Platform Pandu - Balikpapan")
        st.write(
            """
            Pandu - Balikpapan merupakan salah satu upaya pemerintah Kota Balikpapan kepada masyarakat dalam mendapatkan informasi mengenai penyaluran bantuan sosial. Adanya platform ini dapat membuat proses pendistribusian bantuan sosial diharapkan dapat menjadi lebih mudah, transparan, dan jelas.
            """
        )
        
    
    with row6_2:
        st.write("")
        
    
    with row6_3:
        st.write("")
        
    
    st.markdown("""<hr style="height:1px;border:none;color:#bbbbbb;background-color:#bbbbbb;" /> """, unsafe_allow_html=True)

    # Layout 7
    st.markdown("<h4 style='text-align: center; color: dark-blue;'>Mitra kami</h4>", unsafe_allow_html=True)
    
    #custom CSS 
    col1, col2 = st.columns(2)
    img1 = "images/logo_balikpapan.png"
    img2 = "images/logo_mka.png"
    st.markdown( f"""
    <style>
        .img_bpp{{
            margin: auto;
            display:block;
            width: 100px ;
            height: 115px;
        }}
        .img_mka{{
            margin: auto;
            display:block;
            margin-top: 15px;
            width: 300px ;
            height: 100px;
        }}
        .capt{{
            margin-top: 5px;
            text-align:center;
            display: block;
        }}
       
    </style>
    """, unsafe_allow_html=True)


    with col1:
        st.markdown(f"""
        <img class="img_bpp" src="data:image/png;base64,{base64.b64encode(open(img1, "rb").read()).decode()}">
        <span class="capt">Kota Balikpapan</span>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <img class="img_mka" src="data:image/png;base64,{base64.b64encode(open(img2, "rb").read()).decode()}">
        <span class="capt">PT. Media Kreasi Abadi</span>
        """, unsafe_allow_html=True)
