def app_penjumlahan():
    print("=== PROGRAM PENJUMLAHAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 + angka2
        print("hasil penjumlahan", hasil)
    except ValueError:
        print("Error: Masukkan angka yang valid")
    print("=== Program penjumlahan selesai ===")
    input("Enter untuk lanjut")

def app_pengurangan():
    print("=== PROGRAM PENGURANGAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 - angka2
        print("hasil pengurangan", hasil)
    except ValueError:
        print("Error: Masukkan angka yang valid")
    print("=== Program pengurangan selesai ===")
    input("Enter untuk lanjut")

def app_perkalian():
    print("=== PROGRAM PERKALIAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 * angka2
        print("hasil perkalian", hasil)
    except ValueError:
        print("Error: Masukkan angka yang valid")
    print("=== Program perkalian selesai ===")
    input("Enter untuk lanjut")

def app_pembagian():
    print("=== PROGRAM PEMBAGIAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 / angka2
        print("hasil pembagian", hasil)
    except ValueError:
        print("Error: Masukkan angka yang valid")
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi dengan nol")
    print("=== Program pembagian selesai ===")
    input("Enter untuk lanjut")

def app_menu():
    while True:
        print("=== PROGRAM KALKULATOR SEDERHANA ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        print("=== PROGRAM KALKULATOR SEDERHANA ===")

        try:
            pilihan = int(input("Pilihan: "))

            if pilihan == 1:
                app_penjumlahan()
            elif pilihan == 2:
                app_pengurangan()
            elif pilihan == 3:
                app_perkalian()
            elif pilihan == 4:
                app_pembagian()
            elif pilihan == 5:
                print("=== SAMPAI JUMPA LAGI ===")
                break
            else:
                print("Error: Pilihan tidak valid")
        except ValueError:
            print("Error: Masukkan nomor pilihan yang valid")
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