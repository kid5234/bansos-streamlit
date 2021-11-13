import streamlit as st
import pandas as pd
import urllib.request
import requests
from datetime import date
from pandas import json_normalize
from streamlit_lottie import st_lottie
from visualization_page import *

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_bansos = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_3P0UlV.json')

def information():
    # Layout 1
    row1_1, row1_2 = st.columns((3,2))

    with row1_1:
        st.header("Selamat Datang di Platform")
        st.title("E - Bansos Kota Balikpapan")
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
            visualization_page()
    
    with row1_2:
        global lottie_bansos
        st_lottie(lottie_bansos, speed=1, height=400, key="initial")

    st.markdown("""<hr style="height:1px;border:none;color:#bbbbbb;background-color:#bbbbbb;" /> """, unsafe_allow_html=True)
    
    # Layout 2
    st.header("Keterangan Data Bansos dalam E - Bansos")

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

    # Layout 3
    row3_1, row3_2 = st.columns((1,1))

    with row3_1:
        st.subheader("Alur Pemberian Bantuan Sosial")
        st.markdown(
            """
            gimana ya?
            """
        )

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
    row4_1, row4_2, row4_3 = st.columns((1, 1, 1))

    with row4_1:
        st.subheader("Permasalahan Data Bansos di Kota Balikpapan")
        st.write(
            """
            1. Data penerima bantuan sosial tidak akurat.
            2. Sumber daya pendukung dalam penyaluran bantuan sosial belum mampu beradaptasi dengan situasi pandemi COVID-19.
            3. Penyaluran bantuan sosial berpotensi terjadinya korupsi.
            4. Pengawasan dalam penyaluran bantuan sosial masih tergolong lemah. 
            """
        )
    
    with row4_2:
        st.subheader("Peranan Data dalam Penanganan Bansos")
        st.write(
            """
            1. Sebagai pertanggungjawaban dari realisasi sebuah program kerja pemerintah karena bansos berasal dari anggaran APBN.
            2. Sebagai bentuk transparansi dari pemerintah ke masyarakat dalam penyaluran bantuan sosial.
            3. Sebagai bahan evaluasi agar pemerintah kedepannya lebih baik lagi dalam menyelesaikan permasalahan terkait penyaluran bantuan sosial serta mencari solusi bersama dalam menghadapi kendala-kendala yang ada. 
            """
        )
    
    with row4_3:
        st.subheader("Kesimpulan E - Bansos")
        st.write(
            """
            E - Bansos merupakan salah satu upaya pemerintah Kota Balikpapan kepada masyarakat dalam mendapatkan informasi mengenai penyaluran bantuan sosial. Dengan adanya e-bansos proses pendistribusian bantuan sosial diharapkan dapat menjadi lebih mudah, transparan, dan jelas.
            """
        )
    
    st.markdown("""<hr style="height:1px;border:none;color:#bbbbbb;background-color:#bbbbbb;" /> """, unsafe_allow_html=True)

    # Layout 5
    st.markdown("<h1 style='text-align: center; color: dark-blue;'>Supported By:</h1>", unsafe_allow_html=True)
    
    row5_1, row5_2, row5_3, row5_4, row5_5 = st.columns((2,1,0.5,0.7,2))

    with row5_1:
        st.markdown("")
    
    with row5_2:
        st.image("images/logo_mka.png", width=None)

    with row5_3:
        st.image("images/logo_balikpapan.png", width=None)
    
    with row5_4:
        st.image("images/logo_kampus_merdeka.png", width=None)
    
    with row5_5:
        st.markdown("")
        
    