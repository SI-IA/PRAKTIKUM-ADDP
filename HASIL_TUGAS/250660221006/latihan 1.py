# Program Validasi Diskon Belanja

# Meminta input dari pengguna
status_member = input("Apakah Anda member? (ya/tidak): ")
total_belanja = int(input("Masukkan total belanja Anda: "))

# Evaluasi logika promo
dapat_diskon = (status_member == "ya") and (total_belanja >=500000)

# Cetak hasilnya
print("Dapat diskon:", dapat_diskon)
