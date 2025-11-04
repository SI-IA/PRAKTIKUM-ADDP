#MEMINTA INPUT DARI PEMBELI
status_member = input("apakah anda member?? (ya/tidak) ").lower()
total_belanja = int(input("masukan total belanja anda :"))

#EVALUASI LOGIKA : HANYA DAPAT DISKON JIKA MEMBER DAN TOTAL BELANJA > 200000
dapat_diskon = (status_member == "ya") and (total_belanja > 200000)

#CETAK HASIL EVALUASI
print ("Dapat diskon :" , dapat_diskon)

#PESAN TAMABAHAN
if dapat_diskon:
    print ("SELAMAT ANDA MENDAPATKAN DISKON")
else :
    print ("maaf anda belum memenuhi syarat untuk dapat diskon")
