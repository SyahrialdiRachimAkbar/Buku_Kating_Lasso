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
            "https://drive.google.com/uc?export=view&id=170CVWI-5VoNhNSE8epSbAAHfJGcu853_", #ka titi
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
                "nim": "121450065",
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
            "https://drive.google.com/uc?export=view&id=1FAxzGuBSbG2R_6UTUaOZH2aOQZt9OgeX", # ka anisa fitri
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
                "pesan": "Semangat buat ka nisa, terjang semua badainya kakk"# 1
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
                "pesan": "Happy terus ya kak, rajin-rajin belajar sama pak tamaro sebelum lulus kakk, ehehe"# 1
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
                "pesan": "Semangatt terus ya kak. Jangan menyerah dan jangan capek"# 1
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
                "pesan": "Terus semangat dan jangan pernah menyerah"# 1
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
                "pesan": "Sehat-sehat bang feryy, jangan lelah untuk bertemu dengan saya ya bang"# 1
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
                "pesan": "-"# 1
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
                "pesan": "-"# 1
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
                "pesan": "-"# 1
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
                "pesan": "Kak dhea, semangatt ya, semangat apapun intinya"# 1
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
                "pesan": "Bang fahrul, semangat semester 7 nya dan semangat terus apapun ituu ya bang"# 1
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
                "pesan": "Kak berli, happy terus ya kak. Semangat untuk kuliahnya yahhh"# 1
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
                "pesan": "Bang, terus semangat ya, jangan hectic-hectic. Jangan bikin panik anak orang terus-terusan yaaak" # 1
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
                "kesan": "Dari saat GO, aku suka pembawaan kakak pas materi, serius dan juga tegas dalam 1 diri. Asik banget, baik, dan jempol keren buat ka luthfi",  
                "pesan": "Semangattt kak luthfi, terus bersinergi dan terus tersenyum ya kak. Aku suka sama gaya pembawaan kak luthfi"
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
                "pesan": "Bang, Semangat terus yaa. Terus baik ke orang-orang ya bang, keren buat bang bintang"
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
                "pesan": "Bang econ, semangat untuk kuliahnya di semester 7 ini yaa" # 1
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
                "pesan": "Terus tersenyum ya kak abet, semangat kuliahnya" # 2
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
                "pesan": "Jangan hilang senyumnya yang cantik itu ya kak, semangat terus kakkk pipah" # 3
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
                "pesan": "Ka allya, sehat-sehat ya kak, lancar-luncur buat kuliahnya, tidak boleh menyerah ya kak" # 4
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
                "pesan": "Kak eksanty, jangan nangis terus ya kita harus happy-happy" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "Lucu, baik hati, dan gemass pipinyaa",  
                "pesan": "Kalau bisa jangan lunturkan senyum dan ketawanya ya kak" # 6
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
                "pesan": "Bang ferdy, semangat teruss ya bang. Sehat dan lancar buat kuliahnya" # 7
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
                "pesan": "Bang deri, jangan menyerah dan pantang terus rintangannya" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Baik, kalem, asik",  
                "pesan": "Happy-happy buat kak okta ya, jangan menyerah pokoknyaa" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Lucu banget bang, energinya banyakk banget, dan baik hatiii",  
                "pesan": "Bang deyvannn harus semangattt, semangat dalam kuliahnya dan semangat dalam kesehariannya" # 10
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
                "pesan": "Bang jo, sehat-sehat ya bang dan semangat terus buat kuliah serta kesehariannya" # 12
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
                "pesan": "Beri jempol buat bang kemas, semangat terus ya bang kemass" # 13
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
                "kesan": "Cantik bangett deh serius, ramah, dan baik hati",  
                "pesan": "Bahagia terus kak lili, jangan ada sedih yaa kak" #15
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
                "pesan": "Kak rafa ini harus semangat dan harus senyum terus yahh" # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "Suka bercanda, asik, dan baik banget",  
                "pesan": "Semangat ya bang, jangan menyerah apapun kondisinya" # 17
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
                "kesan": "Baik banget bang ateng, asik, dan keren banget",  
                "pesan": "Terus semangat dan jangan menyerah" # 19
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Baikkk banget, informan, dan asik",  
                "pesan": "Bang, lancar-lancar kuliahnya ya bang, sedikit lagi dan harus semangaatt" # 20
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
                "pesan": "Kak jaclin, semangatt dan jangan menyerah yaa" # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Lucu banget bang rafly, keren, asik",  
                "pesan": "Bang rafly, bahagia terus dan jangan lunturkan senyummu yang lucu" # 22
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
                "kesan": "Kerenn bang rafi, asik, dan baik",  
                "pesan": "Tetap semangat dan jangan menyerah ya bang" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Baik banget, lemah lembut, kalem, sabar",  
                "pesan": "Semangat buat kak anova, namanya lucu bisa disingkat ada unsur sains data nya" # 2
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
                "kesan": "Sabar banget abangnya, keren puol",  
                "pesan": "Bang jangan pernah menyerah, untuk mendapatkan hal yang menarik" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Cakep, baik hati, dan asik",  
                "pesan": "Bang kalau pake masker cakep bang" # 5
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
                "kesan": "Baik, kalem, pendiem, lucu banget senyumnya",  
                "pesan": "Terus semangat ya kak, jangan menyerah dan bahagia selalu" # 7
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
                "pesan": "Ka dinda semangat untuk menjalani hari-hari mu yaa" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Tinggi, senyumnya cantik, baik, sabar",  
                "pesan": "Bahagia selalu dan jangan lepasin senyumnya ya kak, semangatt" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Ka rut baik banget, suaranya lembut lucu, kalem",  
                "pesan": "Terus menjadi orang baik yang dikenal orang-orang ya kak, bahagia selalu, semangat kuliahnya kak" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Baik banget, kalem, sabar, lucu gemas",  
                "pesan": "Semangat kuliahnya ya kak, jaga kesehatan dan semangat resume SG nya" # 14
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
                "kesan": "Baik banget, murah senyum, keren banget, cakep banget",  
                "pesan": "Bang eggi bahagia terus ya, semangat terus ya bang, semangat Ngoding WISATA nya dan jaga kesehatan" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Cantik banget, imut, baik",  
                "pesan": "Kak harus bahagia yaa, semangat menjalani hari-harinyaa" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Baik bangett, penyabar, asik banget, seru",  
                "pesan": "Seperti namanya, harus happy ya bang. Semangattt terus yaa" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Keren, baik, sabar, asik",  
                "pesan": "Bang Randa, tetap semanagattt dan jangan menyerah. Rindu di tutorin matdas sama bang randa" # 20
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
            "https://drive.google.com/uc?export=view&id=1B7W4bOkXYJRRCL73Z4X7yrOavZJMzja-", # ka asa
            "https://drive.google.com/uc?export=view&id=1vxC8tuxwUl20CK4YqENq7Njau9o32KU-", # ka chalifia
            "https://drive.google.com/uc?export=view&id=170gydUYL-FEeAY7opoHyWvAokYkuurtw", # bg irvan
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
                "kesan": "Tegas, baik hatii, kece,asik",  
                "pesan": "Semangat kuliahnya ya bangg, semangat di semester 7 ini, dan teruslah bahagia" # 1
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
                "pesan": "Semangat ya kak dita, bahagiaa selalu dan jaga kesehatan ya kak" # 2
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
                "pesan": "Semangatt buat ka dea, jangan lupa bahagia, dan semangat menjalani hari-harinya" # 5
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
                "kesan": "Cantik banget, baik, asik",  
                "pesan": "Semangat terus kak, bahagia selalu, dan jangan menyerah" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobi": "Planning konten",
                "sosmed": "@jasminednva",
                "kesan": "Baik bangett, asik jugaa, kerenn, kalem, independent woman",  
                "pesan": "Sehat terus ya kak mine, jangan kelelahann, bahagia teruss" # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Membaca",
                "sosmed": "@tobiassiagian",
                "kesan": "Baik bangett, suka jawabin pertanyaan kita, keren, sabarr sekali",  
                "pesan": "Semangatt ya bang, udah keren banget abang menjadi ketuplak dimana-mana, sehat terus ya bang tobias" # 10
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
                "pesan": "Ka yoo, jangan lupa bahagia yaa, semangat kuliahnyyaa" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "Baikk, asik, penyabar, cakep banget",  
                "pesan": "Bang semangat terus, semangat juga kuliahnya, " # 12
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
                "pesan": "Masyaallah bang rafi, hobinya sangat mengena relung jiwa dan hati. Semangat ya bang, jaga kesehatan" # 13
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
                "pesan": "Semangatt kakkk uyii, jangan kelelahan yyaa, semangat mencari ice breakingnya karena itu hal yang seru"# 14
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
                "pesan": "Kak, jangan menyerah, tetap semangat, tetap bersinergi" # 15
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
                "pesan": "Semangatt kuliahnya, senyumnya jangan luntur ya bang" # 16
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
                "kesan": "Baiik banget, asik, murah senyum",  
                "pesan": "Masyaallah kak, jangan lupa bahagia dan jaga kesehatan selalu ya kak"# 18
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
                "pesan": "Semangatt kuliahnya bang! Jangan cape buat ikut seminar ya bang" # 19
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
                "pesan": "Semangatt ka yuna, bahagia terus ya kak, dan jangan lupa jaga kesehatan" # 20
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
                "kesan": "Baik banget, seru, asik, tegas, dan punya segala jawaban untuk semua pertanyaan",  
                "pesan": "Terus menjadi orang baik yang dikenal orang-orang ya bang, semangat terus bang dimas jangan sampe kelelahan" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Lucu banget kak catherine, imut, baik hati, ketawa nya lucuu, intinya lucu banget kak catherine",  
                "pesan": "Buat kak catherine, sehat selalu yaa, semangat kuliahnya, gak bosen buat ngelihatin foto kita berdua karena gemes bangettt kak"# 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": "Baik banget abangnyaa, penyabar, murah senyum, mukanya selalu terlihat fresh",  
                "pesan": "S" # 3
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobi": "Dengerin Musik",
                "sosmed": "@rannipu",
                "kesan": "Senyumnya lucu, baik banget, murah senyum",  
                "pesan": "Lancar terus kuliahnya kak rani, always senyum ya kakk lucu banget soalnya, jaga kesehatan jugaa" # 4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Keren bangett, tegas tapi bisa diajak bercanda, baik banget",  
                "pesan": "Sehat-sehat ya banggg, jaga kesehatan, publish lagunya dong mau dengar" # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Gemas, baik banget, asik, dan sabar",  
                "pesan": "Lancar terus kuliahnya ya kak, jangan pantang menyerah, Semangat" # 6
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
                "kesan": "Pendiam banget, sabar, dan baik bangett",  
                "pesan": "Sehat-sehat ya bang, semangat terus, dan jangan lupa jaga kesehatann" # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Imut kakanya, penyabarr, dan baik hati",  
                "pesan": "Ka zizah semangatt ya, bahagia selalu dan jangan lupa jaga kesehatan" # 9
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
                "kesan": "Pendiem, lucu banget, gemes, baik, kalem",  
                "pesan": "Bahagia selalu ya kak, jangan lupa senyum dan jaga kesehatan" # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": "Pendiam banget, tapi baik dan sabar sekali",  
                "pesan": "Semangat terus ya bang, jaga kesehatan, dan semangat menjalani kuliahnya" # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Baik bangett, pendiam",  
                "pesan": "Ka renta, sehat-sehat ya, jangan lupa senyum, semoga kita bisa bertemu di kemudian hari lagi ya kak" # 13
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
                "pesan": "Semangat bang josua, jangan lupa bahagia dan tersenyum selalu yaa bang" # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zMpehay4dtCo9dXCesHdlWokxaL5bVZr", # bg andrian
            "https://drive.google.com/uc?export=view&id=1ybOVOODzlK-ypfL1_iTjMnnkrdHCQbOd", # ka disty
            "https://drive.google.com/uc?export=view&id=1BDwHJc07CVSOLr3l-HNX-4QL4RcVlbrL", # ka nabila
            "https://drive.google.com/uc?export=view&id=12c9KNcT2Xh40CZuaL2_n6s0dOlzcHEZM", # bg ahmad rizqi
            "https://drive.google.com/uc?export=view&id=1zBrlMh-MDanU7AZX4bCEH6vK61dEOJbs", # bg danang
            "https://drive.google.com/uc?export=view&id=1zGmToaLcZALYXyx-JaL89pcSsi6y6Tbl", # bg farel
            "https://drive.google.com/uc?export=view&id=1z3dXykLN0DUyRH4JRA3m-6eoaEV--E8_", # ka tesa
            "https://drive.google.com/uc?export=view&id=1_GvPEJGohf0_4YlHNW3HMOMvGBlRtpgB", # ka nabilah
            "https://drive.google.com/uc?export=view&id=1ypErcS_82HD7H5tjh8Azd17P3eBlXOTX", # ka alvia
            "https://drive.google.com/uc?export=view&id=1yiFpXDE8NP1rW8LTgqqc6Q6SLrSwY6Xt", # bg dhafin
            "https://drive.google.com/uc?export=view&id=1z8jqramPA3N-gbXwvcblOcEqr5RCO6M8", # ka elia
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
                "pesan": "Semangattt terus buat bang andrian, semangat juga buat kuliahnya, semangat untuk semester 7 nya juga" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Asik banget, seru, murah senyum, dannn pastinya baiik banget",  
                "pesan": "Semangat ya kak disty, jaga kesehatan selalu dan jangan kelelahan ya kak" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Baik, cantik kakaknya, asik",  
                "pesan": "Jangan kelelahan ya kak, semangat semester 7 nya okey"  # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": "Pendiam, badannya bagus, cakep bangg",  
                "pesan": "Lancar terus ya bang kuliahnya, semangat dan semangaatttt teruss" # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "Seru, baik bangett, suka jawabin pertanyaan dan tidak sombong",  
                "pesan": "Semangatt buat bang danang yaa, sehat selalu bangg. Kece betul bang danang iniii" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Keren buat bang farel, capo kita semua",  
                "pesan": "Semangat terus bang farel, jaga kesehatan ya bangg"# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Pendiam banget kakaknya, baik dan tidak sombong kok",  
                "pesan": "Kak tessa, jangan diem-diem aja ayok ngobrol sama aku, semangat teruss yahh" # 7
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Baikk banget dan asik",  
                "pesan": "Ka nabilah, semangat kuliahnya di semester 7 ini ya kakk" # 8
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviaginting",
                "kesan": "Kakaknya pendiem, tapi lucu, baik, dan asik banget",  
                "pesan": "Semangat kuliahnya kak alvia, aku jarang lihat kakak semoga kita lebih sering bertemu lagi yah" # 9
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
                "pesan": "Semangatt bang dhafin, pantang mundur sebelum semuanya tercapai" # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "Baik banget, suka senyum, lucu gemes, informatif, dan keren banget",  
                "pesan": "Kak elia senyumnya lucu banget, sehat terus dan semangat terus ya kak" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17IHVFfr4PhBpBy24xw0v9uLJToLcrXMi", #bang wahyu
            "https://drive.google.com/uc?export=view&id=16m3Do-Xmg7u7VCqzAndL5Lekcnt-HenU", #ka elok
            "https://drive.google.com/uc?export=view&id=1ELSeOQNsWCdAoYz6efzNIykq5DFURq0M", #ka arsyiah
            "https://drive.google.com/uc?export=view&id=1BRp0dETWc0kM17j3e4SU9rMHPSuWa8-9", #ka cibel
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ka eka
            "https://drive.google.com/uc?export=view&id=16PgVuZoYlTudP63QagUWLv4eFBgBw1kQ", #ka najla
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ka patricia
            "https://drive.google.com/uc?export=view&id=16aBChBpPKsN8OTtkLA1hKlR3tAeIesYq", #ka rahma
            "https://drive.google.com/uc?export=view&id=167fSuWEoyJRRz_J4R79VszdbVMbFuEzT", #ka try yani
            "https://drive.google.com/uc?export=view&id=16HSXQZjkSAoEMooQXD95S9bFEkzqbppc", #bang kaisar
            "https://drive.google.com/uc?export=view&id=16bjYM20r0murYSlD2sLLzJe4G5WQhrx5", #ka dwi
            "https://drive.google.com/uc?export=view&id=16IBk62LVGCK0dZA8AfR7mafjIqXIrIav", #bang gym
            "https://drive.google.com/uc?export=view&id=16K-dFKHyemlqVbzBtHT3_CDnPEI-LzyB", #ka nasywa
            "https://drive.google.com/uc?export=view&id=16Edrt8IZ-PSIct-oWo_UNv-oJao-Urza", #ka priska
            "https://drive.google.com/uc?export=view&id=170WGWY-T7-iAWqMZm6stuZEX9qXmgskI", #bang arsal
            "https://drive.google.com/uc?export=view&id=1BXwqMfAEEMolgik7iLgRXfTg4B7K5K-y", #bang abit
            "https://drive.google.com/uc?export=view&id=16lfcWmZsf1BT1TwM2NuZw2knSK6Kc0cy", #bang akmal
            "https://drive.google.com/uc?export=view&id=1BMinPCjjwv7wz0gGuch__zUJWB-PrJV_", #bang mawan
            "https://drive.google.com/uc?export=view&id=17E3d_7dOhAukExn7VMYV1OLB4cN4IBo1", #ka khusnun
        ]

        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat":  "Sukarame",
                "hobi": "Nonton donghwa",
                "sosmed": "wayyulaja",
                "kesan": "Baik, lucu, dan tentunya tegas",  
                "pesan": "Semangaattt buat bang tao, lancar juga buat kuliahnya ya bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@Elokviola",
                "kesan": "Cantik banget, baik banget, kalem, cantik banget asliii",  
                "pesan": "Terus semangaatt ka elok, sehat-sehat dan lancar-lancar buat kuliahnya"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Seneng",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "Baikk banget kakaknya, kece betul, dan seru",  
                "pesan" :"Semangat kuliahnya kak, jangan menyerah dan jangan putus asa"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Tinggi bangett, cantik dan baik jugaa",  
                "pesan": "Happy terus ya kak, semangat kuliahnyaa"
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
                "kesan": "Lucuu bangett, baik hati, dan pastinya cantik banget",  
                "pesan": "Terus semangat kak juju, jangan menyerah yaa kak"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobi": "Shopping",
                "sosmed": "@patriciadiajeng",
                "kesan": "Cantik, baik banget, care sekali",  
                "pesan": "Semangaat ya kak cia, jangan capek dan jangan lupa bahagia kakk"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobi": "Membaca merk mobil",
                "sosmed": "@rahmaneliyana",
                "kesan": "Aih, kak neli lucu banget, baik banget, dan aku suka senyum kakakkk",  
                "pesan": "Kakk, sehat-sehat yaa, terus semangat apapun itu"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Ngoding",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Cantik banget asli, asik juga, suka bercandaaa",  
                "pesan": "Lancar terus ya kak kuliahnya, jangan menyerah dan terus semangatt ya kak dalam hal apapun itu"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Masih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Baik bangettt bang kaisar, seru abis, dan lucu banget",  
                "pesan": "Semangat ya bang, lancar terus dalam kuliahnyaa"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobi": "Menonton",
                "sosmed": "@dwiratnn_",
                "kesan": "Pendiem kakaknya, tapi baik hati kooo",  
                "pesan": "Terus berjaya ya kak, happy-happy ya kak"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobi": "baca komik",
                "sosmed": "@jimnn.as",
                "kesan": "Keren, goodjob, asik, dan berani",  
                "pesan": "Jangan menyerah ya bang, tetap semangatt bang gym"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobi": "suka bebersih dan denger musik jj",
                "sosmed": "@nsywanaf",
                "kesan": "Lucu kak nasywa dan juga baik bener",  
                "pesan": "Hal apapun itu, jangan menyerah ya kak. Tetap semangat"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobi": "nonton apapun yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan": "seruuu dan asikkk kak",  
                "pesan": "Sehat terus yaa kak, semangat jugaa untuk menjalani hari-harinya"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsalutama",
                "kesan": "Kece betul, baik hati dan asikk",  
                "pesan": "Semangaatt kuliahnya ya bang, semangat semester 7 nyaa"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobi": "ngoding dan gaming",
                "sosmed": "@abitahmad",
                "kesan": "Kece, asik, dan baik hatii",  
                "pesan": "Sehat selalu bang abit, semangat juga untuk kuliahnya"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobi": "Main hp",
                "sosmed": "@akmal.faiz",
                "kesan": "Baiik bangett, pinter, abang alpro",  
                "pesan": "Semangat kuliahnya ya bang, lancar-lancar terus buat bang akmal"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobi": "baca novel",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Lucuu abis, asik, suka ngelucu",  
                "pesan": "Tetap semangat ya bang, apalagi jadi anak desain harus semangaaatt terussss"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Ngepel",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Baik banget, suka ngedesain, pinter desain, lucu imut",  
                "pesan": "Lancar terus kuliahnya kak, tetap semangat dan jangan menyerah ya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
