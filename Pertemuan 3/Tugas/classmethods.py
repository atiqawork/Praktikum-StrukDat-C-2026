class Pekerjaan:
    def __init__(self, nama, kerja):
        self.nama = nama
        self.kerja = kerja
    def sapa(self):
        print("Halo, nama saya", self.nama, "saya bekerja untuk", self.kerja)
    def get_info(self):
        return f"{self.nama} is {self.kerja}"
p1 = Pekerjaan("Endut", "memberi makan")
p1.sapa()
print(p1.get_info()) # methods accessing properties

# methods with parameters
class Perhitungan:
    def kali(self, a, b):
        return a * b
    def pangkat(self, a, b):
        return a ** b
    def bagi(self, a, b):
        return a / b
hitung = Perhitungan()
print("Hasil perkalian 8 x 8 adalah", hitung.kali(8, 8))
print("8 pangkat 8 hasilnya adalah", hitung.pangkat(8, 8))
print("Hasil pembagian 8 dibagi 8 adalah", hitung.bagi(8, 8))

# methods modifying properties
class Umur:
    def __init__(self, name, umur_before):
        self.name = name
        self.umur_before = umur_before
    def umur_baru(self):
        self.umur_before += 1
        print(f"Selamat berganti umurr!! Kamu sekarang berumur {self.umur_before}")
x1 = Umur("Jennifer", 24)
x1.umur_baru()

# multiple methods
class PinjamBuku:
    def __init__(self, namaa):
        self.namaa = namaa # nama list keranjang
        self.pinjam = [] # keranjang (dalam bentuk struktur data list) kosong yang menampung semua method yang akan dilakukan
    def tambah_pinjaman(self, buku):    # method untuk menambahkan  buku
        self.pinjam.append(buku)    # buku bertambah ke dalam keranjang
        print(f"Menambahkan {buku} ke dalam keranjang")
    def hapus_buku(self, buku):      # method untuk menghapus buku dalam keranjang
        if buku in self.pinjam:     # jika keranjang tambah buku berisi, maka lakukan penghapusan pada isi keranjang tersebut 
            self.pinjam.remove(buku)
            print(f"{buku} dihapus")
    def tampilkan_buku(self):      # method untuk menampilkan isi keranjang buku
        print(f"List buku '{self.namaa}' sebagai berikut: ")
        for buku in self.pinjam:    # untuk setiap buku pada keranjang, tampilkan di layar
            print(f"{buku}")
listbuku = PinjamBuku("Wishlist ku")
listbuku.tambah_pinjaman("Pulang")
listbuku.tambah_pinjaman("1984")
listbuku.tambah_pinjaman("Animal Farm")
listbuku.hapus_buku("1984")
listbuku.tampilkan_buku()
# delete methods => gunakan 'del' 