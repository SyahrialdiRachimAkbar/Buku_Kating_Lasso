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
            "https://drive.google.com/uc?export=view&id=1-1GvIodPS1nrvYnshBd5Ll7ObPb5woN1", # bg econ
            "https://drive.google.com/uc?export=view&id=19QtrmhfbnkJ0jrr99xUsN55hQ9_PlAFF", # ka abet
            "https://drive.google.com/uc?export=view&id=19a60c--2C6FNLdxuyzLUtKDuSHY4marU", # ka pipah
            "https://drive.google.com/uc?export=view&id=10K4AP0IAQ-CxpSB3b6OkKHscjR_qOCfk", # ka allya
            "https://drive.google.com/uc?export=view&id=10emB0I864FfHzfk2h_5keeFMK00BDDPz/", # ka eksanty
            "https://drive.google.com/uc?export=view&id=10XgKssU4n6nxJLKDUJZUSCe18vb3hF7d", # ka hanum
            "https://drive.google.com/uc?export=view&id=10UQmKhUEUejmj1se868DiBT9464v1O37/", # bg ferdy 
            "https://drive.google.com/uc?export=view&id=1105lryHiM7AdCSGsFrIYbWuQCU78l-jp", # bg deri 
            "https://drive.google.com/uc?export=view&id=10dXvtgAEmTNqv2JrEW6DoTp0UQiKH5JD", # ka okta 
            "https://drive.google.com/uc?export=view&id=111AMN1boLxi1JW7u0M3NVpJ5fsNvofBP", # bg deyvan
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", # bg ibnu farhan blm
            "https://drive.google.com/uc?export=view&id=11405CX4cTD9obkfM4xQEPeeuYBw5KK-J", # bg jo
            "https://drive.google.com/uc?export=view&id=11EDGnCtcTY3eQj4NkHMi9_WydDzBSw2I", # bg kemas
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", # bg leon blm
            "https://drive.google.com/uc?export=view&id=19vtDHOk4RKna8GxjHOAIxIGM-ec05hsP", # ka presilia
            "https://drive.google.com/uc?export=view&id=1155cVInNcRloz_dC-exBqOcJsGz_YDjW", # ka aqila
            "https://drive.google.com/uc?export=view&id=113StsZUVOaVMBnbO2TgwIdmWWE8J9qc8", # bg sahid
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", # ka vanes blm
            "https://drive.google.com/uc?export=view&id=11bIE2zu1Iu9CWltKLjVvCumpwrBy7c-2", # bg ateng
            "https://drive.google.com/uc?export=view&id=19vkfXTsEI3r1p7X67frdINhydyuHLLAD", # bg gede
            "https://drive.google.com/uc?export=view&id=11I9LcjNiGAL_q5upDzGyb0HyqH_kqGoV", # ka jaclin
            "https://drive.google.com/uc?export=view&id=19kpucvshcZsjogj9Zx58CdU9P9T1FMxh", # bg rafly
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", # ka syalaisha dini blm
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
                "kesan": "abang nya baik",  
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
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", #ramadita blmm
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", #nazwa blm
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", #bastian blm
            "https://drive.google.com/uc?export=view&id=17kxhBfowNdU6HSYGyqONr4vhIeHHtESU", #dea
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", #rohanauli blm
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", #natasya blm
            "https://drive.google.com/uc?export=view&id=17kwOZOBMSsbm2Sr1S9pbxs2KZ-IZUl9V", #novelia
            "https://drive.google.com/uc?export=view&id=16ClPGsT7lTt3zcr0t-4Y-Pjw6LtPwqdC", #jasmin
            "https://drive.google.com/uc?export=view&id=17lp5w8DJW1nTRLru51WX9tixCId5I0hI", #tobias
            "https://drive.google.com/uc?export=view&id=17xvND4RA8jSEKLaUCXRJwhXDbjLdpaxz", #yohana
            "https://drive.google.com/uc?export=view&id=16ClPGsT7lTt3zcr0t-4Y-Pjw6LtPwqdC", #riszi
            "https://drive.google.com/uc?export=view&id=17k7gOLZf2Te8AuuSe2JO765EJ72cKiCw", #arafi
            "https://drive.google.com/uc?export=view&id=19dKKBDuN7wFF3oCiCU3A7POjWeuZJHmY", #asa
            "https://drive.google.com/uc?export=view&id=15xJJQ9NZ84FVMezAwgZY_4kTvFjoyZGZ", #chalifia
            "https://drive.google.com/uc?export=view&id=10EUhyay18VmmuOYHQ3C7ccrYgMeqQnUe", #irfan
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", #izza blm
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
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", #dearni blm
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
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh", #varrel blm
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
                "nama": "Nabillah Andika Fitrianti",
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
                "nama": "Alvia Asrinda Br.Ginting",
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




