akses_level = input("Masukkan level akses: ").lower()
jam_masuk = int(input("Masukkan jam masuk: "))
boleh_masuk = False

if jam_masuk < 0 and jam_masuk > 24:
    print(f"Lah apaan dah jam {jam_masuk} kocak")
    exit()

if akses_level == "admin":
    boleh_masuk = True
elif akses_level == "teknisi" and jam_masuk >= 8 and jam_masuk <= 17:
    boleh_masuk = True

print(f"Boleh masuk?: {boleh_masuk}")