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
            "https://drive.google.com/uc?export=view&id=1UL6ouOZm_IM4ScGhBrCi_pO9CO5gLZQo",
            "https://drive.google.com/uc?export=view&id=1Vzelw2Kq2eeK27UOB8DCKc7I08MV9GbI",
            "https://drive.google.com/uc?export=view&id=1WGXIPrs7E0EBXAYWs0tyV_e60VrtU1vn",
            "https://drive.google.com/uc?export=view&id=1WIiENdUDZCBLg3ryX34V8vrqlMUWtLcy",
            "https://drive.google.com/uc?export=view&id=1W4RTg878q7LQKCrIzJHgTrNZD06-lH8k",
            "https://drive.google.com/uc?export=view&id=1W-bhle0Wkc8BzFDViT_QIKI7EogkcKVx",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Jl.Pulau Damar, Tanjung Senang",
                "hobi": "kuliah-rapat, dengerin lagu",
                "sosmed": "@gumilangkharisma",
                "kesan": "Terlihat kepemimpinannya yang keren",  
                "pesan":"semoga nambah keren dan diperlancar segala urusannya"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame, Bawean dua",
                "hobi": "Main Gitar",
                "sosmed": "@pndrinsni",
                "kesan": "Bang Pandra asik, seru, dan sepintas mirip pa lurah lasso",  
                "pesan":"semoga kuliah dan kegiatan lainnya dilancarkan!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota baru",
                "hobi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Suka sama public speaking ka liza",  
                "pesan":"Semoga semua urusan diperlancar dan semangat kuliahnya"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Jl. Nangka 4",
                "hobi": "Dengerin bang pandra main gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Ka putri asik, seru, ramah ",  
                "pesan":"Semoga selalu diberi kemudahan dan kelancaran ya kak"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Baca Webtoon",
                "sosmed": "@hrtpdlh",
                "kesan": "Seru karena jadi tau tentang bagaimana menjadi bendahara",  
                "pesan":"semangat terus kak ngurusin perduitannya dan semangat kuliahnya"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota baru",
                "hobi": "Baca wattpad dan au",
                "sosmed": "@nadhillahand26",
                "kesan": "Seru dan menyenangkan",  
                "pesan":"semangat terus kak ngurusin perduitannya dan semoga semuanya dilancarin"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qF8oNuzd-K99PV9E94L5FAdb3uxU5KZ3",
            "https://drive.google.com/uc?export=view&id=1qLnIRwlJ1oRUhCLBodwdQWhAr1zCiNwL",
            "https://drive.google.com/uc?export=view&id=1pn4OL9FMKf8gzjPIRUn4WmKdHZOvb-M6",
            "https://drive.google.com/uc?export=view&id=1qIqtNtizoiJc3lO-lrw_BNo2ne1UrJ7V",
            "https://drive.google.com/uc?export=view&id=1qM_uPkZRX1Ce46ig7hCRLbIhemxiTg33",
            "https://drive.google.com/uc?export=view&id=1qhGLCCnzew3QK8-VN8QP5mH123x07pnF",
            "https://drive.google.com/uc?export=view&id=1VXOpvMuALM722i9ZwgEWqJxMtBUf8Nyq",
            "https://drive.google.com/uc?export=view&id=1qaBZzTY19rWODXuH1g2Cuyw5uulRv7pK",
            "https://drive.google.com/uc?export=view&id=1qaontVYXYyFTwzuOArpTabWom23PHMpe",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Jl. Raden Saleh",
                "hobi": "Searching GPT",
                "sosmed": "@trimurniyaa_",
                "kesan": "Ka niya happy vibes dan asik bangetttt",  
                "pesan":"semoga kesedihan jauh dari kakak"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang selatan",
                "alamat": "Way Huwi",
                "hobi": "Baca buku dan nonton film",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Seru bangett kak",  
                "pesan":"semangat terus kak menjalani kuliahnya"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Jl. Raden Saleh",
                "hobi": "Belajar bersama Pak Tamaro",
                "sosmed": "@wlnsbn0",
                "kesan": "Seruu dan pembawaannya asik",  
                "pesan":"semoga kuliahnya dilancarinn"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Ngobrol",
                "sosmed": "@anisadini10",
                "kesan": "Asikk banget kak dan seru obrolannya",  
                "pesan":"semoga semua hal atau kegiatan dilancarin"# 1
            },
            {
                "nama": "Anisa fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Batam",
                "alamat": "Pesawaran",
                "hobi": "nonton drakor",
                "sosmed": "@ansftynni_",
                "kesan": "Sangat menyenangkann",  
                "pesan":"semoga semua urusan dipermudah ya kak"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Baca buku",
                "sosmed": "@fr_yulius",
                "kesan": "Abangnya seru dan banyak membantu",  
                "pesan":"semangat terus ngaspraknya bang"# 1
            },
            {
                "nama": "Dhea Amelia Puti",
                "nim": "122450004",
                "umur": "20",
                "asal":"Solo",
                "alamat": "Natar",
                "hobi": "Suka ditipu jual akun canva premium",
                "sosmed": "@_.dheamelia",
                "kesan": "Ka dhea seruu dan menyenangkan",  
                "pesan":"semangat menjalani kehidupan kak dan semoga dilancarkan semua urusan"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta, Jawa Tengah",
                "alamat": "Sukarame",
                "hobi": "Badminton, melukis, hiking, dan berenang",
                "sosmed": "@fhrul.pdf",
                "kesan": "Bang fahrul terlihat ramah",  
                "pesan":"semangat terus kuliahnya bang dan semoga dipermudah"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Makeup, nonton podcast, dan denger musik",
                "sosmed": "@berlyyanaa",
                "kesan": "Kakak nya terlihat kalem",  
                "pesan":"semangat terus kuliahnya ka dan semooga selalu dilancarkan"# 1
            },
            {
                "nama": " ",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":" "# 1
            },
             {
                "nama": " ",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":" "# 1
            },
             {
                "nama": " ",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":" "# 1
            },
             {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "-",
                "sosmed": "jeremia_s_",
                "kesan": "Sangat membantu dan baikk",  
                "pesan":"Semoga makin baik ya bang apalagi pas praktikum"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1c9dTqClE4-uiRnqwIeChpUyhab7YvNyK",
            "https://drive.google.com/uc?export=view&id=1budeSov947TAbnOex1VqcFqmJjhZxWjG",
        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": "122450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobi": "Bernyanyi",
                "sosmed": "@anissaluthfi",
                "kesan": "Kerennn banget kayak kece gituuu",  
                "pesan":"Semoga absen nya selalu penuh ya kak, semangat kakk!"
            },
            {
                "nama": "Rian Bintang wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kontrakan kota baru",
                "hobi": "Dengerin Ka Luthfi bernyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Banyak informasi yang bisa diambil",  
                "pesan":"semoga semakin keren kedepannya, semangat bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1quOPlA_jNdzSFBFhShPHFwfXchfkuOe_", # bg econ
            "https://drive.google.com/uc?export=view&id=1qrPoWZs2f9rXZHi0_9RNIDI9qhlVtrFQ", # ka abet
            "https://drive.google.com/uc?export=view&id=1sINvnDusrFUWf4UZT0-0uhhrY0gv-pZS", # ka pipah
            "https://drive.google.com/uc?export=view&id=1sBDOA06RpaNr0KGd0nBdH_hJe1Q7N-C8", # ka allya
            "https://drive.google.com/uc?export=view&id=1rt2SamkUturd0PURAWwsYmRUticTXmBk", # ka eksanty
            "https://drive.google.com/uc?export=view&id=1rusCOh07YUQLShIwPXjZtlMJFaQJaTUz", # ka hanum
            "https://drive.google.com/uc?export=view&id=1s6c7lyghPv4NuLIy66XaDm5SQxDRoRrF", # bg ferdy
            "https://drive.google.com/uc?export=view&id=1rpGBBCLv-7hcRTGbk8epUFcuZMyp3YbC", # bg deri
            "https://drive.google.com/uc?export=view&id=1ruAkK6zC-gnpKasKRKKAHxlj0tXduEVN", # ka okta
            "https://drive.google.com/uc?export=view&id=1rniER6M3txWVVa_zAMf3Z_8-5kEPm60d", # bg deyvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg ibnu farhan
            "https://drive.google.com/uc?export=view&id=1rZbfrqITTA_FPJA7GJGn8ARsYdEUonLg", # bg jo
            "https://drive.google.com/uc?export=view&id=1rVmoHCAJkNUwu4iXv9ztwJbULtshyXdQ", # bg kemas
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg leon
            "https://drive.google.com/uc?export=view&id=1rPIQEVZpW0O8r2FzCaNO5Ysmmn5OJ9h2", # ka presilia
            "https://drive.google.com/uc?export=view&id=1rW8tyU2QjcsXhXbnByh3BEu2pkrOtYef", # ka aqila
            "https://drive.google.com/uc?export=view&id=1rdoime6UmBpGYEeFEmYBxB_Pp2uIMlqS", # bg sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka vanes
            "https://drive.google.com/uc?export=view&id=1qvp12D2PCulZkh0bekPaQ5VHLoak6Pi1", # bg ateng
            "https://drive.google.com/uc?export=view&id=1rA0WZlb2o146kH_0yLAXNJrdDJ8VdQR4", # bg gede
            "https://drive.google.com/uc?export=view&id=1rAplexFBudGpybWQjYwq9HXxFHVv1AEj", # ka jaclin
            "https://drive.google.com/uc?export=view&id=1r1ZIwPIf_Cnp-GbqStUD_sHkDytmsV_e", # bg rafly
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
                "kesan": "Tegas dan disiplin ",  
                "pesan": "Semoga segala urusan dilancarkan dan semangat terus kuliahnya bang" # 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Sangat sangat ceriaaa dan seruuu bangett",  
                "pesan":"Semangat terus kakakk, semoga dilancarin segala urusannya" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Minum kopi",
                "sosmed": "@afifahhnsrn",
                "kesan": "Cantik bangett dan asikk",  
                "pesan":"Semakin sukses kedepannya kak" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Ngukur bandar lampung",
                "sosmed": "@allyaislami_",
                "kesan": "Asikkk banget dann kecee abisss",  
                "pesan":"Sehat sehat terus ka allya" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lampung tengah",
                "alamat": "Rajabasa",
                "hobi": "Ngeroasting orang",
                "sosmed": "@eksantyfebriana",
                "kesan": "Seru parahhh pokoknya",  
                "pesan": "Semoga kepintarannya menular ya kak" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Baca webtoon",
                "sosmed": "@farahanumafifahh",
                "kesan": "Asikk banget terus manis bangett",  
                "pesan": "Semangat kak kuliahnyaaa" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl pangeran senopati raya, gerbang barat",
                "hobi": "Baca buku dan Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Keliatannya kayak pendiem gitu tapi seruu  ",  
                "pesan": "Semakin dilancarin segala urusannya bang" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobi": "Bakar-bakar",
                "sosmed": "@dransyh_",
                "kesan": "Baikk bangett dan ramahh",  
                "pesan": "Semoga jauh dari penyakit bang" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Paling kalem keliatannya dan pendiem",  
                "pesan": "Semoga semakin lancar urusan apapun ya kak" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Lucuu banget dan suka bikin ketawa  ",  
                "pesan": "Semoga semester 7 nya lancar ya bangg" # 10
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
                "kesan": "Asik bangett bang jo terus kocakk parah  ",  
                "pesan": "Jaga kesehatan bangg dan lancar semua urusan" # 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobi": "Ngetik print halo dunia",
                "sosmed": "@kemasverii",
                "kesan": "Kecee banget dan kerennn",  
                "pesan": "Semoga semakin keren per codingannya bang kemas" # 13
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
                "kesan": "Cantikk banget kakk dan ramahh",  
                "pesan": "Selalu bahagia ya kakk" #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kalemm bangett yang tipe pendiem gitu tapi ramah",  
                "pesan": "Semoga jadi orang sukses ya kak" # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobi": "Nonton resilore id",
                "sosmed": "@sahid_maulana",
                "kesan": "Asik bangett bang sahidd pokoknya",  
                "pesan": "Selalu jaga kondisi tubuh bang" # 17
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
                "kesan": "Gokill suka ngelawakk dan bikin ketawa",  
                "pesan": "Semoga semester ini makin diperlancar ya bang" # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Lucuu banget dan seruuuu",  
                "pesan": "Jaga kesehatan dan sehat selalu bang" # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Cantik banget dan ramah banget",  
                "pesan": "Semangat renangnya kakk, semoga makin keren" # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Yang paling diem diantara yang lain tapi seruuu",  
                "pesan": "Semangat terus bang, jangan lupa istirahat" # 22
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
            "https://drive.google.com/uc?export=view&id=1j3_S4gb7KoV15WANbGxcXLjU-knGHCb_", # bg rafi
            "https://drive.google.com/uc?export=view&id=1jSjbMdy5Q1lNO0S-tTApL-dU_mkHrWWJ", # ka anova
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg mujadid
            "https://drive.google.com/uc?export=view&id=1j4GhNrK0HmHCM1ehBkg0U1u_228CHyuV", # ahmad sahidin
            "https://drive.google.com/uc?export=view&id=1jKsigV3tD8sdQI23UQq7N-14-lxqJPbF", # bg fadhil
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg regi
            "https://drive.google.com/uc?export=view&id=1jMNE5-gIzKtTvESp93LvhQjzRk8FagCe", # ka syalasisha dina
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg natanael
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg anwar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka deva
            "https://drive.google.com/uc?export=view&id=1jfBxdiM4vfAMXCPwheLFJ_1sUmoknNLI", # ka dinda
            "https://drive.google.com/uc?export=view&id=1jRRde3vKDx8nnOyBQMWQ_0XA-cj9Nzoj", # ka marleta
            "https://drive.google.com/uc?export=view&id=1jqqE8EZHRVhh3UO2Gzvmgnqy4sRKM4Px", # ka rut
            "https://drive.google.com/uc?export=view&id=1jnvwnXNYBMEluHHUrgYHwoedn1nMmXdW", # ka syadza
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg abdurrahman
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg aditya
            "https://drive.google.com/uc?export=view&id=1j2XHC2PLhbGMX7Rchf6kR0kRzUN0YnWt", # bg eggi
            "https://drive.google.com/uc?export=view&id=1jl4bVRp_d_1czIkMdbuISrHNDmnzJlJ5", # ka febiya
            "https://drive.google.com/uc?export=view&id=1j8Ie_FuCyYtcWIRhS92sIr7drgy0jDqK", # bg happy
            "https://drive.google.com/uc?export=view&id=1jHXnsdalawBH6r4-7oibZAuFJ-vcVBqB", # bg randa
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
                "kesan": "Seru bangett dan mengayomi",  
                "pesan": "Semoga selalu jadi pribadi yang baik bang" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Asikk banget kak dan menyenangkan",  
                "pesan": "Semangat kakak dan selalu jaga kesehatan" # 2
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
                "kesan": "Ramah banget dan seruuu tentunya",  
                "pesan": "Semoga semua kegiatan dilancarin dan disukseskan" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Bikin ngakak dan kece abis",  
                "pesan": "Selalu pentingin kesehatan bangg" # 5
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
                "kesan": "Lucuu banget kakk",  
                "pesan": "Semakin lucu dan diberi keamanan di setiap kegiatan" # 7
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
                "kesan": "Kelihatan banget orang pinternyaa",  
                "pesan": "Semoga semakin pinter ya kak dan semakin keren" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Cantik banget kak terus ramah jugaa",  
                "pesan": "Selalu menyebarkan kebaikan ya kak dan semangat" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kalem gitu kak keliatannya dan pendiem tapi ramah",  
                "pesan": "Semoga jauh dari penyakit ya kak" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Lucuuu dan kalem bangettt",  
                "pesan": "Jangan putus asa ya kak kalo ada sesuatu" # 14
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
                "kesan": "Seru bangettt banggg eggii",  
                "pesan": "Semangat bang dan semakin bermanfaat untuk orang sekitar" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Cantik bangett kakkkk",  
                "pesan": "Selalu jaga kesehatan ya kak, jangan kecapean" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Kecee banget bangg dan pastinya asikk",  
                "pesan": "Semoga semua keinginan yang lagi diinginkan tercapai" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Banyak dapet informasi dari bang randa",  
                "pesan": "Udah keren banget bang, semoga kepintarannya bisa menular ke saya" # 20
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
            "https://drive.google.com/uc?export=view&id=1sW6x-B3wv5A4-mPbMDGUTPjTgDe3TTxd", # bg yogy
            "https://drive.google.com/uc?export=view&id=1sJqtBs5EchyDVdozAs2UaERIZI07mvx6", # ka dhita
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka nazwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # bg bastian
            "https://drive.google.com/uc?export=view&id=1sml6Im5uzJlJBWnoRneGIBuIkH-6nnHt", # ka dea mutia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka ester
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka natasya
            "https://drive.google.com/uc?export=view&id=1smpQpdBOSYICvDnrDY3Z4t30zKOdPToD", # ka novelia
            "https://drive.google.com/uc?export=view&id=1t7s31R7lUDYyUl5OnoPCCVAkaaeI28La", # ka ratu
            "https://drive.google.com/uc?export=view&id=1soXEd62tBClUknCmblT40Z87AXzugh5h", # bg tobias
            "https://drive.google.com/uc?export=view&id=1t7k6ChQyCZkWdyo0WjNLdawvUAEAY4YU", # ka yo
            "https://drive.google.com/uc?export=view&id=1t0l2hL26APyTKIIIOUeJsCz7D2sdAAGZ", # bg rizky
            "https://drive.google.com/uc?export=view&id=1s_aUz8RN9_SURb9JHPaLDVUy5UqVcO4v", # bg arafi
            "https://drive.google.com/uc?export=view&id=1sWpXbIFYFjPapJqWiknBeClEUIo9ZmBH", # ka asa
            "https://drive.google.com/uc?export=view&id=1t6YITH2B6XfVIsqYc5S7902CjktRb8p5", # ka chalifia
            "https://drive.google.com/uc?export=view&id=1s_Mc5_ZI6S0xe594aO67La7nVhDQYalj", # bg irvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka izza
            "https://drive.google.com/uc?export=view&id=1skcSKyPvBqSkKVBJzUdQxwZ_m5i30zmA", # ka khaalishah
            "https://drive.google.com/uc?export=view&id=1t5BX1kl5CMDrlmm0SxddqijqLOArDfgR", # bg raid
            "https://drive.google.com/uc?export=view&id=1sb74LYd23TzCHN7ZO5vYpGkWI2SHR002", # ka tria
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
                "kesan": "seruuu banggg dan banyak becanda",  
                "pesan": "Sehat selalu ya bang dan panjang umur" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Cantik bangett dan baikkk",  
                "pesan": "Semangat kuliahnya kak, semoga segala urusannya dipermudah" # 2
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
                "kesan": "seruuu bangett pastinyaa dan lucuuu",  
                "pesan": "Selalu bahagia ya kak deaa" # 5
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
                "kesan": "Namanya cantik banget kak kaya orangnya",  
                "pesan": "Semangat terus kak dan semakin jadi orang baikk" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobi": "Planning konten",
                "sosmed": "@jasminednva",
                "kesan": "Cantik banget, imutt, ramah, seruuu",  
                "pesan": "Jangan capek-capek dan jangan lupa minum vitamin kak" # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Membaca",
                "sosmed": "@tobiassiagian",
                "kesan": "Menyenangkann karena asik bangett",  
                "pesan": "Jangan lupa istirahat bang, semangat" # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Buat Jurnal",
                "sosmed": "@yo_annamnk",
                "kesan": "Ka Yo ramahhh dan seruuuu",  
                "pesan": "Jangan lupa makan dan minum kak supaya ga sakit" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "Bikin ketawa dan seruuu",  
                "pesan": "Lancar terus bang kuliahnyaa" # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Samping warjo",
                "hobi": "Sholat",
                "sosmed": "@rafiramadhanmaulana",
               "kesan": "Kocakk banget apalagi hobinya sangat masyaAllah",  
                "pesan": "Sehat selalu bang dan makin rajin sholatnya" # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Cari ice breaking",
                "sosmed": "@u_yippy",
                "kesan": "Ka Uyi lucuuu bangettt dan baikk bangett",  
                "pesan": "Sehat terus ya ka uyi, selalu bahagia!"# 14
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Berbuat baik",
                "sosmed": "@chlfawww",
                "kesan": "Keliatannya kalemm bangettt",  
                "pesan": "Semoga segala urusannya dilancarkan kakk" # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Baikkk bangettt dan seruuuu",  
                "pesan": "Semangat bang irvan, jaga kesehatan terus!" # 16
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
                "kesan": "Seruu bangett dan ramahh",  
                "pesan": "Jangan lupa jaga kesehatan ka alyaa"# 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Ikut seminar",
                "sosmed": "@rayths_",
                "kesan": "Paling diem diantara yang lain tapi asikkk",  
                "pesan": "Semangatt bang dan semoga selalu dilancarin urusannya" # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Pemda",
                "hobi": "Sholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kocakk parahh dan suka becandaa",  
                "pesan": "Selalu bahagia ya kak yunaaa" # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fs1QnfSmn4ZLvUxFPZA9V5jXP1kDzc4H", # bg dim
            "https://drive.google.com/uc?export=view&id=1g8jzLEAEIGlQLS_wQXHzgXLCZEmBlfKZ", # ka catherine
            "https://drive.google.com/uc?export=view&id=1fr8WzJrlnm3-frQQlObEaoNLNUx_RRxT", # bg akbar
            "https://drive.google.com/uc?export=view&id=1fqBBafIlqZaBrdAZSEDsiyJRrOMjprWA", # ka rani
            "https://drive.google.com/uc?export=view&id=1fmmrsFvBLrVo5615ddJvzdWyUzAWSdRy", # bg rendra
            "https://drive.google.com/uc?export=view&id=1fkaRqDwsGxSL3iho9mvukI-6NbT0ogDF", # ka salwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka yosia
            "https://drive.google.com/uc?export=view&id=1g2EJZRdmlr5US1VqUsoKPbEKA878eMmR", # bg ari
            "https://drive.google.com/uc?export=view&id=1g9NgSLK4r7gOYt_yDa_g98RQTx-DE5zS", # ka azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka dearni
            "https://drive.google.com/uc?export=view&id=1gAd5sHY0-OCc3ILgFJwQvgT1E6rZhZp0", # ka meira
            "https://drive.google.com/uc?export=view&id=1gBThSf4xBoavR4YPKj2tRTxNljvjGLsK", # bg rendi
            "https://drive.google.com/uc?export=view&id=1l6Da2DztvW62M4AfGA0gTWCGp6-fjDHn", # ka renta
            "https://drive.google.com/uc?export=view&id=1g2LgaJjT2p3zDoWSskNH7ejP52zvLedR", # bg josua
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
                "kesan": "Kocakk bangett, suka bikin candaan, seruu",  
                "pesan": "Semoga urusan perkuliahan ini dilancarin terus ya bang" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Asikkk kakk dan seruuu bangettt",  
                "pesan": "Bahagia terus ya kak catherine!"# 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuan Dalam",
                "hobi": "Nangkep ikan cupang",
                "sosmed": "@akbar_restika",
                "kesan": "Bang akbar ini lucuuu dan pastinyaa seruuu",  
                "pesan": "Sehat selalu bang, semangatt" # 3
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobi": "Dengerin Musik",
                "sosmed": "@rannipu",
                "kesan": "Ka Rani orangnya seruu, baikk, dan kecee",  
                "pesan": "Jangan lupa istirahat ya kak kalo banyak kegiatan" # 4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Kocak bangett dan puitiss",  
                "pesan": "Jangan lupa main air putih bang" # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Seruuu walauu kayak pendiem kalem gitu",  
                "pesan": "Semoga selalu dilancarin segala urusannya ya kak" # 6
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
                "kesan": "Banyak memotivasi yang bermanfaat",  
                "pesan": "Semangat semester 7 nya bang semoga lancar terus" # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kalemm gitu kak kelihatannya",  
                "pesan": "Sehat selalu dan panjang umur ya kak" # 9
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
                "kesan": "Ramahh, seruu, dan baikk",  
                "pesan": "Jangan capek capek ya kak" # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Bernyanyi",
                "sosmed": "@rexander",
                "kesan": "Seruu bangett bang renci terus lucuu jugaa",  
                "pesan": "Semoga dipermudah segala kegiatannya ya bang" # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Bikin ketawaa dan banyakk becandaa",  
                "pesan": "Selalu bahagia ya kak, jaga kesehatan terus" # 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Siantar",
                "alamat": "Gerbang Barat",
                "hobi": "Nonton film",
                "sosmed": "@josuapanggabean_",
                "kesan": "Ramahh bangett teruss baikk dan informatif",  
                "pesan": "Semoga dipermudah dan diperlancar segala urusannya, semangattt bangg!" # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lOrE4XtqKJJz8S0qgrBuAbvnNbg_z7X_", # bg andrian
            "https://drive.google.com/uc?export=view&id=1l_DphehpsppUNouLFqYDCNR-IFvX5wki", # ka disty
            "https://drive.google.com/uc?export=view&id=1lohhh4ucdt7Pgf45LAHqP9ZnLyY_2Rpr", # ka nabila
            "https://drive.google.com/uc?export=view&id=1lYbFIGg5eAfM1sHKdOAElONNT1T1bOeu", # bg ahmad rizqi
            "https://drive.google.com/uc?export=view&id=1lVhSiPHeP3Sen0iDAWx2iHtKtFK4YgiD", # bg danang
            "https://drive.google.com/uc?export=view&id=1lRauBuOtTXYp81tksTZ6zSSr8nMvAoSY", # bg farel
            "https://drive.google.com/uc?export=view&id=1lhWBE1TDhAtIHdFqf04BUJ4XtNDwcE-N", # ka tesa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ka nabilah
            "https://drive.google.com/uc?export=view&id=1l_Ftt5nHsgFefVcxGLszVnO9lslO76EA", # ka alvia
            "https://drive.google.com/uc?export=view&id=1pMd_5oBHikvKNcPSVhmahwfgHKoLOZIO", # bg dhafin
            "https://drive.google.com/uc?export=view&id=1ljioDliAMBFXsSmVvrE5Vx37V_d7P9Ra", # ka elia
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
                "kesan": "Seruu dan abangnya santaiii",  
                "pesan": "Semoga kuliahnya lancar terus bang!!!" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "cantikk banget dan asikk",  
                "pesan": "Semangat terus kak dan selalu bahagia" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "baikk bangett dann cantikk sekali",  
                "pesan": "Jangan lupa minum air putih dan jaga kesehatan ya kak"  # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobi": "Jualan",
                "sosmed": "@ahmad.riz45",
                "kesan": "seruu dan ramah",  
                "pesan": "Sehat selalu bangg, semangat" # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@dananghk_",
                "kesan": "baikkk dan asikkk",  
                "pesan": "Semangat ngaspraknya bang" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "banyak kasih informasi tentang jualan",  
                "pesan": "Semoga segala urusannya dipermudah bang"# 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "lucuu dan pendiem",  
                "pesan": "Selalu bahagia ya ka tessa dan jangan lupa jaga kesehatan" # 7
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
                "kesan": "lucuu bangett dan cantikkk",  
                "pesan": "Bahagia terus ya kakk" # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangka l",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa13",
                "kesan": "seruu dan asikk",  
                "pesan": "Semangat terus bangg, jangan lupa jaga kesehatan" # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "lucuu banget dan seruuu",  
                "pesan": "Selalu bahagia ya ka meyy, semangatttt" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mVpGLcZC4LVgO1pTArPZHTgU7M5CDsmh", #bang wahyu
            "https://drive.google.com/uc?export=view&id=1nELouEA3xVErQ-2DhxsOFvODKvY6euAB", #ka elok
            "https://drive.google.com/uc?export=view&id=1mfqEKHNC3L5pyequPAqBddDXE2t73tha", #ka arsyiah
            "https://drive.google.com/uc?export=view&id=1mixkKSxdWXTvOKbuY4K-Lgsn9QtP115_", #ka cibel
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #ka eka
            "https://drive.google.com/uc?export=view&id=1mk4av5tCS4ELg_37o5mnXB5-D8bhYH-s", #ka najla
            "https://drive.google.com/uc?export=view&id=1mMtGce2aqWyRyMGuyk31EOPj9wf6X_zG", #ka patricia
            "https://drive.google.com/uc?export=view&id=1myG4-rVwnOoEIPWXN05_ttlP5Lk0A4jc", #ka rahma
            "https://drive.google.com/uc?export=view&id=1mXTK8nKXmWyaK3G4EmLV_2uZOezHDAsv", #ka try yani
            "https://drive.google.com/uc?export=view&id=1mkv1CCSaeojQPrjaVH4fWaW2mZgfuQTk", #bang kaisar
            "https://drive.google.com/uc?export=view&id=1n0XKPzQQ2TaUyvnmZA6oaMiC1W1_Bh-Z", #ka dwi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang gym
            "https://drive.google.com/uc?export=view&id=1mr1vtfRz706oWHMRU38BDoWwfCkH8Gci", #ka nasywa
            "https://drive.google.com/uc?export=view&id=1mz_mKAMiz4Mb1WDgdUnc1x-l7djO5clH", #ka priska
            "https://drive.google.com/uc?export=view&id=1n8b1pTkAilAVVdzoSMOt_mS217A6U3M_", #bang arsal
            "https://drive.google.com/uc?export=view&id=1mjM6ztsDZwWDc72lSOYyxEkiQRr_d_HV", #bang abit
            "https://drive.google.com/uc?export=view&id=1n918mxjlOAnO-B37l6AN4TrKXi_tG1Ag", #bang akmal
            "https://drive.google.com/uc?export=view&id=1mZNo-kjk0spEEl-dCPik_697bzzdTBzg", #bang mawan
            "https://drive.google.com/uc?export=view&id=1mVbi6eYnYi52XVNwLkTl1H9SEBdoLf3U", #ka khusnun
        ]

        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobi": "Nonton donghwa",
                "sosmed": "wayyulaja",
                "kesan": "seruuu bangett",  
                "pesan":"Semangat terus bang dan segala urusannya dilancarin"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@Elokviola",
                "kesan": "cantikk dan kalemm",  
                "pesan":"Jangan capek capek ya kak dan semakin kerenn"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Seneng",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "kalem sekaliii",  
                "pesan":"Jangan pantang menyerah ya kak kalo ada sesuatu"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Cantikk bangett",  
                "pesan":"Sehat selalu ka cibel dan semakin rajin ngegymnya"
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
                "kesan": "ramah, cantik, lucu",  
                "pesan":"Selalu tebar kebaikan kakak, semangattt"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobi": "Shopping",
                "sosmed": "@patriciadiajeng",
                "kesan": "Seruuu dan cantikkk bangettt",  
                "pesan":"Jangan sedih sedih ya kak, harus bahagiaa"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobi": "Membaca merk mobil",
                "sosmed": "@rahmaneliyana",
                "kesan": "baikk dan ramahh bangett",  
                "pesan":"Semangat terus ka neli, jaga kesehatan selalu ya"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Ngoding",
                "sosmed": "@tryyaniciaaa",
                "kesan": "seruu, cantikk",  
                "pesan":"Semoga ngodingnya makin jago kak"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Masih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "seruuu bangg",  
                "pesan":"Semangat semester 7 nya bang dan semangat mencari hobinya"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobi": "Menonton",
                "sosmed": "@dwiratnn_",
                "kesan": "pendiemmm kakk",  
                "pesan":"Jangan lupa jaga kesehatan kak dan bahagia selalu"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobi": "baca komik",
                "sosmed": "@jimnn.as",
                "kesan": "baikk dan asikk",  
                "pesan":"Semangat jadi pdd nya bangg"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobi": "suka bebersih dan denger musik jj",
                "sosmed": "@nsywanaf",
                "kesan": "cantik bangett dan seruuu",  
                "pesan":"Semoga makin rajin bebersihnya kak"
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
                "pesan":"Jangan sedih sedih ya kak, bahagia selaluuu"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsalutama",
                "kesan": "baikk dan ramahh",  
                "pesan":"Semoga makin banyak koleksi parfumnya yaa"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobi": "ngoding dan gaming",
                "sosmed": "@abitahmad",
                "kesan": "lucuu banget dan informatif",  
                "pesan":"Semoga makin jago codingannya ya bangg"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobi": "Main hp",
                "sosmed": "@akmal.faiz",
                "kesan": "seruu dan pinter",  
                "pesan":"Sehat selalu bang akmal, jangan lupa minum air putih"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobi": "baca novel",
                "sosmed": "@hermawan.mnrng",
                "kesan": "kocak banget dan asikk",  
                "pesan":"Semakin lancar segala urusannya bangg"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Ngepel",
                "sosmed": "@khusnun_nisa335",
                "kesan": "ramahh dan baikk",  
                "pesan":"Semakin rajin ya kak dan jaga kesehatan selalu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
# Tambahkan menu lainnya sesuai kebutuhan
