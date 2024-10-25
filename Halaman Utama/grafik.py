import matplotlib.pyplot as plt

# Data untuk X dan F(X)
X_values = [0, 1, 2]
CDF_values = [0.2857, 0.8571, 1]

# Membuat grafik distribusi kumulatif
plt.step(X_values, CDF_values, where='post', label='CDF F(X)', color='blue', linewidth=2)

# Tambahkan label dan judul
plt.xlabel('Jumlah Pesawat Rusak (X)')
plt.ylabel('Distribusi Kumulatif F(X)')
plt.title('Grafik Distribusi Kumulatif Jumlah Pesawat Rusak')

# Tampilkan grafik

