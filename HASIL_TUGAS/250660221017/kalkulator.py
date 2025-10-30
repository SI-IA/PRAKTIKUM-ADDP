# kalkulator investasi


# Data Awal
saldo_awal = 5000000
pemasukan_bulanan = 7500000
pengeluaran_tetap = 4500000
investasi_bulanan = 1000000

# Fungsi untuk memformat angka menjadi string mata uang Rupiah
def format_rupiah(angka):
    """Fungsi untuk memformat angka menjadi string mata uang Rupiah (mis. Rp 5.000.000)"""
    return f"Rp {angka:,.0f}".replace(",", "_").replace(".", ",").replace("_", ".")

# --- TODO 1: Hitung saldo setelah pemasukan dan pengeluaran ---
# Menggunakan operator aritmatika dasar: + dan -
saldo_setelah_transaksi = saldo_awal + pemasukan_bulanan - pengeluaran_tetap

# --- TODO 2: Hitung total investasi setelah 6 bulan dengan bunga 5% ---
# Asumsi: Investasi bulanan pertama (Rp 1.000.000) berbunga 5% per periode (bulan) selama 6 bulan.
# Menggunakan operator aritmatika (**) untuk pangkat.
bunga_per_periode = 0.05
jumlah_periode = 6
investasi_6_bulan = investasi_bulanan * (1 + bunga_per_periode)**jumlah_periode
# Hasil: 1000000 * (1.05)^6 = 1,340,095.64

# --- TODO 3: Hitung persentase tabungan dari pemasukan ---
# Untuk mendapatkan hasil yang diharapkan 40.00%, kita asumsikan tabungan = Pemasukan - Pengeluaran Tetap.
# Menggunakan operator pembagian.
tabungan_untuk_persentase = pemasukan_bulanan - pengeluaran_tetap
persentase_tabungan = (tabungan_untuk_persentase / pemasukan_bulanan) * 100

# --- TODO 4: Prediksi saldo setelah 1 tahun dengan asumsi sama ---
# Keuntungan bersih bulanan = Pemasukan - Pengeluaran Tetap - Investasi Bulanan
keuntungan_bulanan_bersih = pemasukan_bulanan - pengeluaran_tetap - investasi_bulanan # 2.000.000

saldo_1_tahun = saldo_awal

# Menggunakan operator penugasan majemuk (+=) untuk simulasi 12 bulan
for _ in range(12):
    saldo_1_tahun += keuntungan_bulanan_bersih
# Hasil: 5.000.000 + (2.000.000 * 12) = 29.000.000

# ===============================================================
#                             OUTPUT
# ===============================================================
print("=== HASIL KALKULASI KEUANGAN ===")
print(f"Saldo Awal: {format_rupiah(saldo_awal)}")
print(f"Pemasukan Bulanan: {format_rupiah(pemasukan_bulanan)}")
print(f"Pengeluaran Tetap: {format_rupiah(pengeluaran_tetap)}")
print(f"Investasi Bulanan: {format_rupiah(investasi_bulanan)}")
print("========================================")

# 1. Saldo setelah transaksi
print(f"1. Saldo setelah transaksi: {format_rupiah(saldo_setelah_transaksi)}")

# 2. Investasi 6 bulan (5% bunga)
# Menggunakan f-string untuk formatting output Rp 1.340.095,64
print(f"2. Investasi 6 bulan (5% bunga): Rp {investasi_6_bulan:,.2f}".replace(",", "_").replace(".", ",").replace("_", "."))

# 3. Persentase tabungan
print(f"3. Persentase tabungan: {persentase_tabungan:.2f}%")

# 4. Prediksi saldo 1 tahun
print(f"4. Prediksi saldo 1 tahun: {format_rupiah(saldo_1_tahun)}")