stok = [15, 50, 30, 25, 40]
# tambahkan stok baru sebesar 100 ke akhir list
stok.append(100)
# sisipkan angka 75 di posisi indeks ke-2
stok.insert(2, 75)
# urutkan list tersebut dari yang terbesar ke terkecil
stok.sort(reverse = True)
print(stok)
# hitung rata rata dari seluruh stok
rata = (15 + 25 + 30 + 40 + 50 + 75 + 100) / 7
print("List stok berisi ", stok, "dengan rata rata ", rata)