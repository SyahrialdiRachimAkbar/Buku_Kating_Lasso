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
            "https://drive.google.com/uc?export=view&id=1RQl3Hnd2BY45FmDxBu8oVHWr-amUYu80", #Kak Cahyani
            "https://drive.google.com/uc?export=view&id=1eKoIc-ov6qa8Xp-9asVAAizZFhkGwJ7N", #Kak Wulan
            "https://drive.google.com/uc?export=view&id=10HsFxDy1A4tshSPjfOEXQvBDdlLZBDF7", #Kak Dini
            "https://drive.google.com/uc?export=view&id=1ywY4tBGgtH_GiKZMj0KkfmLA5yMZM6bd", #Nisa Fitriyani
            "https://drive.google.com/uc?export=view&id=1b75-4qcTgUpJgKKeUtbMkCF7UHgYj7OE", #Bang Feryadi
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

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=130HKlqIKXNYOmVHn3OuhLiumSWo08rWP", # ka luthfi
            "https://drive.google.com/uc?export=view&id=1Y18MxH3Wa6WtjEss223fxThZPi0DRi3v", # bang bintang
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
                "kesan": "Kakaknya pinter banget",  
                "pesan": "Semangat semester 7 nya kak!!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan kota baru",
                "hobi": "Dengerin Ka Luthfi bernyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Baik banget abangnya",  
                "pesan": "Semangatt kuliahnya bang bintang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12OXhsM2gPpsfrf3RBAqINajzUsWIc_tL", # bg econ
            "https://drive.google.com/uc?export=view&id=1LQlbmVEac8aufnHuZuEVXsJNmkoylP6C", # ka abet
            "https://drive.google.com/uc?export=view&id=18QJ9I579J0fnV_VgamrlvfpqH002GG7U", # ka pipah
            "https://drive.google.com/uc?export=view&id=1oFCOEVwVAoh7PWpcjXzTwGwgQuhDS3lJ", # ka allya
            "https://drive.google.com/uc?export=view&id=1xNvmDlXfQIPWnytP8OGjcyrK49yyNiVY", # ka eksanty
            "https://drive.google.com/uc?export=view&id=1NtwSqb1jAvMNsntPjFhpg1ehOY69bCsz", # ka hanum
            "https://drive.google.com/uc?export=view&id=10teQ3K0yIhajP_ePTvEkFwIzBY-mgkL0", # bg ferdy 
            "https://drive.google.com/uc?export=view&id=1OC8iSq43i_VmYmVD4I2X5G8rzB3Bs0k5", # bg deri 
            "https://drive.google.com/uc?export=view&id=1ymiQOVjGOWzlUtCAcwWwn3VoLGM6wz_c", # ka okta 
            "https://drive.google.com/uc?export=view&id=1fP7AvNLDzDV4g4x45ZGCBFKLU6hRQFTe", # bg deyvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1NarfsLnG2FcHV2-no5riQuHRDtAu9r35", # bg Jo
            "https://drive.google.com/uc?export=view&id=15nB7i75OBFRPGz-AsaYUpQbxgx8Tm1LZ", # bg Kemas
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1cyFvuNVHHuXUPZdTXnNGgLKMB_UvNKov", #Kak Presil
            "https://drive.google.com/uc?export=view&id=1qpQcq1ugR0_GEcrukObjBJH_D3Mz5bWj", #Kak Rafa
            "https://drive.google.com/uc?export=view&id=1OAxVVeZZWMvZFPxlaOel84JciNpScPQP", #Bang Sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1b7v-JxiB5yyEi49Qbm086KO_KDoWiu4v", #Bang Farhan
            "https://drive.google.com/uc?export=view&id=1NG1C088pTWJSq4Yswfbn2lDRxWdq9ZqP", #Bang Gede
            "https://drive.google.com/uc?export=view&id=12rc5TuYUfxrzpin2hzfxQSXA-ctAF2lx", #Ksk Jaqlin
            "https://drive.google.com/uc?export=view&id=1V-Nzjp4Hh72Ep2GHHnP_8XLAwk2GRbt0", #Bang Rafly
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
                "kesan": "Asik dan tegas",  
                "pesan": "Semangatt semester 7 nya bang!" # 1
            },
            {
                "nama": "Celisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknya asik",  
                "pesan": "semangat kuliahnya kak!" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": "",  
                "pesan": "semangat kuliahnya kak" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": "kakaknya tegas",  
                "pesan": "semangat kuliahnya kak" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakaknya lucu",  
                "pesan": "semangat kuliahnya kak" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakaknya lucu",  
                "pesan": "semangat kuliahnya kak" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya kalem tapi asik",  
                "pesan": "semangat kuliahnya bang" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": "abangnya lucu",  
                "pesan": "semangat kuliahnya bang" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "kakaknya tegas tapi asik",  
                "pesan": "semangat kuliahnya kak" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abangnya kocak abis",  
                "pesan": "semangat semester 7 nya bang!!" # 10
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
                "kesan": "abangnya baik dan asik",  
                "pesan": "semangat kuliahnya bang" # 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": "abangnya baik banget",  
                "pesan": "semangat kuliahnya bang" # 13
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
                "kesan": "kakaknya asik",  
                "pesan": "semangat kuliahnya kak" #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "kakaknya asik",  
                "pesan": "semangat kuliahnya kak" # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "abangnya asik",  
                "pesan": "semangat kuliahnya bang" # 17
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
                "kesan": "abangnya asik",  
                "pesan": "semangat kuliahnya bang" # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya asik",  
                "pesan": "semangat kuliahnya bang" # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "kakaknya jago bernang",  
                "pesan": "semangat kuliahnya kak" # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abangnya asik",  
                "pesan": "semangat kuliahnya bang" # 22
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
            "https://drive.google.com/uc?export=view&id=1dfaUsXUZruUkmcZ0Qu2ZQAqx2jwkgRmX", # bg rafi
            "https://drive.google.com/uc?export=view&id=1bz5hGgVTGKCX35XFWq1B-2vkKZJFbsDj", # ka anova
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1dPaV10QLq4hflk0rketaau76cycZIsRc", # ahmad sahidin
            "https://drive.google.com/uc?export=view&id=1cqgvWzl8zNre6wkYi2WYqclvh4tCsYYO", # bg fadhil
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1cxCRqL8acgpnaoT-LBEs7oGIkgdNdDVr", # ka syalasisha dina
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1bzYWYrH8X_nOUDqupuDoZb7Wl7erq-fz", # ka dinda
            "https://drive.google.com/uc?export=view&id=1bwIIZnqE3fgsP3bqzyTlNAr1a-vz2dly", # ka marleta
            "https://drive.google.com/uc?export=view&id=1c0IihXc9UfEundRVSZoqRFbNGvxHWK-z", # ka rut
            "https://drive.google.com/uc?export=view&id=1c0k95qgwk-0t9IKYoBFj7ZGhSUKnyOEp", # ka syadza
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1ddULa7v7F8LLWx9NOyNqbAcghnfvn92G", # bg eggi
            "https://drive.google.com/uc?export=view&id=1c-AO7eIJwiVmZCKPq3Opa6_Qgnqn2c6B", # ka febiya
            "https://drive.google.com/uc?export=view&id=1dTWO53Zd3U1TyHvFmpzkmxvuIZIhEySs", # bg happy
            "https://drive.google.com/uc?export=view&id=1d8Ov5oun5Alf7-LtOjBEe9GKbRtqI_bp", # bg randa
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
                "kesan": "abangnya jago badmin",  
                "pesan": "Semangatt kuliahnya bang!" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakanya asik",  
                "pesan": "Semangatt kuliahnya kak!" # 2
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
                "kesan": "abangnya kalem",  
                "pesan": "Semangatt kuliahnya bang!" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "abangnya asik",  
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
                "kesan": "kakaknya asik",  
                "pesan": "Semangatt kuliahnya kak!" # 7
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
                "kesan": "kakaknya asik",  
                "pesan": "Semangatt kuliahnya kak!" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kakanya asik",  
                "pesan": "Semangatt kuliahnya kak!" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kakaknya asik",  
                "pesan": "Semangatt kuliahnya kak!" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya bang",  
                "pesan": "Semangatt kuliahnya bang!" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakaknya asik",  
                "pesan": "Semangatt kuliahnya kak!" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "abangnya asik",  
                "pesan": "Semangatt kuliahnya bang!" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "abangnya asik",  
                "pesan": "Semangatt kuliahnya bang!" # 20
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
            "https://drive.google.com/uc?export=view&id=1pT8XGHCIoFetUZwpDR_K3A-ZotkIVMgW", # bg yogy
            "https://drive.google.com/uc?export=view&id=1w6wj_WdrswFlDwZsYhpLqa1wYwKQvKEL", # ka dhita
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1aKCaQ9P0DK5Wq-f0u85CRJDXJ5P4379z", # ka dea mutia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1imOD84xAGYu4yMfdBeNdWTz9ijXps5-c", # ka novelia
            "https://drive.google.com/uc?export=view&id=18nvBe8EJG30sU08l2XYDGJXTqZ_ukj4r", # ka ratu
            "https://drive.google.com/uc?export=view&id=1Q6mouX7Deo4uXY8Vzr-Zrk3twiizel_G", # bg tobias
            "https://drive.google.com/uc?export=view&id=11HnHfgMaRJ_-bd_-f1MTtQj9zmRZbcvv", # ka yo
            "https://drive.google.com/uc?export=view&id=1PsHCPDk6uhBpbVBhFzQKimtMbC5hBxzs", # bg rizky
            "https://drive.google.com/uc?export=view&id=1xAWIiYDnDIGLjh0_8SGJRmqQKgQObv_Q", # bg arafi
            "https://drive.google.com/uc?export=view&id=1K0zzxflXO80Ku__PYUr1KrSkvhIxPK4W", # ka asa
            "https://drive.google.com/uc?export=view&id=1Bq0XwGwnFj1jmIlh2hVsmX8bFoBGePHS", # ka chalifia
            "https://drive.google.com/uc?export=view&id=1emnQA3mdDokgv556Mq9UgykNchVcm1RQ", # bg irvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1-RrEIMa2HCp0Nh16nCH8awDAphzGcGxy", # ka khaalishah
            "https://drive.google.com/uc?export=view&id=1WDzmzbg90sKOudZYKoBbaUNIrfdUSuZZ", # bg raid
            "https://drive.google.com/uc?export=view&id=17dWFZ-_tPTsbt9fJQtgsSLbC2AUcp-FM", # ka tria

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
                "kesan": "abangnya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya asik",  
                "pesan": "Semangatt kuliahnya kak!" # 5
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
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "abangnya asik dan kocak",  
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
                "kesan": "kakaknya asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abangnya asik",  
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
               "kesan": "abangnya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "abangnya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "abangnya asik",  
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
                "kesan": "kakaknya asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ryxENCCBs7E0HwQ9nhiLQb45Q4VnURkr", # bg dim
            "https://drive.google.com/uc?export=view&id=1j0HGVcxAW7I2_PAzxf-8rR90wp9HTJOH", # ka catherine
            "https://drive.google.com/uc?export=view&id=1zFkLxAYOg31CSZJgvSrm-xFOkbQ7WTlW", # bg akbar
            "https://drive.google.com/uc?export=view&id=1X-JOryObuEhraU3npSFmgso8vGAEyFZ2", # ka rani
            "https://drive.google.com/uc?export=view&id=1hXbKUqcsRGKs8fDQzXsjz6SQYMH6U2vX", # bg rendra
            "https://drive.google.com/uc?export=view&id=103A52I20Yb6_eXLo9GbrlzgC0YdbIuck", # ka salwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1hHmFdFr0fAf-X6ltfTInDAsCovQrOXBd", # bg ari
            "https://drive.google.com/uc?export=view&id=1Mz5GcvuM1oiKB2W_9SSVqrPvoCH6rUMt", # ka azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1OBz_SGmHp2VpkpdJxx-snzUCc1FOPZnt", # ka meira
            "https://drive.google.com/uc?export=view&id=1Ptr6SfVdXZkT7-EMEXZWABwWFK4LZ99z", # bg rendi
            "https://drive.google.com/uc?export=view&id=1GJZG8De_faMeS3OaL8r9RPKyKjXE_2r7", # ka renta
            "https://drive.google.com/uc?export=view&id=1UStnRvO-OVgZv7JJ3ixl4QhNu-jHrq9w", # bg josua
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
                "kesan": "abangnya hiperaktif",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "abangnya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "abangnya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "abangnya asik",  
                "pesan": "Semangatt kuliahnya bang! Semangat semangat semangat" # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=155vmVehyzEANN6ZHRubqzUc4wfECHww7", # Bang adrian
            "https://drive.google.com/uc?export=view&id=1M4Fnruo2YoW91jebmL8M2dL9z4-taQqF", # Kak Adisty
            "https://drive.google.com/uc?export=view&id=1nVlY2BYU8O_uWaKVjRliXQPjh4TfVg3B", # Kak Nabila
            "https://drive.google.com/uc?export=view&id=1N1W8XV2_R_VFESUc1tuv73Ka6uNmdEpE", # Bang Ahmad
            "https://drive.google.com/uc?export=view&id=1AA3dYLmeOkMTHE7F40xZ07VMAEHGX0ew", # Bang Danang
            "https://drive.google.com/uc?export=view&id=1r7pqWHYpPoIxWgURDHHrl5adl6zvR4QY", # Bang Farrel
            "https://drive.google.com/uc?export=view&id=13hqJIYUhi3zgXY_v1Le4Xu_mAFbSlbzE", # Kak Tesa
            "https://drive.google.com/uc?export=view&id=13EmQUdDaWERHTyo-h39_w03q3vyIm0gc", # Kak Nabillah
            "https://drive.google.com/uc?export=view&id=1HdnFxCt25QWLRxyoydtqzsgg9gnSs50U", # Kak Alvia
            "https://drive.google.com/uc?export=view&id=16snK9xBw3Z4OG2sJaFEXXXCp7lrCSvW_", # Bang Davin
            "https://drive.google.com/uc?export=view&id=16MdKOXhjXFf3fBwIPAfUxwc9HvrSI-LX", # Kak Elia
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
                "kesan": "abangnya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "abangnya jago main badmin",  
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
                "kesan": "abangnya asik",  
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
                "kesan": "abangnya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "kakaknya asik",  
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
                "kesan": "abangnya asik",  
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
                "kesan": "kakaknya asik",  
                "pesan": "Semangatt kuliahnya kak! Semangat semangat semangat" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()


# Tambahkan menu lainnya sesuai kebutuhan
