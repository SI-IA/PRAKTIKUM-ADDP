# Program: Validasi Diskon Belanja

# Meminta input dari pengguna
status_member = input("Apakah Anda member? (ya/tidak): ")
total_belanja = int(input("Masukkan total belanja: "))

# Evaluasi logika: dapat diskon jika member dan total belanja > 500000
dapat_diskon = (status_member == "ya") and (total_belanja > 500000)

# Cetak hasil
print(dapat_diskon)
