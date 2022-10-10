## Nama : Hisyam Fausta
## NIM : 20210801191
## Teknik Informatika

---


# Rangkuman

### Tipe Data
* String  
String adalah rangkaian karakter Unicode.  
Penulisan dengan kutip dua (").
``` 
a = "Hello World"
print(a)
print(type(a))

# Output:
# Hello World
# <class 'str'> 
```

* Integer  
Bilangan bulat tanpa koma/desimal.
``` 
b = 13
print(b)
print(type(b))

# Output:
# 13
# <class 'int'>
```

* Float  
Bilangan yang bisa merepresentasikan desimal.
``` 
c = 11.5
print(c)
print(type(c))

# Output:
# 11.5
# <class 'float'>
```

* Tuple  
Tuple digunakan untuk menyimpan beberapa item yang **terurut dan tidak bisa diubah**.  
Penulisan dengan kurung bulat '('.
``` 
d = 21, 5
print(d)
print(type(d))

tuple_f = 1, 2, 3
print(tuple_f[0])

# Output:
# (21, 5)
# <class 'tuple'>
# 1
```

* Bilangan kompleks (Complex Number)  
Bilangan imajiner yang dilambangkan *i*.
``` 
e = 1j
print(e)
print(type(e))

z = complex('5-9j')
print(z)

# Output:
# 1j
# <class 'complex'>
```

* List  
List bisa menyimpan daftar item yang **berurut, dapat diubah, dan bisa untuk item duplikat**.
``` 
f = ["a", "b", "c"]
print(f)
print(type(f))

list_f = [1, 2, 3]
print(list_f[0])

# Output:
# ['a', 'b', 'c']
# <class 'list'>
# 1
```

* Set  
Set atau Himpunan adalah kumpulan item yang **tidak terurut, tidak dapat diubah*, dan tidak terindeks**.
``` 
set_f = {1, 2, 3}
print(set_f)

g = {"a", "b", "c"}
print(g)
print(type(g))

# Output:
# {1, 2, 3}
# {'a', 'c', 'b'}
# <class 'set'>
```

* Frozenset  
Set yang **tidak bisa diubah**.
``` 
h = frozenset({1, 2, 3})
print(type(h))

# Output:
# <class 'frozenset'>
```

* Boolean  
Nilai yang hanya bisa 2 kemungkinan, yaitu **True** (benar) dan **False** (salah).
``` 
i = True
j = False
print(i, j)
print(type(i))
print(type(j))

# Output:
# True False
# <class 'bool'>
# <class 'bool'>
```

---
  
### Variabel
Variabel digunakan untuk menyimpan nilai tipe data

Kata kunci ```def``` digunakan untuk mendefinisikan suatu fungsi.  
  
Fungsi bisa menerima argumen berupa parameter yang bisa digunakan untuk diolah fungsi tersebut. Fungsi juga dapat mengembalikan nilai menggunakan ``` return ```

```
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

```