import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"hobi: {data_list[i]['hobi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/file/d/11bWo2WlbonpYgqwMSftQ2OnOFsSpiLun/view?usp=drivesdk",
            "https://drive.google.com/file/d/1tkATC2BWNGNfLGm2QT-mK6t20sB4TnNm/view?usp=drivesdk",
            "https://drive.google.com/file/d/1c3ROsPZaYiSM0hXB_VuqINwlS4MFNVaZ/view?usp=drivesdk",
            "https://drive.google.com/file/d/1k_7bdYHxD3XUCsMhtZutHM5jrm4DlOOP/view?usp=drivesdk",
            "https://drive.google.com/file/d/17XdxknS11GLcY5zmixhHKCFmYZ-k5GWi/view?usp=drivesdk",
            "https://drive.google.com/file/d/1p-O1O-AUfT54RMq5v6abicU-3iAuNY3a/view?usp=drivesdk",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Jl. Pulau Damar, Tanjung Senang",
                "hobi": "Kuliah-rapat, dengerin lagu",
                "sosmed": "@gumilangkharisma",
                "kesan": "Menjawab pertanyaan dengan bijak dan tetap berwibawa.",  
                "pesan":"Semoga wisuda tepat waktu yaa bang!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450127",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Bawean 2, Sukarame",
                "hobi": "Main Gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "bang Pandra ternyata suka bercanda tapi tetep menjawab semua pertanyaan dengan baik.",  
                "pesan":"Semangat semester 7 nya bang!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450044",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kak Liza cantik banget, pembawaannya juga menyenangkan",  
                "pesan":"semangaat kuliah kakak cantik!"# 1
            },
            {   "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobi": "Dengerin Bang Pandra main gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kak putri lumayan pendiam walaupun ngga sependiam kak Hartiti xixixi",  
                "pesan":"semangat kuliah kak!"# 1
                    
            },
            {   "nama": "Hartiti Fadilah",
                "nim": "121450021",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrdfdlh",
                "kesan": "kak Hartiti kayanya pendiam dan pemalu gitu tapi tetap seruu",  
                "pesan":"semnagat terus sampai wisuda yaa kak"# 1

            },
            {   "nama": "Nadila Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Gangguin Kak Liza Tidur, bawa Wattpad/AU",
                "sosmed": "@nadillaandr26",
                "kesan": "kak nadila seru karena lumayan banyak bercanda nyaa",  
                "pesan":"semangat kuliahnya kakak!"# 1

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/file/d/1isqVgo0L5Q15GkWiUqBbevDgCacg63Mf/view?usp=drivesdk",
            "https://drive.google.com/file/d/1Vc0pUWuhiaQ-ZLktSClRYKbgNPx9LVrj/view?usp=drivesdk",
            "https://drive.google.com/file/d/1maalzyRfBS9O53vsZ_ex9LJSJVFZQ5Yg/view?usp=drivesdk",
            "https://drive.google.com/file/d/1bSAvJehOzCEW07hUxsCE8gGjd552z_AC/view?usp=drivesdk",
            "https://drive.google.com/file/d/1tZ_SKEzJbuovgFv9N8_kKwsG0hy6-uHh/view?usp=drivesdk",
            "https://drive.google.com/file/d/196zcLVySIFxj7bWw2iH35BaXypApRwRx/view?usp=drivesdk",
            "https://drive.google.com/file/d/14eDsio-DpnQdVgtV85lEuw38suMhvkP4/view?usp=drivesdk",
            "https://drive.google.com/file/d/1JBzfyfC0ycwa2cfiITP5uvXmLpVODWqR/view?usp=drivesdk",
            "https://drive.google.com/file/d/1patICp8Zy8S3ONNypyJ_4yOTIj2P_MDT/view?usp=drivesdk",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di GPT",
                "sosmed": "@trimurniyaa_",
                "kesan": "kak Tri asik, humoris juga suka bercanda",  
                "pesan":"semangat terus kakak cantik!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Wayhuwi",
                "hobi": "Baca buku dan Nonton film.",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kak Nisa baik hati terus asik",  
                "pesan":"semangaat kakak!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Belajar bersama Pak Tamaro.",
                "sosmed": "@wlnsbn0",
                "kesan": "senang bisa melakukan wawancara dengan kakak baleg satu ini",  
                "pesan":"semangaat kakak!"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Ngobrol",
                "sosmed": "@anisadini10",
                "kesan": "kakak yang menyenangkan",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "WayHuwi",
                "hobi": "Makeup, Nonton Podcast, Denger Musik, Gossip.",
                "sosmed": "@berliyyanda",
                "kesan": "kakak baleg yang asik dan menyenangkan!",  
                "pesan":"semangaat semester 5 nya kak!"# 1
            },
            {
                "nama": "Dhea Amelia",
                "nim": "122450004",
                "umur": "20",
                "asal":"Solo",
                "alamat": "Natar",
                "hobi": "suka ditipu akun jual canva di shopee.",
                "sosmed": "@_.dheamelia",
                "kesan": "kakak nya asik suka bercanda",  
                "pesan":"semangat menjalani perkuliahan kak!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drama korea.",
                "sosmed": "@ansftynn_",
                "kesan": "senang bisa kenal kakak karena ternyata kita satu smk dan satu jurusan!",  
                "pesan":"semangat menjalani semester lima kakak erpeelku!"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobi": "melukis, hiking, badminton dan berenang.",
                "sosmed": "@fhrul.pdf",
                "kesan": "abang baleg satu ini lumayan jarang bersuara nii",  
                "pesan":"semangat selalu bang!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Baca Buku.",
                "sosmed": "@fr_yulius",
                "kesan": "bang fery pendiam tapi sering ketawa",  
                "pesan":"semangat semester 5 nya yaa bang!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
