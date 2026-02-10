# set => unordered (nggak berurutan), tidak boleh duplikat, menggunakna kurung kurawal {}
iniset = {"sayuran", "buah", "nama", 1, "sayuran", True}
print(iniset) # output: {'buah', 'nama', 'sayuran'} (duplikat dihapus), 1 dan True dianggap sama

# 1. access set items
buah = {"apel", "jeruk", "rambutan", "strawberry"}
for x in buah:
    print(x) # output: apel, jeruk, rambutan, strawberry (urutan tidak tentu)
print("jeruk" in buah) # output: True
# ketika set sudah dibuat, set tidak dapat diubah itemnya namun bisa ditambah itemnya

# 2. add set items
sayur = {"bayam","kangkung", "sawi"}
sayur.add("tomat") # menambah 1 item tomat
print(sayur) # output  acak
sayur_baru = {"wortel", "buncis"}
sayur.update(sayur_baru) # menambah beberapa item sekaligus
print(sayur) # output acak

# 3. remove set items => bisa menggunakan remove dan discard
sayur.remove("kangkung") # menghapus kangkung. jika item yang ingin dihapus tidak ada, akan error
print(sayur) # output acak
sayur.discard("bayam") # menghapus bayam. jika item yang ingin dihapus tidak ada, tidak akan error
print(sayur) # output acak
sayuran = sayur.pop()
print(sayuran) # output: menghapus item acak dari set
print(sayur) # output acak
# clear() untuk menghapus isi set, del untuk menghapus set completely

# 4. loop sets
hari = {"senin", "selasa", "rabu", "kamis"}
for x in hari:
    print(x) # output isi set di new line namun acak

# 5. join sets
set1 = {1, 2, 3, 4}
set2 = {"bus", "truk"}
set3 = set1.union(set2) # menggabungkan set1 dan set2
print(set3) # output acak
set3 = set2 | set1 # cara lain menggabungkan set1 dan set2. | hanya untuk penggabungan set dengan set
print(set3) # output acak
set1.update(set2) # menambahkan set2 ke set1
print(set1) # output acak
 # ====== #
kota_jawa = {"jakarta", "magelang", "surabaya"}
kota_besar = {"jakarta", "surabaya", "medan"}
irisan_kota = kota_jawa.intersection(kota_besar) # intersection mencari item yang sama di kedua set
print(irisan_kota) # output: {'jakarta', 'surabaya'}
# intersection juga bisa menggunakan & (set dengan set)
# True dan 1 serta False dan 0 dianggap sama
difference_kota = kota_jawa.difference(kota_besar) # mencari item di set 1 that are not in set 2
print(difference_kota) # output: {'magelang'}
# difference juga bisa menggunakan - (set dengan set)
symmetric_diff = kota_jawa.symmetric_difference(kota_besar) # mencari item yang tidak sama di kedua set
print(symmetric_diff) # output: {'medan', 'magelang'}
# symmetric_difference juga bisa menggunakan ^ (set dengan set)

# 6. frozenset => immutable (tidak dapat diubah) set
jam = frozenset({"06.00", "12.00", "18.00"})
print(jam) # output: frozenset({'06.00', '12.00', '18.00'})
print(type(jam)) # output: <class 'frozenset'>
# immutable berarti item nya nggak bisa ditambah atau dihapus
