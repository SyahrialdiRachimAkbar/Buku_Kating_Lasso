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
            "https://drive.google.com/uc?export=view&id=1sJGEzrIVJuIqLkE-uGtounefAKXBC8fQ", #bang Gumi
            "https://drive.google.com/uc?export=view&id=1a3L0MES-NCtzYZEiKQdI6wpjqcyePGWb", #bang Pandra
            "https://drive.google.com/uc?export=view&id=1uMJPiOq1FvdUIDeWkkVVMwZcd36wLHCU", #kak iza
            "https://drive.google.com/uc?export=view&id=15lNX5gQ8fAIGJD6wrCJ8qhF_sgo8ncLs", #Kak Putri
            "https://drive.google.com/uc?export=view&id=1tKusakfQcN4S7PqpvcGizzJ7qeALyZPL", #kak Titi
            "https://drive.google.com/uc?export=view&id=1ngr96ah_gviXa967QmkTU58vwa8WylYX", #kak Nadilla
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Kura-kura, Dengerin Musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Ambisius, tapi asik",  
                "pesan":"semangat semester 7 nya"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Bawean, Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Abangnya lucu, tapi ambisinya banyak",  
                "pesan":"semangat semester 7 nya bang"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450044",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Nonton drakor",
                "sosmed": "@wulandarimelinza",
                "kesan": "Kakak nya ramah banget",  
                "pesan":"semangat semester 7 nya kak!"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh",
                "alamat": "Jl Nangka 4",
                "hobi": "Mendengarkan bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakaknya asik banget",  
                "pesan":"semangat semester 7 nya kak!"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakaknya keliatan pendiam",  
                "pesan": "Semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Baca wattpad dan au",
                "sosmed": "@nadillaandr26",
                "kesan": "kakakny asik",  
                "pesan": "semangat semester 7 nya kak!"# 1
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1q4Hi6CGmg8AT2YJ7DwIBSx6851fBTi8r", #kak Tri
            "https://drive.google.com/uc?export=view&id=1ywY4tBGgtH_GiKZMj0KkfmLA5yMZM6bd", #Kak Cahyani
            "https://drive.google.com/uc?export=view&id=1eKoIc-ov6qa8Xp-9asVAAizZFhkGwJ7N", #Kak Wulan
            "https://drive.google.com/uc?export=view&id=10HsFxDy1A4tshSPjfOEXQvBDdlLZBDF7", #Kak Dini
            "https://drive.google.com/uc?export=view&id=1ywY4tBGgtH_GiKZMj0KkfmLA5yMZM6bd", #Nisa Fitriyani
            "https://drive.google.com/uc?export=view&id=1sJGEzrIVJuIqLkE-uGtounefAKXBC8fQ", #Bang Feryadi
            "https://drive.google.com/uc?export=view&id=1AZqXjtKf2GBfQDgStEuVgw0kAURt_7cX", #Kak Dhea
            "https://drive.google.com/uc?export=view&id=1m_ZhNj0le7W4MEwlYuU6CfZ8TgwE1iGc", #Bang Fahrul
            "https://drive.google.com/uc?export=view&id=1_bLblX9yRBh7gWT_KxEsjyjvkwEYkkIM", #Kak Berli

        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Jl. Raden Saleh",
                "hobi": "Searching GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakaknya ramah dan suka becanda",  
                "pesan":"semangat semester 7 nya kak!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Baca buku dan nonton film",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakaknya asik",  
                "pesan":"semangat semester 7 nya kak!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Jl. Raden Saleh",
                "hobi": "Belajar sama pak Tamaro",
                "sosmed": "@wlsbn0",
                "kesan": "Kakaknya asik",  
                "pesan":"semangat semester 7 nya kak!"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Ngobrol",
                "sosmed": "@anisadini10",
                "kesan": "Kakaknya asik",  
                "pesan": "Semangat Kuliahnya kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@ansftrynn_",
                "kesan": "kakaknya asik",  
                "pesan": "Semangat Kuliahnya kak"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya asik, tapi keliatan jail",  
                "pesan": "Semangat Kuliahnya bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Solo",
                "alamat": "Natar",
                "hobi": "Suka ditipu sama penjual akun canva premium di shopee",
                "sosmed": "@_.dheamelia",
                "kesan": "kakaknya asik",  
                "pesan": "Semangat Kuliahnya kak"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta, Jawa Tengah",
                "alamat": "Sukarame",
                "hobi": "Badminton, melukis, hiking, dan berenang",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya keliatan kalem",  
                "pesan": "Semangat Kuliahnya bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Make up, nonton podcast, dan dengerin musik",
                "sosmed": "@berlyyanda",
                "kesan":" kakaknya asik ",  
                "pesan": "Semangat semester 7 nya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
