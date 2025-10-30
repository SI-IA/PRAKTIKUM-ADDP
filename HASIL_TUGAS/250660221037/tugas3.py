# Program untuk Memvalidasi Angka Ganjil

angka = int(input("Masukkan angka: "))
adalah_genap = (angka % 2 == 0)
adalah_ganjil = not adalah_genap

# Mencetak hasil angka ganjil
print(adalah_ganjil)