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
            "https://drive.google.com/uc?export=view&id=1Ql3dMy9j3TXTOC7MEEt0ZDAKWwFzeJv7",
            "https://drive.google.com/uc?export=view&id=1UJVH7TN7iV84uMzxY2OfxuqZI_7AXeZK",
            "https://drive.google.com/uc?export=view&id=1m_fMDhv109z18sE_33_RMNV1GtwWhAHu",
            "https://drive.google.com/uc?export=view&id=1oFTkPf3WmDMfCGzUmi7OZXRONPikt3oU",
            "https://drive.google.com/uc?export=view&id=1oYGtadtTd_if4i2Oy7QsPWWW7IrqY6Kc",
            "https://drive.google.com/uc?export=view&id=19zK3MBcSHX7X3dbiZt1GZEjYTt0-z0Yn",
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
                "kesan": "Keren jadi kahim",  
                "pesan":"keren bang jadi kahim"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450127",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Bawean, Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Keresahan abang keren sehingga bisa jadi sekjen",  
                "pesan":"Semangat bang sekjen"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450044",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobi": "Nonton Drakor",
                "sosmed": "@wulandarimelinza",
                "kesan": "kakanya vibesnya seketaris sekali",  
                "pesan":"Semoga makin cool"# 1
            },
             {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobi": "Dengerin Bang Pandra main gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": " hebat banget  ",  
                "pesan":"Semoga makin kiyowo "# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450021",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrdfdlh",
                "kesan": " Lucu bendahara ternyata baca webtoon ",  
                "pesan":"rekomendasi webtoon kak "# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro, Lampung",
                "alamat": "Kota Baru",
                "hobi": "Gangguin Kak Liza tidur, baca Wattpad/AU",
                "sosmed": "@nadillaandr26",
                "kesan": "Waw Kakak bendahara baca Au",  
                "pesan":"info dong kak au yang seru"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yxnOv0Y0-C2FiNSwgfTe46yROPKAWyEg",
            "https://drive.google.com/uc?export=view&id=1bzuCyHUsTrSikhFMUVfEqmouWF1JwuKp",
            "https://drive.google.com/uc?export=view&id=1DhHkKZG1NYhKyuq3ZohyPI0qNK9pPDER",
            "https://drive.google.com/uc?export=view&id=1uUfJ1y2bVyAc6YVa0BwJcfL8vGy1RZy2",
            "https://drive.google.com/uc?export=view&id=10gbWG7ZzYR2XljFlkskL-AINHIkNtpJC",
            "https://drive.google.com/uc?export=view&id=1raan97SZ7_5b-KpR3EEhfT_D9P-MkmmP",
            "https://drive.google.com/uc?export=view&id=1p28S75h3JlYBq4ejbYUwFOk-rwaFHWqm",
            "https://drive.google.com/uc?export=view&id=1m9ZwgrsvwjTzg_NDpjs2PD7xcQrN_hyN",
            "https://drive.google.com/uc?export=view&id=1eeRe6cFozJpna_8VEM1ZildYi_8UrMUO",
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
                "kesan": "Lucu banget kakanya, kiyowok",  
                "pesan": "Enaknya searching apa ya kak di gpt?"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Baca buku dan nonton film",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Sepertinya suka baca novel",  
                "pesan": "Semngat kakak kuliahnya, mau dung rekomendasi buku" # 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Jl Raden Saleh",
                "hobi": "Belajar bersama Pa Tamaro",
                "sosmed": "@wlsbn0",
                "kesan": "acik banget kakanya",  
                "pesan": "Semoga bisa belajar bersama pa Tamoro tiap semester"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Ngobrol",
                "sosmed": "@anisadini10",
                "kesan": "Lucu banget kakanya suka ngobrol TT",  
                "pesan": "Semoga dapet temen ngobrol tiap hari, jam, menit hehehe"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Batam",
                "alamat": "Pesawaran",
                "hobi": "Nonton drakor",
                "sosmed": "@ansftrynn_",
                "kesan": " wah kakanya ternyata masuk divisi baleg",  
                "pesan": " keren kak bisa jadi anggota baleg" # 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "agak usil sepertinya",  
                "pesan": "Semoga kuliahnya lancar-lancar bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Solo",
                "alamat": "Natar, lampung Selatan",
                "hobi": "Suka ditipu sama penjual akun canva premium di shopee",
                "sosmed": "@_.dheamelia",
                "kesan": "unik hobinya",  
                "pesan": "Semoga dapet berkah canva pro gratis kak"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta, Jawa Tengah",
                "alamat": "Sukarame",
                "hobi": "Badminton, melukis, hiking, dan berenang",
                "sosmed": "@fhrul.pdf",
                "kesan": "Banyak sekali hobinya",  
                "pesan": "Lancar terus bang kuliahnya" # 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi, Bandar Lampung",
                "hobi": "Make up, nonton podcast, dan dengerin musik",
                "sosmed": "@berlyyanda",
                "kesan": "mungkin kakaknya suka makeup-an sambil denegerin podcast",  
                "pesan": "Lacar ya kak kuliahnya, spil dong makeup yang kakak pake"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14gxDYTTlE-x5LRG_6eEZWydErINtW95c",
            "https://drive.google.com/uc?export=view&id=1TCteAgyuSXBXHeoxdweg0DOMG5MCoU3i",
            
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450098",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "kost Putri Rahayu",
                "hobi": "Nyanyi",
                "sosmed": "@anissaluthfi_",
                "kesan": "Keren banget kakanya",  
                "pesan": "Lancar-lancar Kak kuliahnya :)"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Kota Baru",
                "hobi": "Dengerin Ka Luthfi bernyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "keren abangnya jadi senator",  
                "pesan": "Semoga lanjar terus kulianya bang :) " # 1
            },    
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
    
elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_l3oPzM8Anvm7qUqtxGZnKJM5inmOjWM", # bg econ 1
            "https://drive.google.com/uc?export=view&id=1yaEdi_1VXcAta2u3fdW43OxYkh6u_ymV", # ka abet 2
            "https://drive.google.com/uc?export=view&id=12HJCm4AlV-J-l_gKZN8UsM_SLCJHa7IN", # ka pipah 3
            "https://drive.google.com/uc?export=view&id=1Ymy6bNP9ASwawvjjec7xBpLtodDrFBV3", # ka allya 4 
            "https://drive.google.com/uc?export=view&id=1Gj4N-yWljn4aiCCVPEX64R8tpJuyjnkk", # ka eksanty 5
            "https://drive.google.com/uc?export=view&id=1OeBz9lIGsf866YwAXDEvE2R4_WtnoO5d", # ka hanum 6
            "https://drive.google.com/uc?export=view&id=1wBJCnA0Eldt4Z6dp6ulSnkVlKtkPONX7", # bg ferdy 7
            "https://drive.google.com/uc?export=view&id=1y8Om8NVMyvJhkB_Ax2P7pCIIlvhgTaFC", # bg deri 8
            "https://drive.google.com/uc?export=view&id=1nuOLP6mfTYfBtqHO66-BsBajnpojmnfE", # kak okta 
            "https://drive.google.com/uc?export=view&id=18q91sn8UXlAwfYQXEEI635g3deA3kp1H", # bg deyvan 10
            "https://drive.google.com/uc?export=view&id=12JqZYxre6iVWbL3iUpmj2odaDkLThaX5", # bg jo 11
            "https://drive.google.com/uc?export=view&id=1YHr3SIwvh9Lqh9f6BW0SzUr7_bziiizE", # bg kemas 12
            "https://drive.google.com/uc?export=view&id=1CcbP5blvuQmdspOv7lb4sHGClcz7Rna_", # ka presilia 13
            "https://drive.google.com/uc?export=view&id=1YgSBT0Snqoy7eskI6kp6EhIsJQPdIzyv", # ka aqila 14
            "https://drive.google.com/uc?export=view&id=12k8u8w25Z0YfF10JCA1sVbhuNYeTOPy2", # bg sahid 15
            "https://drive.google.com/uc?export=view&id=1o0vtJLsII0jmNx4D2_Brfs9JoDX2YF2y", # bg ateng 16
            "https://drive.google.com/uc?export=view&id=1xYNoYUaJoQA8FDfIGx5jJ4KslNlRIHAl", # bg gede 17
            "https://drive.google.com/uc?export=view&id=1icubbsC-gK3lhqKzrMZQD0Zof5X7sj0T", # ka jaclin 18
            "https://drive.google.com/uc?export=view&id=1nJdFmTzmTP4U8Pvlh-lyX2H5tB990eGz", # bg rafly 19
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
                "kesan": "Abangnya tegas",
                "pesan": "Semoga lancar terus kuliahnya" # 1
            },
            {
                "nama": "Celisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya cakep",
                "pesan": "Lancar terus kuliahnya kak" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": "Keren kak jadi ketua komdis",
                "pesan": "Lancar-lancar kuliahnya kak" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": "Kakaknya tegas sesuai job",
                "pesan": "Lancar terus kuliahnya" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya juga tegas",
                "pesan": "Lancar kuliahnya kak" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "Waw ada juga kakak-kakak dari psda baca webtoon",
                "pesan": "Lancar terus kuliahnya" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Keren bang komdis",
                "pesan": "Semoga kuliahnya lancar terus bang" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": "Wih keren hobi bakar-bakar",
                "pesan": "Semoga kuliahnya berjalan dengan baik" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Unik kak hobinya",
                "pesan": "Semoga kuliahnya berjalan dengan lancar terus kak" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Username ignya unik",
                "pesan": "Lancar terus bang kuliahnya" # 10
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan lapas",
                "hobi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": "Abangnya keren",
                "pesan": "Lancar terus bang ngeaspraknya" # 11
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": "Keren, pernah tutorin saat pra-kader",
                "pesan": "Lancar terus bang kuliahnya" # 12
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobi": "Dengar JPP worship",
                "sosmed": "@presiliamg",
                "kesan": "Nama kakaknya cakep",
                "pesan": "Semoga kuliahnya berjalan lancar terus" # 13
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Hobbinya sama bang",
                "pesan": "Lancar terus bang kuliahnya" # 14
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "Kece bang",
                "pesan": "Lancar terus ya bang kuliahnya" # 15
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Hobbinya beda dari yang lain",
                "pesan": "Semoga ga lelah menolong terus bang" # 16
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abangnya asik",
                "pesan": "Lancar terus kuliahnya bang" # 17
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Wih hobbinya berenang",
                "pesan": "Semoga ITERA punya kolam renang biar kakak bisa berenang ga jauh :)" # 18

            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Asikk abangnya",
                "pesan": "Lancarr terus ya bang kuliahnya" # 19
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()
elif menu == "Departemen MIKFES" :
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1g2J5sFvt954AzixFnLhb9Q51W686ypgY", # bg rafi 1
            "https://drive.google.com/uc?export=view&id=1CdebZMdUGP3XAtUDONHHZtuJOL4e_vuH", # ka anova 2
            "https://drive.google.com/uc?export=view&id=1rx6YrouzyqBmj_gmjbAJchOYjQ7bpvEo", # ahmad sahidin 3
            "https://drive.google.com/uc?export=view&id=15KdPLxPv2D0uuL1J2gz3NOJvcHc_UN3H", # bg fadhil 4
            "https://drive.google.com/uc?export=view&id=1I1aCN7FEUhfqVpaHywK5FgjiW89DSzjs", # ka syalasisha dina 5
            "https://drive.google.com/uc?export=view&id=1HujT1k-5MGK3cVKA9TiRYaVbR171t03C", # ka dinda 6
            "https://drive.google.com/uc?export=view&id=1xjqJfE07rlEvfy7DMg9aezt-tRv3elFf", # ka marleta 7
            "https://drive.google.com/uc?export=view&id=1qo8uX2A4xHfBXXRQpllinaJoMXrxwddq", # ka rut 8
            "https://drive.google.com/uc?export=view&id=18wqDoIASYxfpoqBAC2Wt3pbCj3sxSk9U", # ka syadza 9
            "https://drive.google.com/uc?export=view&id=1EXmYsBrCakia9ig5PKu3PVDdgRSU4cJY", # bg eggi 10
            "https://drive.google.com/uc?export=view&id=1Zn7qpWn3b05CQ2KJxkZRJkKYj_anKqXj", # ka febiya 11
            "https://drive.google.com/uc?export=view&id=11iTmQT48ATmXHWuiH123IEo8nWp-4IhB", # bg happy 12
            "https://drive.google.com/uc?export=view&id=1hUqmkjGwxJVmYY54pzOVH9YAXHIPz22o", # bg randa 13
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
                "kesan": "abangnya asik dan seru",  
                "pesan": "Lancar terus kuliahnya bang" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakanya baik",  
                "pesan": "lancar-lancar kak kuliahnya" # 2
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "abangnya baik",  
                "pesan": "semogah kuliahnya lancar-lancar bang" # 3
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "abangnya keliatan cool",  
                "pesan": "Slancar terus kuliaahnya bang" # 4
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakanya asik",  
                "pesan": "dilancarkan terus perkuliahanya kak" # 5
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya lucu",  
                "pesan": "semoga kuliahnya di lancarkan teruss" # 6
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakanya baik sekali",  
                "pesan": "Semangat kuliahnya kak, lancar teruss" # 7
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kakanya sepertinya baik dan asik",  
                "pesan": "Semoga kuliahnya berjalan dengan lancar terus " # 8
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Kakanya sepertinya asik",  
                "pesan": "Semoga kuliahnya berjalan dengan lancar terus" # 9
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobi": "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan": "sepertinya abangnya lucu",  
                "pesan": "Semoga kuliahnya berjalan dengan lancar terus" # 10
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakanya baik",  
                "pesan": "Semoga kuliahnya berjalan dengan lancar terus" # 11
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Unik banget namanya",  
                "pesan": "Semoga kuliahnya berjalan dengan lancar" # 12
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "sepetinya abangnya baik",  
                "pesan": "Semoga kuliahnya berjalan dengan baik" # 13
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
    
elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1v8VJcqOYZ_wclEJQJLx-_LEEjEcslgWB",  # bg yogy 1
            "https://drive.google.com/uc?export=view&id=1D3L_VJkFjQ7oZStHW9tMHxYQ8KXwtTp9",  # ka dhita 2
            "https://drive.google.com/uc?export=view&id=1QayzATiLfNTTkt33yI6_9_nVxYU3Z3re",  # ka dea mutia 3
            "https://drive.google.com/uc?export=view&id=1wtaDihse7ieV0ckh-PWR1VZLKGGR_eAN",  # ka novelia 4
            "https://drive.google.com/uc?export=view&id=1SZovEVUJZU-dLJi7ZAQeoxGtSUMgniIp",  # ka ratu 5
            "https://drive.google.com/uc?export=view&id=1oanFfVjqeZXtiwxojFvUgAmIt2es8O2m",  # bg tobias 6
            "https://drive.google.com/uc?export=view&id=11Y1p1EzioOohT9dAeOfM015RR99byv8L",  # ka yo 7
            "https://drive.google.com/uc?export=view&id=1eMluaswkmhpBQ-ds51bjNXb6tMhOIhVn",  # bg rizky 8
            "https://drive.google.com/uc?export=view&id=1QItCboQbQZozGF4l5Ns91XiX1GtSeBO3",  # bg arafi 9
            "https://drive.google.com/uc?export=view&id=1JPUqLrqaB1j-b31jOZP-_CWwN4hnhVZW", # ka asa 10
            "https://drive.google.com/uc?export=view&id=1Ly4uYO2OtVmEht1Qvy9pq9pAPT-uyjiC", # ka chalifia 11
            "https://drive.google.com/uc?export=view&id=1nbPNycRX9V8AzOlOpIATjwTRFWliO29T", # bg irvan 12
            "https://drive.google.com/uc?export=view&id=1LnBR6ckA2GDekzkvAhsPNc0mY11On6LR", # ka khaalishah 13
            "https://drive.google.com/uc?export=view&id=1SyBhTCDNujWan85D8a6k8LAOCFouJKiO", # bg raid 14
            "https://drive.google.com/uc?export=view&id=1vHhgcZYoHkrkfwqcQYKBJGxzdpwZ_0jp", # ka tria 15
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
                "kesan": "Abangnya Baik",
                "pesan": "Lancar bang kuliahnya"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "kakanya baik",
                "pesan": "Lancar kak kuliahnya"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "kakanya asik",
                "pesan": "Lancar terus kak kuliahnya"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "asik kakaknya",
                "pesan": "Semoga lancar terus kak kuliahnya"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobi": "Planning konten",
                "sosmed": "@jasminednva",
                "kesan": "asik kakanya",
                "pesan": "Semoga lancar terus kak kuliahnya"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Membaca",
                "sosmed": "@tobiassiagian",
                "kesan": "ternyata abanngya baik dan asik",
                "pesan": "Semoga lancar terus bang kuliahnya"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Buat Jurnal",
                "sosmed": "@yo_annamnk",
                "kesan": "asik  kakakny",
                "pesan": "Semoga lancar terus kak kuliahnya"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "asik abangya",
                "pesan": "Semoga lancar terus bang kuliahnya"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Samping warjo",
                "hobi": "Sholat",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "seru abangnya",
                "pesan": "Semoga lancar terus bang kuliahnya"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Cari ice breaking",
                "sosmed": "@u_yippy",
                "kesan": "kakanya asikkr",
                "pesan": "Semoga lancar terus kak kuliahnya"
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
                "pesan": "Semoga lancar terus kak kuliahnya"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Keren abangnya",
                "pesan": "Semoga lancar terus bang kuliahnya"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Lampung",
                "hobi": "Tilawah Al-quran",
                "sosmed": "@alyaavanevi",
                "kesan": "asikk kaka",
                "pesan": "Semoga lancar terus kak kuliahnya"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Ikut seminar",
                "sosmed": "@rayths_",
                "kesan": "uniq hobinya",
                "pesan": "Semangatt bang menjalani perkulihan"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Pemda",
                "hobi": "Sholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kakaknya cantik, murah senyum, baik, asik",
                "pesan": "semoga kulianya lancar terus"
            },
        ]
        
        display_images_with_data(gambar_urls, data_list)
    
    eksternal()
elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14vc9XoP0k1HCAP3cgbFgkZoUy1BBDHuy",  # bg dim 1
            "https://drive.google.com/uc?export=view&id=1kDWAeiX0sA0yKK1d7T7r4KcyiCpJAQz5",  # ka catherine 2
            "https://drive.google.com/uc?export=view&id=1D_YuMD4jcFZFockOYw7VXeiiu2lZzsUq",  # bg akbar 3
            "https://drive.google.com/uc?export=view&id=1_JnkmQDRDILb8vr82uzWfCHQfGiOgu5K",  # ka rani 4
            "https://drive.google.com/uc?export=view&id=1_ElpmvwGe6baGUOGEDu7OGQWT0qhG7TP",  # bg rendra 5
            "https://drive.google.com/uc?export=view&id=1BSuECjn-NLk1ELvQRtzgFXDONRKXBV_B",  # ka salwa 6
            "https://drive.google.com/uc?export=view&id=1AsjObBWYunTnx4wz_XLIwbrq-DMCMSos",  # bg ari 7
            "https://drive.google.com/uc?export=view&id=1ojzaROt-4JFFiHHZFx9ajFg7d4tEqxGd",  # ka azizah 8
            "https://drive.google.com/uc?export=view&id=1R5kpEDNyO-7WQvSZkUQONMtPX16Ut51r", # ka dearni 9
            "https://drive.google.com/uc?export=view&id=1yEQds-TDiiFCaRU5B2jY0ZjAjO4WIc6A", # bg rendi 10
            "https://drive.google.com/uc?export=view&id=10Fzo-Gnm-CBsFYZDHSQUl6W5YtIkSu11", # ka renta 11
            "https://drive.google.com/uc?export=view&id=1RPXzMZM3tNLFS3DUYp5w49RzROz90bLY", # bg josua 12
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
                "kesan": "Bang Dimas ternyata A6 banget",
                "pesan": "Semoga kuliahnya dilancarkan terus"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "Semoga kuliahnya dilancarkan terus"
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": "Abangnya cool",
                "pesan": "Semoga kuliahnya dilancarkan terus"
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobi": "Dengerin Musik",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya seru dan A6",
                "pesan": "SSemoga kuliahnya dilancarkan terus"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Baik dan murah senyum",
                "pesan": "Semoga kuliahnya dilancarkan terus"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakaknya baik",
                "pesan": "Semoga kuliahnya dilancarkan terus!"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abangnya juga asik",
                "pesan": "Semoga kuliahnya dilancarkan terus"
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kakaknya asik",
                "pesan": "Semoga kuliahnya dilancarkan terus"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobi": "Nonton film",
                "sosmed": "@meirasty_",
                "kesan": "Asik kakaknya",
                "pesan": "Semoga kuliahnya dilancarkan terus"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": "Cool banget abangnya",
                "pesan": "Semoga kuliahnya dilancarkan terus"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kakaknya baik",
                "pesan": "Semoga kuliahnya dilancarkan terus"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Siantar",
                "alamat": "Gerbang Barat",
                "hobi": "Nonton film",
                "sosmed": "@josuapanggabean_",
                "kesan": "Pendiam tapi abangnya A6",
                "pesan": "Semoga kuliahnya dilancarkan terus"
            },
        ]

       
        display_images_with_data(gambar_urls, data_list)

  
    internal()
elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1In7QasFE0sF5iRqzDJX4_Bn3Qr9aiQWl",  # bg andrian
            "https://drive.google.com/uc?export=view&id=1umzyLLUxflRTI3rCFU4JMNJtbdgyApKa",  # ka disty
            "https://drive.google.com/uc?export=view&id=1lKxleP0Rcr6WzUG6oCE85Jhc6_g4IwxU",  # ka nabila
            "https://drive.google.com/uc?export=view&id=1vskdJge96O-eDULtInlaMYNMIeNsbItb",  # bg ahmad rizqi
            "https://drive.google.com/uc?export=view&id=1j293tfmd0KBcQ2151xG9MkNQBhvktaMe",  # bg danang
            "https://drive.google.com/uc?export=view&id=1NsepUXspUQJXUDsHjFB3IBVan3kr0_V5",  # bg farel
            "https://drive.google.com/uc?export=view&id=16xeqG07f0o0SkTevxLlsb4r1-HOJ0uJz",  # ka tesa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  # ka nabilah
            "https://drive.google.com/uc?export=view&id=1JPRSsaa8aFtAU5vdTMzULw2mSdfoVi43",  # ka alvia
            "https://drive.google.com/uc?export=view&id=12FxmbjHUIeeqjDLkug7YA--iJqVpFJdt", # bg dhafin
            "https://drive.google.com/uc?export=view&id=1MuZlt3tmWEYhQmm3B1kqjuxPi4uEUfqk", # ka elia
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
                "kesan": "Abangnya keren",
                "pesan": "dilancarkan terus perkulihanya, bang!"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Asik kakaknya",
                "pesan": "dilancarkan terus perkulihanya,, kak!"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Baik kakaknya",
                "pesan": "dilancarkan terus perkulihanya,, kak!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": "Pendiam dan juga baik",
                "pesan": "dilancarkan terus perkulihanya,, bang!"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya baik dan juga A6",
                "pesan": "dilancarkan terus perkulihanya,, bang!"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Abangnya keren banget dan sangat menginspirasi",
                "pesan": "dilancarkan terus perkulihanya,, bang!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Pendiam dan juga asik",
                "pesan": "dilancarkan terus perkulihanya,kak!"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobi": "Bermain musik",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakaknya baik",
                "pesan": "dilancarkan terus perkulihanya,, kak!"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviaginting",
                "kesan": "Hobinya lucu",
                "pesan": "dilancarkan terus perkulihanya, kak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya pendiam tapi baik",
                "pesan": "dilancarkan terus perkulihanya,, bang!"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "Kakaknya asik banget dan talkative banget menjawab pertanyaan",
                "pesan": "dilancarkan terus perkulihanya,, kak!"
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    ssd()
elif menu == "Departemen MEDKRAF":
    def MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_l3oPzM8Anvm7qUqtxGZnKJM5inmOjWM", # bg wahyu 1
            "https://drive.google.com/uc?export=view&id=1yaEdi_1VXcAta2u3fdW43OxYkh6u_ymV", # ka fiola 2
            "https://drive.google.com/uc?export=view&id=1trzWyUTBC56p0bdws2YQpMC3fuSGFKb1", # ka arysyiah 3
            "https://drive.google.com/uc?export=view&id=1Ymy6bNP9ASwawvjjec7xBpLtodDrFBV3", # ka acintya 4 
            "https://drive.google.com/uc?export=view&id=1PaE2jtAXykRBkb6ZtNFWmVHpwR3rPmTi", # ka najla 5
            "https://drive.google.com/uc?export=view&id=1JU7Y4uoUsx-ciEn9VrSexJNLdmFP9SZb", # bg patricia 6
            "https://drive.google.com/uc?export=view&id=1RKbDy768VwtB05o9CqX9XsOzSW58ssen", # kk rahma 7
            "https://drive.google.com/uc?export=view&id=1Jgez7_yFYK8zq9dwO46BG1VFbaS7XgT-", # kak try 8 
            "https://drive.google.com/uc?export=view&id=1i18DWVeP8iTnXTiqe1XhTzUTqEJWEL_o", # bg kaisar 9
            "https://drive.google.com/uc?export=view&id=1R4bjbDeA2iXc7t9nq0pCGOZYmzWIkE7Z", # bg dwi 10
            "https://drive.google.com/uc?export=view&id=1YHr3SIwvh9Lqh9f6BW0SzUr7_bziiizE", # bg gym 11
            "https://drive.google.com/uc?export=view&id=1hhcYDi0Z0kH8uU66fSpdqPmc3fN51w8M", # ka nasyawa 12
            "https://drive.google.com/uc?export=view&id=1eEfyeXKc_UQTYbht3XU1DgWtgcZFaNs1", # ka priska  13
            "https://drive.google.com/uc?export=view&id=1N1vofRFMQXll1cbz8gdBq8T5YeP46HMH", # bg arsal 14
            "https://drive.google.com/uc?export=view&id=1kk_vGWm_5jw98WvKlADTkTe6Iblx3O5i", # bg abit 15
            "https://drive.google.com/uc?export=view&id=1KA7PtemydVoaUC0mzsfLxVi80UkJNBq_", # bg akmal 16
            "https://drive.google.com/uc?export=view&id=1Mu-iz6FL6lubvQuI4n2lzm6hAgUV1YJb", # ka hermawan 17
            "https://drive.google.com/uc?export=view&id=13CSuL2af526joG0VPoXITM25a4-fG72K", # ka nisa 18
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukaraju, Sukarame",
                "hobi": "nonton Donghua",
                "sosmed": "@wayulaja",
                "kesan": "Abangnya baik dan juga asik",
                "pesan": "kuliahnya dilancarkan terus, bang" # 1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@elokfabiola",
                "kesan": "Kakaknyya cakep dan baik",
                "pesan": "kuliahnya dilancarkan terus, kak" # 2
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "122450035",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobi": "Baca Komik",
                "sosmed": "@arsylah._",
                "kesan": "Keren kak jadi kadiv konten",
                "pesan": "Lancar-lancar terus kuliahnya kak" # 3
            },
            {
                "nama": "Cintya Bellaa",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "produktif sekali hobinya",
                "pesan": "dilacarkan terus kak kuliahnya" # 4
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Nulis, baca, ngefangirl",
                "sosmed": "@nanana.mijo",
                "kesan": "Kakaknya sepertinya fans k-pop",
                "pesan": "semoga perkulihanya lancar teruss kak" # 5
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobi": "Shopping",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakanya cakep dan murah senyum",
                "pesan": "Kuliahnya semoga lancar teruss, kak!" # 6
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "12245036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobi": "Membaca merk mobil",
                "sosmed": "@rahmanellyana",
                "kesan": "Unik banget hobinya",
                "pesan": "Kuliahnya semoga lancar teruss, kak!" # 7
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Kopri",
                "hobi": "Ngoding",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakanya baiks",
                "pesan": "Lancar terus kak kuliahnya" # 8
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450069",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Pulau damar, Way Kandis",
                "hobi": "Masih nyari",
                "sosmed": "@dino_lapet",
                "kesan": "abangnya asikk",
                "pesan": "semoga ketemu bang hobinyaa" # 9
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Pemda",
                "hobi": "menonton",
                "sosmed": "@dwiratnn",
                "kesan": "Kakany baik",
                "pesan": "Semoga kuliahnya berjalan dengan lancar terus kak" # 10
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "lapangan Golf",
                "hobi": "baca komik",
                "sosmed": "@jimnn.as",
                "kesan": "Nama abangnya unik ",
                "pesan": "Lancar terus bang kuliahnya" # 11
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450025",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Durian 1",
                "hobi": "makan seblak pake kecap",
                "sosmed": "@nsywanaf",
                "kesan": "kakanya asikk",
                "pesan": "Semoga kuliahnya berjalan dengna lancar, kak!" # 12
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jl.nangka 2",
                "hobi": "nonton apaja yang bikin nangis",
                "sosmed": "@presiliamg",
                "kesan": "Hobinya lumayan unik kak",
                "pesan": "Semoga kuliahnya berjalan lancar terus, kak!" # 13
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "122450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Jl. Nangka 3",
                "hobi": "main game",
                "sosmed": "@arsa.utama.",
                "kesan": "Keren bangnya jadi kadiv desain",
                "pesan": "Semoga Lancar terus bang kuliahnya" # 14
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "121450042",
                "umur": "20",
                "asal": "Rajabasa",
                "alamat": "Jl. Padat Karya",
                "hobi": "ngoding dan gaming",
                "sosmed": "@abitahmad",
                "kesan": "abangnya baik dan asik",
                "pesan": "dilancarkan terus kuliahnya bang, aminn" # 15
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobi": "Main hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abangnya juga baik dan asik",
                "pesan": "Semoga perkuliahan berjalan dengan lancar, bang!" # 16
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Jl Deket tol",
                "hobi": "Baca novel",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abangnya asik dan baik juga",
                "pesan": "Lancar terus kuliahnya bang" # 17
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Hobi",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kakanya jago desain dan baik",
                "pesan": "Semoga kuliahnya dilacarkan teruss, kak!" # 18

            },

        ]
        display_images_with_data(gambar_urls, data_list)
    MEDKRAF()   
    

    


    
    
    
    
