# === Tugas 4: (Tantangan) Validasi Akses Ruang Server ===

# Meminta input dari pengguna
level_akses = input("Masukkan level akses Anda (admin/teknisi/user): ").lower()
jam_masuk = int(input("Masukkan jam masuk (0-23): "))

# Aturan logika:
# Boleh Masuk = (level_akses == "admin") OR ( (level_akses == "teknisi") AND (8 <= jam_masuk <= 17) )
boleh_masuk = (level_akses == "admin") or ((level_akses == "teknisi") and (jam_masuk >= 8) and (jam_masuk <= 17))

# Cetak hasil evaluasi
print("Boleh masuk ruang server:", boleh_masuk)
