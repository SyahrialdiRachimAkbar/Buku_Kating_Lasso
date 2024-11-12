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
            "Departmen MEDKRAF",
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
            "https://drive.google.com/uc?export=view&id=19UZ_iHV59XyLN4bpDKUI1GLMNJO0Ppmk",
            "https://drive.google.com/uc?export=view&id=10B3ZywV2ENhrEmtczxZrsTKaW9Zm1kID",
            "https://drive.google.com/uc?export=view&id=19__LPBOiVuLXdHLr1_u_IRGx7KIPNJ_s",
            "https://drive.google.com/uc?export=view&id=104Ej5adJttkJyWmVwpWLSmVxC872GmUl",
            "https://drive.google.com/uc?export=view&id=18D8fsCKlVWGJGKUd2dOA2MVKL-qsXvyN",
            "https://drive.google.com/uc?export=view&id=18Ko5r8zC3Tox1KPWjhtTcpxnJYGlvC7U",


        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Kura - Kura dan Mendengarkan Musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Abang nya baik dan seru",  
                "pesan":"semangat bang"# 1
            },
            {
                "nama": "Pandra Insani Putra Adwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame Bawean Dua",
                "hobi": "Gitaran",
                "sosmed": "@pndrinsni",
                "kesan": "Abangnya baik",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak nya baik banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobi": "Dengerin Bang Pandra main gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak nya baik",  
                "pesan":"semangat terus kakak !!!"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450021",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrdfdlh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Gangguin Kak Liza Tidur, bawa Wattpad/AU",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakak nya baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12TDvKnyB0wK6AT8J_UpjPk-OQsx4V4QT",
            "https://drive.google.com/uc?export=view&id=12K0p_mBIqgUFIdsAiTCfrAvfpy_IYWxp",
            "https://drive.google.com/uc?export=view&id=12KYfO4aaIaWGs2LHDe1xk5frLsIqlPbi",
            "https://drive.google.com/uc?export=view&id=12NnXkSmGATPlgRF5BeF_edY0gSgf-9-d",
            "https://drive.google.com/uc?export=view&id=12Hu6xjdqblwnYnU5mNLCVwPLXXELyfmH",
            "https://drive.google.com/uc?export=view&id=12uZ1GzrTtdkCPcDNQxb0y8VMjkX3BGoB",
            "https://drive.google.com/uc?export=view&id=12nIX0slO-ZtEcI0aZErl-V7s2Bzspkl3",
            "https://drive.google.com/uc?export=view&id=12WqZjcYOcaCH3eLCZ5QSjPRVx-U7fR1S",
            "https://drive.google.com/uc?export=view&id=12mTV9Y4HRZv-_gk_15VQmw6qUUtBKorF",
         ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450033",
                "umur": "21 ",
                "asal":"Bogor ",
                "alamat": "Raden Saleh ",
                "hobi": "Searching GPT ",
                "sosmed": "@Trimurniyaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114 ",
                "umur": "21 ",
                "asal":"Tangsel ",
                "alamat": "Way Hui ",
                "hobi": "Baca buku & nonton film ",
                "sosmed": "@wlnsbn0",
                "kesan": "Belajar bersama pak tamaro",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 2
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081 ",
                "umur": "20 ",
                "asal":"Tangerang ",
                "alamat": "Jati Agung ",
                "hobi": "Ngobrol ",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 3
            },
            {

                "nama": "Wulan Sabina",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 5
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 6
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumsel",
                "alamat": "Waykandis",
                "hobi": "baca buku",
                "sosmed": "@fr_yulius",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 7
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Solo ",
                "alamat": "Natar ",
                "hobi": "Suka ditipu jual akun canva di shoope ",
                "sosmed": "@dheamelia",
                "kesan": "Kakaknya asik banget ",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 8
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156 ",
                "umur": "22 ",
                "asal":"Surakarta Jateng ",
                "alamat": "Sukarame ",
                "hobi": "Badminton, berenang, hiking, dan melukis ",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 9
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "12200065 ",
                "umur": "20 ",
                "asal":"Sumbar ",
                "alamat": "Way hui",
                "hobi": "makeup, nonton podcast, dan denger musik ",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 10
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@fleurnsh",
                "kesan": " ",
                "pesan": "Semangat terus kuliahnya ya kak! Semangat Semangat Semangat !!!"# 11
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobi": "",
                "sosmed": "@dylebee",
                "kesan": "",
                "pesan": "Semangat terus kuliahnya ya kak! Semangat semangat semangat !!!"# 12
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobi": "",
                "Sosmed": "@myrrinn",
                "kesan": "",
                "pesan": "Semangat terus kuliahnya ya bang! Semangat semangat semangat !!!"# 13
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "",
                "sosimed": "@jeremia_s_",
                "kesan": "Bang jere baik banget, suka bikin panik anak orang, senyumnya manis",
                "pesan": "Semangat terus kuliahnya bang jeree! Semangat semangat semangat !!!"# 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12HYevK7NdYgT3L10Hp8w4pD2_lzh7Qe3",
            "https://drive.google.com/uc?export=view&id=12BXxIDUtlEVzONPjXIfFEEHFhddQfqH-",
        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobi": "Bernyani",
                "sosmed": "@anissaluthfi_",
                "kesan": "Kakak nya baik",  
                "pesan": "Semangat terus kak kuliahnya"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan kota baru",
                "hobi": "Dengerin Ka Luthfi bernyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "abang nyha baik",  
                "pesan": "Semangatt kuliahnya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg econ
            "https://drive.google.com/uc?export=view&id=19QtrmhfbnkJ0jrr99xUsN55hQ9_PlAFF", # ka abet
            "https://drive.google.com/uc?export=view&id=19a60c--2C6FNLdxuyzLUtKDuSHY4marU", # ka pipah
            "https://drive.google.com/uc?export=view&id=10K4AP0IAQ-CxpSB3b6OkKHscjR_qOCfk", # ka allya
            "https://drive.google.com/uc?export=view&id=10emB0I864FfHzfk2h_5keeFMK00BDDPz", # ka eksanty
            "https://drive.google.com/uc?export=view&id=10biVf1F6rB_GyHc5I3pKPLpgHKVfVyGu", # ka hanum
            "https://drive.google.com/uc?export=view&id=10UQmKhUEUejmj1se868DiBT9464v1O37", # bg ferdy 
            "https://drive.google.com/uc?export=view&id=1105lryHiM7AdCSGsFrIYbWuQCU78l-jp", # bg deri 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka okta 
            "https://drive.google.com/uc?export=view&id=111AMN1boLxi1JW7u0M3NVpJ5fsNvofBP", # bg deyvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg ibnu farhan blm
            "https://drive.google.com/uc?export=view&id=11405CX4cTD9obkfM4xQEPeeuYBw5KK-J", # bg jo
            "https://drive.google.com/uc?export=view&id=11EDGnCtcTY3eQj4NkHMi9_WydDzBSw2I", # bg kemas
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg leon blm
            "https://drive.google.com/uc?export=view&id=19vtDHOk4RKna8GxjHOAIxIGM-ec05hsP", # ka presilia
            "https://drive.google.com/uc?export=view&id=1155cVInNcRloz_dC-exBqOcJsGz_YDjW", # ka aqila
            "https://drive.google.com/uc?export=view&id=113StsZUVOaVMBnbO2TgwIdmWWE8J9qc8", # bg sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka vanes blm
            "https://drive.google.com/uc?export=view&id=11bIE2zu1Iu9CWltKLjVvCumpwrBy7c-2", # bg ateng
            "https://drive.google.com/uc?export=view&id=19vkfXTsEI3r1p7X67frdINhydyuHLLAD", # bg gede
            "https://drive.google.com/uc?export=view&id=11I9LcjNiGAL_q5upDzGyb0HyqH_kqGoV", # ka jaclin
            "https://drive.google.com/uc?export=view&id=19kpucvshcZsjogj9Zx58CdU9P9T1FMxh", # bg rafly
            "https://drive.google.com/uc?export=view&id=1tBo015pxH4N8o3rNk-Iupet4c120ATy_", # ka syalaisha dini blm
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Khobam",
                "hobi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "abang nya baik",  
                "pesan": "Semangatt kuliahnya bang" # 1
            },
            {
                "nama": "Celisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "kakak nya baik",  
                "pesan":"semangat kuliahnya kak" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakak nya baik",  
                "pesan":"semangat kuliahnya kak" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": "kakak nya baik",  
                "pesan":"semangat kuliahnya kak" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakak nya baik",  
                "pesan": "semangat kuliahnya kak" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakak nya baik",  
                "pesan": "semangat kuliahnya kak" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "kakak nya baik",  
                "pesan": "semangat kuliahnya kak" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": "kakak nya baik",  
                "pesan": "semangat kuliahnya bang" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "kakak nya baik",  
                "pesan": "semangat kuliahnya kak" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "kakak nya baik",  
                "pesan": "semangat kuliahnya kak" # 10
            },
            {
                "nama": "Ibnu Farhan Al-Ghifari",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "@",
                "kesan": " ",  
                "pesan": "semangat kuliahnya bang" # 11
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan lapas",
                "hobi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": "abang nya baik",  
                "pesan": "semangat kuliahnya bang" # 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": "abang nya baik",  
                "pesan": "semangat kuliahnya bang" # 13
            },
            {
                "nama": "Leonard Andreas Napitupulu",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "@ ",
                "kesan": "abang nya baik",  
                "pesan":"semangat kuliahnya bang" # 14
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobi": "Dengar JPP worship",
                "sosmed": "@presiliamg",
                "kesan": "kakak nya baik",  
                "pesan": "semangat kuliahnya kak" #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "kakak nya baik",  
                "pesan": "semangat kuliahnya kak" # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "abang nya baik",  
                "pesan": "semangat kuliahnya bang" # 17
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "@",
                "kesan": "kakak nya baik",  
                "pesan": "semangat kuliahnya kak" # 18
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abang nya baik",  
                "pesan": "semangat kuliahnya bang" # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "abang nya baik",  
                "pesan": "semangat kuliahnya bang" # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "kakak nya baik",  
                "pesan": "semangat kuliahnya kak" # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abang nya baik",  
                "pesan": "semangat kuliahnya bang" # 22
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "@",
                "kesan": "abang nya baik",  
                "pesan": "semangat kuliahnya bang" # 23
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen Eksternal":
    def departemen_eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15lIJ2YaoG52YW7B99HvP_zDdgokMzQzG", #yogi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ramadita blmm
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #nazwa blm
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bastian blm
            "https://drive.google.com/uc?export=view&id=17kxhBfowNdU6HSYGyqONr4vhIeHHtESU", #dea
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #rohanauli blm
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #natasya blm
            "https://drive.google.com/uc?export=view&id=17kwOZOBMSsbm2Sr1S9pbxs2KZ-IZUl9V", #novelia
            "https://drive.google.com/uc?export=view&id=16ClPGsT7lTt3zcr0t-4Y-Pjw6LtPwqdC", #jasmin
            "https://drive.google.com/uc?export=view&id=17lp5w8DJW1nTRLru51WX9tixCId5I0hI", #tobias
            "https://drive.google.com/uc?export=view&id=17xvND4RA8jSEKLaUCXRJwhXDbjLdpaxz", #yohana
            "https://drive.google.com/uc?export=view&id=16ClPGsT7lTt3zcr0t-4Y-Pjw6LtPwqdC", #riszi
            "https://drive.google.com/uc?export=view&id=17k7gOLZf2Te8AuuSe2JO765EJ72cKiCw", #arafi
            "https://drive.google.com/uc?export=view&id=19dKKBDuN7wFF3oCiCU3A7POjWeuZJHmY", #asa
            "https://drive.google.com/uc?export=view&id=15xJJQ9NZ84FVMezAwgZY_4kTvFjoyZGZ", #chalifia
            "https://drive.google.com/uc?export=view&id=10EUhyay18VmmuOYHQ3C7ccrYgMeqQnUe", #irfan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #izza blm
            "https://drive.google.com/uc?export=view&id=17wz71Pul1sAPMQu1a5d3JwU983LHppu", #chalisa
            "https://drive.google.com/uc?export=view&id=17n5fMBF83VBke9pt6_W7lBnjPCeVy-m2", #raid
            "https://drive.google.com/uc?export=view&id=19aeV2oM-D_9uOtAllxtQFHUttEEk8alO", #tria
        ]    
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450033",
                "umur": "21 ",
                "asal":"Bogor ",
                "alamat": "Raden Saleh ",
                "hobi": "Searching GPT ",
                "sosmed": "@Trimurniyaa_",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450114 ",
                "umur": "21 ",
                "asal":"Tangsel ",
                "alamat": "Way Hui ",
                "hobi": "Baca buku & nonton film ",
                "sosmed": "@wlnsbn0",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450081 ",
                "umur": "20 ",
                "asal":"Tangerang ",
                "alamat": "Jati Agung ",
                "hobi": "Ngobrol ",
                "sosmed": "@anisadini10",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@",
                "kesan": "kakak nya baik",    
                "pesan":"semangat terus kuliahnya kak !!!"
            },
            {
                "nama": " Esteria Rohanauli Sidauruk",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumsel",
                "alamat": "Waykandis",
                "hobi": "baca buku",
                "sosmed": "@fr_yulius",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Novelia Adinda",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450004",
                "umur": "20",
                "asal":"Solo ",
                "alamat": "Natar ",
                "hobi": "Suka ditipu jual akun canva di shoope ",
                "sosmed": "@dheamelia",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "121450156 ",
                "umur": "22 ",
                "asal":"Surakarta Jateng ",
                "alamat": "Sukarame ",
                "hobi": "Badminton, berenang, hiking, dan melukis ",
                "sosmed": "@fhrul.pdf",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "12200065 ",
                "umur": "20 ",
                "asal":"Sumbar ",
                "alamat": "Way hui",
                "hobi": "makeup, nonton podcast, dan denger musik ",
                "sosmed": "@berlyyanda",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450022",
                "umur": "20 ",
                "asal":"Balam ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@Jeremia_",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Chalifia Wananda",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Irfan Alfaritzi",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Izza Luthia",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Khaalishah Zuhrah Alya Vanefi",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Tria Yunanni",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus ya kak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_eksternal()
elif menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-EfmIT_NEkrtNKquiRGBb0Ugxa9k6Hsx", #dimas
            "https://drive.google.com/uc?export=view&id=11u3nqacgkE37nozkDLYLLHK8b_Q6GiLc", #catherin
            "https://drive.google.com/uc?export=view&id=1222PtaFAtCSXMjpHHaYKFe91XUXBSToP", #akbar
            "https://drive.google.com/uc?export=view&id=1AKZ8Lg8coa275NdCvCh6ez_41A64aYau", #rani
            "https://drive.google.com/uc?export=view&id=127i9RrA2MgG8TdQ05cjLUa9u_hT0zCvN", #rendra
            "https://drive.google.com/uc?export=view&id=1-FjThyz_rIofRVyHNvsjGml7V-7IthEz", #salwa
            "https://drive.google.com/uc?export=view&id=11nKun3Ul4lt5G3xdvH9ymOztmH4hkcx9", #ari 
            "https://drive.google.com/uc?export=view&id=1-2YIH43S0ObaV419HQXZ1zAfrSDWPOjs", #azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #dearni blm
            "https://drive.google.com/uc?export=view&id=1-E-aTDVqsxFz5Lp52KlYI07pYSYHSxBy", #meira
            "https://drive.google.com/uc?export=view&id=1-ANO2JOR9_94-E9L_0p6x49o5xzApwNk", #rendi
            "https://drive.google.com/uc?export=view&id=123nWvDTJXafCRmQPMdwV7YHMdbbnkatl", #ranta
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450033",
                "umur": "21 ",
                "asal":"Bogor ",
                "alamat": "Raden Saleh ",
                "hobi": "Searching GPT ",
                "sosmed": "@Trimurniyaa_",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450114 ",
                "umur": "21 ",
                "asal":"Tangsel ",
                "alamat": "Way Hui ",
                "hobi": "Baca buku & nonton film ",
                "sosmed": "@wlnsbn0",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Akbar Resdika",
                "nim": "121450081 ",
                "umur": "20 ",
                "asal":"Tangerang ",
                "alamat": "Jati Agung ",
                "hobi": "Ngobrol ",
                "sosmed": "@anisadini10",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450019",
                "umur": "19",
                "asal":"Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumsel",
                "alamat": "Waykandis",
                "hobi": "baca buku",
                "sosmed": "@fr_yulius",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Ari Sigit",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Dearni Monica Br Manic",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450004",
                "umur": "20",
                "asal":"Solo ",
                "alamat": "Natar ",
                "hobi": "Suka ditipu jual akun canva di shoope ",
                "sosmed": "@dheamelia",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "121450156 ",
                "umur": "22 ",
                "asal":"Surakarta Jateng ",
                "alamat": "Sukarame ",
                "hobi": "Badminton, berenang, hiking, dan melukis ",
                "sosmed": "@fhrul.pdf",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Ranta Siahaan",
                "nim": "12200065 ",
                "umur": "20 ",
                "asal":"Sumbar ",
                "alamat": "Way hui",
                "hobi": "makeup, nonton podcast, dan denger musik ",
                "sosmed": "@berlyyanda",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()
elif menu == "Departemen SSD":
    def departemen_ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-eDsKFq5Pc_egatwI4WfvarkikI4tqZs", #andrian
            "https://drive.google.com/uc?export=view&id=1-oEep2lO4ZovwUKuEHorOIEypaJi0paI", #adisty
            "https://drive.google.com/uc?export=view&id=10-ILq9evHFRbVbRn2T0GyOCEE3E4Mk8w", #nabila
            "https://drive.google.com/uc?export=view&id=1-Z4YGjjMYqS0GnNP6uBHwTjUEamLOTY8", #ahmad
            "https://drive.google.com/uc?export=view&id=1-c3VGmgR117ALL8I7X3LSvsN-2okL39t", #danang
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #varrel blm
            "https://drive.google.com/uc?export=view&id=1-xNJS2My45Oeh9q_h6EuEGBmw3dqmfn9", #tessa
            "https://drive.google.com/uc?export=view&id=1-YuWrTCX1cgc4XI_wBlJSOs7aR2hT6-G", #nabilah
            "https://drive.google.com/uc?export=view&id=1-xaKJ44MFJ8-L_2vd7XmiIjn46XIWh5i", #alvia
            "https://drive.google.com/uc?export=view&id=102Nov3yv4uHDfKAurh6iGIXLDqMATDZF", #dhafin
            "https://drive.google.com/uc?export=view&id=101dMlPS_1gKbC90EAV7rckYJqCs-Mci1", #elia
        ]
        data_list = [
            {
                "nama": "Adrian Agustinus Lumban Gaol",
                "nim": "121450033",
                "umur": "21 ",
                "asal":"Bogor ",
                "alamat": "Raden Saleh ",
                "hobi": "Searching GPT ",
                "sosmed": "@Trimurniyaa_",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450114 ",
                "umur": "21 ",
                "asal":"Tangsel ",
                "alamat": "Way Hui ",
                "hobi": "Baca buku & nonton film ",
                "sosmed": "@wlnsbn0",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450081 ",
                "umur": "20 ",
                "asal":"Tangerang ",
                "alamat": "Jati Agung ",
                "hobi": "Ngobrol ",
                "sosmed": "@anisadini10",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450019",
                "umur": "19",
                "asal":"Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumsel",
                "alamat": "Waykandis",
                "hobi": "baca buku",
                "sosmed": "@fr_yulius",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "1223450040 ",
                "umur": "20",
                "asal":"Simalungun",
                "alamat": "pemda",
                "hobi": "menulis ",
                "sosmed": "@tessakanias",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Nabillah Andika Fitrianti",
                "nim": "123450139",
                "umur": "20",
                "asal":"bandar Lampung",
                "alamat": "Kedaton",
                "hobi": " ",
                "sosmed": "@nabilahanftr",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Alvia Asrinda Br.Ginting",
                "nim": "123450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri ",
                "hobi": "Nonton windah",
                "sosmed": "@alviaginting",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450004",
                "umur": "20",
                "asal":"Solo ",
                "alamat": "Natar ",
                "hobi": "Suka ditipu jual akun canva di shoope ",
                "sosmed": "@dheamelia",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "121450156 ",
                "umur": "22 ",
                "asal":"Surakarta Jateng ",
                "alamat": "Sukarame ",
                "hobi": "Badminton, berenang, hiking, dan melukis ",
                "sosmed": "@fhrul.pdf",
                "kesan": "kakak nya baik",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_ssd()
elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1BYedSyFj_bLZTqxMfaYFfoZfxErfPlwt",
            "https://drive.google.com/uc?export=view&id=12vtJu_7ngV-MNdKrfee7T7SjfxtzuuOc",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1BlBnQM0_7x520rymPk6ibVz-FnDF_I2k",
            "https://drive.google.com/uc?export=view&id=139GeaI86vv-n2acy5wSFzE_BpU5sC_G5",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=137w9Wlq_QCkTuceZNNTJueqG5h_9qLKI",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=13E-UgiNdBqjoCQe25ecMbDcbhHK1AtQC",
            "https://drive.google.com/uc?export=view&id=137lBN1SGy3lMgFLwZRBubua7YzZjjFLS",
            "https://drive.google.com/uc?export=view&id=1BpYru-HkkJy6ABOw1YQIfTb5yQecLXa_",
            "https://drive.google.com/uc?export=view&id=1Bq1hGBzkqW4kK4LYfsp7Khle_dkmg37r",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1BZrYr-ydiNtx1p2Tppi7dlXiBZtrdX7C",
            "https://drive.google.com/uc?export=view&id=13FUOQ1z71sWxVj0r1WBv_h4UJYFc4TCf",
            "https://drive.google.com/uc?export=view&id=1BkLqR2rDi4c8CxCGe-G3kd6gDYPzWozp",
            "https://drive.google.com/uc?export=view&id=13B8RC4SWWHnHLCSKQgYoVN9O89tHbi9y",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "abangnya baik",  
                "pesan": "Semangatt kuliahnya bang!" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakaknya baik",  
                "pesan": "Semangatt kuliahnya kak!" # 2
            },
            {
                "nama": "Mujadid Choirus Surya",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": "  ",
                "sosmed": "@ ",
                "kesan": "  ",  
                "pesan": "  " # 3
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "abangnya baik",  
                "pesan": "Semangatt kuliahnya bang!" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "abangnya baik",  
                "pesan": "Semangatt kuliahnya bang!" # 5
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan": "  " # 6
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "kakak nya baik",  
                "pesan": "Semangatt kuliahnya kak!" # 7
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan": "  " # 8
            },
            {
                "nama": "Anwar Muslim",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan": "  " # 9
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan": "  " # 10
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "kakaknya baik",  
                "pesan": "Semangatt kuliahnya kak!" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kakaknya baik!",  
                "pesan": "Semangatt kuliahnya kak" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kakaknya baik",  
                "pesan": "Semangatt kuliahnya kak!" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya baik",  
                "pesan": "Semangatt kuliahnya kak!" # 14
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan": "  " # 15
            },
            {
                "nama": "Aditya Rahman",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan": "  " # 16
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobi": "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan": "abangnya baik",  
                "pesan": "Semangatt kuliahnya bang!" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakaknya baik",  
                "pesan": "Semangatt kuliahnya kak!" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "abangnya baik",  
                "pesan": "Semangatt kuliahnya bang!" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "abangnya baik",  
                "pesan": "Semangatt kuliahnya bang!" # 20
            },
            {
                "nama": "Vita Anggraini",
                "nim": "  ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": "  ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"  " # 21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17hJSElClCCSQSUOqNkjs8QVGFqrVjST1", #bang wahyu
            "https://drive.google.com/uc?export=view&id=16Fwot902mA1VZch2rkTfwWch8Y6M0H_q", #ka elok
            "https://drive.google.com/uc?export=view&id=17VZyGTvsgqrJcTKJHwoObwCiTLYxvVMX", #ka arsyiah
            "https://drive.google.com/uc?export=view&id=17b8W-oN5UMv_mgdjU89dEWCINs1Q3mm7", #ka cibel
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ka eka
            "https://drive.google.com/uc?export=view&id=16xGsheIqNQZ_3L1KzJUXLrmN1tEWtQm_", #ka najla
            "https://drive.google.com/uc?export=view&id=15irs-wBOBRICnmjAiD4EyCEqi-xfX_5j", #ka patricia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ka rahma
            "https://drive.google.com/uc?export=view&id=17cCfaowE1VIWPP6S12Jyhzs8IPkp3Qeq", #ka try yani
            "https://drive.google.com/uc?export=view&id=16nXJ9MmTJg_PPvuoCVVhccqtMHbk-MIA", #bang kaisar
            "https://drive.google.com/uc?export=view&id=16RB9fDNwx5ARRXHyGAm0CfTVYwRA-G3A", #ka dwi
            "https://drive.google.com/uc?export=view&id=16IBk62LVGCK0dZA8AfR7mafjIqXIrIav", #bang gym
            "https://drive.google.com/uc?export=view&id=16lL-ZcxVAfysZ73oigBNaPpjhrq5XAmq", #ka nasywa
            "https://drive.google.com/uc?export=view&id=16mlqYNuO8XFy1ram-I5_rbflJZJn72hO", #ka priska
            "https://drive.google.com/uc?export=view&id=16iZtYWKd5eMRZbldhm4AepDSYwmlaFko", #bang arsal
            "https://drive.google.com/uc?export=view&id=17D1OjKdmZjE3-5hAV6wsofEO3vaWVLhc", #bang abit
            "https://drive.google.com/uc?export=view&id=16Q12SMV5yRW0qfytB5317Ktv85BZ0DO0", #bang akmal
            "https://drive.google.com/uc?export=view&id=17bMRlGdR8zZpMffo4zn-hnaW1871gN3j", #bang mawan
            "https://drive.google.com/uc?export=view&id=17iepCTuzUDZe8DlSeeOG-LLZiTKmyQ80", #ka khusnun
        ]

        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobi": "Nonton donghwa",
                "sosmed": "wayyulaja",
                "kesan": "seruuu bangett",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat bang!"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@Elokviola",
                "kesan": "cantikk dan kalemm",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat kak!"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Seneng",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "kalem sekaliii",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat kak!"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Cantikk bangett",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat kak!"
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":" "
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Nulis, baca, ngefangirl",
                "sosmed": "@nanana.minjoo",
                "kesan": "ramah, cantik, lucu",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat kak!"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobi": "Shopping",
                "sosmed": "@patriciadiajeng",
                "kesan": "Seruuu dan cantikkk bangettt",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat kak!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobi": "Membaca merk mobil",
                "sosmed": "@rahmaneliyana",
                "kesan": "baikk dan ramahh bangett",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat kak!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Ngoding",
                "sosmed": "@tryyaniciaaa",
                "kesan": "seruu, cantikk",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat kak!"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Masih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "seruuu bangg",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat bang!"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobi": "Menonton",
                "sosmed": "@dwiratnn_",
                "kesan": "pendiemmm kakk",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat kak!"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobi": "baca komik",
                "sosmed": "@jimnn.as",
                "kesan": "baikk dan asikk",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat bang!"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobi": "suka bebersih dan denger musik jj",
                "sosmed": "@nsywanaf",
                "kesan": "cantik bangett dan seruuu",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat kak!"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobi": "nonton apapun yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan": "seruuu dan asikkk kak",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat kakk!"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsalutama",
                "kesan": "baikk dan ramahh",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat bang!"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobi": "ngoding dan gaming",
                "sosmed": "@abitahmad",
                "kesan": "lucuu banget dan informatif",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat bang!"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobi": "Main hp",
                "sosmed": "@akmal.faiz",
                "kesan": "seruu dan pinter",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat bang!"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobi": "baca novel",
                "sosmed": "@hermawan.mnrng",
                "kesan": "kocak banget dan asikk",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat bang!"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Ngepel",
                "sosmed": "@khusnun_nisa335",
                "kesan": "ramahh dan baikk",  
                "pesan":"Semoga semua yang sedang diusahakan tercapai, semangat bang!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()



