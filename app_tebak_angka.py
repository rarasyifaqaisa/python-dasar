def app_tebak_angka():
    import random
    angka_acak = random.randint(1, 10)
    maksimal_tebakan = 3
    tebakan = 0
    while tebakan < maksimal_tebakan:
        tebakan += 1
        try:
            angka_user = int(input("Masukkan angka: "))
            if angka_user > angka_acak:
                print("Angka terlalu besar")
            elif angka_user < angka_acak:
                print("Angka terlalu kecil")
            else:
                print("Selamat, Angka benar")
                break
        except ValueError:
            print("Error: Masukkan angka yang valid")
            tebakan -= 1
    else:
        print("Kamu telah melewati maksimal tebakan anda")
        print("Angka acak adalah", angka_acak)

    input("Enter untuk lanjut")


def app_menu():
    while True:
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")
        print("1. Tebak Angka")
        print("2. Keluar")
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")

        try:
            pilihan = int(input("Pilihan: "))
            if pilihan == 1:
                app_tebak_angka()
            elif pilihan == 2:
                print("=== Program tebak angka selesai ===")
                break
            else:
                print("Error: Pilihan tidak valid")
        except ValueError:
            print("Error: Masukkan angka yang valid")
        except KeyboardInterrupt:
            print("\n=== Program dihentikan oleh pengguna ===")
            break
        except Exception as e:
            print(f"Error: Terjadi kesalahan - {str(e)}")


if __name__ == "__main__":
    try:
        app_menu()
    except Exception as e:
        print(f"\nError: Program berhenti karena kesalahan - {str(e)}")
    finally:
        print("\n=== Program selesai ===")