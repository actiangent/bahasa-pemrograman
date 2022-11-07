## Nama : Hisyam Fausta  
## NIM : 20210801191  
## Teknik Informatika  

# 

# Jawaban UTS  

1.  ```python
    print("saya belajar Bahasa Pemrograman menggunakan python") 
    ```
    Output:
    ![screenshot](https://raw.githubusercontent.com/actiangent/bahasa-pemrograman/main/uts/images/screenshot-output-jawaban1.jpeg)

2.  ```python
    def areaOfTriangle(base, height):
        return 0.5 * (base * height)


    def main():
        print("MENGHITUNG LUAS SEGITIGA")
        b = int(input("Masukan alas: "))
        h = int(input("Masukan tinggi: "))

        print(areaOfTriangle(b, h))


    if __name__ == "__main__":
        main()
    ```
    Output:
    ![screenshot](https://raw.githubusercontent.com/actiangent/bahasa-pemrograman/main/uts/images/screenshot-output-jawaban2.jpeg)

3.  ```python
    print("=======================\nPROGRAM QUIZ\n=======================")

    name = input("Masukan nama: ")
    nim = input("Masukan NIM: ")

    print("\nNama:", name, "\nNIM:", nim, sep=" ")  
    ```
    Output:
    ![screenshot](https://raw.githubusercontent.com/actiangent/bahasa-pemrograman/main/uts/images/screenshot-output-jawaban3.jpeg)

4.  ```python
    cardinal_direction = ("West", "North", "South")
    islands = ("Kalimantan", "Sumatra", "Sulawesi")


    def main():
        for island in islands:
            for direction in cardinal_direction:
                print(island, direction, sep=" ")


    if __name__ == "__main__":
        main()
    ```
    Output:
    ![screenshot](https://raw.githubusercontent.com/actiangent/bahasa-pemrograman/main/uts/images/screenshot-output-jawaban4.jpeg)

5.  ```python
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
    ```
    Output:
    ![screenshot](https://raw.githubusercontent.com/actiangent/bahasa-pemrograman/main/uts/images/screenshot-output-jawaban5.jpeg)