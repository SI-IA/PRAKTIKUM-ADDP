# Program: Pengecekan Angka Ganjil (Menggunakan NOT)

# Meminta input dari pengguna
angka = int(input("Masukkan sebuah angka: "))
angka2 = int(input("Masukkan Angka ke dua"))

# Mengecek apakah angka genap
adalah_genap = (angka % 2 == 0)

# Mengecek apakah angka ganjil (kebalikan dari genap)
adalah_ganjil = not adalah_genap

adalah_genap1 = (angka2 % 2 == 0)

adalah_ganjil1 = not adalah_genap1





# Cetak hasil
print("Angka 1 genap:", adalah_genap)
print("Angka 1 ganjil:", adalah_ganjil)
print("Angka 2 Genap", adalah_genap1)
print("Angka 2 Ganjil", adalah_ganjil1)