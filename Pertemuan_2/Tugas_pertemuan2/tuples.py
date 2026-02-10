# tuples tidak dapat diubah (immutable), menggunakan kurung biasa ()
inituple = ("sayuran",)
print(type(inituple)) # output: <class 'tuple'>
# jika ingin membuat tuple dengan 1 item, tambahkan koma di akhir item tersebut

# 1. acces tuple items
buah = ("apel", "jeruk", "blueberry", "mangga")
print(buah[1])  # output: jeruk
print(buah[-2]) # output: blueberry
print(buah[1:3]) # output: jeruk, blueberry
print(buah[:2]) # output: apel, jeruk
print(buah[2:]) # output: blueberry, mangga 
print(buah[-3:-1]) # output: jeruk, blueberry       
if "blueberry" in buah:
    print("yap yap yap ada blueberry di sini")

# 2. update tuples
sayur = ("bayam", "kangkung", "wortel", "sawi")
sayuran = list(sayur) # ubah tuple jadi list terlebih dahulu
sayuran[2] = "seledri" # mengubah wortel menjadi seledri
sayur = tuple(sayuran) # ubah kembali list jadi tuple
print(sayur) # output: ('bayam', 'kangkung', 'seledri', 'sawi') 
sayur_tambah = ("tomat",) # buat tuple baru dengan 1 item
sayur += sayur_tambah # gabungkan tuple sayur dengan sayur_tambah
print(sayur) # output: ('bayam', 'kangkung', 'seledri', 'sawi', 'tomat')
sayur_baru = list(sayur) # ubah tuple jadi list terlebih dahulu
sayur_baru.remove("kangkung" ) # menghapus kangkung dari list
sayur = tuple(sayur_baru) # ubah kembali list jadi tuple
print(sayur) # output: ('bayam', 'seledri', 'sawi', 'tomat')    
# sama dengan yang lain, gunakan del untuk hapus tuple completely

# 3. unpack tuples
hari = ("senin", "selasa", "rabu")
(day1, day2, day3) = hari
print(day1) # output: senin
print(day2) # output: selasa    
print(day3) # output: rabu
jalan = ("sudirman", "thamrin", "sm amin", "bangau", "kubang")
(jalan1, jalan2, *jalan3) = jalan
print(jalan1) # output: sudirman
print(jalan2) # output: thamrin 
print(jalan3) # output: ['sm amin', 'bangau', 'kubang']  (karena menggunakan *) 

# 4. loop tuples
warna = ("merah", "kuning", "hijau")
for x in warna:
    print(x)

# 5. join tuples
orang = ("andi", "caca", "budi", "diana")
angka = (4, 5, 2, 3)
gabung = orang + angka
print(gabung) # output: ('andi', 'caca', 'budi', 'diana', 4, 5, 2, 3)   
orang_baru = orang * 2
print(orang_baru) # output: ('andi', 'caca', 'budi', 'diana', 'andi', 'caca', 'budi', 'diana')