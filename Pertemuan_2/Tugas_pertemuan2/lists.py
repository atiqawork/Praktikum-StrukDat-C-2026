# list menggunakan kurunf siku [], bersifat mutable (dapat diubah), ordered (terurut), dan mengizinkan duplikasi

nama = ["Budi", "Andi", "Siti", "Sinta"]
print(nama) # output: seluruh isi list nama
# untuk menentukan berapa banyak item di dalam list, gunakan fungsi len()
print(len(nama)) # output: 4
# isi list bisa mengandung tipe data yang berbeda

# 1. acces list items
warna = ["merah", "hijau", "kuning", "biru"]
print(warna[1]) # output: hijau
print(warna[-2]) # output: kuning
print(warna[1:3]) # output: hijau, kuning biru
print(warna[:2]) # output: merah, hijau
print(warna[2:]) # output: kuning, biru
print(warna[-3:-1]) # output: hijau, kuning

# 2. change list items
buah = ["apel", "jeruk", "rambutan", "strawberry", "melon"]
buah[1] = "mangga" # mengubah jeruk menjadi mangga
print(buah) # output: apel, mangga, rambutan, strawberry, melon
buah[2:4] = ["kiwi", "semangka"] # mengubah rambutan dan strawberry menjadi kiwi dan semangka
print(buah) # output: apel, mangga, kiwi, semangka, melon
buah.insert(2, "pisang") # menyisipkan pisang di indeks ke-2
print(buah) # output: apel, mangga, pisang, kiwi, semangka

# 3. add list items
hewan = ["kucing", "beruang", "kelinci", "marmut", "musang"]
hewan.append("anjing") # menambahkan anjing di akhir list
print(hewan) # output: kucing, beruang, kelinci, marmut, musang, anjing
hewan.insert(1, "tupai") # menambahkan tupai di indeks ke 1
print(hewan) # output: kucing, tupai, beruang, kelinci, marmut, musang, anjing
hewan_air = ["paus", "lumba-lumba", "hiu"]
hewan.extend(hewan_air) # menggabungkan list hewan_air ke list hewan
print(hewan) # output: kucing, tupai, beruang, kelinci, marmut, musang, anjing, paus, lumba-lumba, hiu

# 4. remove list items
kendaraan = ["mobil", "motor", "sepeda"]
kendaraan.remove("sepeda") # menghapus sepeda dari list
print(kendaraan) # output: mobil, motor
kendaraan.pop(1) # menghapus item di indeks ke 1. jika indeks tidak ditentukan, item terakhir yang akan dihapus
print(kendaraan) # output: mobil
del kendaraan[0] # menghapus item di indeks ke 0
print(kendaraan) # output: []
kendaraan.append("bus") # append hanya bisa menambahkan 1 item baru
kendaraan.append("kereta")
print(kendaraan) # output: bus, kereta
kendaraan.clear() # menghapus seluruh item di dalam list
print(kendaraan) # output: []

# 5. loop lists => menggunakan for loop
makanan = ["mie", "bakso", "sate", "cireng"]
for x in makanan:
    print(x) # output: mie bakso sate cireng (setiap item di baris baru)
for i in range(len(makanan)):
    print(makanan[i]) # output: mie bakso sate cireng (setiap item di baris baru)

# 6. list comprehension => cara singkat untuk membuat list baru dari list yang sudah ada
bentuk = ["persegi", "lingkaran", "segitiga", "jajargenjang"]
new_bentuk = []
for x in bentuk:
    if "s" in x: # memeriksa apakah huruf 's' ada di dalam item bentuk
        new_bentuk.append(x) # lalu menambahkan item tersebut ke dalam list new_bentuk
print(new_bentuk) # output: ['persegi', 'segitiga']
new_bentuk = [x for x in bentuk if x != "segitiga"] # menerima item hanya jika item tersebut bukan 'segitiga'
print(new_bentuk) # output: ['persegi', 'lingkaran', 'jajargenjang']
new_bentuk = [x.upper() for x in bentuk] # bikin semua item uppercase
print(new_bentuk) # output: ['PERSEGI', 'LINGKARAN', 'SEGITIGA', 'JAJARGENJANG']

# 7. sort lists
minuman = ["teh", "kopi", "jus", "soda"]
minuman.sort() # mengurutkan list secara ascending (A-Z)
print(minuman) # output: ['jus', 'kopi', 'soda', 'teh']
minuman.sort(reverse = True) # mengurutkan list secara descending (Z-A)
print(minuman) # output: ['teh', 'soda', 'kopi', 'jus']
minumann = ["Teh", "kopi", "Soda"]
minumann.sort(key = str.lower) # mengurutkan list tanpa memperhatikan kapitalisasi
print(minumann) # output: ['kopi', 'Soda', 'Teh'] 

# 8. copy lists
kota_jawa = ["jakarta", "bandung", "semarang", "surabaya"]
kota_besar = kota_jawa.copy() # metode copy()
print(kota_besar) # output: ['jakarta', 'bandung', 'semarang', 'surabaya']

# 9. join lists
riau = ["pekanbaru", "dumai", "bengkalis"]
angka = [1, 2, 3, 4, 5]
gabungan = riau + angka # menggunakan operator +
print(gabungan) # output: ['pekanbaru', 'dumai', 'bengkalis', 1, 2, 3, 4, 5]
# bisa juga menggunakan extend(), append()
