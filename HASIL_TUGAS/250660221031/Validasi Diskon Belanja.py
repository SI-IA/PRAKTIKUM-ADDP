# Validasi Diskon Belanja

status_member = input ("Apakah Anda member? (ya/tidak): ")
total_belanja = int(input("Masukkan total belanjaan (Rp): "))

dapat_diskon = (status_member == "ya") and (total_belanja > 500000)

print ("Dapat_diskon:", dapat_diskon)