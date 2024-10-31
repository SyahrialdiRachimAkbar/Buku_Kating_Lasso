import streamlit as st
from PIL import Image
from io import BytesIO
import requests

def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

st.title("Caesar Cipher Cryptography")
st.header("Apa itu Caesar Cipher Cryptography?")
st.write("""
Caesar Cipher adalah salah satu teknik kriptografi paling sederhana dan paling kuno yang digunakan untuk menyandikan 
         pesan. Metode ini bekerja dengan cara menggantikan setiap huruf dalam teks asli dengan huruf lain yang berada 
         di beberapa posisi setelahnya dalam alfabet. Misalnya, jika pergeseran atau "shift" yang dipilih adalah 3, 
         maka huruf A akan menjadi D, B akan menjadi E, dan seterusnya. Jika mencapai akhir alfabet, ia kembali ke awal 
         (misalnya, Z akan menjadi C).
""")

# Add image from Google Drive link
image_url = "https://drive.google.com/uc?export=view&id=1uRyLAzPuu4IKsgCttJ2gNZDbqyuH2r5l"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))
image = image.resize((400, 267))
st.image(image, caption='Julius Caesar, pencipta Caesar Cipher', use_column_width=True)

option = st.selectbox("Pilih opsi", ("Enkripsi", "Dekripsi"))
text = st.text_input("Masukkan text:")
shift = st.number_input("Masukkan perpindahan huruf (0-25):", min_value=0, max_value=25, step=1, value=3)

if st.button("Ubah"):
    if option == "Enkripsi":
        result = encrypt(text, shift)
        st.write("Teks dienkripsi menjadi:", result)
    else:
        result = decrypt(text, shift)
        st.write("Teks didekripsi menjadi:", result)

