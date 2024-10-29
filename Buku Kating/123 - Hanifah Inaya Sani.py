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
            "https://drive.google.com/uc?export=view&id=18Lo44Hi0yITl7Jcg8GzxAu5O4zKRcpMh/view",
            "https://drive.google.com/uc?export=view&id=10B3ZywV2ENhrEmtczxZrsTKaW9Zm1kID/view",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=104Ej5adJttkJyWmVwpWLSmVxC872GmUl/view",
            "https://drive.google.com/uc?export=view&id=18D8fsCKlVWGJGKUd2dOA2MVKL-qsXvyN/view",
            "https://drive.google.com/uc?export=view&id=18Ko5r8zC3Tox1KPWjhtTcpxnJYGlvC7U/view",


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
            "https://drive.google.com/uc?export=view&id=12TDvKnyB0wK6AT8J_UpjPk-OQsx4V4QT/view",
            "https://drive.google.com/uc?export=view&id=12K0p_mBIqgUFIdsAiTCfrAvfpy_IYWxp/view",
            "https://drive.google.com/uc?export=view&id=12NnXkSmGATPlgRF5BeF_edY0gSgf-9-d/view",
            "https://drive.google.com/uc?export=view&id=12KYfO4aaIaWGs2LHDe1xk5frLsIqlPbi/view",
            "https://drive.google.com/uc?export=view&id=12Hu6xjdqblwnYnU5mNLCVwPLXXELyfmH/view",
            "https://drive.google.com/uc?export=view&id=12uZ1GzrTtdkCPcDNQxb0y8VMjkX3BGoB/view",
            "https://drive.google.com/uc?export=view&id=12nIX0slO-ZtEcI0aZErl-V7s2Bzspkl3/view",
            "https://drive.google.com/uc?export=view&id=12WqZjcYOcaCH3eLCZ5QSjPRVx-U7fR1S/view",
            "https://drive.google.com/uc?export=view&id=12mTV9Y4HRZv-_gk_15VQmw6qUUtBKorF/view",
           
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
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
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
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
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
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
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
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
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
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12HYevK7NdYgT3L10Hp8w4pD2_lzh7Qe3/view",
            "https://drive.google.com/uc?export=view&id=12BXxIDUtlEVzONPjXIfFEEHFhddQfqH-/view",
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
            "https://drive.google.com/uc?export=view&id=1npu72Bsy_AJepQ9ZbZ7mkdWFSEEJ0SnH", # bg econ
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka abet
            "https://drive.google.com/uc?export=view&id=1nVHHuU1VrcBeyScxi0TBxwZkctwM_NdF", # ka pipah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka allya
            "https://drive.google.com/uc?export=view&id=1nkbnr0mzDf4cKlCXpOxBmULP3HSVFSlF", # ka eksanty
            "https://drive.google.com/uc?export=view&id=1nT7UG99x5e_aiF3NLFGztI_L7WimDdv5", # ka hanum
            "https://drive.google.com/uc?export=view&id=1npaBh2Ih87rS95-PShzNhnUrrYLnSCDT", # bg ferdy 
            "https://drive.google.com/uc?export=view&id=1o-1mMVYzYh9Wn2bn2R0R76k3xFDIHMmJ", # bg deri 
            "https://drive.google.com/uc?export=view&id=1ngDQbKok2qNjER3LaKBNd1PDR0jN0KUr", # ka okta 
            "https://drive.google.com/uc?export=view&id=1n5W-Y1roXM0aTOlmpntXWq2gQMTvnJkZ", # bg deyvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg ibnu farhan 
            "https://drive.google.com/uc?export=view&id=1n5xlW1n_4hkw5dz8Fwdwrjme6hot1ODz", # bg jo
            "https://drive.google.com/uc?export=view&id=1nPLglQ44Mofcx_pzhUUPTepQKMkOH6Kx", # bg kemas
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg leon
            "https://drive.google.com/uc?export=view&id=1nC5BcpEJ8bkxlhgOPAwW2Gyv_oMB12vg", # ka presilia
            "https://drive.google.com/uc?export=view&id=1nM-nvwvXWs77-VoNISX6Y1uoX8k2PkG9", # ka aqila
            "https://drive.google.com/uc?export=view&id=1n6FwogQ-E1GrzLrE0BEOD8sumrwXTY9j", # bg sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka vanes
            "https://drive.google.com/uc?export=view&id=1nUh9vyaId4z8OVWkGWU5ZzP0Eznxt9lg", # bg ateng
            "https://drive.google.com/uc?export=view&id=1nNkycHEtdBBKF4bxY9ni0IA3le-fhWuE", # bg gede
            "https://drive.google.com/uc?export=view&id=1nXh8G3m2DRiyuL3WL47hIDejS-xJhWDN", # ka jaclin
            "https://drive.google.com/uc?export=view&id=1nSjN_lLPgB9Udkjh59TFXLc3Rla8HZdx", # bg rafly
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka syalaisha dini
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
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
                "hobbi": "Bernafas",
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
                "hobbi": "Minum kopi",
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
                "hobbi": "Ngukur bandar lampung",
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
                "hobbi": "Ngeroasting orang",
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
                "hobbi": "Baca webtoon",
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
                "hobbi": "Baca buku dan Futsal",
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
                "hobbi": "Bakar-bakar",
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
                "hobbi": "Ngeliatin tingkah orang",
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
                "hobbi": "Belajar",
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
                "hobbi": "-",
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
                "hobbi": "Ngeasprak",
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
                "hobbi": "Ngetik print halo dunia",
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
                "hobbi": "-",
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
                "hobbi": "Dengar JPP worship",
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
                "hobbi": "Baca Webtoon",
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
                "hobbi": "Nonton resilore id",
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
                "hobbi": "-",
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
                "hobbi": "Menolong",
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
                "hobbi": "Belajar, Game, Baca Komik",
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
                "hobbi": "Berenang",
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
                "hobbi": "Main Game",
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
                "hobbi": "-",
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "kakak nya baik"",  
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
                "kesan": "kakak nya baik"",  
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
                "nama": "Rohanauli Sidauruk",
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "kakak nya baik,  
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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




