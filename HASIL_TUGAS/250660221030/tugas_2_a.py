# === Tugas 1: Validasi Diskon Belanja ===

# Meminta input dari pengguna
status_member = input("Apakah Anda member? (ya/tidak): ").lower()
total_belanja = int(input("Masukkan total belanja Anda (Rp): "))

# Aturan logika:
# Dapat diskon jika status_member == "ya" DAN total_belanja > 500000
dapat_diskon = (status_member == "ya") and (total_belanja > 500000)

# Cetak hasil evaluasi
print("Dapat diskon:", dapat_diskon)
