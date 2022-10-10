
name = "Hisyam Fausta"
nim = "20210801191"


def func():
    a = "any"
    print("selamat " + a)


func()

# definisi
def tambah():
    a = 5
    b = 3
    c = a+b
    print(c)


tambah()

# parameter
def data(nama, nim):
    print(f"nama saya {nama} dengan nim {nim}")


data(name, nim)


def total(sisi):
    return sisi*sisi


def segitiga(alas, tinggi):
    return 0.5*alas*tinggi
