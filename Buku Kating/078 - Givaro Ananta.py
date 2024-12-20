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
            "https://drive.google.com/uc?export=view&id=1oL-zeRzcLMGZXpcNJZtI7Da9mSTzx2Tk",
            "https://drive.google.com/uc?export=view&id=13rIsOZ7axnz7W3fttYw7G0FDGiin3yuh",
            "https://drive.google.com/uc?export=view&id=14xBBdb1FmaJxATLcZ1cOSRCMKp_OCghJ",
            "https://drive.google.com/uc?export=view&id=18sbqryNffSdl14vLCE6iLw5t4S0OtvcJ",
            "https://drive.google.com/uc?export=view&id=1lkyvfgq6g0snLhaWIiIRLeNZzb_aPL3q",
            "https://drive.google.com/uc?export=view&id=13sL2D0s6VU90hAiWUocQXcTV383ngcZ3",
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
                "kesan": "santai tapi wibawanya dapet banget",  
                "pesan":"sukses terus bang"# 1
            },
            {
                "nama": "Pandra Insani Puutra Azwar",
                "nim": "121450127",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Bawean 2, Sukarame",
                "hobi": "Main Gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Sekjen paling asik",  
                "pesan": "Semangat kuliahnya bang"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450044",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Humble abis",  
                "pesan":"ayoo kak nonton tapi jangan horror"# 3
                
            },
            {   "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobi": "Dengerin Bang Pandra main gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak baik",  
                "pesan":"semangat kuliahnya kak, semoga lulus tepat waktu"# 4
                    
            },
            {   "nama": "Hartiti Fadilah",
                "nim": "121450021",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrdfdlh",
                "kesan": "Logatnya minang banget",  
                "pesan":"ajarin bahasa minang kakk"# 5

            },
            {   "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Gangguin Kak Liza Tidur, bawa Wattpad/AU",
                "sosmed": "@nadillaandr26",
                "kesan": "Murah senyum banget",  
                "pesan":"Jangan berenti murah senyum ya kak"# 6
            },
        ]

        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kUbZ-vm1mt2cZRMv2srOWCzhF7Wt_pGq",
            "https://drive.google.com/uc?export=view&id=1gD1crrADI1ISmQmYjqV8CtnNeqncK_Lj",
            "https://drive.google.com/uc?export=view&id=1OVb03i_cK70Gqr4XKkDROG6QbOzOzeK8",
            "https://drive.google.com/uc?export=view&id=1DBzq-QeMN8ccdPhHbA025VP63RulXIRK",
            "https://drive.google.com/uc?export=view&id=1ua6w_GnDRpo_JZ2M5lEgQxip2ZtuxqNp",
            "https://drive.google.com/uc?export=view&id=1ocykMHRsQY46ycYsic45GKNAI24XSQZt",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1rjwhwjffpMHvghsBbSgJyIb7py3v0OMB",
            "https://drive.google.com/uc?export=view&id=1gmHlil4bQclDCWzsiR-_69745n-we7As",
            "https://drive.google.com/uc?export=view&id=15R6zgyTBEczvb74Ncqo6WvWOCcxIyxMy",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "positive vibes banget kak",  
                "pesan":"happy terus yaa kak"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Baca buku dan nonton film",
                "sosmed": "@annisacahyanisurya",
                "kesan": "humbles abis, ngobrol jadi asik banget",  
                "pesan": "rekomen film yang ngga bosen buat rewatch dong kak"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Jl Raden Saleh",
                "hobi": "Belajar bersama pak tamaro",
                "sosmed": "@wlsbn0",
                "kesan": "kecee banget",  
                "pesan":"tutor dapet A dari pak tamaro dong kak"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Ngobrol",
                "sosmed": "@anisadini10",
                "kesan": "asikk banget",  
                "pesan":"semoga sukses terus, jangan lupain adek tingkat ya kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@ansftrynn_",
                "kesan": "seruu parah",  
                "pesan":"saran drakor dong kak, tapi jangan yang horror"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "pasti abang jago ngoding",  
                "pesan": "ajarin ngoding dong bang"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Solo",
                "alamat": "Natar",
                "hobi": "Suka ditipu sama penjual akun canva premium di shopee",
                "sosmed": "@_.dheamelia",
                "kesan": "tadinya kirain orang teluk kak",  
                "pesan":"join canva tim gratisan aja kak di yutup banyakk"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta, Jawa Tengah",
                "alamat": "Sukarame",
                "hobi": "Badminton, melukis, hiking, dan berenang",
                "sosmed": "@fhrul.pdf",
                "kesan": "kecee abis bangg",  
                "pesan": "gass bang main badminton bareng"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Make up, nonton podcast, dan dengerin musik",
                "sosmed": "@berlyyanda",
                "kesan": "hobi kita samaa kak",  
                "pesan":"semangat terus kak!"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan":"-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UzKBIK-uWRFOvnWcKsHyYe_h-PmUy4ob",
            "https://drive.google.com/uc?export=view&id=13WksSsi9BHskflHdgQnjN5y2lXwYJ6_i",
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
                "kesan": "public speaking kakak keren banget",  
                "pesan":"semoga sukses terus kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan kota baru",
                "hobi": "Dengerin Ka Luthfi bernyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "bang bintang humble banget",  
                "pesan": "next time main badmin lagi yuk bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1h7KLWbp4fw-5dvSp7zEQFZFC0vReAJax", #bang econ
            "https://drive.google.com/uc?export=view&id=1_eTUki3alEjzZGi3UPiuZt2hICODOzEP", #kak abet
            "https://drive.google.com/uc?export=view&id=1kQrtny1wkj76g_SWtgOW0dLC19ntk1FF", #kak fifah
            "https://drive.google.com/uc?export=view&id=1I_psd8DwMwFxV0NVG21QyVjUvNFc3kUD", #kak aliya
            "https://drive.google.com/uc?export=view&id=1C199C02du7NQ41v4MHzBvahGu_eIhL0e", #kak eksanty
            "https://drive.google.com/uc?export=view&id=1_n7y3jWXGwp3F-yvg1ehNk0U7zVWaahY", #kak hanum
            "https://drive.google.com/uc?export=view&id=1z0TOE_fMjmVqpcYTaaOWNankBMOmDlbI", #bang ferdy
            "https://drive.google.com/uc?export=view&id=1WBSjMBcQku_qGrznK34zi_6MDFnbVzNw", #bang deri
            "https://drive.google.com/uc?export=view&id=13Bi_TPEwEC6jMPMyfCuBDowAxcSUx-e_", #kak oktavia
            "https://drive.google.com/uc?export=view&id=1qQbL9juXtlyKurig3rnAiaYK75TGlz00", #bang devyan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1vDu4GeGD0vHW7kDRGmayW4tdLAXUKNiP", #bang jon
            "https://drive.google.com/uc?export=view&id=1FCiQnY2OdpArFQ6F-2HvfkPUcZBkhyFn", #bang kemas
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1-aljIVRHp2cFkBkZKok7w1i_19mhkj5O", #kak presilia
            "https://drive.google.com/uc?export=view&id=1qEjN85DDEoVz2PbTJlknS7UCD5Trv0-D", #kak rafa
            "https://drive.google.com/uc?export=view&id=1JULRhxfs9ehBMRv5GmxC4ditPbxwXOHY", #bang sahid
 	    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1wJUxdf--TjYCV2NFkBUdl2b1d3oS4J0H", #bang ateng
            "https://drive.google.com/uc?export=view&id=1o34DxRMflw53LI5TKX3mDdEZglifNP52", #bang gede
            "https://drive.google.com/uc?export=view&id=1fQg-nmroiShdaNzFE_4JGvLiifC8QVc-", #kak jaclin
            "https://drive.google.com/uc?export=view&id=11w-Oy7ctQn5RnVlBe5K-FQB0UNRki6PE", #bang rafly
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
                "kesan": "Tegas banget",  
                "pesan": "semangat dan sukses terus bang" # 1
            },
            {
                "nama": "Celisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "kak abet seruu, lucu banget",  
                "pesan": "happy terus yaa kak" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": "humble banget",  
                "pesan": "semangat terus kak sebagai ketuplak" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": "tegas banget",  
                "pesan": "kakak profesional bangett" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakak nim satuu nih",  
                "pesan": "tips biar tinggi kak" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "kirain akamsi kak",  
                "pesan": "ajarin bahasa minang kak" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya agak pendiam",  
                "pesan": "ayoo bang sparing ml lagii" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": "miripp bang devyan dikit",  
                "pesan": "Kayu Agung tempat sepupu saya bang" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "kalem kakaknya",  
                "pesan": "hati hati kak kalo pulkam lamtim banyak begal" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "abang paling humble dan lucu di psda",  
                "pesan": "semangatt kuliahnya bang, semoga lulus tepat waktu" # 10
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
                "kesan": "leader damaskus nih, kecee banget",  
                "pesan": "keep your vibes bangg" # 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": "pasti bang kem jago ngoding",  
                "pesan": "ajarinn ngoding bang" # 13
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
                "kesan": "kakaknya kalem",  
                "pesan": "semangat kuliahnya bang" #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "lumayan pendiem",  
                "pesan": "di webtoon favoritnya apa tuh kak" # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "seruu, asik abangnya",  
                "pesan": "ajarin main alat musik bangg" # 17
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
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
                "kesan": "kirain abang asalnya dari medan",  
                "pesan": "semangatt bang selalu jadi pj setiap lomba" # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "kecee ni, seruu abangnya",  
                "pesan": "maaf ya bang kemaren tim 1 kalah" # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "seruu, asik banget kakaknya",  
                "pesan": "ajarin berenang kak, saya baru bisa renang gaya bebas" # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "humblee banget bang",  
                "pesan": "gass mabar bangg" # 22
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 23
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
	    "https://drive.google.com/uc?export=view&id=1HA4PJfhVOninTzn4MDGZ3wKAaGUOB8ec", #bang rafi	
            "https://drive.google.com/uc?export=view&id=1IVclN1D4IUDoegpSiDFttcmSdaR1AMj4", #kak annisa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1DTY99WPrjHvUOKxRFnIm--RrP6DIcdQ4", #bang sahid
            "https://drive.google.com/uc?export=view&id=1WNOqTUf-Iz_knK8u9sLP9PHF-_CCf-Q2", #bang fadhil
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1cXcM3ndPfDcdckyCEWkfnNM8ddFQ2sRj", #kak syalaisa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1u6gfdmC6BOb6OAZrpIITjyC20n3cYkwk", #kak dinda
            "https://drive.google.com/uc?export=view&id=1BPrsK-uLzhpzsU99VJSDKg3G29-HK_9x", #kak marleta
            "https://drive.google.com/uc?export=view&id=1bDO_9nIiGo1VMCGucCcgfyctu6Ac0W-a", #kak junita
            "https://drive.google.com/uc?export=view&id=1oG7PtYJKvLFPeAErMqmX0sL5K3EwWzQ0", #kak syadza
	    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1qo0-_brdmIFnBAkvi00-zqjBddmQo9xw", #bang eggi
            "https://drive.google.com/uc?export=view&id=1trIaBxb5OEBp_ksrtsOyVcK6tKvAhr49", #kak febiya
            "https://drive.google.com/uc?export=view&id=1On1yB5hKJJOgbfO6Y5qfxokt0Fu7MRQw", #bang syahrul
            "https://drive.google.com/uc?export=view&id=1brQQfuF_yo6mBCQ6pVKsl7HbadpIMAgJ", #bang randa
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
                "kesan": "ngga nyangka ternyata humble banget",  
                "pesan": "tutorin juara badmin bang" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "wah pulang kampung searah ni kak",  
                "pesan": "kalo ke lampung barat jangan lupa mampir ya kak" # 2
            },
            {
                "nama": "Mujadid Choirus Surya",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 3
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "postur badannya bagus bang, ngga heran hobinya olahraga",  
                "pesan": "ajakin olahraga bareng bang" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "abangnya lumayan pendiem",  
                "pesan": "ayoo mabar bang" # 5
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 6
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "atraktif parahh",  
                "pesan": "kalo ketemu di tangerang ajakin main ya kak" # 7
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 8
            },
            {
                "nama": "Anwar Muslim",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 9
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 10
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "vibesnya baik banget kak",  
                "pesan": "ajarin cara dapet A di matkul ADS kakk" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "asprak strukdat kan kakkk",  
                "pesan": "semangatt ngaspraknya kak" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kakaknya humble banget",  
                "pesan": "next time kita fotbar sama lasso lagi ya kak" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "lumayan pendiem",  
                "pesan": "tim pempek kulit atau lenjer kak? kalo saya kulit" # 14
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 15
            },
            {
                "nama": "Aditya Rahman",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 16
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobi": "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan": "vibes abangnya seruu banget",  
                "pesan": "keep your vibes bang" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakaknya baik, lucuu",  
                "pesan": "spill website jurnalnya dong kak" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "positive vibes banget bang",  
                "pesan": "happy selaluu bang, sesuai namanya" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Baikk, seruu",  
                "pesan": "kita sama sama suka tidur bang" # 20
            },
            {
                "nama": "Vita Anggraini",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
	    "https://drive.google.com/uc?export=view&id=1OvK_7TJ8CK--k9NUq6UUNihaP0rfraQ1", #bang yogy
	    "https://drive.google.com/uc?export=view&id=1xEYeDuGleilQNx2a92RskYv-MZNZ5bP3", #kak ramaditha
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
	    "https://drive.google.com/uc?export=view&id=1FfozEqlHcbEAiMjcnnLRei1sU0OjIpKR", #kak dea
	    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
	    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1KQ9HkxnXk-gLbDtD9bFRY_ePWJ3rg6Gw", #kak novelia
	    "https://drive.google.com/uc?export=view&id=1PZzc-S7UQn-3-SGaLPFTkHB8S10LklMv", #kak ratu
	    "https://drive.google.com/uc?export=view&id=1PQwAELzlb6x4xZfc8qy6GdFOMMQeKl9H", #bang tobias
            "https://drive.google.com/uc?export=view&id=1GqXt8Q9E8NmKiyKs9SARmXukYA4U-9eZ", #kak yohana
            "https://drive.google.com/uc?export=view&id=1cKd8g55zhFg8TnY9yTSLuqXWStOlVpe1", #bang rizki adrian
            "https://drive.google.com/uc?export=view&id=1x22H3I1MBzS23Tt9ZDDbdXhJzdsOssFF", #bang arafi        
            "https://drive.google.com/uc?export=view&id=1xtC1bGUFeU4U_8_j2IA-d0se_kAM4sEp", #kak asa
            "https://drive.google.com/uc?export=view&id=1HSC3w-bTCPFGtOMAH0W9HLXi25jYCYAd", #kak chalifia
            "https://drive.google.com/uc?export=view&id=1UNBCFj5E8_e1hML-XS5_fyhJSdmU8lH6", #bang irvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1Kf4RLPbw-3WY7oN7ZY1LqNBITtNjWvvQ", #kak khaalishah
            "https://drive.google.com/uc?export=view&id=13iTOhe6JDcHgSOGdR3FcnfJRYiFJs7xO", #bang raid
            "https://drive.google.com/uc?export=view&id=1kgjuPVoY7X6QGGMM9ipWPhtDlXXLIv81", #kak yunna

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
                "kesan": "humble, asikk banget",  
                "pesan": "kalo hunting hotwheels di wong toys aja bang" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "kakaknya baik",  
                "pesan": "ajakin lasso jalan-jalan kakk" # 2
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 3
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 4
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "seruu",  
                "pesan": "sharing ilmu nerbitin jurnalnyaa kak" # 5
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 6
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 7
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakaknya kecee, seru",  
                "pesan": "sama kak, saya juga suka tidur" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobi": "Planning konten",
                "sosmed": "@jasminednva",
                "kesan": "vibes kakaknya positiff banget",  
                "pesan": "semangaatt terus kaak" # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Membaca",
                "sosmed": "@tobiassiagian",
                "kesan": "abangnya kece, humble, seruu parah",  
                "pesan": "semangat basketnya bangg" # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Buat Jurnal",
                "sosmed": "@yo_annamnk",
                "kesan": "tegas banget kakaknya",  
                "pesan": "semangat jalanin tugasnya kak" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abangnya seruu",  
                "pesan": "semangaatt terus bang" # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Samping warjo",
                "hobi": "Sholat",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "kece abangnya",  
                "pesan": "next time fotbar lagi yaa bang" # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Cari ice breaking",
                "sosmed": "@u_yippy",
                "kesan": "kakaknya baik, pernah sekelompok soalnya",  
                "pesan": "semangat kuliahnya kakk"# 14
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Berbuat baik",
                "sosmed": "@chlfawww",
                "kesan": "ramah dan baik hati",  
                "pesan": "semangat kuliahnya kaak" # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "seruu banget, asik, humble",  
                "pesan": "ayoo mabar baangg" # 16
            },
            {
                "nama": "Izza Lutfia",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 17
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Lampung",
                "hobi": "Tilawah Al-quran",
                "sosmed": "@alyaavanevi",
                "kesan": "kakaknya kalem banget",  
                "pesan": "tips murojaah dong kak"# 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Ikut seminar",
                "sosmed": "@rayths_",
                "kesan": "seruuu, baik",  
                "pesan": "kabar kabar bang kalo ada seminar" # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Pemda",
                "hobi": "Sholawat",
                "sosmed": "@tria_y062",
                "kesan": "udah kenal dari pplk kakaknya aktif bangett",  
                "pesan": "semangaat kuliahnya kak" # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
	    "https://drive.google.com/uc?export=view&id=1M8Qi9qH3poV4k3QV6S7JwiD2PO2lRw8z", #bang dimas
	    "https://drive.google.com/uc?export=view&id=1wIMsuCr4ANyVHWnT_pAw8viw_b4hovXD", #kak catherine
            "https://drive.google.com/uc?export=view&id=1HG1hm0ClgfmMnOtHIYicbXtzWau8wgej", #bang akbar
            "https://drive.google.com/uc?export=view&id=14594ZEo-HG_CKq4JHLYJBd4RuGnoES_S", #kak rani
	    "https://drive.google.com/uc?export=view&id=1nLC0X_k_ou_JMeR39MVPoEjc7iLUie8Z", #bang rendra
	    "https://drive.google.com/uc?export=view&id=1FJmKmaDhK2b1N30oUPtR4NM-dzHauU9i", #kak salwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
	    "https://drive.google.com/uc?export=view&id=1lFyH32mWvtenMG1pw_lg9P-dz2oHrr_T", #bang ari
	    "https://drive.google.com/uc?export=view&id=1ELf2v1FDJZ_UZAyYoTCBGcxPrS6BdTZO", #kak azizah	
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1Znummq8aOfVaEEEbQR_481RMYWo0Swc8", #kak meira
            "https://drive.google.com/uc?export=view&id=1k05U8nSs_r47F8DFCnWHMnMEsIJTNuNg", #bang rendi       
            "https://drive.google.com/uc?export=view&id=1NjxUsx6C6sa0PUuVIF2LwOOA1NNrTlZc", #kak renta
            "https://drive.google.com/uc?export=view&id=17ck2bhso_hJx13cclM13q9hKraj1SPtv", #bang joshua

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
                "kesan": "bang dimas kece parah, humble banget, seruu",  
                "pesan": "semangat bang, semoga lulus tepat waktu" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "kakaknyaa lucu, seru",  
                "pesan": "jangan lupain lasso yaa kak"# 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": "akhirnya punya kating yang dari lambar juga",  
                "pesan": "kapan-kapan pulang kampung bareng bang" # 3
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
                "kesan": "humble abis, baikk banget",  
                "pesan": "semangat ngaspraknya bangg" # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "humble, asikk kakaknya",  
                "pesan": "saran film favorit kakak dongg" # 6
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan":"-" # 7
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "positive vibes banget bang",  
                "pesan": "kapan-kapan pulang ke lambar bareng bang" # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "baikk, seru kakaknya",  
                "pesan": "jangan lupa sama lasso ya kak, waktu itu seru banget kita semua ketawaa" # 9
            },
            {
                "nama": "Dearni Monica Br Manik",
                "nim": "122450075",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-" # 10
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobi": "Nonton film",
                "sosmed": "@meirasty_",
                "kesan": "seruu kakaknya baik",  
                "pesan": "saran film disney yang menurut kakak paling baguss dong" # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": "kalem bangettt",  
                "pesan": "semangat terus bangg" # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": "kak renta jugaa kalem banget",  
                "pesan": "semangat kuliahnya kaak" # 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Siantar",
                "alamat": "Gerbang Barat",
                "hobi": "Nonton film",
                "sosmed": "@josuapanggabean_",
                "kesan": "agak pendiam, tapi abangnya seruu kalo ngobrol",  
                "pesan": "film marvel favorit abang apaa bang?" # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
	    "https://drive.google.com/uc?export=view&id=192zwcrCJTQ2deleyEHp8Fn1LARZlvfeU", #bang andrian
	    "https://drive.google.com/uc?export=view&id=1_dS51MxMIER7iD2FP9zqtAuQJF_fcQMK", #kak adisty
            "https://drive.google.com/uc?export=view&id=135UVUvjiM04qoeQcS804EFkt-SPoomB_", #kak nabila
            "https://drive.google.com/uc?export=view&id=1sA0-z0RUyGwMwsBT6IK1DQ0QOd8TjCVj", #bang ahmad
	    "https://drive.google.com/uc?export=view&id=1JnVJIA_XM0-v6-WxmLLyNO7_HGC1WmbY", #bang danang
	    "https://drive.google.com/uc?export=view&id=1c-mDHujTdBOIFQAoWq3g6XpyYClI_Gj0", #bang farrel
            "https://drive.google.com/uc?export=view&id=1FkXALX7qWhqyeHqKmuT11NDGRaDehGtK", #kak tessa
	    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak nabilah
	    "https://drive.google.com/uc?export=view&id=1KuODiQwrWdOIrk43wnY_XhzuvEKR5qZ9", #kak alvia
            "https://drive.google.com/uc?export=view&id=1AkYM6M4Ji1P6nHhk6Npyl4HI0UYhPTMD", #bang dhafin
            "https://drive.google.com/uc?export=view&id=1vzUt1_GXPxcbspEAYNozFhjDkG98-p0Q", #kak elia

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
                "kesan": "kirain akamsi bang",  
                "pesan": "ajakin saya bang cari uangnya" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "seruu kakaknya",  
                "pesan": "film disney yang jadi favorit kakak apa tuh kak" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "humblee banget",  
                "pesan": "sama kak saya juga suka ngitung uang"  # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": "seruu tapi pendiam",  
                "pesan": "semangat kuliahnya bangg" # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "seruu banget ngobrol sama bang danang",  
                "pesan": "keep your vibes bangg" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "humble parah, kecee abangnya",  
                "pesan": "semangat terus bang, damaskus kecee abis"# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "kakaknya lumayan pendiam",  
                "pesan": "semangat terus yaa kak" # 7
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobi": " ",
                "sosmed": "@nabilahanftr",
                "kesan": "seruu kakaknya",  
                "pesan": "semangaat terus kak" # 8
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviaginting",
                "kesan": "humble banget",  
                "pesan": "saya juga suka nonton papa brando kak" # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abangnya kalem banget",  
                "pesan": "semangat terus bang" # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "baik, asikk kakaknya",  
                "pesan": "sehat selalu yaa kak" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
	    "https://drive.google.com/uc?export=view&id=1dJ4ue31dpjUIuXete8QtUGzV8ehg08ho", #bang tao
	    "https://drive.google.com/uc?export=view&id=1iAx6v70woMO0fRSsK1eeOdJFN17JvlaQ", #kak elok
            "https://drive.google.com/uc?export=view&id=1nsGP6lsVCoLFhXy6ch0FT4vE2yivVri0", #kak arsyiah
            "https://drive.google.com/uc?export=view&id=18qAYHv4sF6645FQmU3TZjLUXFxqU4Bga", #kak cibel
	    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
	    "https://drive.google.com/uc?export=view&id=1_VY-F8a4CD2taDOCsX41icrbVXXrZt7-", #kak juju
	    "https://drive.google.com/uc?export=view&id=1SmbXd_MaNwTkzd1kZSENrmFBkosZ15fB", #kak cia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak rahma
	    "https://drive.google.com/uc?export=view&id=1Ns5IVheW7sm8CfCSPZ_z88voDdz5iz6w", #kak try
	    "https://drive.google.com/uc?export=view&id=1Xcxbmb9BNygeIXc35L9NPTob_S8ox20i", #bang firdaus
            "https://drive.google.com/uc?export=view&id=1Ku6cLV_sw1WfThlCV5IPU4eQoj6jPixl", #kak dwi
            "https://drive.google.com/uc?export=view&id=1tu9i46rGlHHpxZxIoyve9iH9lr-2JJ5D", #bang gym
	    "https://drive.google.com/uc?export=view&id=13-BAentMcyjmLmGGnP2YGTNsLoQzpWTN", #kak nasywa
	    "https://drive.google.com/uc?export=view&id=1dW2hV-LS68J_qauUyD98FDGTUkmeh5Dy", #kak Priska
            "https://drive.google.com/uc?export=view&id=19YeGqHy9t0edk8hnYsr8dTsQqIE0q_9d", #bang arsal
            "https://drive.google.com/uc?export=view&id=1PHUmSnGWAm1P_VwrrUt-moquQg1Arwuu", #bang abit
	    "https://drive.google.com/uc?export=view&id=1JEwKPcGiuE55jt7BQb9TDTey2-2vecEu", #bang akmal
	    "https://drive.google.com/uc?export=view&id=1dTnef0gmrDC-j2HMMbFSjQrtHK0atfvq", #bang her
	    "https://drive.google.com/uc?export=view&id=1VM9Pg-D_Ot3dXfZkHUatBlKZT1uoy-yF", #kak khusnun

        ]

        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobi": "Nonton donghua",
                "sosmed": "@wayyulaja",
                "kesan": "kecee banget abangnya, seruu",  
                "pesan": "sering sering sharingg dong bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@Elokviola",
                "kesan": "kakaknya baik, lucuu",  
                "pesan": "share ilmu editingnya dong kak"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Seneng",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "seru kakaknya asik banget",  
                "pesan": "sehat selalu kaak"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "kakaknya humble, asik bangett",  
                "pesan": "sukses terus kak cibell"
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan": "-"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Nulis, baca, ngefangirl",
                "sosmed": "@nanana.minjoo",
                "kesan": "asikk banget, seru orangnya",  
                "pesan": "ajakin yunipom main bareng lasso kak hehe"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobi": "Shopping",
                "sosmed": "@patriciadiajeng",
                "kesan": "baikk, humble banhget",  
                "pesan": "ayoo shopping bareng kak"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobi": "Membaca merk mobil",
                "sosmed": "@rahmaneliyana",
                "kesan": "seruu kakaknya",  
                "pesan": "kalo merk impian saya landrover kak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Ngoding",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakak pj tugas lasso niii",  
                "pesan": "semangaatt kak jalanin tugasnya"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Masih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "abangnya asik banget, pose foto kita paling kece bangg",  
                "pesan": "semoga cepet ketemu yaa bang hobinya"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobi": "Menonton",
                "sosmed": "@dwiratnn_",
                "kesan": "kakaknya agak pendiem",  
                "pesan": "nonton disneyy suka ngga kak"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobi": "baca komik",
                "sosmed": "@jimnn.as",
                "kesan": "seruu, humble banget",  
                "pesan": "koleksi komiknya banyak yaa bang"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobi": "suka bebersih dan denger musik jj",
                "sosmed": "@nsywanaf",
                "kesan": "lumayan pendiem kakaknyaa",  
                "pesan": "sehat selalu kak"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobi": "nonton apapun yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan": "kalem banget",  
                "pesan": "tim pempek goreng apa pempek rebus kak"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsalutama",
                "kesan": "seruu banget abangnya",  
                "pesan": "jangan cape yaa bang share ilmu ke anak desain"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobi": "ngoding dan gaming",
                "sosmed": "@abitahmad",
                "kesan": "humblee parah",  
                "pesan": "semangaatt terus bang jalanin tugasnya"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobi": "Main hp",
                "sosmed": "@akmal.faiz",
                "kesan": "agak pendiam",  
                "pesan": "ajarin ngeditt bangg"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobi": "baca novel",
                "sosmed": "@hermawan.mnrng",
                "kesan": "abang asprak + mentor desain nih",  
                "pesan": "semangatt terus bang sharing ilmunya"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Ngepel",
                "sosmed": "@khusnun_nisa335",
                "kesan": "asikk banget kakaknya",  
                "pesan": "jangan ngepel malem-malem yaa kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()


# Tambahkan menu lainnya sesuai kebutuhan
