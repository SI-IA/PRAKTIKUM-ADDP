expected_ipk = 4.0
max_pendapatan_ortu = 1_500_000
ipk = float(input("Masukkan IPK Anda: "))
pendapatan_ortu = int(input("Masukkan pendapatan orang tua: "))
lolos_seleksi = False

if (ipk == expected_ipk) or (pendapatan_ortu <= max_pendapatan_ortu):
    lolos_seleksi = True

print("lolos beasiswa?:", lolos_seleksi)
