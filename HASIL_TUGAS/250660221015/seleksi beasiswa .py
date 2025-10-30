expected_ipk = 4.0
max_pendapatan_ortu = 1_500_000
ipk = float(input("Masukkan IPK mahasiswa:" ))
pendapatan_orangtua = int(input("Masukkan Pendapatan Ortu mahasiswa: "))
lolos_seleksi = False

if (ipk == 4.0) or (pendapatan_orangtua <= max_pendapatan_ortu):
    lolos_seleksi = True

print("Lolos beasiswa?: ", lolos_seleksi) 