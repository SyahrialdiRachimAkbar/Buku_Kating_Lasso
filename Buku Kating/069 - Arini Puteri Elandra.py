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
            "https://drive.google.com/uc?export=view&id=1hbA-ILDgGlnqYwsVBJCcRSBOZzOxyfX4",
            "https://drive.google.com/uc?export=view&id=1tkATC2BWNGNfLGm2QT-mK6t20sB4TnNm",
            "https://drive.google.com/uc?export=view&id=1c3ROsPZaYiSM0hXB_VuqINwlS4MFNVaZ",
            "https://drive.google.com/uc?export=view&id=1k_7bdYHxD3XUCsMhtZutHM5jrm4DlOOP",
            "https://drive.google.com/uc?export=view&id=1h4zAqwGaTXw6zN7d29vmbYH35PPJfLVj",
            "https://drive.google.com/uc?export=view&id=1p-O1O-AUfT54RMq5v6abicU-3iAuNY3a",
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
                "kesan": "Sesuai dengan namanya berkharisma dan punya wibawa yang tinggi",  
                "pesan":"Semoga selalu dimudahkan dalam segala proses menuju masa depan ya bang!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450127",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Bawean 2, Sukarame",
                "hobi": "Main Gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Bang Pandra orangnya santuy dan asik",  
                "pesan":"Lancar lancar ya bang untuk semua proses yang lagi dikerjakan sekarang"# 1
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
                "pesan":"jaga kesehatan dan semangat menjalani semuanya kak!"# 1
            },
            {   "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobi": "Dengerin Bang Pandra main gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kak putri orangnya asik",  
                "pesan":"jangan bosan dengerin Bang Pandra main gitar ya kak hihi!"# 1
                    
            },
            {   "nama": "Hartiti Fadilah",
                "nim": "121450021",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrdfdlh",
                "kesan": "kak titi orangnya pendiem sekali ternyata",  
                "pesan":"ayoo kakak semangat jangan diem diem ya kakak!"# 1

            },
            {   "nama": "Nadila Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Gangguin Kak Liza Tidur, baca Wattpad/AU",
                "sosmed": "@nadillaandr26",
                "kesan": "kak nadila orangnya asik dan suka bercanda",  
                "pesan":"be happy kak, people's happy around you!"# 1

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1isqVgo0L5Q15GkWiUqBbevDgCacg63Mf",
            "https://drive.google.com/uc?export=view&id=1Vc0pUWuhiaQ-ZLktSClRYKbgNPx9LVrj",
            "https://drive.google.com/uc?export=view&id=1maalzyRfBS9O53vsZ_ex9LJSJVFZQ5Yg",
            "https://drive.google.com/uc?export=view&id=1bSAvJehOzCEW07hUxsCE8gGjd552z_AC",
            "https://drive.google.com/uc?export=view&id=1tZ_SKEzJbuovgFv9N8_kKwsG0hy6-uHh",
            "https://drive.google.com/uc?export=view&id=196zcLVySIFxj7bWw2iH35BaXypApRwRx",
            "https://drive.google.com/uc?export=view&id=14eDsio-DpnQdVgtV85lEuw38suMhvkP4",
            "https://drive.google.com/uc?export=view&id=1JBzfyfC0ycwa2cfiITP5uvXmLpVODWqR",
            "https://drive.google.com/uc?export=view&id=1patICp8Zy8S3ONNypyJ_4yOTIj2P_MDT",
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
                "pesan":"semester 7 katanya semester yang berat nih kak, ayoo kak lebih semangat disemester ini!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Baca buku dan Nonton film.",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kak Nisa baik hati terus asik",  
                "pesan":"keep humble kakak, semangaat!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Belajar bersama Pak Tamaro.",
                "sosmed": "@wlnsbn0",
                "kesan": "Kak Wulan kakak yang aktif dan seru diajak ngomong",  
                "pesan":"keep up your spirit kakk!"# 1
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
                "pesan":"semangaat dan sehat selalu ya kakak, jangan sampai sakit ya kak!"# 1
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
                "pesan":"semangaat menempuh semester 5 nya kak, katanya semester 5 ini semester yang sibuk loh kak, semangat!"# 1
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
                "pesan":"semangat dalam keseharian, perkuliahan dan be happy selalu kak!"# 1
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
                "pesan":"semoga apa yang kita pelajarin di erpeel bisa dimanfaatkan dengan baik yaa kak disini, aamiinn!"# 1
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
                "pesan":"semangat selalu bang baik dalam keseharian maupun perkuliahan!"# 1
            },
           {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Baca Buku",
                "sosmed": "@fr_yulius",
                "kesan": "bang fery pendiam tapi sering ketawa nih",  
                "pesan":"semangat semester 5 nya ya bang, may God always bless u bang!"# 1
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
            "https://drive.google.com/uc?export=view&id=1eKZr7burmiS8lW7I6mBKmkLdiwR8Novp",
            "https://drive.google.com/uc?export=view&id=1o1PEx7V8nb8EdbgEipcxhXW_-YHz_JTM",
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
                "pesan": "Semangat terus kuliahnya ka luthfi! Jangan sampai patah semangat apalagi sampai menyerah, be happy selalu kakak!"
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
                "pesan": "keep your spirit and keep santuy bang~!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KZ-rMOhKQP6XeLMpsUqqEFNK56SP1DIQ",
            "https://drive.google.com/uc?export=view&id=11ULWumnR-QzM3dzeKO1Qrssy4pZ8dc0G",
            "https://drive.google.com/uc?export=view&id=1hlQPqSCBr6aSuWW2co0E86vKv1LxqK0v",
            "https://drive.google.com/uc?export=view&id=1_PvWEqPXxFFPrR5RYuGfMudtbwK0W0Dz",
            "https://drive.google.com/uc?export=view&id=1YNdUY14dl7LAPmhf-c_hArJnhvRmBYVS",
            "https://drive.google.com/uc?export=view&id=11xsY8nvkd1wcYfsdoogkakqiLG82Z3uz",
            "https://drive.google.com/uc?export=view&id=1AjW842H_gOLJNAt_MA9KFhRP7RKew_9p",
            "https://drive.google.com/uc?export=view&id=1nMI9eAK-3j9x7BiWvdrb6eInRhkNjQJi",
            "https://drive.google.com/uc?export=view&id=1R1JcQwpeHhAemQVUiTAcoXZoz7dyUXdR",
            "https://drive.google.com/uc?export=view&id=1Uvp1T6nRTKKQpBpWIMyxtN4r5uyZ0ipb",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1nGMCbnQ7V_WgsxOYppaXyVZTUxk6tg16",
            "https://drive.google.com/uc?export=view&id=12XwmGh5XKn40_c5kjc0YnkTrhLv3C3Ue",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=11dTunTSl3tH44t0b5comUjbOFwqJUYzx",
            "https://drive.google.com/uc?export=view&id=1mGEeBTcpRwC-T9Le93udnFJuKYvxvNgN",
            "https://drive.google.com/uc?export=view&id=1lN0fQTyTOFLJMAil3JkBjNmWeBt-KvN7",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1_hcyfwKFBOCVYVFLIqUlYNjLmM4fncAW",
            "https://drive.google.com/uc?export=view&id=1F2-FwvNzAhTWwl8qpbm_LLHj6rt-27lr",
            "https://drive.google.com/uc?export=view&id=1Rh7yWj5qQiYxJFBONzuA3my7rC1W331H",
            "https://drive.google.com/uc?export=view&id=1TVnDrpim-1Nn_D3HGl68GIR7M0PPyDya",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "abang yang baik, berwibawa dan tegas",  
                "pesan": "keep up your spirit bang! stay berwibawa!" # 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "kak abeth orangnya ramah sekalii",  
                "pesan":"semangat menempuh semester 5 dengan segala kegiatan dan perkuliahannya kak abeth!" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakak pipah cantik sekalii",  
                "pesan":"semangat kuliahnya kak pipah! be happy and stay awesome kak!" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": "kakak tegas tapi diluar itu asik",  
                "pesan":"kakak keren banget kak! bisa tegas dan asik disaat yang bersamaan" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": "kak eksan kakak yang baik sekali",  
                "pesan": "semangat menempuh kuliahnya kak eksan! konon katanya disemester 5 ini banyak kegiatan loh kak! semangat!" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakak ini baik banget",  
                "pesan": "semangat kuliahnya kak hanum! be happy selalu kakak!" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "bang ferdy abang yang pendiam tapi tegas",  
                "pesan": "semangat kuliahnya bang ferdy! semangat juga futsalnya ya bang!" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": "bang deri pun abang yang pendiam tapi tegas",  
                "pesan": "tetap semangat dalam keseharian dan perkuliahan ya bang, semoga selalu dilancarkan!" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": " kak okta ini kakak yang baik dan asik",  
                "pesan": "semangat kuliahnya kak okta! semoga selalu dipermudah dalam berproses ya kak!" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "abang yang humoris dan murah senyum",  
                "pesan": "semangat kuliahnya bang D! keep up your spirit and be happy bang!" # 10
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
                "kesan": "abang yang punya sifat tegas tapi juga asik",  
                "pesan": "semoga selalu dipermudah oleh Tuhan dan semangat selalu bang jo!"# 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": "bang kemas abang yang baik, pinter dan ramah",  
                "pesan": "semangat kuliahnya bang kemas! keep humble selalu!" # 13
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
                "kesan": "kak presilia kakak yang baik dan cantik",  
                "pesan": "semangat kuliahnya and be happy always kak presilia!" #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "kakak ini kakak yang baik, cantik, dan pendiam",  
                "pesan": "semangat kuliahnya kak rafa! keep up your spirit and be happy kakak!" # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "abang sahid ini abang yang baik dan asik",  
                "pesan": "semangat kuliahnya dan be happy always bang sahid!" # 17
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
                "kesan": "ini abang yang ramah, baik dan juga humoris",  
                "pesan": "semangat kuliahnya bang ateng! keep humble and be happy selalu!" # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "yang ini abang yang baik dan humoris",  
                "pesan": "semangat untuk segala kegiatan dan kuliahnya di semester ini dan seterusnya ya bang gede!" # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "kakak ini kakak yang baik, cantik dan ramah sekali",  
                "pesan": "semangat selalu ya kak dalam keseharian dan perkuliahannya, semoga selalu diberi kemudahan ya kak!" # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "bang rafly ini abang yang baik dan asik",  
                "pesan": "semangat ya bang rafly baik dalam kegiatan perkuliahan maupun diluar perkuliahan, keep up you spirit bang!" # 22
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
            "https://drive.google.com/uc?export=view&id=1yY9to5AzNf2EBa5MZ1idmlgFKJuPHyOB",
            "https://drive.google.com/uc?export=view&id=1DTBhU_E_WS-TFJp5ljIYJ-Wb3mZqRP3Q", 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1eMI13ngZ7_Ec5K8ZPUq1fDiZDsp2oVvp",
            "https://drive.google.com/uc?export=view&id=1zGOvHbztGUQOm6V0Iw2jNBLALwOPBAHJ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1iNhXkFSZRt2pk_bWSxDsMojRyikI__kM",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1QnwFsepuA4uFZRnN7dDb74fxo4mcq-RW",
            "https://drive.google.com/uc?export=view&id=1l2n3QnvFywTOC42q596_jruem4bDQLfe",
            "https://drive.google.com/uc?export=view&id=1Z67z7Ed0nJTiBls193qCb4oi7Ey8LivJ",
            "https://drive.google.com/uc?export=view&id=1uaDIhtnaUoIrv0XSXMtMG4rGIFUg7g7m",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1YG1f9b8Dyt6bLCcTRqamVlX_NH1gg0MX",
            "https://drive.google.com/uc?export=view&id=1fJc_JzW8mDspctCnxPFC1OacZYWdmXAA",
            "https://drive.google.com/uc?export=view&id=1_F6xIomFpt_owoL33Q20N4EHaMsQTBKJ",
            "https://drive.google.com/uc?export=view&id=1zvafsNyJoABCMsUq0u0HkTb0-DOQYRMB",
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
                "kesan": "bang rafi ini abang yang berwibawa, baik",  
                "pesan": "Semangat dalam keseharian, olahraga dan kuliahnya bang rafi!" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakak yang baik dan ramah",  
                "pesan": "Semangatt kuliahnya Annisa! jangan lupa jaga kesehatan selalu ya kak!" # 2
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
                "kesan": "abang yang baik dan asik",  
                "pesan": "Semangatt kuliah dan olahraganya bang! keep up your spirit!" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "bang fadhil ini abang yang baik, asik",  
                "pesan": "Semangatt kuliahnya bang fadhil di semester 5 yang katanya sibuk ini!" # 5
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
                "kesan": "kakak kembar, lucu sekalii",  
                "pesan": "Semangatt kuliahnya kak andina! be happy selalu dan jaga kesehatan ya kakak!" # 7
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
                "kesan": "kak dinda itu kakak yang baik dan ramah ",  
                "pesan": "Semangatt menjalani semester 5 perkuliahannya kak dinda! jangan lupa jaga kesehatan ya kak!" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kakak ini baik, cantik, ramah, dan dia asprak strukdat RC!",  
                "pesan": "Semangatt ya kak menjalani kuliahnya dan semangat meng-aspraknya ya kak marleta!" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kak junita ini baik dan ramah",  
                "pesan": "Semangatt kuliahnya kak junita! selain semangat kuliahnya, jangan lupa jaga kesehatan ya kak!" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "kak syadza itu kakak yang baik dan ramah",  
                "pesan": "Semangatt kuliahnya kak syadza! be happy and always be kind!" # 14
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
                "kesan": "bang eggi ternyata abang yang baik, ramah",  
                "pesan": "Semangatt kuliahnya bang eggi jangan menyerah dan be happy!" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "kak febiya ini kakak yang baik dan ramah",  
                "pesan": "Semangatt kuliahnya kak febi! be happy dan jaga kesehatan ya kak disemester ini dan selanjutnya!" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "abang yang ramah",  
                "pesan": "Semangatt dalam perkuliahannya ya bang syahrul! be happy selalu bangg!" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "abang yang ramah, tinggi",  
                "pesan": "Semester 5 katanya semester yang padet jadwalnya nih bang, semangat selalu ya bang!" # 20
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
            "https://drive.google.com/uc?export=view&id=1ZYwoG2rosRV7891KzVuuppxHhP97Gbgy",
            "https://drive.google.com/uc?export=view&id=14UCNKBDSkwihwIOgPU0vynpcHDfojE5H",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=14nTSKAaRfXX9EnlO2RkUgrQZDSVc8qDr",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1SutBGrgC2IkRBgHAaZEquvegTFO_p_jr",
            "https://drive.google.com/uc?export=view&id=1VAiQtqwIyOq_64GeZ_t0hfqyURt3sOrV",
            "https://drive.google.com/uc?export=view&id=1G59NKwSKdRLaScvEu5aHo54YWWaWZ-Qi",
            "https://drive.google.com/uc?export=view&id=1-u3KlLL6kzwd0MjPJbCepzrf3lyd1Zsy",
            "https://drive.google.com/uc?export=view&id=1C1kPEtyU0DL1zyNEjCW8Jp1juw5Z5r1U",
            "https://drive.google.com/uc?export=view&id=1c0TNsnySX9n0lOzaDXVkIFmu8OkakPlK",
            "https://drive.google.com/uc?export=view&id=1rFDYU0WxxZtE0wsA78pW0r38yUVwDY4z",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1G-TU9w9EnMiV9xDFMJLAcR84KRvQk_7F",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1cLNT7Mf9W7wIpgaeHEX2TKUSTx-sba8I",
            "https://drive.google.com/uc?export=view&id=1jLGFI8g-cAgdRMggzCe6_ClDvg_vM-jM",
            "https://drive.google.com/uc?export=view&id=1I2LDcDZokzDzfr8z73rcGiv9ZWdMJkN9",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "79",
                "asal": "Tangerang",
                "alamat": "Lampung Selatan",
                "hobi": "Nyari Hotwheels",
                "sosmed": "@yogyyyyyyy",
                "kesan": "abang yang baik, humoris, ramah",  
                "pesan": "Semangatt kuliahnya bang yogy! dan semoga dapet hotwheels yang rare ya bang! semangat hunting hotwheelsnya bang!" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "kakak yang ini baik, cantik dan ramah",  
                "pesan": "Semangatt kuliahnya kak dhita! semangat juga menemani bang yogy hunting hotwheels hihi!" # 2
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
                "kesan": "kakak ini kakak yang baik, cantik dan humble",  
                "pesan": "Semangatt kuliahnya kak dea! always be humble kakakku!" # 5
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
                "kesan": "kakak yang ini sudah baik, cantik juga",  
                "pesan": "Semangatt kuliahnya kak novelia! jangan lupa untuk jaga dan utamakan kesehatan dan kebahagiaan kakak ya!" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobi": "Planning konten",
                "sosmed": "@jasminednva",
                "kesan": "kalo kakak yang ini ramah sekalii",  
                "pesan": "Semangatt menjalani perkuliahannya kak jasmine! be happy and stay humble ya kak!" # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Membaca",
                "sosmed": "@tobiassiagian",
                "kesan": "abang ini baik, ramah dan tegas",  
                "pesan": "Semangatt menjalani semester 5 dan seterusnya bang tob! keep up your spirit!" # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Buat Jurnal",
                "sosmed": "@yo_annamnk",
                "kesan": "baik, cantik, tegas, daplok pplk-ku tercinta",  
                "pesan": "Semangatt menjalani perkuliahannya kak yow! semoga selalu dilancarkan dalam segala proses ya kak!" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abang yang baik dan seru",  
                "pesan": "Semangatt menjalani semester 5 nya bang rizki! semangat juga untuk semester selanjutnya ya bang!" # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Samping warjo",
                "hobi": "Sholat",
                "sosmed": "@rafiramadhanmaulana",
               "kesan": "abang abang yang baik, ramah, seru juga",  
                "pesan": "Semangatt kuliahnya bang rafi! be happy and keep up your spirit!" # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Cari ice breaking",
                "sosmed": "@u_yippy",
                "kesan": "baik dan lumayan pendiam sepertinya",  
                "pesan": "Semangatt kuliahnya kak uyi! semoga bisa menemukan ice breaking yang seru ya kak!"# 14
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Berbuat baik",
                "sosmed": "@chlfawww",
                "kesan": "yang ini kakak yang baik dan ramah",  
                "pesan": "Semangatt kuliahnya kak lifia! jangan patah semangat apalagi sampai menyerah!" # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "abang yang baik dan seru",  
                "pesan": "Semangatt kuliahnya bang irvan! semoga semester 5 ini dan seterusnya lancar ya!" # 16
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
                "kesan": "ini kakak yang baik, cantik dan ramah",  
                "pesan": "Semangatt dan semoga istiqomah dalam tilawah Al-Quran ya kak!"# 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Ikut seminar",
                "sosmed": "@rayths_",
                "kesan": "abang yang baik dan seru",  
                "pesan": "Semangatt kuliahnya bang raid! semoga bisa mengikuti seminar yang abang inginkan ya!" # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Pemda",
                "hobi": "Sholawat",
                "sosmed": "@tria_y062",
                "kesan": "kakak ini baik dan cantik terus ramah juga",  
                "pesan": "Semangatt kuliahnya kak yuna! semoga konsisten dalam sholawatnya ya kak!" # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()


elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ruZPGUAs1wQoBLxmZwaG-yyJcRwp--YZ",
            "https://drive.google.com/uc?export=view&id=1EvCA0oHDz1l3zHjYH6mTQSy2SZN3DiYd",
            "https://drive.google.com/uc?export=view&id=18iRi9mD6jaLMs0OlSYFTyKXQ8LuxlUvh",
            "https://drive.google.com/uc?export=view&id=1Xv_JNVpnFeBaIQIx3IVjVXb60I13YLWL",
            "https://drive.google.com/uc?export=view&id=1udoHFG8jOZjA7gxJPxHaMbaCjpnQyS5q",
            "https://drive.google.com/uc?export=view&id=1Vk5bLZLmiHh7fz-QhqGLt7g-dLS6JqsF",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1iuhgTxRh6c8T_rpJkAYuKKHcfKIC1ZaF",
            "https://drive.google.com/uc?export=view&id=1i15Yc9kgzVcv8RtlmNCtrXvX6T39FdfU",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1A-HSkIPEoU8g0uD0SkplxlrgRA8bwR3g",
            "https://drive.google.com/uc?export=view&id=1nwJouRelU4cksq4eLb9QQLK2sYXjTwGt",
            "https://drive.google.com/uc?export=view&id=1v7sgShQwbSXRdlFgjjZoS47cDi4IRK4r",
            "https://drive.google.com/uc?export=view&id=1RAwb_DdouzdFct2u5gyhpIRK9in3kQkX",
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
                "kesan": "bang dimas abang yang baik, humoris, seru dan lucu",  
                "pesan": "Semangatt kuliahnya bang dimas! semoga disemester ini dan selanjutnya dilancarkan dan bisa lulus tepat waktu ya!" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "kakak yang baik, cantik dan suka ketawa",  
                "pesan": "Semangatt kuliahnya ya kak catherine! semoga kakak bisa menyelesaikan novel favorit kakak ya!"# 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": "bang akbar ini abang yang ramah dan seru",  
                "pesan": "Semangatt kuliahnya bang akbar! semoga bisa dapet ikan cupang yang abang inginkan ya bang!" # 3
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobi": "Dengerin Musik",
                "sosmed": "@rannipu",
                "kesan": "kakak yang baik dan tegas",  
                "pesan": "Semangatt kuliahnya ya kak rani! semoga disemester ini dan kedepannya dapat hasil yang maksimal ya kak!" # 4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "baik, seru, asprak strukdatku juga",  
                "pesan": "Semangatt kuliahnya bang rendra! dan semangat meng-aspraknya ya bang!" # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "kakak ini kakak yang baik dan cantik, plus seru juga",  
                "pesan": "Semangatt kuliahnya kak salwa! semoga selalu diberi kelancaran dalam tiap proses ya kak!" # 6
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
                "kesan": "abang ini abang yang baik, ramah dan abang nimku juga",  
                "pesan": "Semangatt kuliahnya bang ari! semoga disemester ke-7 ini dapat hasil yang maksimal dan semoga abang bisa lulus tepat waktu ya bang!" # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "kakak yang baik, terus ramah, dan seru juga",  
                "pesan": "Semangatt kuliahnya ya kak zizah! semoga kakak selalu diberi kelancaran ya kak baik dalam kuliah ataupun diluar kuliah!" # 9
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
                "kesan": "kakak ini baik dan ramah",  
                "pesan": "Semangatt kuliahnya ya kak meira! selain itu semangat dalam menjelajah film film ya kak hihi!" # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": "abang ini baik, lalu ramah, terus seru juga",  
                "pesan": "Semangatt kuliahnya bang rendi! keep humble dan be happy bang!" # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": "kak renta kakak yang baik, lucu dan menggemaskan",  
                "pesan": "Semangatt kuliahnya ya kak renta! keep up your spirit and i wish u all the best untuk semester ini dan seterusnya kak!" # 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Siantar",
                "alamat": "Gerbang Barat",
                "hobi": "Nonton film",
                "sosmed": "@josuapanggabean_",
                "kesan": "bang josua abang yang baik, seru dan ramah juga",  
                "pesan": "Semangatt kuliahnya bang josua! semoga disemester ini abang dilancarkan dan begitupun disemester - semester berikutnya ya bang!" # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rbhUDx1BM5_GRvpcldhmUjV26zBmLSLb",
            "https://drive.google.com/uc?export=view&id=1G5PodPj6fPQ26B9boMsoqWelvs97kTns",
            "https://drive.google.com/uc?export=view&id=1_T-N6vW07JzS0U-AkucSTomygGIMEg-q",
            "https://drive.google.com/uc?export=view&id=1cYqbM9cvMRCdBG0M749M23VdJx5w4fL6",
            "https://drive.google.com/uc?export=view&id=1Q_Ni-2GwQ3MtchXddVviP-9tQWbmn3jM",
            "https://drive.google.com/uc?export=view&id=11Y2G3g6a1LgiFf0dPk82E3IxCTl9dppt",
            "https://drive.google.com/uc?export=view&id=1JFI6AaHLlG-r_-_1JtxZ-jCmYC4Ey-XL",
            "https://drive.google.com/uc?export=view&id=1ipFbH4MXRFFLR8F2fLXlj8Pq47lcCPSS",
            "https://drive.google.com/uc?export=view&id=16wVVh_AejoiT2hIGeFomDXC4DiwsHOwa",
            "https://drive.google.com/uc?export=view&id=1CrQJt12g8y7m43N1VRlQnhXMeoYZmH93",
            "https://drive.google.com/uc?export=view&id=1h1OchojZXh5HAnhPpZEcNSPTPfEPy3Iz",
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
                "kesan": "abang andrian ini selain baik, beliau juga seru",  
                "pesan": "Semangatt kuliahnya bang andrian! keep up your spirit bang, jangan sampai putus asa apalagi sampai menyerah!" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "kakak yang bukan cuma baik dan cantik, tapi juga ramah",  
                "pesan": "Semangatt kuliahnya kak adisty! semoga kakak bisa menjalani semester ini dan kedepannya dengan lancar dan bisa lulus tepat waktu ya kak!" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobi": "Menghitung",
                "sosmed": "@zhjung",
                "kesan": "kakak yang baik dan juga ramah",  
                "pesan": "Semangatt kuliahnya kak nabila! selain semangat jangan lupa untuk jaga kesehatan dan be happy kak!"  # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": "abang yang baik dan ramah",  
                "pesan": "Semangatt kuliahnya bang rizqi! selain soal akademik, semangat juga ya bang dalam menjalankan hobi abang!" # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "bang danang abang yang baik dan tinggi",  
                "pesan": "Semangatt kuliahnya bang danang! semangat juga ya bang dalam membacanya!" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "bang farrel abang yang baik, tegas dan juga seru",  
                "pesan": "Semangatt kuliahnya bang farrel! bang farrel apapun hobinya semangat ya bang menjalaninya!"# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "kak tessa kakak yang baik, cantik dan ramah",  
                "pesan": "Semangatt kuliahnya ya kak tessa! selain kuliah, semangat juga dalam menulis kak tessa!" # 7
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
                "kesan": "kakak ini kakak yang baik dan juga ramah",  
                "pesan": "Semangatt kuliahnya ya kak alvia! semoga nonton windah bisa menghilangkan jenuh dan lelahnya kakak ya!" # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abang yang baik dan seru",  
                "pesan": "Semangatt kuliahnya bang dhafin! semoga disemester 5 yang katanya padet ini masih ada waktu untuk bisa istirahat ya bang!" # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "kak elia kakak yang baik, ramah dan seru",  
                "pesan": "Semangatt kuliahnya kak elia! semoga kakak diberi kemudahan dalam perkuliahan, keseharian dan juga dalam bermain badmintonnya ya kak!" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dBud41Mue4JI229iRwDUlljFdxMb0B0f",
            "https://drive.google.com/uc?export=view&id=1mIpqQ7kVPbIv0k37iju29_KJYRnwr5Dp",
            "https://drive.google.com/uc?export=view&id=1zIt5GD2hqsGsgICVMtf3gxV4A71Q7aLy",
            "https://drive.google.com/uc?export=view&id=15kgVkQpjJcrNzNqGq9tdNAvubgNKsl1l",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #0
            "https://drive.google.com/uc?export=view&id=1Nx9mEGhhXMIBrHCf9c46BxE10_ElxQ6q",
            "https://drive.google.com/uc?export=view&id=1EA-BugN4DMCXn3blPXrqPJ9QjKtYtQ3P",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak nely?
            "https://drive.google.com/uc?export=view&id=1dkS6SrewVYNtLkmB5xNn3dN2eWYl5BVs",
            "https://drive.google.com/uc?export=view&id=1DKmZO7IliU7Z-Cd31BeBtelZjOQuFPE1",
            "https://drive.google.com/uc?export=view&id=1ww_HPCjYwHuztZf9zTOiFZPpsO0cla5v",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang gym?
            "https://drive.google.com/uc?export=view&id=1mmcFAtTRMGiNMI4exyY05kFX82m2p1eA",
            "https://drive.google.com/uc?export=view&id=1QOMPfrwyRg9wfxYx9YClw1HxxJS_7OhR",
            "https://drive.google.com/uc?export=view&id=19LlU61RM-fsIUC8NCFXznXte9lDn7PmD",
            "https://drive.google.com/uc?export=view&id=12OxBzsn3j0HJ02CWIHS8XDj7pWeWUOIx",
            "https://drive.google.com/uc?export=view&id=1ltAGnv0JIZJBWboUY1CIoX1evpMjdj5K",
            "https://drive.google.com/uc?export=view&id=1x3kTmr9VE4T4yGiaFLeaPfiqnBtDfkxg",
            "https://drive.google.com/uc?export=view&id=15zq4KiTok5wFALBsuKuF1UsBsn_lfOzn",
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
                "kesan": "abang yang baik, ramah dan menyenangkan",  
                "pesan": "semangat kuliahnya bang wahyu! semoga diberi kelancaran dan bisa lulus tepat waktu ya bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@Elokviola",
                "kesan": "kakak yang baik, ramah dan cantik sekali?!",  
                "pesan": "semangat kuliahnya kak elok! semoga kakak disemester ini dan selanjutnya diberi kemudahan selalu ya kak dalam menjalani perkuliahan maupun keseharian!"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Seneng",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "kakak yang baik dan cantik terus juga ramah",  
                "pesan": "semangat kuliahnya kak zahra! semoga kakak bisa diberi kelancaran dalam kuliah dan ngontennya ya kak!" #3
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "kakak yang baik, ramah, dan ternyata kami sama sama anak teluk",  
                "pesan": "semangat kuliahnya kak cibel! semoga kakak selalu diberi kelancaran dan kemudahan ya kak!"
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
                "pesan": " "
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Nulis, baca, ngefangirl",
                "sosmed": "@nanana.minjoo",
                "kesan": "kakak yang baik dan cantik lalu ramah",  #6
                "pesan": "semangat ya kakak dalam menjalani perkuliahan dan kesehariannya, semoga selalu diberi kelancaran ya kak!"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobi": "Shopping",
                "sosmed": "@patriciadiajeng",
                "kesan": "kakak yang baik, cantik, ramah, dan suaranya menggemaskan",  
                "pesan": "semangat kuliahnya kak cia! keep humble and be happy always kak cia!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobi": "Membaca merk mobil",
                "sosmed": "@rahmaneliyana",
                "kesan": "kakak yang ini baik dan ramah sekaliii",  
                "pesan": "semangat kuliahnya kak neli! selain semangat, jaga kesehatannya selalu ya kak!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Ngoding",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakak yang baik dan cantik, dan ini kakak pj tugasku tercintaa",  
                "pesan": "semangat kuliahnya kak ciaa! semoga kakak selalu diberi kelancaran ya kak baik dalam kuliah, keseharian atau dihobi kakak yaitu ngoding!" #9
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Masih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "bang kaisar ini abang yang baik dan ramah",  
                "pesan": "semangat kuliahnya bang kaisar! keep up your spirit and keep humble bang kaisar!"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobi": "Menonton",
                "sosmed": "@dwiratnn_",
                "kesan": "kak dwi itu kakak yang baik, cantik dan ramah",  
                "pesan": "semangat kuliahnya kak dwi! selain semangat dalam kuliah, semangat juga dalam menontonnya ya kak semoga bisa ketemu film yang kakak suka!"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobi": "baca komik",
                "sosmed": "@jimnn.as",
                "kesan": "abang yang baik, ramah dan humble",  
                "pesan": "semangat kuliahnya bang gym! semoga abang diberikan kelancaran ya bang disemester ini dan selanjutnya!" #12
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobi": "suka bebersih dan denger musik jj",
                "sosmed": "@nsywanaf",
                "kesan": "kakak ini kakak yang baik, ramah dan cantik",  
                "pesan": "semangat kuliahnya kak nasywa! be happy and keep humble kakak!"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobi": "nonton apapun yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan": "kak priska ini kakak yang baik, cantik dan juga ramah",  
                "pesan": "semangat kuliahnya kak priska! semoga kakak bisa menjalani tahun ini dengan lancar dan bisa lulus tepat waktu ya kak!"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsalutama",
                "kesan": "bang arsal ini abang yang baik dan ramah",  
                "pesan": "semangat kuliahnya bang arsal! untuk bang arsal semoga abang bisa lulus tepat waktu dan dilancarkan ya bang dalam segala prosesnya!" #15
            },
            {
                "nama": "A'bit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobi": "ngoding dan gaming",
                "sosmed": "@abitahmad",
                "kesan": "abang yang baik, ramah dan menyenangkan",  
                "pesan": "semangat kuliahnya bang abid! semoga abang bisa selalu jadi abang yang humble dan menyenangkan ya bang bagi adik adiknya!"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobi": "Main hp",
                "sosmed": "@akmal.faiz",
                "kesan": "abang yang baik, ramah, dan ternyata sama sama alumni rpl1 smk4!",  
                "pesan": "semangat kuliahnya bang akmal! semoga dilancarkan selalu ya bang dalam proses dikampus maupun diluar kampus!"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobi": "baca novel",
                "sosmed": "@hermawan.mnrng",
                "kesan": "abang ini abang yang baik, humoris, tapi sedikit menyebalkan yaa abang nim satu ini hihi",  
                "pesan": "semangat kuliahnya bang awan! always be kind and always be happy abang nim!" #18
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Ngepel",
                "sosmed": "@khusnun_nisa335",
                "kesan": "kak nisa ini kakak yang baik dan ramah",  
                "pesan": "semangat kuliahnya ya kak nisa! keren banget nih kak nisa hobinya bersih bersih!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()