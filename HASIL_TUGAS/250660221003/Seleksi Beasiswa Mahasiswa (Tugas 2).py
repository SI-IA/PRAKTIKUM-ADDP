# Program: Seleksi Beasiswa Mahasiswa

# Meminta input dari pengguna
ipk = float(input("Masukkan IPK Anda: "))
pendapatan_ortu = int(input("Masukkan pendapatan orang tua Anda: "))

# Evaluasi logika seleksi
lolos_seleksi = (ipk == 4.0) or (pendapatan_ortu < 1500000)

# Menampilkan hasil
print("Lolos seleksi tahap pertama:", lolos_seleksi)