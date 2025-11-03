siswa = {
    "nama": "Rara",
    "umur": 17,
    "kelas": "15A"
}
print(siswa)

print(siswa["nama"])
print(siswa["kelas"])
print(siswa["umur"])

siswa["kelas"] = "15B"
print(siswa)

del siswa["umur"]
print(siswa)

for key in siswa:
    print(key, siswa[key])

for key, value in siswa.items():
    print(key, value)