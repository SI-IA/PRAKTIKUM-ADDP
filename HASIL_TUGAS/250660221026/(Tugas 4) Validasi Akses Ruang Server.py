# Program Validasi Akses Ruang Server

# Meminta input dari pengguna
level_akses = input("Masukkan level akses Anda (admin/teknisi/user): ")
jam_masuk = int(input("Masukkan jam masuk (0-23): "))

# Aturan logika akses
boleh_masuk = (level_akses == "admin") or (
    (level_akses == "teknisi") and (jam_masuk >= 8) and (jam_masuk <= 17)
)

# Menampilkan hasil
print("Apakah orang tersebut boleh masuk ke ruang server?", boleh_masuk)
