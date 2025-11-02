# angka = int(input("Masukkan angka : "))
# if angka > 0:
#     print("Angka positif")
#
# if angka < 0:
#     print("Angka negatif")
#
# if angka == 0:
#     print("Angka NOL")

# nilai = int(input("Masukkan nilai: "))
#
# if nilai >= 60:
#     print("Anda lulus")
# else:
#     print("Anda tidak lulus")

# nilai = int(input("Masukkan nilai: "))
#
# if nilai >= 90:
#     print("Nilai A")
# elif nilai >= 80:
#     print("Nilai B")
# elif nilai >= 70:
#     print("Nilai C")
# elif nilai >= 60:
#     print("Nilai D")
# else:
#     print("Nilai E")

# umur = int(input("Masukkan umur : "))
# punya_sim = input("Punya SIM? (ya/tidak)")
#
# if umur >= 17 and punya_sim == "ya":
#     print("Boleh mengendarai motor")
# else:
#     print("Tidak boleh mengendarai motor")

# username = input("Username :")
# password = input("Password :")
#
# if username == "admin":
#
#     if password == "12345":
#         print("Login berhasil")
#         print("Selamat datang admin")
#     else :
#         print("Password salah")
#
# else:
#     print("Username tidak ditemukan")

# hari = input("Masukkan nama hari :").lower()
#
# match hari:
#     case "senin" | "selasa" | "rabu" | "kamis" | "jumat" :
#         print("Hari kerja")
#     case "sabtu" | "minggu" :
#         print("Hari libur")
#     case _:
#         print("Nama hari tidak valid")

# if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
#     print("Hari kerja")
# elif hari == "sabtu" or hari == "minggu" :
#     print("Hari libur")
# else:
#     print("Nama hari tidak valid")

angka = int(input("Masukkan angka : "))

# hasil = ""
# if angka > 0:
#     hasil = "Positif"
# else:
#     hasil = "Negatif"

hasil = "Positif" if angka > 0 else "Negatif"
print(hasil)