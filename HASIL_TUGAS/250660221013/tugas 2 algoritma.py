expected_ipk = 4.0
max_pendapatan_ortu = 1_500_000
ipk = float(input("Masukan IPK mahasiswa: "))
lolos_seleksi = False
pendapatan_orangtua = int(input("Masukan pendapatan ortu mahasiswa: "))


if (ipk >=  4.0) or (pendapatan_orangtua <= 1_500_000):
    lolos_seleksi = True

print("Lolos beasiswa?: ", lolos_seleksi)