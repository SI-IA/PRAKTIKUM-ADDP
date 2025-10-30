# Data Awal
saldo_awal = 5000000
pemasukan_bulanan = 7500000
pengeluaran_tetap = 4500000
investasi_bulanan = 1000000

# TODO 1: Hitung saldo setelah pemasukan dan pengeluaran
# Gunakan operator aritmatika dasar
saldo_setelah_transaksi = saldo_awal + pemasukan_bulanan - pengeluaran_tetap

# TODO 2: Hitung total investasi setelah 6 bulan dengan bunga 5%
# Gunakan operator penugasan dan aritmatika
investasi_6_bulan = investasi_bulanan * (1 + (5 / 100)) ** 6

# TODO 3: Hitung persentase tabungan dari pemasukan
# Gunakan operator modulus dan pembagian
persentase_tabungan = (pemasukan_bulanan % saldo_awal) / saldo_awal * 100

# TODO 4: Prediksi saldo setelah 1 tahun dengan asumsi sama
# Gunakan operator penugasan majemuk
saldo_1_tahun = saldo_awal
for i in range(12):
    saldo_1_tahun = saldo_1_tahun + pemasukan_bulanan - pengeluaran_tetap


print("saldo_setelah_transaksi:", saldo_setelah_transaksi)
print("investasi_6_bulan:", investasi_6_bulan)
print("persentase_tabungan:", persentase_tabungan)
print("saldo_1_tahun:", saldo_1_tahun)
