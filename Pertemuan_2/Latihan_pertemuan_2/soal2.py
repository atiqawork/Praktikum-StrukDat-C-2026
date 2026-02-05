barang = ("B001", "Laptop Gaming", 15000000)
print(barang[2])

# harga = 14000000
# harga tidak dapat diubah karen merupakan tuple dan tuple tidak dapat diubah
# jika ingin tetap diubah, ubah jadi list terlebih dahulu

(kode, nama_barang, harga) = barang
print("harga barang tetap adalah ", harga)
