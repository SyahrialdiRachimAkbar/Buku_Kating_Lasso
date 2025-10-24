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
            "Departemen MEDKRAF",
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
            "https://drive.google.com/uc?export=view&id=1Wv_kc_W9xsh4ffw5O_IpWEcUQdNDtUoG", #bg gumi
            "https://drive.google.com/uc?export=view&id=1lUB2JTpc9PfJ3gt5ZXrpmZNOMLE0Xa_E", #bg pandra
            "https://drive.google.com/uc?export=view&id=1-rv5Rzae3-ra4NOY-y-X4NAwdjsI9Cbg", #ka liza
            "https://drive.google.com/uc?export=view&id=1sTqC6pjJhRBJczP7js0FkFxDbeTn_30i", #ka putri
            "https://drive.google.com/uc?export=view&id=1yrKYVqL4Ty84l6gj89yNaWpsEz93bU8u", #ka titi
            "https://drive.google.com/uc?export=view&id=1KQxf3ki4FY52eC62N6VIcUYo4tLlRSDd", #ka nadilah
        ]
        data_list = [
            {
                "nama": "Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Kuliah-rapat dan dengerin musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Ramah dan berwibawa",  
                "pesan": "Semangat semoga sukses!!!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl Bawean2, Sukarame",
                "hobi": "Bermain gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Asik",  
                "pesan": "Semangat semoga sukses untuk kedepannya!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450044",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Asik dan ramah",  
                "pesan": "Semangat kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh",
                "alamat": "Jl Nangka 4",
                "hobi": "Mendengarkan bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Murah senyum",  
                "pesan": "Semangat teruss kuliahnya kak putri!"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrtfdlh",
                "kesan": "Kalem",  
                "pesan": "Semangat kuliah kak titii!"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Baca wattpad dan au",
                "sosmed": "@nadillaandr26",
                "kesan": "Ramah dan asik",  
                "pesan": "Semangat kuliahnya kak !"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OzpZrta1hgmTYfcJLf0cIQX6Jh71vstO", # ka niya
            "https://drive.google.com/uc?export=view&id=1v5t6jHLD9_v6DokIJIeHN_Sve8Ihhgnw", # ka annisa cahyani
            "https://drive.google.com/uc?export=view&id=1x6K-b91vISTOXuyvpqXCEMbmiS-lG5Cg", # ka wulan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka anisa dini
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka anisa fitri
            "https://drive.google.com/uc?export=view&id=1sJhQoXAtbxWYAB7oeYLTA3Y43Jy67Fh8", # bang fery
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka renisha
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka claudea
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bang mirzan
            "https://drive.google.com/uc?export=view&id=1wGvo6CyssAfOkTkJdD9G1Slavj6pxYq3", # ka dhea
            "https://drive.google.com/uc?export=view&id=14UY6Ztrx5GlkESrncGiog6kfHOKR5ND-", # bang fahrul
            "https://drive.google.com/uc?export=view&id=1QtlJQt6UwNI_89fGQQWnEEarfYMY-RQX", # ka berli
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bang jere
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Jl Raden Saleh",
                "hobi": "Searching GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Ramah dan asik ",  
                "pesan": "Semangat terus kuliahnya kakk!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Baca buku dan nonton film",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Ramah dan murah senyum",  
                "pesan": "Semangat terus ya kak kuliahnya kakak NIM saya 114! "# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Jl Raden Saleh",
                "hobi": "Belajar bersama pak tamaro",
                "sosmed": "@wlsbn0",
                "kesan": "Kakaknya suka bercanda",  
                "pesan": "Semangat terus kuliahnya ya kakak dan tetap sehat!"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Ngobrol",
                "sosmed": "@anisadini10",
                "kesan": "Asik dan ceria",  
                "pesan": "Semangattt teruss ya kakk, sehat-sehat juga!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@ansftrynn_",
                "kesan": "Pendiam dan ramah",  
                "pesan": "Semangat terus kuliahnya kakkk!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Asik",  
                "pesan": "Semangat terus dan sukses kuliahnya bang!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "@fleurnsh",
                "kesan": "-",  
                "pesan": "-"# 1
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "@dylebee",
                "kesan": "-",  
                "pesan": "-"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "@myrrinn",
                "kesan": "-",  
                "pesan": "-"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Solo",
                "alamat": "Natar",
                "hobi": "Suka ditipu sama penjual akun canva premium di shopee",
                "sosmed": "@_.dheamelia",
                "kesan": "Baik dan ramah",  
                "pesan": "Semangat dan sehat terus kak !! "# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta, Jawa Tengah",
                "alamat": "Sukarame",
                "hobi": "Badminton, melukis, hiking, dan berenang",
                "sosmed": "@fhrul.pdf",
                "kesan": "Baik",  
                "pesan": "Semangat terus kuliahnya bang!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Make up, nonton podcast, dan dengerin musik",
                "sosmed": "@berlyyanda",
                "kesan": "Baik dan pendiam",  
                "pesan": "Semangat terus kuliahnya kak!!"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "-",
                "sosmed": "@jeremia_s_",
                "kesan": "-",  
                "pesan": "Semangat terus kuliahnya ya bang!" # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()


elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1s7V4QqwvAQ1RkMdeAmXjbtlZLBgp8oGX", # ka luthfi
            "https://drive.google.com/uc?export=view&id=1Xsm_OeZjg_Jdxmr6ww3JnnNplXy-dL1p", # bang bintang
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
                "kesan": "Baik dan ramah",  
                "pesan": "Semangat terus kuliahnya ya kak, tetap sehat juga!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan kota baru",
                "hobi": "Dengerin Ka Luthfi bernyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Baik",  
                "pesan": "Semangat terus kuliahnya bang, sehat-sehat teruss!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()


elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-LzlmGfP_u3beagYQ35xZyYRNixeHJLK", # bg econ
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka abet
            "https://drive.google.com/uc?export=view&id=1vTj_Ek5HdC9l698W44WCmg20-YdPpy9d", # ka pipah
            "https://drive.google.com/uc?export=view&id=19NXiuiUd6AVxjcJzjuE_c69O6k3CyttT", # ka allya
            "https://drive.google.com/uc?export=view&id=14245INryXMKtd5D6GPu5ayAhpASXTe6c", # ka eksanty
            "https://drive.google.com/uc?export=view&id=1E5V1YVZAOV19R7IvDuu3mNWAILW6nv3V", # ka hanum
            "https://drive.google.com/uc?export=view&id=1n2KxlVnLFtiDHv3WEdiFLA0v3gKyQL7y", # bg ferdy
            "https://drive.google.com/uc?export=view&id=1YkQAEyzSPWJPmPJsM2DhjutqAR_dscZF", # bg deri
            "https://drive.google.com/uc?export=view&id=1AmriYiZSNN5MEHPsxkpSJkjdc8nk3w_C", # ka okta
            "https://drive.google.com/uc?export=view&id=1udGgtNvMcEIcrT_yJRunTLmKkJzApehD", # bg deyvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg ibnu farhan
            "https://drive.google.com/uc?export=view&id=1S5XBc33iUoLyYvA2BU59SRCWCk1M67FQ", # bg jo
            "https://drive.google.com/uc?export=view&id=1p-J4MJKTTcy_pjsKDCnNd4SU186CA1dQ", # bg kemas
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg leon
            "https://drive.google.com/uc?export=view&id=1MEQbJ2UJm7GEwt98hkEDpMsIkD3fwDat", # ka presilia
            "https://drive.google.com/uc?export=view&id=1eQckjqAryfSywgZxZOajOlK_eP8HVOeY", # ka aqila
            "https://drive.google.com/uc?export=view&id=1AlTiZe0kw0HRFVUs7ADHd5nF114a1Utl", # bg sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka vanes
            "https://drive.google.com/uc?export=view&id=1sCTeYF4IsYAAL4XMtAh_UpeA4eKjlVM0", # bg ateng
            "https://drive.google.com/uc?export=view&id=1j0hVUGEkUp2F8DwGm5Mt9ifHo0n1dR9_", # bg gede
            "https://drive.google.com/uc?export=view&id=1-DlYLMdnQ6BJUmpFw6Oo0VWV_WCtkXcD", # ka jaclin
            "https://drive.google.com/uc?export=view&id=1codJNFZbU6CwVan_O4605XcGYK6knKpn", # bg rafly
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka syalaisha dini
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
                "kesan": "Baik dan tegas",  
                "pesan": "Semangat terus kuliahnya ya bang, semoga sukses!" # 1
            },
            {
                "nama": "Celisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": " Ramah dan asikk ",  
                "pesan": "Semangat terus kuliahnya ya kak, tetap asik juga!" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak, tetap sehat!" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat jugaa!" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": " Baik dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya kak Eksanty, semoga suksess!" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "Baik",  
                "pesan": "Semangat terus kuliahnya ya kak Hanum, tetap sehatt!" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": " Baik dan asik ",  
                "pesan": "Semangat terus kuliahnya ya bang, semoga cita-cita dalam waktu dekat ini tercapai hhe!" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": " Asik ",  
                "pesan": "Semangat terus kuliahnya ya bang Derr, suksess!" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": " Pendiam, namun baik ",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat teruss!" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": " Baik, asik ",  
                "pesan": "Semangat terus kuliahnya ya bang, semoga sukses kedepannya!" # 10
            },
            {
                "nama": "Ibnu Farhan Al-Ghifari",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
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
                "hobi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": " Baik dan asik",  
                "pesan": "Semangat terus banggg!" # 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya bang Kemas!" # 13
            },
            {
                "nama": "Leonard Andreas Napitupulu",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
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
                "hobi": "Dengar JPP worship",
                "sosmed": "@presiliamg",
                "kesan": "  Pendiam",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat juga!" #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": " Pendiam ",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehattt!!!" # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": " Baik, ramah, asik ",  
                "pesan": "Semangat terus kuliahnya ya bang, sering-sering ngejamming hhe!" # 17
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
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
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": " Baik, ramah, asikk ",  
                "pesan": "Semangat terus kuliahnya ya bang, sehat-sehat teruss dan sukses kedepannya. Btw, saya suka cara bagus abang hhe!" # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": " Baik dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya bang Gede, suksess!" # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": " Ramah banget ",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat teruss!!!" # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya bang Rafly!" # 22
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
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
            "https://drive.google.com/uc?export=view&id=1YsurjBh4J2u0lzl4IKlYzm24bVyorZQW", # bg rafi
            "https://drive.google.com/uc?export=view&id=1A0Qbqk0L3O1FZ9BsUWka8Vg9GQsO1j3J", # ka anova
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg mujadid
            "https://drive.google.com/uc?export=view&id=1e5hMrBsQ_TKZyzE_0CEWjx7bEHLbSE1J", # ahmad sahidin
            "https://drive.google.com/uc?export==view&id=1ZWq-M7bCIuZDSxbsILZLJOQMit-LPbiy", # bg fadhil
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg regi
            "https://drive.google.com/uc?export=view&id=1daSeufwWtQmoN-25F71nOItO6RT5FwLe", # ka syalasisha dina
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg natanael
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg anwar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka deva
            "https://drive.google.com/uc?export=view&id=1La_0n2PqOtgi-jYqNIrEHq9yVU6jmtrV", # ka dinda
            "https://drive.google.com/uc?export=view&id=1djvq5Fkc4h4x442y4jtBtdk-Tv3ZSn8z", # ka marleta
            "https://drive.google.com/uc?export=view&id=10IEgX6BdSmx80cA8s0wndoWanrO9eTTI", # ka rut
            "https://drive.google.com/uc?export=view&id=1jt5_tnzdsDns16IFqHG-EfbfmUK5usCl", # ka syadza
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg abdurrahman
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg aditya
            "https://drive.google.com/uc?export=view&id=1Phc1fTN24m74UtC6vLhO6xORvtjbQjBi", # bg eggi
            "https://drive.google.com/uc?export=view&id=15V7U2kOjXrfX8LGiOBkaxadhomeNMs0L", # ka febiya
            "https://drive.google.com/uc?export=view&id=1Hd0aia3eOHleO6uUzwHSB7aCsPTmSiD_", # bg happy
            "https://drive.google.com/uc?export=view&id=13yKyletbJvRZuhDc7TSmd6p9qKGNaFSS", # bg randa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka vita
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
                "kesan": "Pendiam dan baik  ",  
                "pesan": "Semangat terus kuliahnya ya bang, semoga cepat wisuda hhe!" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat terus!" # 2
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
                "kesan": "  Baik dan ramah",  
                "pesan": "Semangat terus kuliahnya ya bang, sukses kedepannya!" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya bang, tetap sehat!" # 5
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
                "kesan": "Ramah",  
                "pesan": "Semangat terus kuliahnya Kak, suksess kedepannya!" # 7
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
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak Dindaaa!" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat teruss!" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": " Baik dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya kak, semangat semester limanya!" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": " Baik dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya kak Puspa, sehat-sehat teruss!" # 14
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
                "kesan": " Baikk dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya bang, juga semangat terus ngodingnya !" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat terus!" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": " Ramah ",  
                "pesan": "Semangat terus kuliahnya ya bang, sukses kedepannya!" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": " Baik dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya bang, suskes kedepannya!" # 20
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


elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12OsKOQfUaqCfoRABOvvyYUr_Fwk-t7-X", # bg yogy
            "https://drive.google.com/uc?export=view&id=1zJYvWp1TDiRMHvuqU6ZdRZVUGyPguN1-", # ka dhita
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka nazwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg bastian
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka dea mutia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka ester
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka natasya
            "https://drive.google.com/uc?export=view&id=1rXsOpxMaGsjtaVNN7fKujrAnSDkW0tkb", # ka novelia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka ratu
            "https://drive.google.com/uc?export=view&id=16GgiI6hBrH7Y3PDjbmYjCtG7NwkXkikJ", # bg tobias
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka yo
            "https://drive.google.com/uc?export=view&id=1MrYzJ0JXXrKzolLYa2KgLdUIBOKStnIp", # bg rizky
            "https://drive.google.com/uc?export=view&id=1vrfCknMS48n_0NyvXPYiwM0pLNoqotbv", # bg arafi
            "https://drive.google.com/uc?export=view&id=1CnEMxoGCOXlYRbCvC--j7ELmeyD9F8m9", # ka asa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka chalifia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg irvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka izza
            "https://drive.google.com/uc?export=view&id=1ay9Hk3t3F5V9teAjEkefUP94q3Xwzcbe", # ka khaalishah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg raid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka tria


        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "79",
                "asal": "Tangerang",
                "alamat": "Lampung Selatan",
                "hobi": "Nyari Hotwils",
                "sosmed": "@yogyyyyyyy",
                "kesan": "Asikk  ",  
                "pesan": "Semangat terus kuliahnya bang, semoga cepat luluss!"# 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak, semoga suksess!" # 2
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan": "  " # 3
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan": "  " # 4
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "  ",  
                "pesan": "Semangat terus kuliahnya ya kak!" # 5
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
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
                "nama": "Natasya Ega Lina",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan": "  " # 7
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": " Baikk banget ",  
                "pesan": "Semangat terus kuliahnya ya kak, tetap sehatt!" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobi": "Planning konten",
                "sosmed": "@jasminednva",
                "kesan": "  ",  
                "pesan": "Semangat terus kuliahnya ya kak!" # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Membaca",
                "sosmed": "@tobiassiagian",
                "kesan": " Baik dan asikk ",  
                "pesan": "Semangat terus kuliahnya ya bang Tob!" # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Buat Jurnal",
                "sosmed": "@yo_annamnk",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak Yohana!" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "Baik",  
                "pesan": "Semangat terus kuliahnya ya bang, suksess kedepannya!" # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Samping warjo",
                "hobi": "Sholat",
                "sosmed": "@rafiramadhanmaulana",
               "kesan": " Baik dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya bang, sehat-sehat juga!" # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Cari ice breaking",
                "sosmed": "@u_yippy",
                "kesan": "Baik",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat teruss!"# 14 
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Berbuat baik",
                "sosmed": "@chlfawww",
                "kesan": "  ",  
                "pesan": "Semangat terus kuliahnya ya kak!" # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "  ",  
                "pesan": "Semangat terus kuliahnya ya bang!" # 16
            },
            {
                "nama": "Izza Lutfia",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan": "  " # 17
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Lampung",
                "hobi": "Tilawah Al-quran",
                "sosmed": "@alyaavanevi",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kakk, dan tetap sehatt!" # 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Ikut seminar",
                "sosmed": "@rayths_",
                "kesan": "  ",  
                "pesan": "Semangat terus kuliahnya ya bang!" # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Pemda",
                "hobi": "Sholawat",
                "sosmed": "@tria_y062",
                "kesan": " Baik dan asikk ",  
                "pesan": "Semangat terus kuliahnya ya kak Tria!" # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()


elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IBX7BtFPpjIraMnn1OdObDpHOh0iBG1H", # bg dim
            "https://drive.google.com/uc?export=view&id=18SNXJjYUDC0Nd0FiduG1uY4Fljz2dCrB", # ka catherine
            "https://drive.google.com/uc?export=view&id=1eDyNM2Y2nQyDPC5Jby_AkQYc91ArLcrL", # bg akbar
            "https://drive.google.com/uc?export=view&id=1mRO0eb8kQ78aNx4KrpQzqTNQ4KWqQO9m", # ka rani
            "https://drive.google.com/uc?export=view&id=1qATNJ-GLWUi-sZQGHnhSLtfM2KQr00qJ", # bg rendra
            "https://drive.google.com/uc?export=view&id=1QI0RYQqpIiNtsmqDQ6avyLXjGBuW0PF5", # ka salwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka yosia
            "https://drive.google.com/uc?export=view&id=1gwQbfZgUSdfC-y031eJ_F9mEuNUR5n7A", # bg ari
            "https://drive.google.com/uc?export=view&id=1IuCkXkKVB7HSJ-vCzPt7d7E3fSD5V7Te", # ka azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka dearni
            "https://drive.google.com/uc?export=view&id=1R2Qy42G-te_zvJI0IxuRaipVM7R-6IQI", # ka meira
            "https://drive.google.com/uc?export=view&id=12LI-yZ_AaeQ7BwcTaNpu9Kc8mZD8CSFe", # bg rendi
            "https://drive.google.com/uc?export=view&id=1WRguRKxZfAYfb1ZX6mf23FDZtl20LWvE", # ka renta
            "https://drive.google.com/uc?export=view&id=1hE-H0Yhs6rHtzZ9bZ-TkM7LwL052PLD3", # bg josua
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobi": "Nangkep bulu babi",
                "sosmed": "@dimzrky_",
                "kesan": "  Asikk",  
                "pesan": "Semangat terus kuliahnya ya bang, semoga cepat wisudaa hhe!" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak Catherine!" # 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": " Baikk dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya bang Akbar, suksess!" # 3
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobi": "Dengerin Musik",
                "sosmed": "@rannipu",
                "kesan": "Baik",  
                "pesan": "Semangat terus kuliahnya ya kak Rani!" # 4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": " Ramah ",  
                "pesan": "Semangat terus kuliahnya ya bang, tetap sehat!" # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak, suksess kedepannya!" # 6
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"  " # 7
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": " Baik dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya bang, semoga suksess!" # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Asik",  
                "pesan": "Semangat terus kuliahnya ya kak, tetap sehatt!" # 9
            },
            {
                "nama": "Dearni Monica Br Manik",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"  " # 10
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobi": "Nonton film",
                "sosmed": "@meirasty_",
                "kesan": "Baik  ",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat jugaa!" # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya bang, suksess!" # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak Renta!" # 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Siantar",
                "alamat": "Gerbang Barat",
                "hobbi": "Nonton film",
                "sosmed": "@josuapanggabean_",
                "kesan": " Baik dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya bang, semoga sukses kedepannya!" # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17K5cPghvqfcO3glZIlA8Q87tuaTElDAv", # bg andrian
            "https://drive.google.com/uc?export=view&id=1F3Z6mDQsGCrt2YSxRB01KpOUSQbqB0QM", # ka disty
            "https://drive.google.com/uc?export=view&id=1xeU6VMmm0S_Aki-eMs27DIDhnY81guiM", # ka nabila
            "https://drive.google.com/uc?export=view&id=1V4s66aorJ_uOl81DA--4lF_1sHguRam1", # bg ahmad rizqi
            "https://drive.google.com/uc?export=view&id=1uDsKmaRZDRmQMntGX36ijov-bjYuxZsY", # bg danang
            "https://drive.google.com/uc?export=view&id=1SC70uNL6nLI2Pi7-m6L8WWEtPiLAXpCE", # bg farel
            "https://drive.google.com/uc?export=view&id=1SwDQNe-Ip0EMlhqVCMj6R-TSOZFn8y4c", # ka tesa
            "https://drive.google.com/uc?export=view&id=1SwDQNe-Ip0EMlhqVCMj6R-TSOZFn8y4c", # ka nabilah
            "https://drive.google.com/uc?export=view&id=1pjtYSVkK7BRAIsIUu-VxKNQdPLaPCoIl", # ka alvia
            "https://drive.google.com/uc?export=view&id=1iPDcvDl6rLgI4wsMOB4mgOrBdZiOy7_I", # bg dhafin
            "https://drive.google.com/uc?export=view&id=1VBPHRrAVLlLQKfwo0-Oj9zOlj67WvoGU", # ka elia
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": " Baik dan ramah ",  
                "pesan": "Semangat terus kuliahnya bang, semoga cepat lulus!" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": " Ramah ",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat!" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Baik ",  
                "pesan": "Semangat terus kuliahnya ya kak, tetap jaga kesehatan!"  # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya bangg, suksess!!!" # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": " Baik dan asik",  
                "pesan": "Semangat terus kuliahnya ya bang Danang!" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Asikk",  
                "pesan": "Semangat terus kuliahnya ya bang, semoga sukses!"# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": " Baik ",  
                "pesan": "Semangat terus kuliahnya ya kakk!" # 7
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"  " # 8
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviaginting",
                "kesan": " Baik dan ramah ",  
                "pesan": "Semangat terus kuliahnya ya kak, sehat-sehat teruss!" # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Pendiam dan baik",  
                "pesan": "Semangat terus kuliahnya bang!" # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": " Baik dan asikk ",  
                "pesan": "Semangat terus kuliahnya ya kak Meyy!" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w0Wq0TTljx5Y7yLQESQjXceFbjBCYqCF", #bang wahyu
            "https://drive.google.com/uc?export=view&id=1MpvY7mlqQ6eYSXfLEr0ITws99-vCSYmJ", #ka elok
            "https://drive.google.com/uc?export=view&id=1BMxIdlUOC18shXG-9WCsMz3DxI_4Ja1q", #ka arsyiah
            "https://drive.google.com/uc?export=view&id=1s0Liy7px7qmFdetVQm1vTulbXj_fd-QW", #ka cibel
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ka eka
            "https://drive.google.com/uc?export=view&id=1ndyWG3EM-bZb9dlpP694dJtombn_r-KD", #ka najla
            "https://drive.google.com/uc?export=view&id=1tRKN4uU7ZPeuyaPX4JksgDUOIPVrQtfV", #ka patricia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ka rahma
            "https://drive.google.com/uc?export=view&id=13RGppCLH_fD0cEmdEv4HTtuHHIzR8KWl", #ka try yani
            "https://drive.google.com/uc?export=view&id=1OamA-f0bYcUUC0MvDjijKcVuVB4kio_H", #bang kaisar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ka dwi
            "https://drive.google.com/uc?export=view&id=13_U_rmMx_hSRnKmoZtSMQ44aPeYZ5khf", #bang gym
            "https://drive.google.com/uc?export=view&id=1HQcxMHyjKq_lK11-Pvf1Z6PWJ6xV-v0b", #ka nasywa
            "https://drive.google.com/uc?export=view&id=1ZWzUss-OrahcuRHHfsmcTaiakhexoz8_", #ka priska
            "https://drive.google.com/uc?export=view&id=15dTPe1bRy68IKTU0ddO5gdiveizDUZOl", #bang arsal
            "https://drive.google.com/uc?export=view&id=1Xs3XTY4Ys7gmwqKfx6o4DPSa12L_4WFT", #bang abit
            "https://drive.google.com/uc?export=view&id=13_U_rmMx_hSRnKmoZtSMQ44aPeYZ5khf", #bang akmal
            "https://drive.google.com/uc?export=view&id=1W1mCHlhjapPJ-EZa7cHIQwJc_x3MJQjL", #bang mawan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ka khusnun
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
                "pesan":"Semangat semester tujuhnya bangg!"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@Elokviola",
                "kesan": "Baik dan ramah",  
                "pesan":"Semangat kuliahnya kak, sehat-sehat terus!"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Seneng",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "Ramah",  
                "pesan":"Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Baik",  
                "pesan":"Semangat kak!"
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
                "kesan": "Ramah dan lucu",  
                "pesan":"Semangat kak!"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobi": "Shopping",
                "sosmed": "@patriciadiajeng",
                "kesan": "Baik dan ramah",  
                "pesan":"Semangat dan tetap sehat kak"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobi": "Membaca merk mobil",
                "sosmed": "@rahmaneliyana",
                "kesan": "Ramah",  
                "pesan":"Semangat terusss kak!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Ngoding",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Asikk",  
                "pesan":"Semangat kak, tetap sehat!"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Masih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Asik",  
                "pesan":"Semamngat dan tetap kuat kuliahnya bang!"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobi": "Menonton",
                "sosmed": "@dwiratnn_",
                "kesan": "Pendiam",  
                "pesan":"Semangat kuliahnya kak!"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobi": "baca komik",
                "sosmed": "@jimnn.as",
                "kesan": "Baik",  
                "pesan":"Semangat bang jalani kuliahnya!"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobi": "suka bebersih dan denger musik jj",
                "sosmed": "@nsywanaf",
                "kesan": "Ramah",  
                "pesan":"Tetap semangat dan sehat-sehat kak!"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobi": "nonton apapun yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan": "Seruuu dan asik",  
                "pesan":"Tetap semangat kuliahnya kak!"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsalutama",
                "kesan": "Baik dan juga ramah",  
                "pesan":"Tetap semangat bang! Sukses kedepannya!!"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobi": "ngoding dan gaming",
                "sosmed": "@abitahmad",
                "kesan": "lucu dan asik",  
                "pesan":"Semangat terus bang Abit!"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobi": "Main hp",
                "sosmed": "@akmal.faiz",
                "kesan": "Ramah",  
                "pesan":"Tetap semangat kuliahnya bang!"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobi": "baca novel",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Asik",  
                "pesan":"Semangat bang, semoga tetap kuat!"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Ngepel",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Pendiam",  
                "pesan":"Semangat kak untuk kuliahnya!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

