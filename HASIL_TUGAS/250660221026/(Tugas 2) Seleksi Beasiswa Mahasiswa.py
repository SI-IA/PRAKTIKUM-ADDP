# Program Seleksi Beasiswa Universitas

# Meminta input dari pengguna
ipk = float(input("Masukkan IPK Anda: "))
pendapatan_ortu = int(input("Masukkan pendapatan orang tua Anda (Rp): "))

# Aturan logika seleksi
lolos_seleksi = (ipk == 4.0) or (pendapatan_ortu < 1500000)

# Menampilkan hasil
print("Apakah mahasiswa lolos seleksi tahap pertama?", lolos_seleksi)
