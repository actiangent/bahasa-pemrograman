# Nama : Hisyam Fausta
# NIM : 20210801191
# Teknik Informatika
nim = "20210801191"
name = "Hisyam Fausta"


def main():
    while (True):
        print("\nNama:", name, "\nNIM:", nim, sep=" ")
        print("Pilihan\n1. Cappuccino\n2. Teh\n3. Exit")

        option = int(input("Masukan pilihan: "))
        if (option == 3):
            print("\nExit..")
            break

        elif (option == 1):
            print("Memilih Cappuccino")

            harga = int(input("Masukan harga: "))
            total = harga + (harga * 0.1)

            print("Jumlah yang harus dibayarkan:", total, sep=" ")
        elif (option == 2):
            print("Memilih Teh")

            harga = int(input("Masukan harga: "))
            total = harga + (harga * 0.1)

            print("Jumlah yang harus dibayarkan:", total, sep=" ")
        else:
            print("Maaf, pilihan tidak ada")


if __name__ == "__main__":
    main()
