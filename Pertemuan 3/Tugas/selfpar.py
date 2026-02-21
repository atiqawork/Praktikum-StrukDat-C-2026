class Greetings:
    def __init__(self, nama, asal, pekerjaan):
        self.nama = nama
        self.asal = asal
        self.pekerjaan = pekerjaan
    def sapa(self):
        print("Haiiii nama aku", self.nama, "\naku asal", self.asal, "\naku bekerja sebagai", self.pekerjaan)

p1 = Greetings("Joko", "Solo", "Tukang Kayu")
p1.sapa()

# nggak harus 'self'
class Tebak:
    def __init__(hachu, hari, bulan):
        hachu.hari = hari
        hachu.bulan = bulan
    def greet(hachu):
        print("Hari ini adalah hari", hachu.hari, "pada bulan", hachu.bulan)

q1 = Tebak("Selasa", "Maret")
q1.greet()

# access properties with self
class Buku:
    def __init__(self, judul, penulis, tahun_terbit, penerbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit
    def info_buku(self):
        print(f"{self.judul} {self.penulis} {self.tahun_terbit} {self.penerbit}")

buku1 = Buku("Laut Bercerita", "Leila Chudori", 2017, "KPG")
buku2 = Buku("Strange House", "Uketsu", 2023, "HarperVia")
buku1.info_buku()
buku2.info_buku()

# panggil method with self
class Orang:
    def __init__(self, name):
        self.name = name
    def hoii(self):
        return "HOII " + self.name
    def selamat(self):
        pesan_sapa = self.hoii()
        print(pesan_sapa + "! Selamat datang siapapun itu")

x1 = Orang("Jack")
x1.selamat()