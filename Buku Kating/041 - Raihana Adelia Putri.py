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
            "https://drive.google.com/uc?export=view&id=114UC2P4J7jhhPS7CIZRhRbXg_Eyx3AW4", #bang gumi
            "https://drive.google.com/uc?export=view&id=1bvpcXoOp1ZZgoiKwoBLeB4xZ_0kag8Q3", #bang pandra
            "https://drive.google.com/uc?export=view&id=1SCWm4mtoh1YqlaZTTHsrAxoYdmQ6pS-w", #kak meliza
            "https://drive.google.com/uc?export=view&id=114_Z-rf8BJT2hXbm7QA3QY9qBf3ZOeh-", #kak putri
            "https://drive.google.com/uc?export=view&id=1fte1BlFq1hdtrQuHjzkBWBPWjpdPz6pp", #kak hartiti
            "https://drive.google.com/uc?export=view&id=1LEEG3-HCwsD66SXh1cg2qHrWTFY0Fgf2", #kak nadhila
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
                "kesan": "Tegas, asik, dan santai",  
                "pesan":"Semangat kuliahnya bang gumilang !" # 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450142",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang pandraa !!!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450044",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobi": "Nonton Drakor",
                "sosmed": "@wulandarimelinza",
                "kesan": "Kakaknya lucuuuu",  
                "pesan":"semangat dan lancarr terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobi": "Dengerin Bang Pandra main gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Asik dan santai",  
                "pesan":"semangat dan lancarrr terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Baca webtoon",
                "sosmed": "@hrtpdlh",
                "kesan": "Seyumnya manis banget kak",  
                "pesan":"semangat dan lancarr terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadhilah Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Gangguin Kak Liza tidur, Baca wattpad dan AU",
                "sosmed": "@nadhillahand26",
                "kesan": "Asik dan santai",  
                "pesan":"semangat dan lancarrr terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xUjjVPTUsryvWE9ZtmVJT1kD_oVdkriN", #kak nia
            "https://drive.google.com/uc?export=view&id=1G2W_f5s2jM1QKN7CHJo4NSSk05zyrPyq", #anisa cahyani
            "https://drive.google.com/uc?export=view&id=1ozndOquiwQe0LaE_uyHjCi3MbFUuIZjB", #kak wulan
            "https://drive.google.com/uc?export=view&id=1FWvTMASuOyn5s-gngP0rG2yFa5uo4aFd", #kak anisa dini
            "https://drive.google.com/uc?export=view&id=1BeJ29q9O1an6AxJcTArTjMuxmVL2Akhi", #kak anisa fitriyani
            "https://drive.google.com/uc?export=view&id=1lo07cn-IXTs53H6jLloRAXeTLGvsSPET", #kak feryadi
            "https://drive.google.com/uc?export=view&id=1GkeJNX2sQupZMytr9vHZkkT4V8AeHRI8", #kak dhea
            "https://drive.google.com/uc?export=view&id=1s6nIZ563N0filIIZGMT4znGHHar2XP3i", #bang fahrul
            "https://drive.google.com/uc?export=view&id=1e98TEBoW1MTBhhH5Zy660J3jWiqjLs25", #kak berliana


        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450033",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching GPT",
                "sosmed": "@Trimurniyaa_",
                "kesan": "Kakaknya asikkk banget",  
                "pesan":"semangat ngaspraknya kak niaaa, semangat juga kuliahnya kakak !!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Baca buku dan nonton film",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Seruu abissss kak",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Belajar bersama Pak Tamaro",
                "sosmed": "@wlsbn0",
                "kesan": "Ramahhh sekali dan tentunya cantikkk dong",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Ngobrol",
                "sosmed": "@anisadini10",
                "kesan": "Kakaknya asikkk banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Annisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@ansftynni_",
                "kesan": "Kakaknya asikkk banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatra Selatan",
                "alamat": "Way Kandis",
                "hobi": "Baca buku",
                "sosmed": "@fr_yulius.",
                "kesan": "Abangnya asikkk banget",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Solo",
                "alamat": "Natar",
                "hobi": "Ngobrol",
                "sosmed": "@.dheamelia",
                "kesan": "Kakaknya asikkk banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450081",
                "umur": "22",
                "asal":"Surakarta, Jawa Tengah",
                "alamat": "Sukarame",
                "hobi": "Badminton, melukis, hiking, dan berenang",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya asikkk banget",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450069",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Way Huwi",
                "hobi": "Make up, nonton, podcast, dan dengerin musik",
                "sosmed": "@berlyyana",
                "kesan": "Kakaknya asikkk",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": ".",
                "sosmed": "@Jeremia_",
                "kesan": "Abangnya asikkk",  
                "pesan":"semangat terus kuliahnya bang !"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1g2lw5YpLkylPfVrFIJZqkmd15-JSRnMo", # ka luthfi
            "https://drive.google.com/uc?export=view&id=1iKubLnX9-artTGwc3oSH8JI8TaNA88Nz", # bang bintang
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
                "kesan": "kagum banget sama public speaking kak luthfiii",  
                "pesan": "Semangat terus kak luthfiii!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan kota baru",
                "hobi": "Dengerin Ka Luthfi bernyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Informasi yang di share bergunaaaa banget",  
                "pesan": "Semangatt kuliahnya bang bintang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oGHqJjk2hC5u-byQIS91JQefc3NOKSUz", # bang econ
            "https://drive.google.com/uc?export=view&id=1qJsA_oCjBFX6w29mc46_ljkfeZrlLhBT", # kak elisabet
            "https://drive.google.com/uc?export=view&id=1ezlLTQS8wYYP58MgTke4DxeE6HagzPzT", # kak afifah
            "https://drive.google.com/uc?export=view&id=1uDr5p4VpfTne6oSB6-VgjaV_BYDsZZtO", # kak allya
            "https://drive.google.com/uc?export=view&id=1DbZ_oJ_W6T_1tFRiSn-rxk2yfBtARtFE", # kak eksanty
            "https://drive.google.com/uc?export=view&id=1TtKOlM6xg8JLfK7aN5JA-kXUJxpmz-pI", # kak hanum
            "https://drive.google.com/uc?export=view&id=1nwbx4R_Sw5eKUcID-Ja6ualzvaMsf6H3", # bang ferdy
            "https://drive.google.com/uc?export=view&id=1ZGHO1ZSyZk4zBd_gix5jTBv48YOHSiX-", # bang deri
            "https://drive.google.com/uc?export=view&id=1pCE7KqD6aQsoFcCrSJp1uTOytqPm6wOJ", # kak okta
            "https://drive.google.com/uc?export=view&id=1vOLY6k8y0S4qaDZpiD282leXaF0P1QWn", # bang deyvan
            "https://drive.google.com/uc?export=view&id=1p4cmK0WJKgjTpc1TUx2eavjwGiThZifb", # bang jo
            "https://drive.google.com/uc?export=view&id=1rnF2TYRQhEq_kR_7p6-azRGjcRaUiXjE", # bang kemas
            "https://drive.google.com/uc?export=view&id=1-Lt8Uz8CBxdWNqQLIqLGUIvDjdQgRLEZ", # kak presilia
            "https://drive.google.com/uc?export=view&id=1udQGS5lGqqYbUA3AM7wAvb6Uc36AR895", # kak aqila
            "https://drive.google.com/uc?export=view&id=12quKfK8ISOR_sEXay4IKOoWh77n7hYph", # bang sahid
            "https://drive.google.com/uc?export=view&id=1poNXU0ECUf555IW5cCjOxEmudQuGxLU9", # bang ateng
            "https://drive.google.com/uc?export=view&id=1fnc62L5pO7-Dx9G7leyRm2csoSctjCt4", # bang gede
            "https://drive.google.com/uc?export=view&id=1DuikvVKdn7UuEeJEzfXaqW4B7OY5q6Z1", # kak jaclin
            "https://drive.google.com/uc?export=view&id=1xsvc2-p24g66e_jMftYyoySFllDZwnHx", # bang rafly
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
                "kesan": "Disiplin dan tegas",  
                "pesan": "Semangatt kuliahnya bang!" # 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknyaaa maniss ",  
                "pesan":" Semangat terusss kak abettt >_<" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": "Lucu dan seru",  
                "pesan":"Semangatt terus kak fifaah >_<" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": "Asik banget kakaknya",  
                "pesan": "Semangattt terus kak alya >_<" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": "",  
                "pesan": "Semangatt terus kak eksantyy" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "  ",  
                "pesan": "Semangat kak hanummm" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya pendiem",  
                "pesan": "Kuliahnya semangatt terus bang kevinn" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": "Abangnya asikk",  
                "pesan": "Semangat teruss banggg " # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya maniss",  
                "pesan": "Semangat teruss kak okta" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "ASIKKKKK BANGET BANGGG",  
                "pesan": "Semangattt teruss bang devyannn" # 10
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
                "kesan": "Asik dan tegas",  
                "pesan": "Semangattt teruss bang joooo" # 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": "Singkat saja, seruuu bang",  
                "pesan": "Semaangatttt terussss bang kemass" # 13
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
                "kesan": "  ",  
                "pesan": "  " #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "  ",  
                "pesan": "  " # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "  ",  
                "pesan": "  " # 17
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
                "kesan": "  ",  
                "pesan": "  " # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "  ",  
                "pesan": "  " # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "  ",  
                "pesan": "  " # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "  ",  
                "pesan": " " # 22
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
            "https://drive.google.com/uc?export=view&id=18QXTkiHrgp1s6Om1N7CgnMrjNJg83c7h", # bg rafi
            "https://drive.google.com/uc?export=view&id=1PPd42ERx0thczRZrmeC8CT6uUAt4gaHG", # ka anova
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bang mujadid
            "https://drive.google.com/uc?export=view&id=1_mFAEZVEUC85eqnUDnUpC58oJcO5bDgu", # bang ahmad sahidin
            "https://drive.google.com/uc?export=view&id=17kl4MoBegKJcL1WA1uYUYIS8r2YK40Oh", # bang fadhil
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bang regi
            "https://drive.google.com/uc?export=view&id=1TGE3zC4eVCXIPT9k4Iguf9IzedrRfDUK", # kak syalasisha dina
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bang nathanel
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bang anwar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bang deva
            "https://drive.google.com/uc?export=view&id=1LSrkQAdwzxTZueY8PAIN-x80j-D14wIO", # ka dinda
            "https://drive.google.com/uc?export=view&id=1DcRCdcsXNyTF8FmRxjP6h8tC2cfmYYCv", # ka marleta
            "https://drive.google.com/uc?export=view&id=10bmd_hd82pQaXG1BF_Wo6ufdyCoWktLf", # ka rut
            "https://drive.google.com/uc?export=view&id=1acJtd2VxrgnVm-emISpe0EiOKEvDoqW0", # ka syadza
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bang abbdurahman
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bang aditya
            "https://drive.google.com/uc?export=view&id=1jVxb2f1YMm3DuG8XKGTcWN5si0ARA-_q", # bg eggi
            "https://drive.google.com/uc?export=view&id=128Ya4UE1Erx0g0jaONVFiyzcPycY_vpO", # ka febiya
            "https://drive.google.com/uc?export=view&id=1ZZrVACwtMBa_5ejagBj95pS1bKJ3BtmX", # bg happy
            "https://drive.google.com/uc?export=view&id=11P8gq9tqfkIMC18aZywRg5QL23mTSJTP", # bg randa
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
                "kesan": "seruu abiss bang rafii ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "Cantikkkk sekalii kak leta >_< ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 20
            },
            {
                "nama": "Vita Anggraini",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobi": "  ",
                "sosmed": "@",
                "kesan": "Cantikk kakak nya >_<",  
                "pesan": "Sehatttt dan semangatt selalu kak" # 21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14IN-RBEUAAeW5M9qnCj0iIjP94Dgz_PG", # bg yogy
            "https://drive.google.com/uc?export=view&id=1U2XPjEu2uZb9V9CUeddqgxZzeRWIPQaW", # ka dhita
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka nazwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg bastian
            "https://drive.google.com/uc?export=view&id=1q2H3KeujMqItDcJcSGYG3wJY2SlYy6xS", # ka dea mutia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka ester
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka natasya
            "https://drive.google.com/uc?export=view&id=1aCjiAsqD1Nf-ErHaS1pL6KrH5Us6Z4eD", # ka novelia
            "https://drive.google.com/uc?export=view&id=1KoeskJXY__GvmRzC84uEuIlYQhaZ-5d7", # ka ratu
            "https://drive.google.com/uc?export=view&id=1ofMDqeruC6CbF3-RzxIgtTQ6WK3Yeibh", # bg tobias
            "https://drive.google.com/uc?export=view&id=1e5O7j_xZgZgK6PjMY7E-SIJMht6GaQAn", # ka yo
            "https://drive.google.com/uc?export=view&id=1jDNxunlxEGJSbdvQbfg3XDZBYysaSFV8", # bg rizky
            "https://drive.google.com/uc?export=view&id=1MnBpCPs67BZXKVBR7QmivbtyMsdup9AA", # bg arafi
            "https://drive.google.com/uc?export=view&id=1exe9-hHo62lmWOBTLhl3r5VJHy1hEN3C", # ka asa
            "https://drive.google.com/uc?export=view&id=1p8jC_-ij6a_c5VxgPVgfzK_rfcbkujWm", # ka chalifia
            "https://drive.google.com/uc?export=view&id=1fiqxwx0VqOURxzFyjQAOvC5jY08OzSAS", # bg irvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka izza
            "https://drive.google.com/uc?export=view&id=1c-sBbHWnKKjgZZuk7iS5qUi1OEraBWI3", # ka khaalishah
            "https://drive.google.com/uc?export=view&id=1JOGFqWk1f0hmvW30awTQEeYCmIMpC1z9", # bg raid
            "https://drive.google.com/uc?export=view&id=1C-eqhBDRFqcWKyf6S3IUxrNs0HWIb1aY", # ka tria
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
                "kesan": " serius tapi asik ",  
                "pesan": "Semangatt kuliahnya bang!" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
                "kesan": "  ",  
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
               "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang!" # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Cari ice breaking",
                "sosmed": "@u_yippy",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak!"# 14
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
                "pesan": "Semangatt kuliahnya kak!" # 15
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
                "pesan": "Semangatt kuliahnya bang!" # 16
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
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! "# 18
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
                "pesan": "Semangatt kuliahnya bang! " # 19
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
                "pesan": "Semangatt kuliahnya kak! " # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()




elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qi7DHBBl_hdOafdb1bVc3paKjq1u6-u_", # bg dim
            "https://drive.google.com/uc?export=view&id=1k_MjgdDdNr7unyyFzc7tp5WoynnU7J60", # ka catherine
            "https://drive.google.com/uc?export=view&id=1EbvTd6YJ_GpEs557F91ptzwwEC9l1C_7", # bg akbar
            "https://drive.google.com/uc?export=view&id=1INF8jB1HmWLGdsUQRI07mEqFr2reipi7", # ka rani
            "https://drive.google.com/uc?export=view&id=13t4fAbmckVG15C0Zkg8FUJzUEjm9dwWO", # bg rendra
            "https://drive.google.com/uc?export=view&id=1eh-is3yDJf22_kgz9DNXEZANoCH_S4_x", # ka salwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka yosia
            "https://drive.google.com/uc?export=view&id=1dS6wNzNPHy5ktHrYNKfmXlSzwF-M4TRZ", # bg ari
            "https://drive.google.com/uc?export=view&id=19VRo00rZc2Z4u1jhlR79UzF_P4Fnk7xV", # ka azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka dearni
            "https://drive.google.com/uc?export=view&id=1tHvtKYKnd5I2aCvNaGPGM1GyIAAYMRdk", # ka meira
            "https://drive.google.com/uc?export=view&id=1Exi9gsqGTAQ4s8VyB7U1it5Z5meX6qFa", # bg rendi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka renta
            "https://drive.google.com/uc?export=view&id=19rQqz499-Z7eKHiGmsQvYhJH0XWtggkZ", # bg josua
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
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang!" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak!"# 2
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! " # 3
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobi": "Dengerin Musik",
                "sosmed": "@rannipu",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak! " # 4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang! " # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak!" # 6
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
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang!" # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak!" # 9
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
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak!" # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang!" # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak!" # 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Siantar",
                "alamat": "Gerbang Barat",
                "hobi": "Nonton film",
                "sosmed": "@josuapanggabean_",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang!" # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ymq7dNU9EnCg6-QGgLwYMXt9qzZUrKYT", # bg andrian
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka disty
            "https://drive.google.com/uc?export=view&id=1SsemnF_6kL63UoLsSsqTwtK9CL1LDqlZ", # ka nabila
            "https://drive.google.com/uc?export=view&id=1oRYp3aCrsBL7BnSfRw6Ze8q2cSRzBWzv", # bg ahmad rizqi
            "https://drive.google.com/uc?export=view&id=1IHpFZWVfzmy8sKQhKVQQ9SJslaSpx2tq", # bg danang
            "https://drive.google.com/uc?export=view&id=1W2SPrFfAAmik-Db0Mk-36tolW7mSlMOP", # bg farel
            "https://drive.google.com/uc?export=view&id=1tmdL76ts-5RnS9gv4le2U_XX4id7vHnz", # ka tesa
            "https://drive.google.com/uc?export=view&id=1dRWnpFlL32knlJdKcoTY8JyXb2lpB7fJ", # ka nabilah
            "https://drive.google.com/uc?export=view&id=1xPOSE_dlHE2DPv-LYeL6BOmQyKPNs02w", # ka alvia
            "https://drive.google.com/uc?export=view&id=1k2rAljh-4tEF8nXlfMN_e7VFE5Pv1--_", # bg dhafin
            "https://drive.google.com/uc?export=view&id=1VepYRRT8HjlwECsk3F0gjwdfhv11nMDP", # ka elia
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
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang!" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "  ",  
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
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak!"  # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang!" # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang!" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "kerenn bang",  
                "pesan": "Semangatt dan lancar kuliahnya bang!"# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Ramaahhh sekalii kak ",  
                "pesan": "Semangatt kuliahnya kak!" # 7
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
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak!" # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya bang!" # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "  ",  
                "pesan": "Semangatt kuliahnya kak!" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()


# Tambahkan menu lainnya sesuai kebutuhan


