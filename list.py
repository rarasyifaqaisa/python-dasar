daftar_kosong = []
print(daftar_kosong)

angka = [1, 2, 3, 4, 5, 6]
print(angka)

nama = ["Rara", "Syifa", "Qaisa"]
print(nama)

campuran = ["Rara", 90, "Syifa", 85, "Qaisa", 90]
print(campuran)

buah = ["apel", "jeruk", "pisang", "mangga"]
print(buah[0])
print(buah[1])
print(buah[2])
print(buah[3])

warna = ["merah", "biru", "hijau"]
print(warna)
warna[1] = "kuning"
print(warna)

buah = ["apel", "jeruk"]
print(buah)
buah.append("durian")
print(buah)
buah.insert(1, "buah naga")
print(buah)

buah.remove("jeruk")
print(buah)

buah.pop()
print(buah)

del buah[0]
print(buah)

buah = ["apel", "jeruk", "mangga"]
print(len(buah))

satu = [1,2,3,4,5]
print(satu)
dua = [6,7,8,9,10]
print(dua)

gabungan = satu + dua
print(gabungan)

banyak_buah = ["apel", "jeruk", "mangga", "salak"]
for buah in banyak_buah:
    print(buah)

for i in range(0, len(banyak_buah)):
    print(banyak_buah[i])

if "durian" in banyak_buah:
    print("Ada durian")
else:
    print("Tidak ada durian")