status_member = input("Status Member: ").lower()
total_belanja = int(input("Masukkan Total Belanja: "))
status_diskon = False

if (status_member != "ya") or (status_member != "tidak"):
    print("Pilih antara ya atau tidak")

if status_member == "ya" and total_belanja >= 700_000:
    status_diskon = True


print(f"Mendapatkan diskon?: {status_diskon}")