# dengan __init__
class Murid:
    def __init__(self, nama, umur, kelas):
        self.nama = nama
        self.umur = umur
        self.kelas = kelas

p1 = Murid("Angel", "7 tahun", "1 B")
print(p1.nama, "umur", p1.umur, "kelas", p1.kelas)

# without __init__
class Siswa:
    pass
q1 = Siswa()
q1.name = "Hanifah"
q1.age = "7 tahun"
print(q1.name, q1.age) 