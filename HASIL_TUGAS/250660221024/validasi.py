akses_level = input("Masukan level akses: ").lower()
jam_masuk = int(input("Masukan jam masuk:"))
boleh_masuk = False

if jam_masuk <0 and jam_masuk > 23:
    print(f"Yailah mau maju gmn perusahaan kalo masuk jam {jam_masuk} Kespret")
    exit()

if akses_level == "admin":
    boleh_masuk = True
elif akses_level == "teknisi" and jam_masuk >= 8 and jam_masuk <= 17:
    boleh_masuk = True
    
print(f"Boleh masuk: {boleh_masuk}")
