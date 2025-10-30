# validasi akses ruangan admin

level_akses = input ("Masukkan level akses (admin/teknisi/user): ")
jam_masuk = int(input("masukkan jam masuk (0-23): "))

boleh_masuk = (level_akses == "admin") or ((level_akses == "teknisi") and (jam_masuk <= 17))

print ("boleh masuk:", boleh_masuk)