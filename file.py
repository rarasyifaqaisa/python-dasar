# print("=== SIMPAN DATA NILAI ===")
#
# file = open("nilai_siswa.txt", "w")
#
# while True:
#     nama = input("Nama siswa (enter untuk selesai): ")
#     if nama == "":
#         break
#
#     nilai = input("Nilai siswa :")
#
#     file.write(nama + "," + nilai + "\n")
#     print("Data", nama, "berhasil disimpan")
#
# file.close()
# print("=== PROGRAM SELESAI ===")

print("=== MENAMPILKAN DATA NILAI ===")

try:
    with open("nilai_siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0], ":", data[1])
except FileNotFoundError:
    print("file tidak ditemukan")

print("=== PROGRAM SELESAI ===")