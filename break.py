angka_rahasia = 7

while True:
    tebakan = int(input("Masukkan tebakan: "))
    if tebakan == angka_rahasia:
        print("selamat, Anda benar")
        break
    else:
        print("Salah, coba lagi")