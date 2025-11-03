def ambil_soal():
    soal_asli = []
    try:
        with open("bank_soal.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    soal_asli.append(line)
    except FileNotFoundError:
        print("Error: file 'bank_soal.txt' tidak ditemukan. Pastikan file ada di folder yang sama.")
    except Exception as e:
        print(f"Error membaca file 'bank_soal.txt': {e}")
    return soal_asli

def buat_soal():
    soal_asli = ambil_soal()

    import random
    # acak soal
    random.shuffle(soal_asli)
    soal_ujian = []

    if len(soal_asli) < 10:
        # tidak cukup soal untuk membuat ujian 10 soal
        raise ValueError("Bank soal kurang dari 10 soal. Tambahkan lebih banyak baris pada 'bank_soal.txt'.")

    for i in range(10):
        soal = soal_asli[i]  # pertanyaan|jawaban1,jawaban2,jawaban3,jawaban4
        try:
            data = soal.split("|")  # ["pertanyaan", "jawaban1,jawaban2,jawaban3,jawaban4"]
            if len(data) < 2:
                raise ValueError(f"Format soal tidak valid (harus ada '|' sebagai pemisah): {soal}")

            pertanyaan = data[0].strip()
            semua_jawaban = data[1].strip()

            jawaban = [j.strip() for j in semua_jawaban.split(",")]
            if len(jawaban) < 4:
                raise ValueError(f"Jumlah jawaban kurang dari 4: {soal}")

            jawaban_benar = jawaban[0]  # jawaban asli sebelum diacak

            # acak jawaban
            random.shuffle(jawaban)

            soal_ujian.append({
                "pertanyaan": pertanyaan,
                "jawaban": jawaban,
                "jawaban_benar": jawaban_benar
            })
        except Exception as e:
            # lewati soal yang bermasalah tetapi beri peringatan
            print(f"Warning: Melewati soal ke-{i+1} karena format tidak valid: {e}")
            continue

    if len(soal_ujian) < 10:
        raise ValueError("Tidak cukup soal valid untuk membuat ujian 10 soal setelah memfilter input yang bermasalah.")

    return soal_ujian

def app_ujian():
    try:
        soal_ujian = buat_soal()
    except Exception as e:
        print(f"Error menyiapkan soal ujian: {e}")
        return

    opsi = ["A", "B", "C", "D"]

    jawaban_benar = 0
    jawaban_salah = 0

    for i, soal in enumerate(soal_ujian):
        print("Pertanyaan", i + 1, ":", soal["pertanyaan"])
        print("Jawaban:")

        for j, jawaban in enumerate(soal["jawaban"]):
            # tampilkan hanya 4 opsi (A-D)
            if j < len(opsi):
                print(opsi[j], ".", jawaban)

        # minta input sampai valid
        while True:
            try:
                jawaban_user = input("Pilih jawaban (A/B/C/D): ").strip().upper()
                if jawaban_user == "":
                    print("Error: Masukkan pilihan (A/B/C/D)")
                    continue
                if jawaban_user not in opsi:
                    print("Error: Pilihan tidak valid. Gunakan A, B, C atau D.")
                    continue

                jawaban_user_index = opsi.index(jawaban_user)
                jawaban_asli_user = soal["jawaban"][jawaban_user_index]
                break
            except KeyboardInterrupt:
                print("\n=== Program dihentikan oleh pengguna ===")
                return
            except IndexError:
                print("Error: Opsi jawaban tidak tersedia untuk soal ini.")
                break
            except Exception as e:
                print(f"Error input: {e}")
                continue

        # jika jawaban_asli_user belum ditetapkan karena masalah opsi, lanjutkan
        if 'jawaban_asli_user' not in locals():
            continue

        if jawaban_asli_user == soal["jawaban_benar"]:
            print("Jawaban benar")
            jawaban_benar += 1
        else:
            print("Jawaban salah")
            jawaban_salah += 1

    print("Hasil Ujian")
    print("Jawaban benar:", jawaban_benar)
    print("Jawaban salah:", jawaban_salah)
    total = jawaban_benar + jawaban_salah
    if total == 0:
        print("Tidak ada jawaban yang diberikan.")
    else:
        try:
            hasil = jawaban_benar / total * 100
        except Exception:
            hasil = 0
        print("Hasil Ujian:", hasil, "%")


if __name__ == "__main__":
    try:
        app_ujian()
    except KeyboardInterrupt:
        print("\n=== Program dihentikan oleh pengguna ===")
    except Exception as e:
        print(f"\nError: Program berhenti karena kesalahan - {e}")
    finally:
        print("\n=== Program selesai ===")