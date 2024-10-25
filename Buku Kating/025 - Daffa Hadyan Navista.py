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
            "https://drive.google.com/uc?export=view&id=1G5AJN4tuNJcYfElNhwtW_l44aJeH4fCQ",
            "https://drive.google.com/uc?export=view&id=1kOcPRmG3YehAjQ9IB9QhzDarMT0zFrUq",
            "https://drive.google.com/uc?export=view&id=1GALxe3gqN_qQRCzUDq_PqmQ8phsyN3L9",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1GA2_e9Vy03J4Ln83W260ZDO86s8FqJkj",
            "https://drive.google.com/uc?export=view&id=1GCAmspaBpCrC-EnSsV5wl2cGfijilZoY",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Kuliah-rapat dan dengerin musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "bang gumi sangat berwibawa dan bijaksana dan kritis dalam berfikir",  
                "pesan":"semangat kedepannya bang him setelah demis dari himpunan jangan lupa bimbingnnya terus bang jangan tinggalin kita"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl Bawean2, Sukarame",
                "hobi": "Bermain gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "bang pandra keren pemikirannya juga kritis tentang keadaan di organisasi",  
                "pesan":"semangat bang pan jangan lupa dengan akademiknya gacor gacor"# 1
            },
            {         
                 "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "senyum kakanya meneduhkan dunia ini masyaallah kak ",  
                "pesan":"semangat dalam segala halnya kakak sekre HMSD gacor gacor"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh",
                "alamat": "Jl Nangka 4",
                "hobi": "Mendengarkan bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "dari mata saya kakak keliatannya jutek tapi baik",  
                "pesan":"semangat kak jangan jutek jutek mukanya kak"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrtfdlh",
                "kesan": "kak titi sangat hemat dalam kata kata",  
                "pesan": "semangat jangan lupa makan kak"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Baca wattpad dan au",
                "sosmed": "@nadillaandr26",
                "kesan": "kak nadila baik lumayan ramah juga",  
                "pesan": "semangat kak jangan lupa istirahat ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FjvcgIH1JxdPm9KLJnH3sSbH73Vhcdme",
            "https://drive.google.com/uc?export=view&id=1FXX0b7IpnvUZRE9McF-bL6VyrMmS7bdd",
            "https://drive.google.com/uc?export=view&id=1FXX3P06Wf5ndn7Uyxl2Ih-80dmN-qlIN",
            "https://drive.google.com/uc?export=view&id=1FctwxIFojQTi51m8BL-lDmgVX7HEIK3b",
            "https://drive.google.com/uc?export=view&id=1FWHpNhOMP9LegU4W5YW0n3j7D2SGcLtL",
            "https://drive.google.com/uc?export=view&id=1FHxLgNXjd6CivXZCEnsQph8vqsTHh7xB",
            "https://drive.google.com/uc?export=view&id=1FHxLgNXjd6CivXZCEnsQph8vqsTHh7xB",
            "https://drive.google.com/uc?export=view&id=1FVxogGIVOmNgslzMTH8SDBCtO69Y2cNI",
            "https://drive.google.com/uc?export=view&id=1FI623y__z2ALytH-xlEgx_J7vTVaApMV",
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
                "kesan": "kak niya lucu suka becanda juga",  
                "pesan": "tetap semangat dalam semua keadaan kak"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Baca buku dan nonton film",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Ka nisa keren asik dan baik",  
                "pesan": "semangat akademiknya kak setelah demis dari HMSD ini"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Jl Raden Saleh",
                "hobi": "Belajar bersama Pa Tamaro",
                "sosmed": "@wlsbn0",
                "kesan": "kak wulan baik cantik dan ramah",  
                "pesan": "apapun keadaannya jangan lupa senyum kak"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Ngobrol",
                "sosmed": "@anisadini10",
                "kesan": "lucu suka becanda juga ramah kerenlah pokoknya",  
                "pesan": "semangat mengejar S.SI.D nya kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@ansftrynn_",
                "kesan": "Kak nisa sedikit pendiam cuman keren dan ramah",  
                "pesan": "semangat kak jangan lupa akademik dan tuhan kak"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "bang fer keren kritis dan rada suka becanda dan usil",  
                "pesan": "semangat bang kritisi segala yang menurutmu tidak sesuai itu bang "# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Solo",
                "alamat": "Natar",
                "hobi": "Suka ditipu sama penjual akun canva premium di shopee",
                "sosmed": "@_.dheamelia",
                "kesan": "kakanya baik lucu ramah dan suka becanda",  
                "pesan": "apapun itu semangat pokoknya kak "# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta, Jawa Tengah",
                "alamat": "Sukarame",
                "hobi": "Badminton, melukis, hiking, dan berenang",
                "sosmed": "@fhrul.pdf",
                "kesan": "abangnya keren baik dan ramah",  
                "pesan": "tetap dengan pendiriannya bang semangat"# 1
            }, 
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Make up, nonton podcast, dan dengerin musik",
                "sosmed": "@berlyyanda",
                "kesan": "ka berli cantik baik kerenlah pokoknya",  
                "pesan": "semangat kakak baik hati dan tidak sombong"# 1
            },         
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vlB29RHITxrYbXf0PvzdtNlpl6ADqN59", # ka luthfi
            "https://drive.google.com/uc?export=view&id=1vka32eiA4wXS2zYNeV-7jM5kSG_dblLP", # bang bintang
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
                "kesan": "Kakak ini asik baik keren",  
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
                "kesan": "sangat sangat berisi dan berilmu",  
                "pesan": "Semangatt kuliahnya bang bintang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg econ
            "https://drive.google.com/uc?export=view&id=1vsCxmrQH0uX-7cNLoqgeuRob3CaE9uDm", # ka abet
            "https://drive.google.com/uc?export=view&id=1w70bgBtGx0iGaILmAu_k6rEVej6CHa_5", # ka pipah
            "https://drive.google.com/uc?export=view&id=1vzE4x0bQ-mltG9bmIjSvTa76xBnQ_04a", # ka allya
            "https://drive.google.com/uc?export=view&id=1vsNlRTX7OrFPBk4Hnli2xljasOYGy6vc", # ka eksanty
            "https://drive.google.com/uc?export=view&id=1w06oVMmxu_Muu7mELXYg7zXVGMgUpsgI", # ka hanum
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg ferdy 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg deri 
            "https://drive.google.com/uc?export=view&id=1vuks_AD-Dv758ZQbdZBe7F15BH3IP2F3", # ka okta 
            "https://drive.google.com/uc?export=view&id=1wPztMdaZBfFC2FxS7Uh5oHd0uS786ONx", # bg deyvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg ibnu farhan 
            "https://drive.google.com/uc?export=view&id=1wP-mKTKZK85ojHL8364l8urbnbMhMEc_", # bg jo
            "https://drive.google.com/uc?export=view&id=1wOclBqBy97X0F5-EePAOvGSJb58MryaJ", # bg kemas
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg leon
            "https://drive.google.com/uc?export=view&id=1wHZYsgRpolMK6_iqQFq9btFWrs6TBpRH", # ka presilia
            "https://drive.google.com/uc?export=view&id=1wChrM064N5f8tGol7684C_xXuaAV_SbB", # ka aqila
            "https://drive.google.com/uc?export=view&id=1wNjdgbGdQpfMr-dsPCeICM_jGc-_6LKw", # bg sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka vanes
            "https://drive.google.com/uc?export=view&id=1w7i7FSe-n9ixszZOb62CIE_1vDHxbfgD", # bg ateng
            "https://drive.google.com/uc?export=view&id=1w9XlFWFKMvS0AFxwpl1QFTGNhO55CHYP", # bg gede
            "https://drive.google.com/uc?export=view&id=1w7liz5PZJLShXipfEz9rwPSfO9NyQrWY", # ka jaclin
            "https://drive.google.com/uc?export=view&id=1wBZ4ixSoqKWqb6gBbwmNkfqNil2UyibT", # bg rafly
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
                "kesan": "Berwibawa dan tegas",  
                "pesan": "Semangatt kuliahnya bang!" # 1
            },
            {
                "nama": "Celisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": " Lucu dan baik ",  
                "pesan":" semangat dalam segala hal kak " # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": " cantik, pintar, dan baik ",  
                "pesan":" semangat kak " # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": " tegas dan keren ",  
                "pesan":" semangat kuliahnya kak alyaa " # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobbi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": " lucu dan suka becanda ",  
                "pesan": " semangat kak NIM 1 " # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": " cantik dan baik ",  
                "pesan": " semangat kak hunam dlam hidupnya " # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobbi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": " pendiam namun pintar ",  
                "pesan": " semangat ca kadepnya bang " # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": " keliatan pendiam tapi ternyata asik ",  
                "pesan": " semangat bang jangan demis yak " # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": " cantik dan baik ",  
                "pesan": " semangat kak okta dalam segala hal " # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": " keren, suka becanda dan baik ",  
                "pesan": " semangat dalam segala hal bang de " # 10
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
                "kesan": " tegas, berwibawa ",  
                "pesan": " semangat dalam segala hal bang jo " # 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": " gacor abang abang kodingan keren ",  
                "pesan": " semangat dalam segala hal bang kem " # 13
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
                "kesan": " cantik,lucu dan baik ",  
                "pesan": " semangat dalam segl hal kak lili " #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": " pendiam, cantik dan pintar dalam nari ",  
                "pesan": " semangat dalam segala hal kak " # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": " baik, pinter gitaran ",  
                "pesan": " semangat dalam segala hal bang sahid " # 17
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
                "kesan": " abang abang pujaan wanita ",  
                "pesan": " semangat dalam segala hal bang ateng " # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": " baik, keren ",  
                "pesan": " semangat dalam segala hal bang gede " # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": " cantik, jago renang ",  
                "pesan": " semangat dalam segala hal kak jaclin " # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": " keren,abang abang bela diri ",  
                "pesan": "semangat dalam segala hal bang raply " # 22
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


# Tambahkan menu lainnya sesuai kebutuhan
