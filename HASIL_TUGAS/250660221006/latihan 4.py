# Meminta input dari pengguna
level_akses = input("Masukkan level akses (admin/teknisi/user): ").lower()
jam_masuk = int(input("Masukkan jam masuk (0-23): "))

# Aturan logika
boleh_masuk = (level_akses == "admin") or ((level_akses == "teknisi") and (jam_masuk >= 8) and (jam_masuk <= 17))

# Menampilkan hasil
print("Boleh masuk ke ruang server:", boleh_masuk)
