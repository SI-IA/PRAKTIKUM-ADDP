#beasiswa kip

try:
    ipk = float(input("Masukkan Nilai IPK Anda: "))
except ValueError:
    print("Input IPK tidak valid. Harap masukkan angka.")
    exit()


try:
    pendapatan_ortu = int(input("Masukkan Pendapatan Orang Tua (tanpa titik/koma): "))
except ValueError:
    print("Input Pendapatan tidak valid. Harap masukkan bilangan bulat.")
    exit()

# Menentukan kriteria kelulusan
# Lolos Seleksi = (IPK == 4.0) OR (Pendapatan Ortu < 1500000)

kriteria_ipk = (ipk == 4.0)
kriteria_pendapatan = (pendapatan_ortu < 1500000)

print("-" * 40)
print("HASIL SELEKSI TAHAP PERTAMA")
print("-" * 40)
print(f"IPK yang dimasukkan: {ipk}")
print(f"Pendapatan Ortu yang dimasukkan: Rp {pendapatan_ortu:,}")
print("-" * 40)

# Menggunakan struktur if-else untuk menampilkan hasil
if kriteria_ipk or kriteria_pendapatan:
    print("SELAMAT! Anda dinyatakan LOLOS Seleksi Tahap Pertama.")
    
    # Menampilkan alasan kelulusan (opsional)
    if kriteria_ipk and kriteria_pendapatan:
        print("Keterangan: Lolos karena memenuhi kriteria IPK Sempurna dan Pendapatan Ortu Rendah.")
    elif kriteria_ipk:
        print("Keterangan: Lolos karena memenuhi kriteria IPK Sempurna (4.0).")
    elif kriteria_pendapatan:
        print("Keterangan: Lolos karena memenuhi kriteria Pendapatan Orang Tua (< Rp 1.500.000).")
else:
    print("MOHON MAAF. Anda dinyatakan TIDAK LOLOS Seleksi Tahap Pertama.")
    print("Keterangan: IPK tidak 4.0 DAN Pendapatan Ortu di atas Rp 1.500.000.")

print("-" * 40)