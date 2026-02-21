class Nama:
    def __init__(self, nama, asal, prodi):
        self.nama = nama 
        self.asal = asal
        self.prodi = prodi
        
p1 = Nama("Erina", "Surakarta", "Gizi")
print(p1.nama)
print(p1.asal)
print(p1.prodi)

# modify properties
p1.asal = "Jakarta"
print(p1.asal) # dari yang awalnya asal = Surakarta, setelah dimodify menjadi asal = Jakarta
# delete properties
del p1.prodi
 # print(p1.prodi) akan mengakibatkan terjadinya error

# class properties and object properties
class Buah:
    warna = "oren" # ini merupakan properti class
    akhiran = ""
    def __init__(self, fruit):
        self.fruit = fruit # ini merupakan instance propert
q1 = Buah("Pepaya")
x1 = Buah("Mangga")
print(q1.fruit, x1.fruit)
print("Buah nya", q1.warna, x1.warna, end= " ")
# modifying class properties
Buah.akhiran = "manis"
print("dan", q1.akhiran, x1.akhiran)
# add new properties
z1 = Buah("Nangka")
z1.dimakan = "tanggal 1"
z1.masuk_perut = "setelah dimakan"
print(z1.fruit, "dimakan pada", z1.dimakan, "dan masuk perut", z1.masuk_perut)