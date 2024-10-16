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
            "https://drive.google.com/uc?export=view&id=1c7N1pIkSFtcAL-9lVq9HddC7b5xuy8XL", #bg gumi
            "https://drive.google.com/uc?export=view&id=1c1-TgRbJpngxy60jhQ90xjddbekM27tP", #bg pandra
            "https://drive.google.com/uc?export=view&id=1c36nZBM0IfupJ0ZjsaPwTUZPxU8Ob4Wu", #ka liza
            "https://drive.google.com/uc?export=view&id=1dqsNzwqrWwGieL5kVSWgK6b05OnZ22lb", #ka putri
            "https://drive.google.com/uc?export=view&id=1dsw1Jixqz_z4zbXAKt3zTUcsSer425oV", #ka titi
            "https://drive.google.com/uc?export=view&id=1_vZ19zdmOnJ_f0uapQy2YBrofT3yodC2", #ka nadilah
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
                "kesan": "Tegas tapi disatu sisi bisa bercanda juga",  
                "pesan":"Semangat kuliahnyaaa bang gumi!!!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl Bawean2, Sukarame",
                "hobi": "Bermain gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Bang pandra asik, tidak terlalu tegang, dan tegas ",  
                "pesan": "Semangatt semester 7 nya bang pandraa!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450044",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh",
                "alamat": "Jl Nangka 4",
                "hobi": "Mendengarkan bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Murah senyum sekalii kaa putri",  
                "pesan":"Semangat teruss buat kak putri!"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakaknya pendiam banget",  
                "pesan": "Semangat kuliah dan mengurus uang-uangnya ka titii!"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Baca wattpad dan au",
                "sosmed": "@nadillaandr26",
                "kesan": "Senyumnyaa cantik bangett kak",  
                "pesan": "Semangat terus buat ka nadilla, semangat kuliah dan semangat mengurus uangnya kak !"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1e4PZBkXva2IBxnlC-tiJ2wHuDwd54c9Q", #ka niya
            "https://drive.google.com/uc?export=view&id=1e9vUz9kq62zZnSQhfrqfOq97fCcnn-sn", #ka nisa
            "https://drive.google.com/uc?export=view&id=1eN6L3z4t3F2szlIoI6-T0fcHVUKow2fx", #ka wulan
            "https://drive.google.com/uc?export=view&id=1dzci07xxxXGleDNF7D8esgfuwsXaS2tA", #ka anisadini
            "https://drive.google.com/uc?export=view&id=1e9peUo_wPGGXcvk11tE5gLQzJLOkhGCk", #ka anisa fit
            "https://drive.google.com/uc?export=view&id=1eW3I-EwZIb081TEqRHd0ila_i7amYPoL", #bg fery
            "https://drive.google.com/uc?export=view&id=1eSQQH9orUDWR-9AKLzB1Y25fLtk8swvy", #ka dhea
            "https://drive.google.com/uc?export=view&id=1eLfb03NmqHDNo9Ai31uYlzbh_PKTv7rf", #bg fahrul
            "https://drive.google.com/uc?export=view&id=1eCoXeoR-10tEpJHMi8r9gpdzvFtOC2mK", #ka berli
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
                "kesan": "Kak niya ini baik syekali, asik, dan suka bercanda",  
                "pesan": "Semangat terus kuliahnya kakk! Jangan capek-capek ya"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Baca buku dan nonton film",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Ka nisa baik betull, dan asik betull",  
                "pesan": "Semangat terus ya kak kuliahnya! Jangan capek-capek ya"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Jl Raden Saleh",
                "hobi": "Belajar bersama pak tamaro",
                "sosmed": "@wlsbn0",
                "kesan": "Kakaknya baik sekali, suka bercanda, dan asik",  
                "pesan": "Semangat terus kuliahnya ya kakak! Jangan capek-capek ya"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Ngobrol",
                "sosmed": "@anisadini10",
                "kesan": "Ceria banget kakaknya, suka bercanda, dan cantik betul",  
                "pesan": "Semangattt teruss ya kakk! Jangan capek-capek"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Pendiam dan senyumnya manis banget",  
                "pesan": "Semangattt teruss kuliahnya ya kakk! Jangan capek-capek loh"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Bang fery ini baik tapi kadang usil, punya senyum yang memiliki banyak makna",  
                "pesan": "Semangat terus kuliahnya bang! Jangan capek-capek bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Solo",
                "alamat": "Natar",
                "hobi": "Suka ditipu sama penjual akun canva premium di shopee",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak dhea ini lucu, asik, suka banget bercanda, dan baik syekalii",  
                "pesan": "Semangat terus kuliahnya ka! Jangan capek-capek ya"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta, Jawa Tengah",
                "alamat": "Sukarame",
                "hobi": "Badminton, melukis, hiking, dan berenang",
                "sosmed": "@fhrul.pdf",
                "kesan": "Bang fahrul baik sekali, asik, dan suka bercanda",  
                "pesan": "Semangat terus kuliahnya bang! Jangan capek-capek ya!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Make up, nonton podcast, dan dengerin musik",
                "sosmed": "@berlyyanda",
                "kesan": "Ka berli pendiam, baik syekalii, dan asikk",  
                "pesan": "Semangat terus kuliahnya ka! Jangan capek-capek ya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
