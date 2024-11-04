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
                "pesan": "tegakkan aturan yang benar itu kak semangat"
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
                "pesan": "semangat bang bintang peenerus senator HMSD"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BT0L0hmP_nLTqGm-y-c0i2TA6FcwcRHc", # bg econ
            "https://drive.google.com/uc?export=view&id=1vsCxmrQH0uX-7cNLoqgeuRob3CaE9uDm", # ka abet
            "https://drive.google.com/uc?export=view&id=1w70bgBtGx0iGaILmAu_k6rEVej6CHa_5", # ka pipah
            "https://drive.google.com/uc?export=view&id=1vzE4x0bQ-mltG9bmIjSvTa76xBnQ_04a", # ka allya
            "https://drive.google.com/uc?export=view&id=1vsNlRTX7OrFPBk4Hnli2xljasOYGy6vc", # ka eksanty
            "https://drive.google.com/uc?export=view&id=1w06oVMmxu_Muu7mELXYg7zXVGMgUpsgI", # ka hanum
            "https://drive.google.com/uc?export=view&id=1BP0EIsKOeAiYAUEQ8gXHDx6f1AAEo9qd", # bg ferdy 
            "https://drive.google.com/uc?export=view&id=1BMcG580J_W15dH5oeWV0ga8Yl7yfrz4n", # bg deri 
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
                "hobi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Berwibawa dan tegas",  
                "pesan": " semangat terus bang econ jngan lupa dengan akademik, sering senyum bang econ" # 1
            },
            {
                "nama": "Celisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": " Lucu dan baik ",  
                "pesan": " selalu ceria dan senyum kak abet " # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": " cantik, pintar, dan baik ",  
                "pesan":" lanjutka himpunan kak pipah jangan demis doonggssss " # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": " tegas dan keren ",  
                "pesan":" tetap selalu ceria dan berwibawa kak alya kakak keren " # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": " lucu dan suka becanda ",  
                "pesan": " semangat kak NIM 1, tetaplah senyum terus dan receh terus kak " # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": " cantik dan baik ",  
                "pesan": " semangat kak hunam dlam hidupnya, pantang mundur pokokna kak" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": " pendiam namun pintar ",  
                "pesan": " semangat calon kadepnya bang, harus jadi pokoknya " # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": " keliatan pendiam tapi ternyata asik ",  
                "pesan": " semangat bang derr jangan demis yak " # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": " cantik dan baik ",  
                "pesan": " janga lupa senyum kak okta, semangt kak " # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": " keren, suka becanda dan baik ",  
                "pesan": " bang de gacorr semangat bang, jangan ampe ke recehanmu ilang ya bang de " # 10
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
                "kesan": " tegas, berwibawa ",  
                "pesan": " jnga lupa senyum bang jo, jangan tegang tegang gitu bang, semangat bang " # 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": " gacor abang abang kodingan keren ",  
                "pesan": " semangat yok bang kem banyk project sains data menunggu " # 13
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
                "kesan": " cantik,lucu dan baik ",  
                "pesan": " kak lili janga ampe ilang yaa kak senyummu itu " #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": " pendiam, cantik dan pintar dalam nari ",  
                "pesan": " jangan lppa tetp tersenyum kak, dan humblenya juga kak keren jangan ampe ilang " # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": " baik, pinter gitaran ",  
                "pesan": " semangat kembangkan musik HMSD kita bang " # 17
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
                "kesan": " abang abang pujaan wanita ",  
                "pesan": " jangan kebanyakan cewe bang ateng, inget saya bang bagi satulah " # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": " baik, keren ",  
                "pesan": " semangat kembangkan esport HMSD ni bang " # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": " cantik, jago renang ",  
                "pesan": " jangan menyerah dalam segala yang dilakukan ya kak " # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": " keren,abang abang bela diri ",  
                "pesan": "semangat silatnya bang " # 22
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
            "https://drive.google.com/uc?export=view&id=1z8aAlYIWvvC7GpQHY2g6zu-6c-dLyZhc", # bg rafi
            "https://drive.google.com/uc?export=view&id=1yzXtnrE5PoE5XA99VhvISZ_WCnkOrhf8", # ka anova
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg mujadid
            "https://drive.google.com/uc?export=view&id=1z3hifK2r76aNYx4mUumKGSFWtO9nEGv7", # ahmad sahidin
            "https://drive.google.com/uc?export=view&id=1z1LJ2AuOeI-F8D8YOrFwf2H4EspzXCHl", # bg fadhil
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg regi
            "https://drive.google.com/uc?export=view&id=1z-gp9V0vijze_3Yqg2TWw-tAHgca7AWF", # ka syalasisha dina
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg natanael
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg anwar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka deva
            "https://drive.google.com/uc?export=view&id=1yVhZot_k3iudA2GF0BTLaOgFoudmVFoe", # ka dinda
            "https://drive.google.com/uc?export=view&id=1z-Fy8iEglj9qREo2-T-vdLGIiMGLHuJn", # ka marleta
            "https://drive.google.com/uc?export=view&id=1yWMJW0RyaBiPhzY8bmhWA6YYUkMPBsm1", # ka rut
            "https://drive.google.com/uc?export=view&id=1yVpRfdOSHi5Py2IRoY8qG1_P8FIjBx3p", # ka syadza
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg abdurrahman
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg aditya
            "https://drive.google.com/uc?export=view&id=1z9rUCcEBYELSaGeEi9CGxYvmx4WIHwC4", # bg eggi
            "https://drive.google.com/uc?export=view&id=1yTE-k_lQhXrnAC9KcztKBYNRz55-ko1h", # ka febiya
            "https://drive.google.com/uc?export=view&id=1z4xnlNyTi9YQHjhCM9d8toVpoUnwuxGH", # bg happy
            "https://drive.google.com/uc?export=view&id=1z2sS_CtvGQnvHhAgIgRQDXGggB0QRQEU", # bg randa
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
                "kesan": " baik, keren dan pintar ",  
                "pesan": "tuntaskn akademik itu bang semangat" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": " cantik, baik dan pintar ",  
                "pesan": "apapun rintangan semangat kak" # 2
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
                "kesan": "cool banget, keren", 
                "pesan": "tetap semangat dan jangan patah bang" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": " keren,baik ",  
                "pesan": "semangat dalam segala situasi bang" # 5
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
                "kesan": " cantik,baik dan pintar",  
                "pesan": "bimbing kami kedepannya kak" # 7
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
                "kesan": " cantik, pintar, dan baik",  
                "pesan": "tetap menjadi terbaik kak" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": " baik,cantik,dan pintar",  
                "pesan": "jadilah yang paling gacorr kak" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": " kece,cantik,dan pintar",  
                "pesan": "tetap pertahankan yang sudah baik kak" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": " cantik, dan baik ",  
                "pesan": "jadilah yang terbaik kak" # 14
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
                "kesan": " keren,gaul,dan pintar",  
                "pesan": "semangat dlam belajarnya bang tingkatkan semuanya bang" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": " kakanya baik ",  
                "pesan": "semangat dalam segala hal kak febiya" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": " abangnya keren beut ",  
                "pesan": "tetalah selalu ceria seperti namanya bang" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": " abang serba bisa keren dan pintar ",  
                "pesan": "semangat bang menjadi kadep mikfes ya bang periode selanjutnya" # 20
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
            "https://drive.google.com/uc?export=view&id=1x74ZTLXWQHe1WtMZJtet-MNo7ETtcMAo", # bg yogy
            "https://drive.google.com/uc?export=view&id=1x6aj_hhKZMlRwe4xn52_PQhlQwaAsHbV", # ka dhita
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka nazwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg bastian
            "https://drive.google.com/uc?export=view&id=1wlPsOenDT-CvR-6Qzy0DjAkcw6y1q9t5", # ka dea mutia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka ester
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka natasya
            "https://drive.google.com/uc?export=view&id=1wkNFaJ07BfEOt5gNKesvgK6VZLF133bu", # ka novelia
            "https://drive.google.com/uc?export=view&id=1wo14l0QMBiFvNc6561-FbwUf0vOJTICc", # ka ratu
            "https://drive.google.com/uc?export=view&id=1wi2E8A3QXqSI8J-OAfWHRYOZikshxlHO", # bg tobias
            "https://drive.google.com/uc?export=view&id=1wlgcdrmBUVXcUETRbRqbvRVvHEIKu5qw", # ka yo
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg rizky
            "https://drive.google.com/uc?export=view&id=1wzlRVNfeMokUI9DmuNdhWBYCjwdwyVbi", # bg arafi
            "https://drive.google.com/uc?export=view&id=1wqEoqbrjyXjkOafWEDz6mUZCYqmM9E9k", # ka asa
            "https://drive.google.com/uc?export=view&id=1x-_jdgB6GpfM2MZSUu7f1AL-XGnrtVoa", # ka chalifia
            "https://drive.google.com/uc?export=view&id=1wrgePVnDURYpTFw-inXUmz5aaglYq5CE", # bg irvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka izza
            "https://drive.google.com/uc?export=view&id=1x1HwMzhFE_3bSSUyah01CDDzQ4FNBdy4", # ka khaalishah
            "https://drive.google.com/uc?export=view&id=1wtceYk9Li7wMzQQSWKu3h7684i8-JGvQ", # bg raid
            "https://drive.google.com/uc?export=view&id=1x5pmdSrW-F1UQlaL7lc6u2t91hbMdK4E", # ka tria


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
                "kesan": " abang abang keren inimah, keliatan pendiam cuman suka becanda ",  
                "pesan": "semakin didepan pokoknya bang yogg" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": " baik, cantik ceria ",  
                "pesan": "selalu happy and senyum kak dit" # 2
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
                "kesan": " kakanya baik cantik keren ",  
                "pesan": "jangan cape cape dengan segala urusa kak semangat" # 5
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
                "kesan": " kakanya cantik, tinggi keren ",  
                "pesan": "keep smile kak, semester pasti berlalu kata orang kak" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobi": "Planning konten",
                "sosmed": "@jasminednva",
                "kesan": " kaka kaka pnutan anak humas itera gacorr ",  
                "pesan": "tetap jadi yang keren dan teraik kak" # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Membaca",
                "sosmed": "@tobiassiagian",
                "kesan": " abang gondrong seram tapi suka becanda gacorr bang ",  
                "pesan": "jangan potong rambut ya bang tob" # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Buat Jurnal",
                "sosmed": "@yo_annamnk",
                "kesan": " kakany baik cantik kerenlah pokoknya gacorr ",  
                "pesan": "jadilah yang terseru selalu kak" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": " abangnya keren gacorr lah ",  
                "pesan": "tetaplah menjadi abang abang keren dan cool itu bang" # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Samping warjo",
                "hobi": "Sholat",
                "sosmed": "@rafiramadhanmaulana",
               "kesan": " abangnya gaul baik keren ceria ",  
                "pesan": "semangat dalam segala hal kegiatanya bang arafi" # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Cari ice breaking",
                "sosmed": "@u_yippy",
                "kesan": " kakanya sangat islam banget masyaallah lah gacorr ",  
                "pesan": "pertahankan segala sikap baik mu itu kak kerenn"# 14
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Berbuat baik",
                "sosmed": "@chlfawww",
                "kesan": " kaka pendiam keliatannya cantik gacoorlaah ",  
                "pesan": "jangan lupa jaga kesehatannya kak chalifia" # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": " abang minang saya ini keren abizzz gacorr ",  
                "pesan": "tetap semangat dengang dua kesibkan organisasinya bang" # 16
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
                "kesan": " kakanya baik cantik gacorr",  
                "pesan": "semangat dalam segala hal kak"# 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Ikut seminar",
                "sosmed": "@rayths_",
                "kesan": " abang keren baik gacorrlah ",  
                "pesan": "terslah berkembang dan berkarya bang" # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Pemda",
                "hobi": "Sholawat",
                "sosmed": "@tria_y062",
                "kesan": " kaka baik cantik gacorrlah ",  
                "pesan": "jangan pernah hilang senyum itu ya kak" # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()


elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zhagquiUXDigSAdVh3v8ff3Zdtkqe-63", # bg dim
            "https://drive.google.com/uc?export=view&id=1zHWDH6AmOI1u5ZC2XIpDqP9UJFOAJJbv", # ka catherine
            "https://drive.google.com/uc?export=view&id=1zdckOBFLQFqL-SsIEjrQFoCJnve0Loo2", # bg akbar
            "https://drive.google.com/uc?export=view&id=1zcvkBC4MwtYxgqe_6b5s4JsSmdPbl5a7", # ka rani
            "https://drive.google.com/uc?export=view&id=1zVayCY9pAZcBQzVXzs1vmqMDnqln-VBN", # bg rendra
            "https://drive.google.com/uc?export=view&id=1zSQgto9T38b8pjIiboYt8acZNFdyVLfa", # ka salwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka yosia
            "https://drive.google.com/uc?export=view&id=1zMmCbgT7n2LjBu__nxgrr0dw9UL8MHj-", # bg ari
            "https://drive.google.com/uc?export=view&id=1zI0Ya0xkJRiWWi7QUcUnrpv6ru8_cQvW", # ka azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka dearni
            "https://drive.google.com/uc?export=view&id=1zJ6gWyyAjWlCtf1ttwcGIIkxejYJGApH", # ka meira
            "https://drive.google.com/uc?export=view&id=1zJ9NvHo6GODBZ0n8yswBQUT27ngl4CDc", # bg rendi
            "https://drive.google.com/uc?export=view&id=1zXq1Gqo_3oARtgaIGF1FScDmF0-X6Wrk", # ka renta
            "https://drive.google.com/uc?export=view&id=1zLyrDplZOuIZNDDyTKgNq0P4_E3YhTCR", # bg josua
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
                "kesan": " abang keren ini bagus bnget publik speakingnya organisasinya apalagi gacorrlah ",  
                "pesan": "tetaplah jadi panutan saya dalam organisasi ini bang" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": " kaka cantik,lucu baik suka ketawa lagi ",  
                "pesan": "selalu jadi yang murah senyum dan ketawa kak"# 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": " abang abang keren baik segalanyalah ",  
                "pesan": "stay humble bang akbar" # 3
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobi": "Dengerin Musik",
                "sosmed": "@rannipu",
                "kesan": " kaka mukanya jutek ternyata baik banget keren orangnya kacau gacorr ",  
                "pesan": "tetaplah jadi kak rani yang saya kenal" # 4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": " abang keren ini suaranya bagus ca kahim kata orang wkwk gacorlah ",  
                "pesan": "jangan patah dengan keinginan awalnya bang" # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": " kak baik cantik dan keren gacorrlah",  
                "pesan": "semngat terus pantang menyerah kak" # 6
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
                "kesan": " abang keren baik gacorrlah ",  
                "pesan": "tetapla menyebrkan kebaikan bang" # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": " kakanya baik cantik gacorrlah ",  
                "pesan": "tetaplah dengan pedirianmu kak" # 9
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
                "kesan": " kakanya baik keren manteplah gacorr ",  
                "pesan": "jangan pernah menyerah dalam segala hal kak" # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": " abang keren baik gacoor banget ",  
                "pesan": "jadilah yang paling semangat bang" # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": " kaka cantik baik pinter kerenlah kak ",  
                "pesan": "jangan lupa ketawa ama senyum kak" # 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Siantar",
                "alamat": "Gerbang Barat",
                "hobi": "Nonton film",
                "sosmed": "@josuapanggabean_",
                "kesan": " abang keren baik berilmu gacorrlah ",  
                "pesan": "jangan kalah dengan apapun bang" # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg andrian
            "https://drive.google.com/uc?export=view&id=1yiwJTM98oCV6jxyfN5al_K8LUIQ2VKqy", # ka disty
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka nabila
            "https://drive.google.com/uc?export=view&id=1yg-a330XI4n8Ji-z88inKefqmjGTa_6k", # bg ahmad rizqi
            "https://drive.google.com/uc?export=view&id=1yaWIbyK5LCwenndmS2utubA8NNtySsWk", # bg danang
            "https://drive.google.com/uc?export=view&id=1yfmxNUSe4JQmG-6dBmKhRykHkXEVvL1U", # bg farel
            "https://drive.google.com/uc?export=view&id=1yisseBI8Dbbi8qJvPHQUTEjUHONzyRfP", # ka tesa
            "https://drive.google.com/uc?export=view&id=1yh5i9dxDPFsrcWvouC9R5pUdJyJzcrox", # ka nabilah
            "https://drive.google.com/uc?export=view&id=1yiuiccEkuzPzrQf-FRPHmhVnvEo7wHqp", # ka alvia
            "https://drive.google.com/uc?export=view&id=1yq27j5XTvQpLpudLOYeIFmVyA4NEm-Ro", # bg dhafin
            "https://drive.google.com/uc?export=view&id=1yi0pKBNogYcs-9O-PtDrQTCCnqEMCDcI", # ka elia
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
                "kesan": " bang adrian berwibawa berilmu keren emang abang ini gacorrlah",  
                "pesan": "semangat kembangkan usahanya bang" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": " kakak cantik baik kerenlah gacorrlah",  
                "pesan": "jaga kesehatan dan jangan lupa beribadah kak" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": " kakanya baik banget cantik keren gacorrlah",  
                "pesan": "selalu rendah hati kak"  # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": " abang abang keren cool banget ini ",  
                "pesan": "lakukan yang terbaik untuk menjadi lebih baik bang" # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": " abang keren dan gaul satu ini suka jualan keknya ini langsung ditawarin stiker ama ganci ",  
                "pesan": "jangan sia siakan segala kesempatan" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": " beuh inimah abang capo keren saya ini berwibawa kacau gacorrlah ",  
                "pesan": "lakukan semua hal yang menurutmu benar bang"# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": " kakak cantik baik kerenlah gacorrlah ",  
                "pesan": "jangan takut gagal kak" # 7
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
                "kesan": " kakak cantik baik dan suka menabung sepertinya ",  
                "pesan": "selalu bersyukur atas segala hal yang didapatkan kak" # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": " kakak pintar baik kerenlah pokoknaa ",  
                "pesan": "selalu percaya diri bang" # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": " kakanya ceria abiss , gaul cantik beuh gacor nian inimah  ",  
                "pesan": "selalu ceriakan hari dengan senyumnya kak" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xWBgr5bXhMKSvXTQQ-cvmMc53SBa7Xd6", #bang wahyu
            "https://drive.google.com/uc?export=view&id=1xuCQcw6RQWc9WFfLvkj0ewFwexV3AoRN", #ka elok
            "https://drive.google.com/uc?export=view&id=1xfjhbrceOxuED51gI39d75OCpi6jUVkz", #ka arsyiah
            "https://drive.google.com/uc?export=view&id=1xgX_wWtKGaQsMcFGVVPyY7sVFC_29_Xu", #ka cibel
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ka eka
            "https://drive.google.com/uc?export=view&id=1xkQgyO0XRSUuoDINtZ_sLwvwWMtL_oMa", #ka najla
            "https://drive.google.com/uc?export=view&id=1xTFGbpg8pnxrmBJrUaZZWdDDrNZl0fwC", #ka patricia
            "https://drive.google.com/uc?export=view&id=1xotsZzD_DOXimrMlYQjntiRglzk2lgZW", #ka rahma
            "https://drive.google.com/uc?export=view&id=1xZcDtcObA3DJBjLjm0LycSNsWxrEJ7k1", #ka try yani
            "https://drive.google.com/uc?export=view&id=1xmeiiFi1pAmacQ8mZdBU5HfAOi32uzUf", #bang kaisar
            "https://drive.google.com/uc?export=view&id=1xvL0PP8vTl-4aKskVOnejW-qb-Qv2D5B", #ka dwi
            "https://drive.google.com/uc?export=view&id=1y0ClwTqKn2JM7mGTHxQRYw145C6-_42d", #bang gym
            "https://drive.google.com/uc?export=view&id=1xnctN4rzqfscD-iK-2GMHTMwRAKx1TZa", #ka nasywa
            "https://drive.google.com/uc?export=view&id=1xkh8X0vxp56T1XjIzp6oq_GyhAWYdy7t", #ka priska
            "https://drive.google.com/uc?export=view&id=1y08k4bk0svNH4iGJgdW10BzNVkQfhO14", #bang arsal
            "https://drive.google.com/uc?export=view&id=1xi_pwjZAh52ojvkY2Si60KS_cjFhGFLb", #bang abit
            "https://drive.google.com/uc?export=view&id=1xra2FHwziBUzeuVapjTrILYHTZE5Urbw", #bang akmal
            "https://drive.google.com/uc?export=view&id=1xZh4WSbyf71WtavMnvbbgHo3WBnA3TU2", #bang mawan
            "https://drive.google.com/uc?export=view&id=1xVsTL-U22-3B22YcvAbKPuV2tu1NwMD3", #ka khusnun
        ]

        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobi": "Nonton donghwa",
                "sosmed": "@wayyulaja",
                "kesan": "abangnya seru abiss",  
                "pesan":"semangat dan gigih dalam melakuan sesuatu bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@Elokviola",
                "kesan": "kakanya cantik dan ramah",  
                "pesan":"tetaplah jadi disiri sendiri kak "
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Seneng",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "baik cantik",  
                "pesan":"apapun tantanganya jalani aja kak"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "kakanya cantik banget baik ramah",  
                "pesan":"jangan lupa bahagia tiap harinya kak"
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
                "kesan": "baik, cantik, ramah",  
                "pesan":"jadikan segala kesalahan jadi pembelajran kak"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobi": "Shopping",
                "sosmed": "@patriciadiajeng",
                "kesan": "kakanya sangat sangat baik, ekstrovert parss",  
                "pesan":"jangan pernah pudar senyum itu kak, cerialah setiap saat dengan senyumnya"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobi": "Membaca merk mobil",
                "sosmed": "@rahmaneliyana",
                "kesan": "kakanya ramah dan baik",  
                "pesan":"tetaplah menjadi orang yang random baik dan ramah kak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Ngoding",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakanya cantik, ramah, dan kerenlah",  
                "pesan":"kak jangan jutek gitu kak takut saya"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Masih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "abang gokil ini mah keren humble parah",  
                "pesan":"selesaikan semua ini  bang kaiii"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobi": "Menonton",
                "sosmed": "@dwiratnn_",
                "kesan": "kakanya rada pendiem ",  
                "pesan":"tetaplah jadi disiplin kak"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobi": "baca komik",
                "sosmed": "@jimnn.as",
                "kesan": "abangnya asik, baik kerenlah",  
                "pesan":"kembangkanlah segala skill mu itu bang gym"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobi": "suka bebersih dan denger musik jj",
                "sosmed": "@nsywanaf",
                "kesan": "kakanya seru cantik ama asik",  
                "pesan":"tetaplah jadi yang hebat dan kreatif"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobi": "nonton apapun yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan": "kaknya seru cantik ama asik",  
                "pesan":"tetaplah lemah lembut dan berbakat"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsalutama",
                "kesan": "keren baik ",  
                "pesan":"arahkanlah teman teman kami kedepanya bang"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobi": "ngoding dan gaming",
                "sosmed": "@abitahmad",
                "kesan": "keren banget sangat sangat berpandangan kedepan, gacorrlah",  
                "pesan":"senyumnya jangan pernah ilang bang humblenya juga abangnya keren"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobi": "Main hp",
                "sosmed": "@akmal.faiz",
                "kesan": "baik, pinter, dan ramah",  
                "pesan":"semangat dalam menjalani kedepannya bang"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobi": "baca novel",
                "sosmed": "@hermawan.mnrng",
                "kesan": "abangnya lucu, keren, abis itu pinterlagi",  
                "pesan":"selalulah menebarkkan keceriaan dan ilmu kepada semua orang bng"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Ngepel",
                "sosmed": "@khusnun_nisa335",
                "kesan": "baik, cantik, ramah",  
                "pesan":"selalu jdi yang terbaik yang terkeren dan humble dalam segala situasi kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

