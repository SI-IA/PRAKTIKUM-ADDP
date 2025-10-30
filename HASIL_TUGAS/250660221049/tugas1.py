# Buat program untuk memvalidasi diskon belanja

status_member = input("Memasukkan status member(ya/tidak):")
total_belanja = int(input("Masukkan total belanja dalam ruoiah (Rp):"))
dapat_diskon =  (status_member == "ya") and ("total belanja > 500000")

# Mencetak hasil dsikon
print(dapat_diskon)