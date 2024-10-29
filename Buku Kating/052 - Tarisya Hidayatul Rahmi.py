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
            "https://drive.google.com/uc?export=view&id=18AaDc-KVHDMt2XLPpaFykc136rFFjuWZ",
            "https://drive.google.com/uc?export=view&id=1PS7Pb82BkKKCXHBFuX_WrXRTD5dJLo4S",
            "https://drive.google.com/uc?export=view&id=1EZKP62tA5o4db3tcqUBjXDsp9M4pZjzz",
            "https://drive.google.com/uc?export=view&id=1mIV2SPn1tIVUXSqBXYTI13cCnuhM6tzT",
            "https://drive.google.com/uc?export=view&id=1vZRY_0kZSpWYOdaPNWygOEodJZWawv1o",
            "https://drive.google.com/uc?export=view&id=1LHzU9sQG8Qk5SeaFrsouV8cQRDR5fqjm",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Kura-kura, denger musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Abangnya tegas, publick speakingnya bagus banget",  
                "pesan":"semangat bang kura-kuranya dan  semester 7-nya !!!"# 1
            },
            {
                "nama": "Pandra Insani Putra Adzwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung utara",
                "alamat": "Sukarame, Bawean dua",
                "hobi": "Gitaran",
                "sosmed": "@pndrinsni",
                "kesan": "Abangnya kritis banget",  
                "pesan":"semangat bang menjalani semester 7-nya !!!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450015",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakaknya positif vibes banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobi": "dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakaknya pembawaan ngomongnya tenang banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Baca webtoon",
                "sosmed": "@hrtpdlh",
                "kesan": "Kakaknya kalem banget, lebih banyak nyimak dari pada ngobrolnya",  
                "pesan":"semangat  menjalani semester 7-nya kak !!!"# 1
            },
            {
                "nama": "Nadhillah Andharz Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Baca wattpad, au",
                "sosmed": "@nadhillahand26",
                "kesan": "Kakaknya seru banget, banyak bantu jawab dan jelasin semua pertanyaan dari kami",  
                "pesan":"semangat menjalani semester 7-nya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Zw5sClP6fg2SsTgr9xc4Om9HTxMpc6tg",
            "https://drive.google.com/uc?export=view&id=1rBxdfb5MNWjtTLoE5oHMFz-nIWPMVPe4",
            "https://drive.google.com/uc?export=view&id=1MOT1skWITQV8Dd20pdas6s80Ard9LQzY",
            "https://drive.google.com/uc?export=view&id=1SxFxbPurFQj3PqMQBTDxH4I2vTG6Ij43",
            "https://drive.google.com/uc?export=view&id=1ghkVhAPHKStmJmKip0l7i0lxygNUb-3h",
            "https://drive.google.com/uc?export=view&id=1EEX8DtJqKoUHdzc8bciWItdGa5OgwBF5",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1IKOBOtCymsMR4uyCDHotM3nSBymrmMYt",
            "https://drive.google.com/uc?export=view&id=1I9Ii-6ZSjcPFCS4akAi0a8GhlD6DzpaP",
            "https://drive.google.com/uc?export=view&id=1Mo0ZF8rLBlCpo5jYhtegNYc3VKOvh1kM",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "nama": "Renisha Putri Giani",
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
                "nama": "Claudhea Ageliani",
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
                "nama": "Mirzan Yusuf Rabbani",
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
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20 ",
                "asal":"Balam ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@Jeremia_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17aaQLLKXEYm9eEVHu1ty6N7fCH8I-zqY",
            "https://drive.google.com/uc?export=view&id=103L7GhmAXS05Bl9HJBvXHrZ-MSmPeadn",
        ]
        data_list = [
            {#data belum diubah, foto sudah
                "nama": "Annisa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobi": "Bernyani",
                "sosmed": "@anissaluthfi_",
                "kesan": "Public speaking kak annisa bagus banget, kalau ditanya dijelasin detail",  
                "pesan": "Semangat kak kuliahnya!!!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan kota baru",
                "hobi": "Dengerin Ka Luthfi bernyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Ga jauh beda sama kak luthfi, bang bintang juga public speaking bagus banget, terus juga tegas",  
                "pesan": "Semangatt terus bang bintang ngejalinin kuliah dan semua kegiatannya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
elif menu == "Departemen PSDA":
    def departemen_psda():
        gambar_urls = [ #foto belum ditambah, data baru sampa kak oktavia
            "https://drive.google.com/uc?export=view&id=17m55Tf62sr7oSdycqufOlNXzyoFaNVlH",
            "https://drive.google.com/uc?export=view&id=1LZTtWrkvp8wQbFV18BD21T5gwFNHuF-F",
            "https://drive.google.com/uc?export=view&id=1yyuRD6NzKgcA5nRvwS8eznUyEgzhSrfn",
            "https://drive.google.com/uc?export=view&id=1elvMSULK_-_zQSbNPqJBJWt63w_swoPL",
            "https://drive.google.com/uc?export=view&id=1OM4MjjoA4Z8xP0A2pyqgs7KFx40xO3Mn",
            "https://drive.google.com/uc?export=view&id=1mWM5OeztUQuqiIGiKmQleh3oSlNUqU_-",
            "https://drive.google.com/uc?export=view&id=1tSIJ8bEuO7qk7TE4GLLOv1GLZBSF_Juj",
            "https://drive.google.com/uc?export=view&id=1Y9XUTkHb3EQumz3PRnBIt57ApD9KKwlJ",
            "https://drive.google.com/uc?export=view&id=17Rdl5FofXLfqzFVsUUddmdsLULyy6vU-",
            "https://drive.google.com/uc?export=view&id=1Sp12kbsGFk_nrU4qVmxDo-o96L6SWLDz",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1wP9gFaD3uy5Ec5v2CozSYrm_MpdWKBPN",
            "https://drive.google.com/uc?export=view&id=1UAmNDP-clv7GDBF9zSb-3xpQa8EG8DSB",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1sAPhcGY9A9bcsfxJo27xqf54OHeuIej4",
            "https://drive.google.com/uc?export=view&id=1D370moIoQE1NS9ZSCtUmwmUdw9X5lFvQ",
            "https://drive.google.com/uc?export=view&id=1E85GPr0LvJvgUTKgzhKHLLuSZsAKznjX",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1zl6S1HfKSF5dlVwDV7oG3lVvy9thETP6",
            "https://drive.google.com/uc?export=view&id=1NMoUPjNWJlXvGpLh_SLsiOPJ3r9HKZZu",
            "https://drive.google.com/uc?export=view&id=1YE4XMcymGIlvLu1i4nLQPEw_wbKzM5Fu",
            "https://drive.google.com/uc?export=view&id=16W8ER4Tdt_84HSt9Le6xAXwY4y6cB_WO",
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
                "kesan": "Abangnya baik dan tegas",  
                "pesan": "Semangat terus kuliahnya bang!!!" # 1

            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kak elisabeth orangnya baik, lucu juga ",  
                "pesan":"Semangat menjalani semester limanya kak!!!  " # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak nim yang baik dan humble banget  ",  
                "pesan":"Semangat kak jalani semua kegiatan dan semester limanya" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033 ",
                "umur": "20 ",
                "asal":"Sumatra Barat ",
                "alamat": "Gang Pewira ",
                "hobi": "Ngukur Balam ",
                "sosmed": "@Allyaislami_",
                "kesan": "Kak Alya orangnya asik, tapi tegas",  
                "pesan":"semangat terus kak Alya, jangan lupa istirahat kak !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001 ",
                "umur": "20 ",
                "asal":"Kopri ",
                "alamat": "Kopri ",
                "hobi": "Bikin Kak Alya badmood",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak eksanty orangnya sangat ambisius dan serius",  
                "pesan":"semangat terus kuliahnya kak, istirahat yang cukup juga !!!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056 ",
                "umur": "20 ",
                "asal":"Padang ",
                "alamat": "Sukarame ",
                "hobi": "Baca Webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak hanum orangnya terlihat sangat santai ",  
                "pesan":"semangat terus kuliahnya kak!!!"# 1
            },
            {
                "nama": "Ferdy kevin Naibaho",
                "nim": "122450107 ",
                "umur": "19 ",
                "asal":"Medan ",
                "alamat": "Jl. Pangeran Senopati ",
                "hobi": "Baca Buku Filsafat ",
                "sosmed": "@ferdy_kevin",
                "kesan": "Agak kaget pas tau umur abangnya baru 19, bang ferdy orangnyanya keliatan serius banget ",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101 ",
                "umur": "19 ",
                "asal":"Kayu Agung ",
                "alamat": "Jl. PA kedaton ",
                "hobi": "bakar-bakar ",
                "sosmed": "@Dransyh_",
                "kesan": "Abangnya suka banget ketawa, keliatan kocak juga ",  
                "pesan":"semangat bang kuliahnya!!!"# 1
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "1 ",
                "umur": "20 ",
                "asal":"Lampung Timur ",
                "alamat": "Way huwi ",
                "hobi": "Ngeliatin Tingkah Orang ",
                "sosmed": "@oktavianrwnda_",
                "kesan": "Kakak ini lucu banget, pas foto kita disuruh buat cari gaya foto yang rumit ",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abangnya lucu, baik, kalau ngomong tenang banget  ",  
                "pesan": "Semangat terus bang kuliahnya!!!  " # 10

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
                "kesan": "Abangnya orangnya keliatan balance, bisa serius, bisa juga becanda  ",  
                "pesan":"semangat kuliah dan ngaspraknya bang !!!"# 1
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": "Wajah abangnya sangat keliatan orang pintarnya  ",  
                "pesan": "Semangat bang kuliahnya dan jangan berhenti berbagi ilmunya   " # 13

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
                "kesan": "kakaknya keliatan agak kalem  ",  
                "pesan": "Semangat kuliahnya kak  " #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak asik, baik dan humble juga",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "abangnya keliatan agak kalem, kalau ngomong juga seadanya aja ",  
                "pesan": "Semangat bang kuliahnya  " # 17
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
                "kesan": "abangnya baik dan humble  ",  
                "pesan": "Semangat kuliah dan menolongnya bang  " # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya baik,seru juga",  
                "pesan":"semangat terus kuliahnya bang !!!"# 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kakaknya baik, sopan, lembut juga",  
                "pesan":"semangat terus kak jalani semester limanya !!!"# 1
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Abangnya seru banget  ",  
                "pesan": "Semangat bang kuliahnya " # 22
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
    departemen_psda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
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
                "nama": "Rafi Fadhillah",
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
                "nama": "Annisa Novantika",
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
                "nama": "Mujadid Choirus Surya",
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
                "nama": "Ahmad Sahidin Akbar",
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
                "nama": "fadhil Fitra Wijaya",
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
                "nama": "Muhammad Regi Abdi Putra Amanta",
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
                "nama": "Syalaisha Andina Putriansyah",
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
                "nama": "Natanael Oktavianus Partahan Sihombing",
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
                "nama": "Anwar Muslim",
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
                "nama": "Deva Anjani Khayyuninafsyah",
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
                "nama": "Dinda Nababan",
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
                "nama": "Marleta Cornelia Leander",
                "nim": "12200065 ",
                "umur": "20 ",
                "asal":"Sumbar ",
                "alamat": "Way hui",
                "hobi": "makeup, nonton podcast, dan denger musik ",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450022",
                "umur": "20 ",
                "asal":"Balam ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@Jeremia_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
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
                "nama": "Abdurrahman Al-atsary",
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
                "nama": "Aditya Rahman",
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
                "nama": "Eggi Satria",
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
                "nama": "Febiya Jomy Pratiwi",
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
                "nama": "Happy Syahrul Ramadhan",
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
                "nama": "Randa Adriana Putra",
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
                "nama": "Vita Anggraini",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kaka !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()


elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg yogy
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka dhita
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka nazwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg bastian
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka dea mutia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka ester
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka natasya
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka novelia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka ratu
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg tobias
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka yo
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg rizky
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg arafi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka asa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka chalifia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg irvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka izza
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka khaalishah
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
                "hobbi": "Nyari Hotwils",
                "sosmed": "@yogyyyyyyy",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 2
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
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
                "hobbi": " ",
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
                "hobbi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 5
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
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
                "nama": "Natasya Ega Lina",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
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
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Planning konten",
                "sosmed": "@jasminednva",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca",
                "sosmed": "@tobiassiagian",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Buat Jurnal",
                "sosmed": "@yo_annamnk",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Samping warjo",
                "hobbi": "Sholat",
                "sosmed": "@rafiramadhanmaulana",
               "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Cari ice breaking",
                "sosmed": "@u_yippy",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat"# 14
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfawww",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 16
            },
            {
                "nama": "Izza Lutfia",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
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
                "hobbi": "Tilawah Al-quran",
                "sosmed": "@alyaavanevi",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat"# 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ikut seminar",
                "sosmed": "@rayths_",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Pemda",
                "hobbi": "Sholawat",
                "sosmed": "@tria_y062",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()


elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg dim
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka catherine
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg akbar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka rani
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg rendra
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka salwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka yosia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg ari
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka dearni
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka meira
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg rendi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka renta
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg josua
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobbi": "Nangkep bulu babi",
                "sosmed": "@dimzrky_",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat"# 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobbi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 3
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rannipu",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 6
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
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
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 9
            },
            {
                "nama": "Dearni Monica Br Manik",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
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
                "hobbi": "Nonton film",
                "sosmed": "@meirasty_",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Siantar",
                "alamat": "Gerbang Barat",
                "hobbi": "Nonton film",
                "sosmed": "@josuapanggabean_",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PoCNIb1M63HLK2aKOcXvDpt8sKM6JUtL", # bg andrian
            "https://drive.google.com/uc?export=view&id=1HmtRgdwEW27M18G7ugACX4XKgs7y5IOm", # ka disty
            "https://drive.google.com/uc?export=view&id=1OD9w6PKTInARnS-8eHD53H6jNoxdBNcE", # ka nabila
            "https://drive.google.com/uc?export=view&id=1Zq35b5JrqAkGEP9g_GMdNRfUSOS4v-Ma", # bg ahmad rizqi
            "https://drive.google.com/uc?export=view&id=1HqObbpV5vRhROJPo4jDYOw0tyWCuEnoG", # bg danang
            "https://drive.google.com/uc?export=view&id=1YbA6XEg7zWw6exIRKIs2xfxY5SGhIkf-", # bg farel
            "https://drive.google.com/uc?export=view&id=1aVJFbdCU91s3f5R2bb3El6b-ejEOILt5", # ka tesa
            "https://drive.google.com/uc?export=view&id=1gR6SrJYCPvhEhPYMQ621Sf7iN8zpN9v6", # ka nabilah
            "https://drive.google.com/uc?export=view&id=10p5UQQC49b9fkYL5_XsUjzjzGTVkb0do", # ka alvia
            "https://drive.google.com/uc?export=view&id=1IoS6iE6xK4l3_-oT55QySUnR6CMYqulo", # bg dhafin
            "https://drive.google.com/uc?export=view&id=1MvYhY8EydgvkfLKJK8uJ-_OPV4gzaW4d", # ka elia
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Abangnya baik  ",  
                "pesan": "Semangatt kuliahnya bang!" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakaknya ramah, keliatan tegas juga ",  
                "pesan": "Semangatt kuliahnya kak!!" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kakaknya baik, ramah  ",  
                "pesan": "Semangatt kuliahnya kak"  # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobbi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": "Abangnya agak kalem ",  
                "pesan": "Semangatt kuliahnya bang! " # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya energic, kalau jelasin detail  ",  
                "pesan": "Semangatt kuliahnya bang" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Abangnya baik, humble  ",  
                "pesan": "Semangatt kuliahnya bang"# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakaknya lucu, baik juga  ",  
                "pesan": "Semangatt kuliahnya kak! " # 7
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
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
                "hobbi": "Nonton Windah",
                "sosmed": "@alviaginting",
                "kesan": "Kakaknya baik, seru juga  ",  
                "pesan": "Semangatt kuliahnya kak " # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobbi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()