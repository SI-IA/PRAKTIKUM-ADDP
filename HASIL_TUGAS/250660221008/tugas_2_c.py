# === Tugas 3: Pengecekan Angka Ganjil ===

# Meminta input dari pengguna
angka = int(input("Masukkan sebuah angka: "))

# Mengecek apakah angka genap
adalah_genap = (angka % 2 == 0)

# Menentukan apakah angka ganjil (kebalikan dari genap)
adalah_ganjil = not adalah_genap

# Cetak hasil
print("Angka tersebut ganjil:", adalah_ganjil)
