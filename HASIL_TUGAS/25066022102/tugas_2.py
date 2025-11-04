#MEMINTA INPUT DARI MAHASISWA
ipk =float(input("masukan ipk anda :"))
pendapatan_ortu =int(input("masukan pendapatan orang tua (dalam rupiah):"))

#ATURA LOLOS KULIAH JIKA IPK> = 3.0 DAN PENDAPATAN ORANG TUA < 5.000.000
lolos_sleksi = ( ipk >=3.0) and (pendapatan_ortu <5000000)

#hasil evaluasi 
print("Lolos sleksi :",lolos_sleksi)

if lolos_sleksi :
    print ("selamat anda dinyatakan LOLOS SLEKSI DAN MENDAPATKAN BEASISWA")
else :
    print (" anda tidak lolos sleksi dan tidak mendapatkan beasiswa")
