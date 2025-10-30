# Meminta input dari pengguna
angka = int(input("Masukkan sebuah angka: "))

# Menentukan apakah angka genap
adalah_genap = (angka % 2 == 0)

# Menentukan apakah angka ganjil menggunakan operator not
adalah_ganjil = not adalah_genap

# Menampilkan hasil
print("Apakah angka tersebut ganjil?", adalah_ganjil)
