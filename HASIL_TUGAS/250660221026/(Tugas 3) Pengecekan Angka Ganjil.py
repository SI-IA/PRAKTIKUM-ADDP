# Program Validasi Angka Ganjil

# Meminta input dari pengguna
angka = int(input("Masukkan sebuah angka: "))

# Mengecek apakah angka genap
adalah_genap = (angka % 2 == 0)

# Mengecek apakah angka ganjil (kebalikan dari genap)
adalah_ganjil = not adalah_genap

# Menampilkan hasil
print("Apakah angka tersebut ganjil?", adalah_ganjil)
