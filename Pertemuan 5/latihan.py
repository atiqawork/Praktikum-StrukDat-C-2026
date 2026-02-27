# nomor 1
stok_barang = [15, 40, 30, 10, 25]
stok_barang[3] = 50
print(stok_barang)
stok_barang.append(5)
print(stok_barang)
stok_barang.sort(reverse=True)
print(stok_barang)
jumlah = sum(stok_barang)
print(jumlah)
rata = jumlah/len(stok_barang)
print("Rata rata adalah: ", rata)
status = "Stok Aman" if rata > 20 else "Waspada"

# nomor 2
data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for nama, poin in data_aktivitas:
    if poin > 80:
        print (f"{nama} mendapat gold")
    elif 50 <= poin <= 80:
        print(f"{nama} mendapat silver")
    else:
        print(f"{nama} mendapat bronze")


# nomor 3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
coding_saja = ukm_coding - ukm_robotik
print("Mahasiswa di ukm coding saja ", coding_saja)
unik = ukm_coding | ukm_robotik
print("Mahasiswa unik di kedua ukm ", unik)
for x in ukm_coding:
    print(x)
print("Andi" in ukm_coding) 

# nomor 4
gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 12},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20}
]
# inidict["asal"] = "pekanbaru" # menambah item baru dengan key "asal"
gudang_pc[1]["kategori"] = "Aksesoris"
print(gudang_pc)
gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 8})
for x in range(len(gudang_pc)):
    print(f"item: {gudang_pc[x]["item"]} total aset: {gudang_pc[x]["harga"]*gudang_pc[x]["stok"]}")