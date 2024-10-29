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
            st.write(f"Hobi: {data_list[i]['hobi']}")
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
            "https://drive.google.com/uc?export=view&id=1e4PZBkXva2IBxnlC-tiJ2wHuDwd54c9Q", # ka niya
            "https://drive.google.com/uc?export=view&id=1e9vUz9kq62zZnSQhfrqfOq97fCcnn-sn", # ka annisa cahyani
            "https://drive.google.com/uc?export=view&id=1eN6L3z4t3F2szlIoI6-T0fcHVUKow2fx", # ka wulan
            "https://drive.google.com/uc?export=view&id=1dzci07xxxXGleDNF7D8esgfuwsXaS2tA", # ka anisa dini
            "https://drive.google.com/uc?export=view&id=1e9peUo_wPGGXcvk11tE5gLQzJLOkhGCk", # ka anisa fitri
            "https://drive.google.com/uc?export=view&id=1eW3I-EwZIb081TEqRHd0ila_i7amYPoL", # bang fery
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka renisha
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka claudea
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bang mirzan
            "https://drive.google.com/uc?export=view&id=1eSQQH9orUDWR-9AKLzB1Y25fLtk8swvy", # ka dhea
            "https://drive.google.com/uc?export=view&id=1eLfb03NmqHDNo9Ai31uYlzbh_PKTv7rf", # bang fahrul
            "https://drive.google.com/uc?export=view&id=1eCoXeoR-10tEpJHMi8r9gpdzvFtOC2mK", # ka berli
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
                "sosmed": "@ansftrynn_",
                "kesan": "Kakanya pendiam, baik sekalii, dan asik",  
                "pesan": "Semangat terus kuliahnya ka! Jangan capek-capek ya"# 1
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
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "@fleurnsh",
                "kesan": "-",  
                "pesan": "Semangat terus kuliahnya ya kak! Semangat Semangat Semangat"# 1
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
                "pesan": "Semangat terus kuliahnya ya kak! Semangat semangat semangat"# 1
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
                "pesan": "Semangat terus kuliahnya ya bang! Semangat semangat semangat"# 1
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
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "-",
                "sosmed": "@jeremia_s_",
                "kesan": "Bang jere baik banget, suka bikin panik anak orang, senyumnya manis",  
                "pesan": "Semangat terus kuliahnya bang jeree! Semangat semangat semangat" # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mkTak5uIF-h4Cmo54MMFxO8-FjRsJK6Y", # ka luthfi
            "https://drive.google.com/uc?export=view&id=1mm0tNq_UMbInh9X-Rj1dGgoM9gfwKjlj", # bang bintang
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "Semangat terus kuliahnya ka luthfi! Semangat semangat semangat"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan kota baru",
                "hobi": "Dengerin Ka Luthfi bernyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang bintang baik bener, suka share info dan suka jawabin pertanyaan dari ku, semua orang kenal beliau",  
                "pesan": "Semangatt kuliahnya bang bintang! Semangat semangat semangat"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1npu72Bsy_AJepQ9ZbZ7mkdWFSEEJ0SnH", # bg econ
            "https://drive.google.com/uc?export=view&id=1ujyyRLNrBBeLpy0-oXTDiXKg4VV2XJxT", # ka abet
            "https://drive.google.com/uc?export=view&id=1nVHHuU1VrcBeyScxi0TBxwZkctwM_NdF", # ka pipah
            "https://drive.google.com/uc?export=view&id=1ulXtsBjcDhGwVHNM4iC6YjdRog9_E54V", # ka allya
            "https://drive.google.com/uc?export=view&id=1nkbnr0mzDf4cKlCXpOxBmULP3HSVFSlF", # ka eksanty
            "https://drive.google.com/uc?export=view&id=1nT7UG99x5e_aiF3NLFGztI_L7WimDdv5", # ka hanum
            "https://drive.google.com/uc?export=view&id=1npaBh2Ih87rS95-PShzNhnUrrYLnSCDT", # bg ferdy 
            "https://drive.google.com/uc?export=view&id=1o-1mMVYzYh9Wn2bn2R0R76k3xFDIHMmJ", # bg deri 
            "https://drive.google.com/uc?export=view&id=1ngDQbKok2qNjER3LaKBNd1PDR0jN0KUr", # ka okta 
            "https://drive.google.com/uc?export=view&id=1n5W-Y1roXM0aTOlmpntXWq2gQMTvnJkZ", # bg deyvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg ibnu farhan 
            "https://drive.google.com/uc?export=view&id=1n5xlW1n_4hkw5dz8Fwdwrjme6hot1ODz", # bg jo
            "https://drive.google.com/uc?export=view&id=1nPLglQ44Mofcx_pzhUUPTepQKMkOH6Kx", # bg kemas
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg leon
            "https://drive.google.com/uc?export=view&id=1nC5BcpEJ8bkxlhgOPAwW2Gyv_oMB12vg", # ka presilia
            "https://drive.google.com/uc?export=view&id=1nM-nvwvXWs77-VoNISX6Y1uoX8k2PkG9", # ka aqila
            "https://drive.google.com/uc?export=view&id=1n6FwogQ-E1GrzLrE0BEOD8sumrwXTY9j", # bg sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka vanes
            "https://drive.google.com/uc?export=view&id=1nUh9vyaId4z8OVWkGWU5ZzP0Eznxt9lg", # bg ateng
            "https://drive.google.com/uc?export=view&id=1nNkycHEtdBBKF4bxY9ni0IA3le-fhWuE", # bg gede
            "https://drive.google.com/uc?export=view&id=1nXh8G3m2DRiyuL3WL47hIDejS-xJhWDN", # ka jaclin
            "https://drive.google.com/uc?export=view&id=1nSjN_lLPgB9Udkjh59TFXLc3Rla8HZdx", # bg rafly
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
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 1
            },
            {
                "nama": "Celisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Lucu dan energinya tidak abis-abis",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": "Baik, cantik bener, asik banget",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": "Baik, asik, murce senyum",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": "Friendly banget, gerak terus, energinya banyak banget",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "Lucu, baik hati, dan murah senyum",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Pendiam banget abangnya",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": "Senyum terus, baik, dan asik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Baik dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Lucu banget bang, energinya banyakk banget, dan baik hatiii",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 10
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
                "kesan": "Baik dan asik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": "Baik dan sepuh coding",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 13
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
                "kesan": "Cantik bangett, ramah, dan baik hati",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Baik banget, sabar, dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "Baik, sabar, dan asik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 17
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
                "hobi": "Dianggap malas nyatanya tidak",
                "sosmed": "@mfarhan.ath",
                "kesan": "Baik banget bang ateng, asik, dan keren",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Baikkk banget, informan, dan asik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Asikk banget kakanya, baik hati, dan sabar",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Lucu banget bang rafly, sabar, dan baik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 22
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
            "https://drive.google.com/uc?export=view&id=1u6-7SjzuDWnLdZ2ABbyE6v3nM4szsjIg", # bg rafi
            "https://drive.google.com/uc?export=view&id=1u1LLJtxfJJFmBLTjsErxA6x9Yegrjhu2", # ka anova
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg mujadid
            "https://drive.google.com/uc?export=view&id=1u9ZRC488KX1LpHHps9ip5BZhEvI-xbUf", # ahmad sahidin
            "https://drive.google.com/uc?export=view&id=1tCso8wDy5FSWNbHvcJ8EWrKjklIZ5Mgd", # bg fadhil
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg regi
            "https://drive.google.com/uc?export=view&id=1tKABvIYrr1CcngL63K9h-NUd9s4HE_8y", # ka syalasisha dina
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg natanael
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg anwar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka deva
            "https://drive.google.com/uc?export=view&id=1tyxHIjcEq--zJvrdqrd9utzRTxs2xAZY", # ka dinda
            "https://drive.google.com/uc?export=view&id=1tZSFhgwQ-0EszJc0j5kNBWuUKTH4G39y", # ka marleta
            "https://drive.google.com/uc?export=view&id=1uJ1BOWOfcxTzLmMGxU6XcqXRtDZWAiDb", # ka rut
            "https://drive.google.com/uc?export=view&id=1u6fxFZqrU09ji5B_if6JKdh270eqOKBB", # ka syadza
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg abdurrahman
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg aditya
            "https://drive.google.com/uc?export=view&id=1u-5W6pt0BykwmSSd7hgByaQ9yFvCENwh", # bg eggi
            "https://drive.google.com/uc?export=view&id=1uA-Wl3hFsrfbfGj53S_NTfg2rdFFP7Nt", # ka febiya
            "https://drive.google.com/uc?export=view&id=1u9L2KPD_z6Knv5qPpZLiWDT3_sTfjMKk", # bg happy
            "https://drive.google.com/uc?export=view&id=1uQtP-JwyU8eAaaGngbC04ntKYnhcJpkQ", # bg randa
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
                "kesan": "Kerenn buat bang rafi, asik, dan baik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Asik dan baik hatii",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 2
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
                "kesan": "Baik abangnya, sabar, dan asik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Baik abangnyaa dan asik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 5
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
                "kesan": "Baik, sabar, dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 7
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
                "kesan": "Lucu bangett, baik, dan sabar",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Baik hati dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Baikk banget kakanyaa dan asik juga",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Baik syekalii kakaknyaa",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 14
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
                "kesan": "Baik banget, murah senyum, dan keren banget",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Baik bangett dan asik benerr",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Baik bangett, penyabar, dan asik banget",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Baikk banget, sabar bangett, dan keren buat bang randa",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 20
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
            "https://drive.google.com/uc?export=view&id=1vtYRL4h5Ybw6KuYaYI7dMRA-TFkQtQ6q", # bg yogy
            "https://drive.google.com/uc?export=view&id=1v_L5tYZJhaE4jtbUORbl7B346ml2Mvb-", # ka dhita
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka nazwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg bastian
            "https://drive.google.com/uc?export=view&id=1usZgfREBEi0c-iKNCn7cyGqXpAcmnrTU", # ka dea mutia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka ester
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka natasya
            "https://drive.google.com/uc?export=view&id=1vLVA7oZrM8zgXo0TliIdGKPB3bbgJyrD", # ka novelia
            "https://drive.google.com/uc?export=view&id=1vMX5Ze14ySCUA6wydaQYWJUSNEr4Ol-g", # ka ratu
            "https://drive.google.com/uc?export=view&id=1uqjea-YW7IQkgnTNd2SlywoVy3Y_b6R9", # bg tobias
            "https://drive.google.com/uc?export=view&id=1um2cydTqVxUiwMCcdX1YyChQG6GfEeVA", # ka yo
            "https://drive.google.com/uc?export=view&id=1vEoDhNgUgc_F-vlYwKWlsYSd1_TPIcHY", # bg rizky
            "https://drive.google.com/uc?export=view&id=1vqc9nZKJUaUyE5vaGhFs_b6t-BIGDG9g", # bg arafi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka asa
            "https://drive.google.com/uc?export=view&id=1vxC8tuxwUl20CK4YqENq7Njau9o32KU-", # ka chalifia
            "https://drive.google.com/uc?export=view&id=1vBWQT0h5HPBVDt7JkgZfv_qcVt-D3yIm", # bg irvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka izza
            "https://drive.google.com/uc?export=view&id=1viMHNfTX1yakSevw2PszbONC-z5y7wUp", # ka khaalishah
            "https://drive.google.com/uc?export=view&id=1w1Hqubjy3IlEpM53KrK1HoHT16KGbVGo", # bg raid
            "https://drive.google.com/uc?export=view&id=1v7vcnfeA-S6jrc_0UBNbidm0RZkXTxf7", # ka tria


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
                "kesan": "Tegas, baik hatii, dan asik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Baik hati, asik, dan tersusun rapi",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 2
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
                "kesan": "Baikkk hati, lucu, dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 5
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
                "kesan": "Baikk hati dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobi": "Planning konten",
                "sosmed": "@jasminednva",
                "kesan": "Baik bangett, asik jugaa, kerenn banget kakaknya",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Membaca",
                "sosmed": "@tobiassiagian",
                "kesan": "Baik bangett, suka jawabin pertanyaan kita, keren bang tobiass",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Buat Jurnal",
                "sosmed": "@yo_annamnk",
                "kesan": "Baikk banget, bisa diajak bercandaa, asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "Baikk, asik, dan penyabar bangett",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Samping warjo",
                "hobi": "Sholat",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Kerenn abangnyaa, baik banget, asik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Cari ice breaking",
                "sosmed": "@u_yippy",
                "kesan": "Energinya sepertinya gak abis-abis kak uyi ini, baik banget, murah senyum, dan penyabar",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat"# 14
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Berbuat baik",
                "sosmed": "@chlfawww",
                "kesan": "Cantik bangett, ramah dan baik hati",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Keren bangett bang irvan, baik bener, dan murah senyum juga",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 16
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
                "kesan": "Baiik banget kakaknya, asik, dan murah senyum",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat"# 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Ikut seminar",
                "sosmed": "@rayths_",
                "kesan": "Baik banget abangnya, asik, dan penyabar",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Pemda",
                "hobi": "Sholawat",
                "sosmed": "@tria_y062",
                "kesan": "Lucuuu, baik banget, dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()


elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg dim
            "https://drive.google.com/uc?export=view&id=1wpijC68d2eRRkBLkZ0l-KKMP9hsBsEk3", # ka catherine
            "https://drive.google.com/uc?export=view&id=1w7oDAUw2xsYM9yLTnRZwv7KCVG_SGb2X", # bg akbar
            "https://drive.google.com/uc?export=view&id=1wCDWBo1dPm90l8xK2pvwU9GjYTHKc0dU", # ka rani
            "https://drive.google.com/uc?export=view&id=1wLI1_dbfvGy_N0hMTAVpdbRq2eMPjcxU", # bg rendra
            "https://drive.google.com/uc?export=view&id=1wDnaSLPRzhBCMhBAnzC1Yrh0fGdj0kdT", # ka salwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka yosia
            "https://drive.google.com/uc?export=view&id=1wwJOU-wtos7AInY5R5qqT0UzwOX2vUug", # bg ari
            "https://drive.google.com/uc?export=view&id=1wWb__YMl48YjcjjWaE1yUW1dhS2I0Njd", # ka azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka dearni
            "https://drive.google.com/uc?export=view&id=1wkPoelI8KcPM22Gh0csUsZDKoUYQYZc0", # ka meira
            "https://drive.google.com/uc?export=view&id=1wVB28qJP3TnazifwmYuUo7k7X2T-Ay3f", # bg rendi
            "https://drive.google.com/uc?export=view&id=1wP0vyCa3S8y3xFPbJOucIG6QmwcS1_mw", # ka renta
            "https://drive.google.com/uc?export=view&id=1wl4NjXIRyVyi6HGcpcq7uLM5crapFpyR", # bg josua
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
                "kesan": "Baik banget bang dimas, penyabar, asik, dan tegas",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Lucu banget kakk, imut banget, baik hati",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat"# 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": "Baik banget abangnyaa, penyabar, dan murah senyum",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 3
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobi": "Dengerin Musik",
                "sosmed": "@rannipu",
                "kesan": "Baik bangett dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Baikkk sekali, penyabar, dan keren bangett",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Baik hatii dan asik kakanya",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 6
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
                "kesan": "Pendiam banget, keren banget bang, dan sabar banget",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Imut kakanya, penyabarr, dan keren",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 9
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
                "kesan": "Baik banget dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": "Pendiam bangettt dan baik hati",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Baik bangett dan pendiam juga",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Siantar",
                "alamat": "Gerbang Barat",
                "hobi": "Nonton film",
                "sosmed": "@josuapanggabean_",
                "kesan": "Pendiam dan baik bangett abangnya",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zMpehay4dtCo9dXCesHdlWokxaL5bVZr", # bg andrian
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka disty
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka nabila
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg ahmad rizqi
            "https://drive.google.com/uc?export=view&id=1zBrlMh-MDanU7AZX4bCEH6vK61dEOJbs", # bg danang
            "https://drive.google.com/uc?export=view&id=1zGmToaLcZALYXyx-JaL89pcSsi6y6Tbl", # bg farel
            "https://drive.google.com/uc?export=view&id=11z3dXykLN0DUyRH4JRA3m-6eoaEV--E8_", # ka tesa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka nabilah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka alvia
            "https://drive.google.com/uc?export=view&id=1yiFpXDE8NP1rW8LTgqqc6Q6SLrSwY6Xt", # bg dhafin
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka elia
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Lapas",
                "hobi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Tegas, baik, dan sabaar",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Baik bangett dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Baik bangett dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat"  # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": "Pendiam, asik, dan baik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "Seru, lucuu, asik, dan baik bangett",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Keren banget bang, baik, dan asik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat"# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Pendiam banget kakaknya, sabar, dan baik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 7
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
                "kesan": "Baikk dan asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Pendiam banget dan asik banget",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "Baik banget, suka senyum, lucu gemes, dan keren bangett",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
