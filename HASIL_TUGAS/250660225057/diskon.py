# diskon 

status_member = input("dia member? (pilih ya atau tidak): "). lower()
total_belanja = int(input ("total_belanja" ))
dapat_diskon  = False



if (status_member == "ya") and (total_belanja >= 500000):
        dapat_diskon = True

print(dapat_diskon)