import streamlit as st

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
Kriptografi Caesar Cipher adalah teknik enkripsi yang menggunakan penggantian huruf dalam 
teks asli dengan huruf lain yang memiliki posisi tetap dalam alfabet. 
Teknik ini merupakan salah satu teknik kriptografi tertua dan paling sederhana
""")
option = st.selectbox("Pilih opsi", ("Enkripsi", "Dekripsi"))
text = st.text_input("Masukkan text:")
shift = st.number_input("Masukkan perpindahan huruf (0-25):", min_value=0, max_value=25, step=1, value=3)

if st.button("Submit"):
    if option == "Enkripsi":
        result = encrypt(text, shift)
        st.write("Teks dienkripsi menjadi:", result)
    else:
        result = decrypt(text, shift)
        st.write("Teks didekripsi menjadi:", result)
