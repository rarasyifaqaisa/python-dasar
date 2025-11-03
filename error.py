# print("Hello World"

# print(nama)

# print("5" + 5)

# value = int("salah")

# list_data = [1, 2, 3]
# print(list_data[5])

# orang = {"nama" : "Rara"}
# print(orang["umur"])

# print(10 / 0)

# print("=== KALKULATOR SEDERHANA ===")
#
# try:
#     angka1 = int(input("angka1: "))
#     angka2 = int(input("angka2: "))
#     hasil = angka1 / angka2
#     print("Hasil", hasil)
# except ValueError:
#     print("Input pengguna bukan angka")
# except ZeroDivisionError:
#     print("Tidak bisa dibagi dengan 0")
# except:
#     print("Terjadi kesalahan program")
#
# print("=== PROGRAM SELESAI ===")

try:
    angka = int(input("Masukkan angka : "))
except ValueError:
    print("Angka tidak valid")
else:
    print("Angka yang anda masukkan", angka)
    if angka > 0:
        print("Angka positif")
    elif angka < 0:
        print("Angka negatif")
    else:
        print("Angka nol")
finally:
    print("Program selesai")