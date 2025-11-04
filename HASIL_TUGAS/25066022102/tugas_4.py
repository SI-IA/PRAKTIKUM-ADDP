# Meminta input level akses dari pengguna
level_akses = input("Masukkan level akses (admin/teknisi/pengguna): ").lower()

# Meminta input jam masuk
jam_masuk = int(input("Masukkan jam masuk (0-23): "))

# Aturan logika:
boleh_masuk = (
    (level_akses == "admin") or
    (level_akses == "teknisi" and 7 <= jam_masuk <= 19) or
    (level_akses == "pengguna" and 9 <= jam_masuk <= 16)
)

# Cetak hasil evaluasi logika
print("Boleh masuk:", boleh_masuk)