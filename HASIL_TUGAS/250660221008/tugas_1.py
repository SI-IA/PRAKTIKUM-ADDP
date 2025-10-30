#=== DATA AWAL ===
saldo_awal = 5_000_000
pemasukan_bulanan = 7_500_000
pengeluaran_tetap = 4_500_000
investasi_bulanan = 1_000_000

# === PERHITUNGAN ===

# 1 Saldo setelah pemasukan dan pengeluaran
saldo_setelah_transaksi = saldo_awal + pemasukan_bulanan - pengeluaran_tetap - investasi_bulanan

# 2 Total investasi setelah 6 bulan dengan bunga 5%
# Asumsi bunga majemuk bulanan (5% per 6 bulan ≈ 0.0008 per bulan)
bunga_bulanan = 0.05 / 6
investasi_6_bulan =  0
for i in range(6):
    investasi_6_bulan += investasi_bulanan
    investasi_6_bulan += investasi_6_bulan * bunga_bulanan

# 3 Persentase tabungan dari pemasukan
tabungan_bulanan = pemasukan_bulanan - pengeluaran_tetap - investasi_bulanan
persentase_tabungan =(tabungan_bulanan / pemasukan_bulanan) * 100

# 4 Prediksi saldo setelah 1 tahun
saldo_1_tahun = saldo_awal
for i in range(12):
    saldo_1_tahun += pemasukan_bulanan - pengeluaran_tetap - investasi_bulanan

# === OUTPUT ===

def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",",".")

print("=== HASIL KALKULASI KEUANGAN ===")
print(f"Saldo Awal: {format_rupiah(saldo_awal)}")
print(f"Pemasukan Bulanan: {format_rupiah(pemasukan_bulanan)}")
print(f"Pengeluaran Tetap: {format_rupiah(pengeluaran_tetap)}")
print(f"Investasi Bulanan: {format_rupiah(investasi_bulanan)}")
print("========================================")
print(f"1. Saldo setelah transaksi: {format_rupiah(saldo_setelah_transaksi)}")
print(f"2. Investasi 6 bulan (5% bunga): {format_rupiah(investasi_6_bulan)}")
print(f"3. Persentase tabungan: {persentase_tabungan:.2f}%")
print(f"4. Prediksi saldo 1 tahun: {format_rupiah(saldo_1_tahun)}")