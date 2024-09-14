import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)
    
    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)
        
        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#C96868"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#FADFA1"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div> Lasso berasal dari kata Least Absolute Shrinkage and Selection Operator yang berarti pendektan regresi yang menggunakan regulasi L satu.
              Lasso merupakan kelompok ke-5 dalam CEO Himpunan Mahasiswa Sains Data 2024. Nama Lasso dapat dilambangkan sebagai kekompakan atau ikatan antar anggota serta focus, kecepatan, 
              kekuatan dan fleksibilitas.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Kelompok Lasso terdiri dari 13 anak yang menggemaskan dan 2 daplok yang sangat kece yaitu bang daris dan kak vita.
              Kelompok 5 keren, kelompok 5 paham, kelompok 5 NGIHAAA!</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
    home_page()


elif menu == "About Us":
    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aKgGYHML81d3_zF3uYM_BVcfA5iUJgmu",
            "https://drive.google.com/uc?export=view&id=137heKwmLXr_7wamKCV3s-o0TJPewNPOz",
            "https://drive.google.com/uc?export=view&id=1IBqxztysrM7MZ50gnq9B2hKcMHRvOwyC",
            "https://drive.google.com/uc?export=view&id=13_82BrUUVdyHLT5yMntXFvH3kuPHaEQs",
            "https://drive.google.com/uc?export=view&id=1ktGnPU5MGDSFmsUogiZ_lPvUNzP_VZOF",
            "https://drive.google.com/uc?export=view&id=1tdMNJ9i1I1sjCBj0QhFFnrEXEXXco7wY", # bgdap
            "https://drive.google.com/uc?export=view&id=10M72Db-tdMqJ9RP51CacDqZ1KIlnQRls",
            "https://drive.google.com/uc?export=view&id=1SxLAxycX64ZjlACAqQWxEnZ3tKEzqRKK",
            "https://drive.google.com/uc?export=view&id=1Qdf0jwwMKbqypEk1or3Rsozi8f4nTvN6",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Xgr4r69s6TzbjyI4QPjXk0MrVwa-D09a",
            "https://drive.google.com/uc?export=view&id=12rDP1bZ5rl5uM--JeI521GKuF4U83e2V",
            "https://drive.google.com/uc?export=view&id=1iFZJNN1zYjjpo3Kx7nzP2teJ9D4FUaqE",
        ]
        data_list = [
            {
                "nama": "Syahrialdi Rachim Akbar",
                "sebagai": "Pak Lurah",
                "nim": "123450093",
                "fun_fact": "Suka makan geprekk",
                "motto_hidup": "Pls gaada bug",
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "sebagai": "Bu Lurah",
                "nim": "123450004",
                "fun_fact": "Cinta es batu banget",
                "motto_hidup": "Jangan takut untuk mencoba",
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "sebagai": "Anggota",
                "nim": "123450119",
                "fun_fact": "Suka berenang, tapi gak jago renang",
                "motto_hidup": "Tidak ada kesuksesan tanpa usaha dan doa",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "sebagai": "Anggota",
                "nim": "123450123",
                "fun_fact": "Owner Risol dan Bakso Bakar",
                "motto_hidup": "Life With a Smile",
            },
            {
                "nama": "Raihana Adelia Putri",
                "sebagai": "Anggota",
                "nim": "123450041",
                "fun_fact": "Menulis is my laipppp",
                "motto_hidup": "Just keep on dreaming and one day you will see",
            },
            {
                "nama": "Daffa Hadyan Navista",
                "sebagai": "Anggota",
                "nim": "123450025",
                "fun_fact": "Suka baca komik, gak galak mukanya aja yang ketuaan",
                "motto_hidup": "Segala yang dilakukan ada gamblingnya",
            },
            {
                "nama": "Refa Destiny Pranata",
                "sebagai": "Anggota",
                "nim": "123450016",
                "fun_fact": "Anak teluk tapi udah pindah",
                "motto_hidup": "Kalo gagal coba lagi",
            },
            {
                "nama": "Feby Angelinna",
                "sebagai": "Anggota",
                "nim": "122450045",
                "fun_fact": "Orang kemiling tapi ngekos",
                "motto_hidup": "Yang penting bisa survive",
            },
            {
                "nama": "Givaro Ananta",
                "sebagai": "Anggota",
                "nim": "123450078",
                "fun_fact": "Gak bisa nonton horror",
                "motto_hidup": "Hal-hal sulit bukan berarti mustahil",
            },
            {
                "nama": "Arini Puteri Elandra",
                "sebagai": "Anggota",
                "nim": "123450069",
                "fun_fact": "Bisa bawa motor tapi gabisa belok.",
                "motto_hidup": "To Infinity And Beyond.",
            },
            {
                "nama": "Muhammad Ridwan",
                "sebagai": "Anggota",
                "nim": "123450091",
                "fun_fact": "Hobi badminton",
                "motto_hidup": "If you can believe it, you can achieve it",
            },
            {
                "nama": "Desman Velius Halawa",
                "sebagai": "Anggota",
                "nim": "123450114",
                "fun_fact": "Bisa makan mie seminggu tanpa nasi",
                "motto_hidup": "Kebahagiaan saya yang utama dan paling utama, kebahagiaan orang lain bukan tanggungjawab saya"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "sebagai": "Anggota",
                "nim": "123450052",
                "fun_fact": "Bisa tidur lebih dari 13 jam hari",
                "motto_hidup": "Tetaplah hidup",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    
    about_page()
