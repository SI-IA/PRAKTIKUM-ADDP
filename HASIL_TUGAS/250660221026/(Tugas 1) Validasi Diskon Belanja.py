# Program Validasi Diskon Toko Online

# Meminta input dari pengguna
status_member = input("Apakah Anda member? (ya/tidak): ")
total_belanja = int(input("Masukkan total belanja Anda (Rp): "))

# Aturan logika untuk mendapatkan diskon
dapat_diskon = (status_member == "ya") and (total_belanja > 500000)

# Menampilkan hasil
print("Apakah pelanggan mendapat diskon?", dapat_diskon)
