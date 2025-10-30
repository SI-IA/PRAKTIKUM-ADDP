# Program Hak Akses Ruang Server

# 1. Minta input level_akses (string)
level_akses = input("Masukkan Level Akses (admin/teknisi/user): ").lower()

# 2. Minta input jam_masuk (integer 0-23)
try:
    jam_masuk = int(input("Masukkan Jam Masuk (0-23): "))
except ValueError:
    print("Input jam masuk tidak valid. Harap masukkan angka bulat (0-23).")
    exit()

# 3. Evaluasi Aturan Logika
# Aturan: Boleh Masuk = (Level Akses == "admin") OR ((Level Akses == "teknisi") AND (Jam Masuk >= 8) AND (Jam Masuk <= 17))

# Kriteria 1: Akses Admin
kriteria_admin = (level_akses == "admin")

# Kriteria 2: Akses Teknisi di Jam Kerja
kriteria_teknisi_jam_kerja = (
    (level_akses == "teknisi") and
    (jam_masuk >= 8) and
    (jam_masuk <= 17)
)

# Gabungkan kedua kriteria dengan operator OR
boleh_masuk = kriteria_admin or kriteria_teknisi_jam_kerja

print("\n" + "=" * 40)
print("HASIL VALIDASI AKSES")
print("=" * 40)
print(f"Level Akses: {level_akses.upper()}")
print(f"Jam Masuk: {jam_masuk:02d}.00")
print("-" * 40)

# Menggunakan struktur if-else untuk menampilkan hasil
if boleh_masuk:
    # Blok ini dijalankan jika boleh_masuk bernilai True
    print("✅ STATUS: AKSES DIBERIKAN. Silakan Masuk.")
    
    # Menampilkan detail alasan lolos (opsional, untuk info tambahan)
    if kriteria_admin:
        print("Alasan: Level Akses 'ADMIN' selalu diizinkan.")
    elif kriteria_teknisi_jam_kerja:
        print("Alasan: Level Akses 'TEKNISI' diizinkan pada jam kerja (08.00 - 17.00).")
    
else:
    # Blok ini dijalankan jika boleh_masuk bernilai False
    print("❌ STATUS: AKSES DITOLAK.")
    
    # Menampilkan detail alasan penolakan (opsional, untuk info tambahan)
    if level_akses == "teknisi":
        print(f"Alasan: Teknisi hanya diizinkan pukul 08.00-17.00. Jam masuk ({jam_masuk:02d}.00) di luar batas.")
    elif level_akses == "user":
        print("Alasan: Level Akses 'USER' tidak memiliki izin masuk.")
    else:
        print("Alasan: Level Akses tidak dikenali atau tidak memiliki izin.")

print("=" * 40)