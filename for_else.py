kata = input("Masukkan kata : ")
huruf_dicari = input("Masukkan huruf dicari : ")

for huruf in kata:
    if huruf == huruf_dicari:
        print("Huruf", huruf_dicari, "ditemukan di kata")
        break
else:
    print("Huruf", huruf_dicari, "tidak ditemukan di kata")