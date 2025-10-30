# Buat program untuk mengakses ruang sserver

level_masuk = input("Masukkan level akses: ")
jam_masuk = int(input("Masukkan jam masuk: "))
boleh_masuk = (level_masuk == "admin/teknis") and (jam_masuk == ">= 8" or "<= 7)")

# Mencetak hasil boleh masukin
print(boleh_masuk)
