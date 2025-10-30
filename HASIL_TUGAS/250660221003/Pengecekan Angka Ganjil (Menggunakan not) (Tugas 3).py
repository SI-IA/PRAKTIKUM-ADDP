# Program: Pengecekan Angka Ganjil

# Meminta input dari pengguna
angka = int(input("Masukkan sebuah angka: "))

# Mengecek apakah angka genap
adalah_genap = (angka % 2 == 0)

# Menggunakan operator not untuk menentukan apakah angka ganjil
adalah_ganjil = not adalah_genap

# Menampilkan hasil
print("Apakah angka tersebut ganjil?", adalah_ganjil)
