import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd

st.title("Analisa Kepuasan Peserta Magang Kaderisasi CEO HMSD ADYATAMA 2024 Saat Diterima")
st.write("""
Magang untuk peserta kaderisasi CEO HMSD ADYATAMA 2024 sudah dimulai. Para peserta sangat antusias 
         menyambut hal tersebut karena mereka bisa terjun secara langsung dalam himpunan dan 
         mempelajari bagaimana program kerja dari masing masing divisi di HMSD berjalan. 
         Sebelum dimulainya magang, para peserta di wawancara terlebih dahulu oleh divisi masing-masing. 
         Para peserta diberi 2 pilihan divisi sebagai tempat magang. 
         Tentu akan sangat bagi para peserta jika diterima sesuai dengan pilihannya. 
         Namun, bagaimana jika mereka diterima, namum tidak di pilihannya? 
         Untuk itu kami menganalisa seberapa senang para peserta saat diterima magang dengan menggunakan 
         skala 1 - 5 (Sangat tidak senang - Sangat senang). Berikut hasil analisa yang telah kami (Lasso) kerjakan.
""")

url = "https://drive.google.com/uc?export=view&id=1X5kvHyrJDp0Jj-sC6H9a1JMSrYYMTYFE"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
image = image.resize((600, 1000))
st.image(image, caption='Analisa kepuasan menggunakan diagram batang', use_column_width=True)

st.write("""
Dari data diatas, bisa kita lihat dari total 113, 71 menyatakan 5 (Sangat senang), 
33 menyatakan 4 (Senang), 9 menyatakan 3 (Biasa saja). Hal ini menunjukkan bahwa mayoritas peserta magang sangat senang
saat diterima magang."\n"
Tidak hanya analisa lewat diagram batang, kami juga menganalisa melalui Density Plot. Berikut Density Plot untuk
rating kepuasan magang.
""")

url = "https://drive.google.com/uc?export=view&id=1eIoIBtT_JhtDjTbBJuSTuAjblWWW_-r3"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
image = image.resize((600, 400))
st.image(image, caption='Density Plot', use_column_width=True)

st.write("""
Dari grafik yang kita lihat diatas, data cenderung terdistribusi di rentang 3.5 - 5.0. Menunjukkan mayoritas peserta magang
         sangat senang saat diterima magang di HMSD ADYATAMA.
""")

st.subheader("Resources")
data_url = "https://raw.githubusercontent.com/LaboNapitupulu/File/main/Pendataan_Peserta_Magang_CEO_HMSD_2024.csv"
df = pd.read_csv(data_url)
st.write(df.head())
st.write("Link Google Colab: https://colab.research.google.com/drive/1bIHiCd3mmffSAsQBHO3gbJJdbCUhr4Yp#scrollTo=2d6n_n29QEvk")
