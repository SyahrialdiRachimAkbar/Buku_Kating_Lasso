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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilan",
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
                "kesan": "bang pandra orangnya santuy dan asik",  
                "pesan":"semangat kuliahnya bang pandra!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450044",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "kakak cantik dan baik hati",  
                "pesan":"semangat kuliahnya kak melin"# 1
            },
            {   "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobi": "Dengerin Bang Pandra main gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kak putri orangnya asik",  
                "pesan":"semangat kuliahnya kak putri!"# 1
                    
            },
            {   "nama": "Hartiti Fadilah",
                "nim": "121450021",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrdfdlh",
                "kesan": "kak titi orangnya pendiem sekali ternyata",  
                "pesan":"semangat kuliahnya kak titi!"# 1

            },
            {   "nama": "Nadila Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Gangguin Kak Liza Tidur, bawa Wattpad/AU",
                "sosmed": "@nadillaandr26",
                "kesan": "kak nadila orangnya asik dan suka bercanda",  
                "pesan":"semangat kuliahnya kak nadila!"# 1

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
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
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": ".",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": ".",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": ".",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": ".",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "one of my role model, bener bener takjub selama denger kakak jawab pertanyaan waktu wwc",  
                "pesan": "Semangat terus kuliahnya ka luthfi!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan kota baru",
                "hobi": "Dengerin Ka Luthfi bernyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "selama wwc baru tau kalo ternyata bang bin orangnya sesantuy itu",  
                "pesan": "Semangatt kuliahnya bang bintang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Baik, berwibawa dan tegas",  
                "pesan": "Semangatt kuliahnya bang econ!" # 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "kak abeth orangnya ramah sekalii",  
                "pesan":"semangat kuliahnya kak abeth!" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakak pipah cantik sekalii",  
                "pesan":"semangat kuliahnya kak pipah!" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": "tegas tapi diluar itu asik",  
                "pesan":"semangat kuliahnya kak allya!" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobbi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": "baik sekali",  
                "pesan": "semangat kuliahnya kak eksan!" # 5
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
                "pesan": "semangat kuliahnya kak hanum!" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobbi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "pendiam tapi tegas",  
                "pesan": "semangat kuliahnya bang ferdy!" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": "pendiam tapi tegas",  
                "pesan": "semangat kuliahnya bang deri!" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "baik dan asik",  
                "pesan": "semangat kuliahnya kak okta!" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "humoris dan murah senyum",  
                "pesan": "semangat kuliahnya bang D! " # 10
            },
            {
                "nama": "Ibnu Farhan Al-Ghifari",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@",
                "kesan": "-",  
                "pesan": "-" # 11
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": "tegas tapi asik",  
                "pesan": "semangat kuliahnya bang jo!" # 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": "baik, pinter, ramah",  
                "pesan": "semangat kuliahnya bang kemas!" # 13
            },
            {
                "nama": "Leonard Andreas Napitupulu",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ ",
                "kesan": "-",  
                "pesan":"-" # 14
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengar JPP worship",
                "sosmed": "@presiliamg",
                "kesan": "baik, cantik",  
                "pesan": "semangat kuliahnya kak presilia!" #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "baik, cantik, pendiam",  
                "pesan": "semangat kuliahnya kak rafa!" # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "baik dan asik",  
                "pesan": "semangat kuliahnya bang sahid!" # 17
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@",
                "kesan": "-",  
                "pesan": "-" # 18
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "ramah, baik, humoris",  
                "pesan": "semangat kuliahnya bang ateng!" # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "baik dan humoris",  
                "pesan": "semangat kuliahnya bang gede " # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "baik, cantik, ramah",  
                "pesan": "semangat kuliahnya kak jaclin" # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "baik dan asik ",  
                "pesan": "semangat kuliahnya bang rafly" # 22
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@",
                "kesan": "-",  
                "pesan": "-" # 23
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
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
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 2
            },
            {
                "nama": "Mujadid Choirus Surya",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
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
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 5
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
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
                "hobbi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 7
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
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
                "hobbi": " ",
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
                "hobbi": " ",
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
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 14
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
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
                "hobbi": " ",
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
                "hobbi": "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 20
            },
            {
                "nama": "Vita Anggraini",
                "nim": "  ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"  " # 21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
