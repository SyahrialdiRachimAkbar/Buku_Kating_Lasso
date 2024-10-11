import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/093 - Syahrialdi Rachim Akbar.py",
    title="093 - Syahrialdi Rachim Akbar",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/004 - Luthfia Laila Ramadhani.py",
    title="004 - Luthfia Laila Ramadhani",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/078 - Givaro Ananta.py",
    title="078 - Givaro Ananta",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating - Hanifah Inaya Sani.py",
    title="123 - Hanifah Inaya Sani",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/Mahasiswa5.py",
    title="Mahasiswa5",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/025 - Daffa Hadyan Navista.py",
    title="025 - Daffa Hadyan Navista",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/Mahasiswa7.py",
    title="Mahasiswa7",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/039 - Feby Angelina.py",
    title="039 - Feby Angelina",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/Mahasiswa9.py",
    title="Mahasiswa9",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/Mahasiswa10.py",
    title="Mahasiswa10",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/091 - Muhammad Ridwan.py",
    title="091 - Muhammad Ridwan",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/Mahasiswa12.py",
    title="Mahasiswa12",
    icon=":material/person:",
)
Mahasiswa13 = st.Page(
    "Buku Kating/Mahasiswa13.py",
    title="Mahasiswa13",
    icon=":material/person:",
)

#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, 
                            Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12, Mahasiswa13],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

