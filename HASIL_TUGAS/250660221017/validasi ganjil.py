# Program Validasi Angka Ganjil

try:
    angka = int(input("Masukkan sebuah angka (bilangan bulat): "))
except ValueError:
    print("Input tidak valid. Harap masukkan bilangan bulat.")
    exit()

# Menentukan apakah angka tersebut genap
# Jika angka dibagi 2 sisa 0, maka genap.
adalah_genap = (angka % 2 == 0)

print("-" * 35)
print(f"Angka yang dimasukkan: {angka}")
print("-" * 35)

# Menggunakan struktur if-else
if adalah_genap:
    # Blok ini dijalankan jika adalah_genap bernilai True
    print("HASIL: Angka yang Anda masukkan adalah bilangan GENAP.")
else:
    # Blok ini dijalankan jika adalah_genap bernilai False (berarti ganjil)
    print("HASIL: Angka yang Anda masukkan adalah bilangan GANJIL.")

print("-" * 35)