akses_level = input("Masukan level akses: ").lower()
jam_masuk = int(input("Masukan jam masuk: "))
boleh_masuk = False

if jam_masuk < 0 and jam_masuk > 24:
    print(f"Mikir dong mana ada jam {jam_masuk} anjay")
    exit()

if akses_level == "admin":
    boleh_masuk = True
elif akses_level == "teknisi" and jam_masuk >= 8 and jam_masuk <= 17:
    boleh_masuk = False

print(f"Boleh masuk?: {boleh_masuk}")
