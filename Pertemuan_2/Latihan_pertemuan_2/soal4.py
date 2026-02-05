nilai_siswa = { 
    "S01": {"nama": "Dina", "tugas": 80, "uts": 75, "uas": 85},
    "S02": {"nama": "Abdul Harris", "tugas": 90, "uts": 88, "uas": 92},
    "S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}

# tambah data siswa baru "S04" dengan nama "Fafa", nilai tugas 85, uts 80, uas 90
nilai_siswa ["S04"] = {
    "nama": "Fafa",
    "tugas": 85,
    "uts": 80,
    "uas": 90 
}
print(nilai_siswa)

# hitung nilai akhir setiap siswa dengan bobot tugas 20% + uts 30% + uas 50%
print("Nilai akhir siswa: ")
for x in nilai_siswa.values():
    nilai_akhir = (x["tugas"] * 0.2) + (x["uts"] * 0.3) + (x["uas"] * 0.5)
    print(f"{x["nama"]}: {nilai_akhir}")

# tampilkan nama siswa yang nilai uas di atas 80
print("Siswa dengan nilai uas di atas 90 adalah sebagai berikut: ")
for x in nilai_siswa.values():
    if x["uas"] > 80:
        print(x["nama"])