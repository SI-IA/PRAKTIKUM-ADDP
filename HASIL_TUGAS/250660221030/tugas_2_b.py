# === Tugas 2: Seleksi Beasiswa Mahasiswa ===

# Meminta input dari pengguna
ipk = float(input("Masukkan IPK Anda: "))
pendapatan_ortu = int(input("Masukkan pendapatan orang tua Anda (Rp): "))

# Aturan logika:
# Lolos seleksi jika IPK == 4.0 atau pendapatan orang tua < 1.500.000
lolos_seleksi = (ipk == 4.0) or (pendapatan_ortu < 1500000)

# Cetak hasil evaluasi
print("Lolos seleksi tahap pertama:", lolos_seleksi)
