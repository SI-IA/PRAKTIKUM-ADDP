# Program: Seleksi Beasiswa Mahasiswa

# Meminta input dari pengguna
ipk = float(input("Masukkan IPK Anda: "))
pendapatan_ortu = int(input("Masukkan pendapatan orang tua Anda: "))

# Evaluasi logika: lolos jika IPK == 4.0 atau pendapatan orang tua < 1500000
lolos_seleksi = (ipk == 4.0) or (pendapatan_ortu < 1500000)

# Cetak hasil
print(lolos_seleksi)