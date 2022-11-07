# Nama : Hisyam Fausta
# NIM : 20210801191
# Teknik Informatika
def areaOfTriangle(base, height):
    return 0.5 * (base * height)


def main():
    print("MENGHITUNG LUAS SEGITIGA")
    b = int(input("Masukan alas: "))
    h = int(input("Masukan tinggi: "))

    print(areaOfTriangle(b, h))


if __name__ == "__main__":
    main()
