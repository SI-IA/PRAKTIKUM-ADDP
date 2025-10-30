# Program: Validasi Akses Ruang Server

# Meminta input dari pengguna
level_akses = input("Masukkan level akses (admin/teknisi/user): ")
jam_masuk = int(input("Masukkan jam masuk (0-23): "))

# Evaluasi logika sesuai aturan
boleh_masuk = (level_akses == "admin") or ((level_akses == "teknisi") and (jam_masuk >= 8) and (jam_masuk <= 17))

# Cetak hasil
print(boleh_masuk)
