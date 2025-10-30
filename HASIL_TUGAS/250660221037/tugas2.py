# Buat program untuk seleksi beasiswa universitas

ipk = float(input("Masukkan IPK: "))
pendapatan_ortu = int(input("Masukkan pendapatan orang tua (Rp): "))
lolos_seleksi = (ipk == 4.0) or (pendapatan_ortu < 1500000)

# Mencetak hasil evaluasi
print(lolos_seleksi)