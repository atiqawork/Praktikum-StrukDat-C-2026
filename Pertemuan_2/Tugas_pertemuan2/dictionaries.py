# dictionaries = dapat diubah, menyimpan pasangan key:value
inidict = {
    "nama": "budi",
    "umur": 20,
    "hobi": ["makan", "tidur", "main"],
    "umur": 21 # tidak bisa duplikat key, yang terakhir yang diambil
}
# bisa juga dengan dict()

# 1. access dictionary items
baru = inidict["umur"] # mengakses item dengan key "umur"
print(baru) # output: 21
# bisa juga menggunakan get()
key = inidict.keys() # mendapatkan semua key dalam dictionary
print(key) # output: dict_keys(['nama', 'umur', 'hobi'])
values = inidict.values() # mendapatkan semua value dalam dictionary
print(values) # output: dict_values(['budi', 21, ['makan', 'tidur', 'main'], 'pekanbaru'])

# 2. change dictionary items
inidict["nama"] = "anton" # mengubah value dari key "nama"
print(inidict)

# 3. add dictionary items
inidict["asal"] = "pekanbaru" # menambah item baru dengan key "asal"
print(inidict)

# 4. remove dictionary items
inidict.pop("hobi") # menghapus item dengan key "hobi"
print(inidict)
# jika hanya .pop() maka item terakhir yang dihapus
# bisa juga menggunakan del dan clear()

# 5. loop dictionaries
for x in inidict:
    print(x) # output hanya keys. bisa juga menggunakan inidict.keys()
for x in inidict:
    print(inidict[x]) # output hanya values. bisa juga menggunakan inidict.values()
for x, y in inidict.items():
    print(x, y) # output key dan value secara bersamaan

# 6. copy dictionaries
dict_baru = inidict.copy()
print(dict_baru)
# bisa juga menggunakan dict_baru = dict(inidict)

# 7. nested dictionaries => dictionary yang didalamnya banyak dictionary lain
ortu = {
    "ayah": {
        "nama": "soekarno",
        "umur": 50,
        "pekerjaan": "presiden"
    },
    "ibu": {
        "nama": "fatmawati",
        "umur": 45,
        "pekerjaan": "irt"
    }
}
print(ortu["ayah"]["nama"]) # akses dict di dalam dict, output:soekarno
