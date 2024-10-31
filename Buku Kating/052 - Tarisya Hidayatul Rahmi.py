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
            "https://drive.google.com/uc?export=view&id=18AaDc-KVHDMt2XLPpaFykc136rFFjuWZ",
            "https://drive.google.com/uc?export=view&id=1PS7Pb82BkKKCXHBFuX_WrXRTD5dJLo4S",
            "https://drive.google.com/uc?export=view&id=1EZKP62tA5o4db3tcqUBjXDsp9M4pZjzz",
            "https://drive.google.com/uc?export=view&id=1mIV2SPn1tIVUXSqBXYTI13cCnuhM6tzT",
            "https://drive.google.com/uc?export=view&id=1vZRY_0kZSpWYOdaPNWygOEodJZWawv1o",
            "https://drive.google.com/uc?export=view&id=1LHzU9sQG8Qk5SeaFrsouV8cQRDR5fqjm",
        ]
        data_list = [
            {
                "nama"  : "Kharisma Gumilang",
                "nim"   : "121450142",
                "umur"  : "21",
                "asal"  :"Palembang",
                "alamat": "Pulau Damar",
                "hobi"  : "Kura-kura, denger musik",
                "sosmed": "@gumilangkharisma",
                "kesan" : "Abangnya tegas, publick speakingnya bagus banget",  
                "pesan" :"semangat bang kura-kuranya dan  semester 7-nya !!!"# 1
            },
            {
                "nama"  : "Pandra Insani Putra Adzwar",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  :"Lampung utara",
                "alamat": "Sukarame, Bawean dua",
                "hobi"  : "Gitaran",
                "sosmed": "@pndrinsni",
                "kesan" : "Abangnya kritis banget",  
                "pesan" :"semangat bang menjalani semester 7-nya !!!"# 1
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450015",
                "umur"  : "20",
                "asal"  :"Palembang",
                "alamat": "Kota Baru",
                "hobi"  : "nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "Kakaknya positif vibes banget",  
                "pesan" :"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  :"Payakumbuh",
                "alamat": "Nangka 4",
                "hobi"  : "dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "Kakaknya pembawaan ngomongnya tenang banget",  
                "pesan" :"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"  : "Hartiti Fadhilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  :"Palembang",
                "alamat": "Pemda",
                "hobi"  : "Baca webtoon",
                "sosmed": "@hrtpdlh",
                "kesan" : "Kakaknya kalem banget, lebih banyak nyimak dari pada ngobrolnya",  
                "pesan" :"semangat  menjalani semester 7-nya kak !!!"# 1
            },
            {
                "nama"  : "Nadhillah Andharz Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  :"Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi"  : "Baca wattpad, au",
                "sosmed": "@nadhillahand26",
                "kesan" : "Kakaknya seru banget, banyak bantu jawab dan jelasin semua pertanyaan dari kami",  
                "pesan" :"semangat menjalani semester 7-nya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_RmztPRRH6kogQo-rMerIalimuojSuBM",
            "https://drive.google.com/uc?export=view&id=1i0Q9sh585z2Py5r-0SDHCg4vFAWWKG5W",
            "https://drive.google.com/uc?export=view&id=1ajBy_2NQ_lXf6oygSwmqe8CxJiYL0OUE",
            "https://drive.google.com/uc?export=view&id=1TvSBekFlaCpcsYeri0wUzVOL6B6RwTSy",
            "https://drive.google.com/uc?export=view&id=1oyYTyQRjEdieRRiKYydZQS6dm2_xzCWh",
            "https://drive.google.com/uc?export=view&id=1YnaAk6vDAtS_lzGF_VYq_d-LJTuN1CyX",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1dRckSrKwKruziu-e0ZS2CVM0ASA5yI2H",
            "https://drive.google.com/uc?export=view&id=13TpaxNL_9I68zOAjDpDWgzS4kd2Uv72C",
            "https://drive.google.com/uc?export=view&id=1L7M-vnlJI2K1lYyR7FslAjHjPnOCRkgb",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama" : "Tri Murniya Ningsih",
                "nim": "121450033",
                "umur": "21 ",
                "asal":"Bogor ",
                "alamat": "Raden Saleh ",
                "hobi": "Searching GPT ",
                "sosmed": "@Trimurniyaa_",
                "kesan": "Kakaknya energic banget, ramah, baik banget deh pokoknya",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114 ",
                "umur": "21 ",
                "asal":"Tangsel ",
                "alamat": "Way Hui ",
                "hobi": "Baca buku & nonton film ",
                "sosmed": "@wlnsbn0",
                "kesan": "Kakaknya baik, tapi agak kalem dikit",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081 ",
                "umur": "20 ",
                "asal":"Tangerang ",
                "alamat": "Jati Agung ",
                "hobi": "Ngobrol ",
                "sosmed": "@anisadini10",
                "kesan": "Public speaking kakaknya bagus banget, humble juga",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150 ",
                "umur": "21 ",
                "asal":"Medan ",
                "alamat": "Jl Raden Saleh ",
                "hobi": "Belajar bersama pak Tamaro ",
                "sosmed": "@wlsbn0",
                "kesan": "Kakaknya baik, sangat terlihat independen womennya",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@ansftrynn_",
                "kesan": "Kak anisa baik, lucu, suka senyum-senyum gitu",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya kak !!!"# 1
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
                "pesan":"Bahagia selalu dan semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": " ",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Claudhea Ageliani",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Solo ",
                "alamat": "Natar ",
                "hobi": "Suka ditipu jual akun canva di shoope ",
                "sosmed": "@dheamelia",
                "kesan": "Kak dhea orangnya lucu banget, asik juga ",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156 ",
                "umur": "22 ",
                "asal":"Surakarta Jateng ",
                "alamat": "Sukarame ",
                "hobi": "Badminton, berenang, hiking, dan melukis ",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya seru, asik ",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "12200065 ",
                "umur": "20 ",
                "asal":"Sumbar ",
                "alamat": "Way hui",
                "hobi": "makeup, nonton podcast, dan denger musik ",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak seru, cuma nggak terlalu banyak ngomong",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20 ",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobi": " ",
                "sosmed": "@Jeremia_",
                "kesan": "Abangya baik, seru, lucu juga",  
                "pesan":"Bahagia selalu dan semangat terus kuliahnya bang !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1St-94r2YY1D0LKDavDeoWGEFB4i6zEXc",
            "https://drive.google.com/uc?export=view&id=1RwU6XP0-al8vEbNiaqqf1ZAExgJn3R7r",
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
                "pesan": "Bahagia selalu dan semangat kak kuliahnya!!!"
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
            "https://drive.google.com/uc?export=view&id=1iV8_sFUb1CZE3vKIquL7wzadw8q0P7rc",
            "https://drive.google.com/uc?export=view&id=1bcF-5SaMid67ijU421Ig4Jn0c0BPbxMK",
            "https://drive.google.com/uc?export=view&id=1jFk-kc6QrRiF1aAa0BaLrC1iY6SnTOit",
            "https://drive.google.com/uc?export=view&id=1GsCnWNM9CSkDMlncVcJi08oTzHgao60d",
            "https://drive.google.com/uc?export=view&id=1Vwz_rc8fodOxwIPCW0wL0rpv6RHSXEF4",
            "https://drive.google.com/uc?export=view&id=102k9KXmIZQOG6bauk6eDr9KrA8ivWnB0",
            "https://drive.google.com/uc?export=view&id=1OYe_Lqx-CKUFAKsGIRBXj_8HKlDiq5Hi",
            "https://drive.google.com/uc?export=view&id=1HtqSRxJIWhodzFQ4v3abYHN8HL_sel2b",
            "https://drive.google.com/uc?export=view&id=1UdPS2WaKG9v-NXG8Bldpby-d1lvbtPr8",
            "https://drive.google.com/uc?export=view&id=1Sp12kbsGFk_nrU4qVmxDo-o96L6SWLDz",
            "https://drive.google.com/uc?export=view&id=1CfgegBY5TYywHDVPxtzRbbK9SktAHzne",
            "https://drive.google.com/uc?export=view&id=1nPoW1aNluTuM2c8U6upBqJhVvKc4d8Zb",
            "https://drive.google.com/uc?export=view&id=1UAmNDP-clv7GDBF9zSb-3xpQa8EG8DSB",
            "https://drive.google.com/uc?export=view&id=1qOMlStd_LsYvAGfjxuqkaml7TdB5G-VQ",
            "https://drive.google.com/uc?export=view&id=1Bj5962yjMcIfuthtYMy6PGCwm88G1sbq",
            "https://drive.google.com/uc?export=view&id=1D370moIoQE1NS9ZSCtUmwmUdw9X5lFvQ",
            "https://drive.google.com/uc?export=view&id=1E85GPr0LvJvgUTKgzhKHLLuSZsAKznjX",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1BkjBzft8AcA3bqBMp-eCtkg0u1954DeC",
            "https://drive.google.com/uc?export=view&id=1sBUpRh2iG8nAqhq9G83UTLSHwBgs_7k5",
            "https://drive.google.com/uc?export=view&id=1aBA5NZ7wiQpzXIGPFGyamS1jnxQpq9Jq",
            "https://drive.google.com/uc?export=view&id=13ozJFjecD7mirVsi4Z2jTQYUcdNOJVTc",
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
                "kesan": "Abangnya baik dan tegas",  
                "pesan": "Semangat terus kuliahnya bang!!!" # 1

            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
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
                "hobi": "Minum kopi",
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
                "nama": "Eksanty Febriana Sugma Islamiaty",
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
                "kesan": "Kakak hanum orangnya terlihat sangat santai,suka senyum juga ",  
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
                "pesan":"Bahagia selalu dan semangat terus kuliahnya bang !!!"# 1
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
                "pesan":"Bahagia selalu, semangat terus kuliahnya dan jangan lupa istirat juga kak!!!"# 1
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abangnya lucu, baik, kalau ngomong tenang banget  ",  
                "pesan": "Bahagia selalu, semangat terus kuliahnya dan jangan lupa istirat juga bang!!!" # 10

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
                "kesan": "Abangnya orangnya keliatan balance, bisa serius, bisa juga becanda  ",  
                "pesan":"Bahagia selalu, semangat terus kuliahnya dan jangan lupa istirat juga bang jo!!!"# 1
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
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
                "kesan": "kakaknya keliatan agak kalem  ",  
                "pesan": "Bahagia selalu, semangat terus kuliahnya dan jangan lupa istirat juga kak!!!" #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak asik, baik dan humble juga",  
                "pesan":"Bahagia selalu, semangat terus kuliahnya dan jangan lupa istirat juga kak!!!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "abangnya keliatan agak kalem, kalau ngomong juga seadanya aja ",  
                "pesan": "Bahagia selalu, semangat terus kuliahnya dan jangan lupa istirat juga bang sahid!!!" # 17
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
                "kesan": "abangnya baik dan humble  ",  
                "pesan": "Semangat kuliah dan menolongnya bang  " # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya baik,seru juga",  
                "pesan":"Bahagia selalu, semangat terus kuliahnya dan jangan lupa istirat juga bang!!!"# 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
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
                "hobi": "Main Game",
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
                "hobi": "-",
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
                "nim": "121450143",
                "umur": "21 ",
                "asal":"Lubuk Linggau ",
                "alamat": "Jl. Nangka 4 ",
                "hobi": "Olahraga ",
                "sosmed": "@Rafadhilillahh13",
                "kesan": "Bang rafi berwibawa, trus keliatan tenang juga ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya bang !!!"# 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005 ",
                "umur": "21 ",
                "asal":"LAmpung Utara ",
                "alamat": "Jl. Pulau Sebesi, Sukarame ",
                "hobi": "Memasak ",
                "sosmed": "@anovavona",
                "kesan": "Kakaknya baik, asik, lucu ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya kak !!!"# 1
            },
            {
                "nama": "Mujadid Choirus Surya",
                "nim": "- ",
                "umur": "- ",
                "asal":"- ",
                "alamat": "- ",
                "hobi": "- ",
                "sosmed": "@ ",
                "kesan": "- ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya bang !!!"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044 ",
                "umur": "20 ",
                "asal":"Tulang Bawang ",
                "alamat": "Sukarame ",
                "hobi": "Olahraga ",
                "sosmed": "@sahid22__",
                "kesan": "Abangnya asik, lucu ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya bang !!!"# 1
            },
            {
                "nama": "fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20 ",
                "asal":"Bekasi ",
                "alamat": "Teluk Betung ",
                "hobi": "Main Game ",
                "sosmed": "@fadhilfwee ",
                "kesan": "Abangnya baik, agak kalem "  
                "pesan":"semangat terus kuliahnya bang dan jangan lupa istirahat juga "
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya bang !!!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121 ",
                "umur": "21 ",
                "asal":"Tangerang ",
                "alamat": "Gg. Yudhistira ",
                "hobi": "Baca jUrnal ",
                "sosmed": "@dkselsd_31 ",
                "kesan": "Kak dina seru banget, trus gampang ketawa, baik ",  
                "pesan":"semangat terus kuliahnya dan baca jurnalnya kak, jangan lupa istirahat !!!"# 1
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@i",
                "kesan": " ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya bang !!!"# 1
            },
            {
                "nama": "Anwar Muslim",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya bang !!!"# 1
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya kak !!!!"# 1
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120 ",
                "umur": "20 ",
                "asal":"Medan ",
                "alamat": "Jl. Lapas ",
                "hobi": "Belajar ",
                "sosmed": "@dindanababan_ ",
                "kesan": "Kakaknya baik, nggak banyak ngomong, tapi lucu ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya kak !!!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "12200092 ",
                "umur": "20 ",
                "asal":"Depok, Jawa Barat ",
                "alamat": "gg. Nangka 3 ",
                "hobi": "Review Jurnal ",
                "sosmed": "@marletacornelia ",
                "kesan": "Kakaknya baik, kalau ngomong lembut, suka senyum juga ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya kak !!!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103 ",
                "umur": "20 ",
                "asal":"Batam, Kep. Riau ",
                "alamat": "Gg. Nanangka 3 ",
                "hobi": "Review Jurnal ",
                "sosmed": "@junitaa_0406 ",
                "kesan": "Kakaknya baik, lembut dan ramah ",  
                "pesan":"semangat terus kuliahnya kak dan jangan lupa istirahat !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072 ",
                "umur": "20 ",
                "asal":"Palembang ",
                "alamat": "Belwis ",
                "hobi": "Resume SG ",
                "sosmed": "@puspadrr ",
                "kesan": "Kakaknya baik dan seru ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya kak !!!"# 1
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Aditya Rahman",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032 ",
                "umur": "20 ",
                "asal":"Sukabumi ",
                "alamat": "Korpri ",
                "hobi": "Ngoding WISATA ",
                "sosmed": "@egistr ",
                "kesan": "Bang egi baik banget, suka sharing ilmu juga ",  
                "pesan":"Bahagia selalu dan semangat kuliahnya bang !!! !!!"# 1
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074 ",
                "umur": "20 ",
                "asal":"Tulang Bawang ",
                "alamat": "Jl. Kelengkeng Raya ",
                "hobi": "Review Jurnal ",
                "sosmed": "@",
                "kesan": "Kakaknya baik, ramah ",  
                "pesan":"Bahagia selalu dan semangat kuliahnya kak !!!"# 1
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013 ",
                "umur": "20 ",
                "asal":"Lampung Timur ",
                "alamat": "Karang Anyar ",
                "hobi": "Main Game ",
                "sosmed": "@sudo.syahrulramadhannn ",
                "kesan": "Abangnya baik, cuma agak kalem aja ",  
                "pesan":"Semangat terus bang kuliahnya"# 1
            },
            {
                "nama": "Randa Adriana Putra",
                "nim": "122450083 ",
                "umur": "21 ",
                "asal":"BAnten ",
                "alamat": "Sukarame ",
                "hobi": "Tidur dan Berkembang ",
                "sosmed": "@",
                "kesan": "Abangnya baik, ramah ",  
                "pesan":"Bahagia selalu dan semngat kuliahnya bang !!!"# 1
            },
            {
                "nama": "Vita Anggraini",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan":"Bahagia selalu dan semnagat kuliahnya bang, semoga bisa 100% pulih !!!"# 1
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
                "hobi": "Nyari Hotwils",
                "sosmed": "@yogyyyyyyy",
                "kesan": " Bang yogi orangnya tegas, baik ",  
                "pesan": "Bahagia selalu dan semangat kuliahnya bang !!!" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kak dhita keliatannya agak judes, tapi ternyata baik banget ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak" # 2
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
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak  " # 3
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
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang  " # 4
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak dea orangnya lucu, baik  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak" # 5
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
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak  " # 6
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
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak  " # 7
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakaknya baik, ramah, humble ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobi": "Planning konten",
                "sosmed": "@jasminednva",
                "kesan": "Kak jasmine orangnya humble, ceria banget  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak" # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Membaca",
                "sosmed": "@tobiassiagian",
                "kesan": "Bang tobias orangnya keliatan serius, tapi masih bisa santai  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang" # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Buat Jurnal",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakaknya baik, ceria, suka senyum  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "Bang beno orangnya keliatan agak santai, humble ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang" # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Samping warjo",
                "hobi": "Sholat",
                "sosmed": "@rafiramadhanmaulana",
               "kesan": "Bang rafi orangnya lucu banget, gampang ketawa  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang" # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Cari ice breaking",
                "sosmed": "@u_yippy",
                "kesan": "LKak uyi orangnya baik, jiwa keibuannya kuat banget, ramah  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak"# 14
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Berbuat baik",
                "sosmed": "@chlfawww",
                "kesan": "Kak oca orangnya baik, ramah, lembut  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak" # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "BAng ivan humble, ramah  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang" # 16
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
                "kesan": "Kak alya orangnya baik, ceria dan humble  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak"# 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Ikut seminar",
                "sosmed": "@rayths_",
                "kesan": "Bang raid orangnya agak pendiam dikit, tapi kadang juga suka ngelucu  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang " # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Pemda",
                "hobi": "Sholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kak yuna orangnya lucu, humble, suka ketawa  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak" # 20
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
                "hobi": "Nangkep bulu babi",
                "sosmed": "@dimzrky_",
                "kesan": "Bang dimas orangnya serius, tegas, tapi lucu juga  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kakaknya baik, humble  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya kak"# 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": "Abangnya ramah, baik  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang" # 3
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobi": "Dengerin Musik",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya baik, ceria ",  
                "pesan": "Semangatt kuliahnya bang, semoga IP-nya naik disemester ini" # 4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abangnya humble, baik, ramah  ",  
                "pesan": "Semoga lagunya bisa segera rilis bang, semangat juga kuliahnya !!" # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakaknya seru, gampang senyum juga  ",  
                "pesan": "Semangatt kuliahnya kak, sehat selalu " # 6
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
                "kesan": "Abangnya tenang banget, lembut, ramah  ",  
                "pesan": "Semangatt kuliahnya bang, bahagia selalu" # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kakaknya baik, lembut, agak kalem  ",  
                "pesan": "Semangatt kuliahnya kak, jangan lupa istirahat juga !! " # 9
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
                "kesan": "Kakaknya gampang banget ketawa, baik, dan ramah ",  
                "pesan": "Bahagia selalu dan semangat kuliahnya kak" # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": "Abangnya baik, tapi agak kalem  ",  
                "pesan": "Semangatt kuliah dan jalanin aktivitasnya " # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kakaknya baik, ramah, dan humble  ",  
                "pesan": "Semangatt kuliahnya kak dan sehat selalu" # 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Siantar",
                "alamat": "Gerbang Barat",
                "hobi": "Nonton film",
                "sosmed": "@josuapanggabean_",
                "kesan": "Abangnya baik, ramah  ",  
                "pesan": "Jangan lupa istirahat yang cukup dan semangat kuliahnya bang" # 14
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
                "hobi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Abangnya baik, keliatan agak serius juga  ",  
                "pesan": "Semangatt kuliahnya bang, semoga usahanya makin berkembang!" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakaknya ramah, keliatan tegas juga ",  
                "pesan": "Semangatt kuliahnya kak!" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kakaknya baik, ramah  ",  
                "pesan": "Semangatt kuliahnya kak, jangan lupa istirahat "  # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": "Abangnya agak kalem ",  
                "pesan": "Semangatt kuliahnya bang, semoga IP-nya bisa naik " # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya energic, kalau jelasin detail  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Abangnya baik, humble  ",  
                "pesan": "Semangatt kuliahnya bang, semoga sehat selalu! "# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakaknya lucu, baik juga  ",  
                "pesan": "Semangatt kuliahnya kak, semoga bisa jadi penulis buku " # 7
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
                "pesan": "Semangatt terus kak dan bahagia selalu " # 9
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
                "pesan": "semangat menjalani hari- harinya bang " # 10
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
                "pesan": "Semangat selalu dan lancar kuliahnya kak " # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def  MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PoCNIb1M63HLK2aKOcXvDpt8sKM6JUtL", # 
            "https://drive.google.com/uc?export=view&id=1HmtRgdwEW27M18G7ugACX4XKgs7y5IOm", #
            "https://drive.google.com/uc?export=view&id=1OD9w6PKTInARnS-8eHD53H6jNoxdBNcE", # 
            "https://drive.google.com/uc?export=view&id=1Zq35b5JrqAkGEP9g_GMdNRfUSOS4v-Ma", #
            "https://drive.google.com/uc?export=view&id=1HqObbpV5vRhROJPo4jDYOw0tyWCuEnoG", # 
            "https://drive.google.com/uc?export=view&id=1YbA6XEg7zWw6exIRKIs2xfxY5SGhIkf-", # 
            "https://drive.google.com/uc?export=view&id=1aVJFbdCU91s3f5R2bb3El6b-ejEOILt5", # 
            "https://drive.google.com/uc?export=view&id=1gR6SrJYCPvhEhPYMQ621Sf7iN8zpN9v6", # 
            "https://drive.google.com/uc?export=view&id=10p5UQQC49b9fkYL5_XsUjzjzGTVkb0do", # 
            "https://drive.google.com/uc?export=view&id=1IoS6iE6xK4l3_-oT55QySUnR6CMYqulo", # 
            "https://drive.google.com/uc?export=view&id=1MvYhY8EydgvkfLKJK8uJ-_OPV4gzaW4d", # 
                        "https://drive.google.com/uc?export=view&id=1Zq35b5JrqAkGEP9g_GMdNRfUSOS4v-Ma", # 
            "https://drive.google.com/uc?export=view&id=1HqObbpV5vRhROJPo4jDYOw0tyWCuEnoG", # 
            "https://drive.google.com/uc?export=view&id=1YbA6XEg7zWw6exIRKIs2xfxY5SGhIkf-", # 
            "https://drive.google.com/uc?export=view&id=1aVJFbdCU91s3f5R2bb3El6b-ejEOILt5", #
            "https://drive.google.com/uc?export=view&id=1gR6SrJYCPvhEhPYMQ621Sf7iN8zpN9v6", # 
            "https://drive.google.com/uc?export=view&id=10p5UQQC49b9fkYL5_XsUjzjzGTVkb0do", # 
            "https://drive.google.com/uc?export=view&id=1IoS6iE6xK4l3_-oT55QySUnR6CMYqulo", # 
            "https://drive.google.com/uc?export=view&id=1MvYhY8EydgvkfLKJK8uJ-_OPV4gzaW4d", # 
    
        data_list = [
            {
                "nama": "Wahyudiyanto ",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar, Sulawesi Selatan ",
                "alamat": "Sukaraju Sukarame",
                "hobi": "Nonton Donghwa",
                "sosmed": "@wahyulaja",
                "kesan": "Abangnya baik, seru  ",  
                "pesan": "Semangatt terus bang jalanin kuliahnya !!" # 1
            },
            {
                "nama": "Elok Fiola ",
                "nim": "122450051 ",
                "umur": "19 ",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung ",
                "hobi": "Editing ",
                "sosmed": "@elokfiola ",
                "kesan": "Kakaknya ramah,baik,ramah,  humble juga ",  
                "pesan": "Semangatt kuliahnya kak jangan lupa istirahat juga !" # 2
            },
            {
                "nama": "Arsyiah Azahra ",
                "nim": "121450035 ",
                "umur": "21",
                "asal": "Bandar Lampung ",
                "alamat": Tanjung senang ",
                "hobi": "Ngonten ",
                "sosmed": "@arsiah._",
                "kesan": "Kakaknya seru, ceria banget  ",  
                "pesan": "Semangatt kuliahnya kak, semoga sehat selalu "  # 3
            },
            {
                "nama": "Chintiya Bella ",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Teluk ",
                "hobi": "Ngegym ",
                "sosmed": "@cintyabella28 ",
                "kesan": "Kakaknya baik dan seru  ",  
                "pesan": "Semangatt kuliahnya kak, semoga IP-nya bisa naik " # 4
            },
            {
                "nama": "Eka Fidiya Putri ",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya energic, kalau jelasin detail  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang" # 5
            },
            {
                "nama": "Najla Juwairia ",
                "nim": "122450037 ",
                "umur": "19 ",
                "asal": "Sumatra Utara ",
                "alamat": "Airan ",
                "hobi": "Nulis, baca, ngefangirl ",
                "sosmed": "@nanana.minjoo ",
                "kesan": "Kakaknya baik, seru banget ",  
                "pesan": "Semangatt kuliahnya kak, semoga sehat selalu! "# 6
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri ",
                "nim": "122450050",
                "umur": "20",
                "asal": "Lampung Selatan ",
                "alamat": "Jatimulyo ",
                "hobi": "Gonta-ganti HP ",
                "sosmed": "@patriciadiajeng ",
                "kesan": "Kak cia orangnya seru dan energic banget  ",  
                "pesan": "Semangatt kuliahnya kak, jangan lupa juga istirahat " # 7
            },
            {
                "nama": "Rahma Neliyana ",
                "nim": "122450036 ",
                "umur": "20 ",
                "asal": "Lampung ",
                "alamat": "Sukarame ",
                "hobi": "Membaca merk mobil ",
                "sosmed": "@Rahmanellyana",
                "kesan": "Kak nely orangnya seru banget, suka banget ngomong  ",  
                "pesan":"Bahagia terus kak Nely, semangat juga kuliah  " # 8
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah ",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviaginting",
                "kesan": "Kakaknya baik, seru juga  ",  
                "pesan": "Semangatt terus kak dan bahagia selalu " # 9
            },
            {
                "nama": "Muhammad Kaisar Firdaus ",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": "  ",  
                "pesan": "semangat menjalani hari- harinya bang " # 10
            },
            {
                "nama": "Dwi Ratna Anggraeni ",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi ",
                "alamat": "Pemda ",
                "hobi": "Menonton ",
                "sosmed": "@dwiratnn_ ",
                "kesan": "Kak ratna orangnya lucu banget, seru dan gampang ketawa  ",  
                "pesan": "Semangat selalu dan lancar kuliahnya kak " # 11
            },
            {
                "nama": "Gymnastiar Al Khoarizmy ",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": "Abangnya agak kalem ",  
                "pesan": "Semangatt kuliahnya bang, semoga IP-nya bisa naik " # 4
            },
            {
                "nama": "Nasywa Nur Afifah ",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya energic, kalau jelasin detail  ",  
                "pesan": "Bahagia selalu, istirahat yang cukup dan semangat kuliahnya bang" # 5
            },
            {
                "nama": "Priska Silvia Ferantiana ",
                "nim": "122450053 ",
                "umur": "20 ",
                "asal": "Palembang ",
                "alamat": "Jl. Nangka 2 ",
                "hobi": "Nonton apa aja yang bikin nangis-nagis ",
                "sosmed": "@prskslv ",
                "kesan": "Kakaknya baik dan seru banget  ",  
                "pesan": "Semangatt kuliahnya kak, semoga sehat selalu! "# 6
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama ",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakaknya lucu, baik juga  ",  
                "pesan": "Semangatt kuliahnya kak, semoga bisa jadi penulis buku " # 7
            },
            {
                "nama": "Abit Ahmad Oktarian ",
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
                "nama": "Akmal Faiz Abdillah ",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviaginting",
                "kesan": "Kakaknya baik, seru juga  ",  
                "pesan": "Semangatt terus kak dan bahagia selalu " # 9
            },
            {
                "nama": "Hermawan Manurung ",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": "  ",  
                "pesan": "semangat menjalani hari- harinya bang " # 10
            },
            {
                "nama": "Khusnun Nisa ",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "Kakaknya  baik dan seru ",  
                "pesan": "Semangat selalu dan lancar kuliahnya kak " # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
     MEDKRAF()
