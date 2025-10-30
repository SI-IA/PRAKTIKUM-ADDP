# Program Seleksi Beasiswa Universitas

def seleksi_beasiswa (ipk, pendapatan_orang_tua): 
    if ipk == 4.0:
        lolos_seleksi = True
        alasan = "Lolos karena IPK sempurna (4.0)."
    elif pendapatan_orang_tua < 1500000:
        lolos_seleksi = True
        alasan = "Lolos karena pendapatan orang tua di bawah 1.500.000, -."
    else:
        lolos_seleksi = False
        alasan = "Tidak lolos karena IPK < 4.0 dan pendapatan orang tua tidak memenuhi syarat."

    return lolos_seleksi, alasan
ipk = float(input("Masukkan IPK Anda: "))
pendapatan_orang_tua = int(input("Masukkan pendapatan orang tua (dalam rupiah): 1"))

lolos_seleksi, alasan = seleksi_beasiswa (ipk, pendapatan_orang_tua)

print("Lolos seleksi tahap pertama:", lolos_seleksi)
print("Alasan:", alasan)