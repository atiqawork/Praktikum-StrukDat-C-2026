pengunjung_hari_ini = [
    {"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi", "kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
    {"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi", "kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
    {"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains", "kembali": False},
    {"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum", "kembali": False},
]


# Soal 1
def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama   | Usia | Kategori | Status Kembali")
    print("---+------+--------+------+----------+---------------")

    for i, p in enumerate(pengunjung_hari_ini, start=1):
        status = "Sudah Kembali" if p["kembali"] else "Belum Kembali"
        print(f"{i:<2} | {p['id']} | {p['nama']:<6} | {p['usia']:<4} | {p['kategori']:<8} | {status}")

def filter_belum_kembali():
    belum = [p["nama"] for p in pengunjung_hari_ini if not p["kembali"]]
    belum.sort()

    print("\n===== PENGUNJUNG BELUM KEMBALI =====")
    for i, nama in enumerate(belum, start=1):
        print(f"{i}. {nama}")

    print(f"Total belum kembali: {len(belum)} pengunjung")


# Soal 2
def info_perpustakaan():
    info = (
        "Perpustakaan Kampus Terpadu",
        "Jl. Pendidikan No. 5, Pekanbaru",
        "0761-54321"
    )

    print("\nInfo Perpustakaan:")
    print("Nama   :", info[0])
    print("Alamat :", info[1])
    print("Telp   :", info[2])

def rekap_kategori():
    kategori_unik = {p["kategori"] for p in pengunjung_hari_ini}
    print("\nKategori Buku Unik:", kategori_unik)
    print("Jumlah kategori:", len(kategori_unik))

    rekap = {}
    for p in pengunjung_hari_ini:
        kat = p["kategori"]
        rekap[kat] = rekap.get(kat, 0) + 1

    print("\nRekap per kategori:")
    for k, v in rekap.items():
        print(f"{k:<6}: {v} pengunjung")

    max_val = max(rekap.values())
    terbanyak = [k for k, v in rekap.items() if v == max_val]

    print("\nKategori terbanyak:", ", ".join(terbanyak), f"({max_val} pengunjung)")


# Soal 3
class Pengunjung:
    total = 0

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.total += 1

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_kategori(self):
        return self.__kategori

    def tampilkan_info(self):
        print("ID       :", self.__id)
        print("Nama     :", self.__nama)
        print("Kategori :", self.__kategori)

    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.total


class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Prioritas :", self.prioritas)
        if self.prioritas == "Mendesak":
            print("** Layani segera! **")


# Soal 4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AntrianPeminjaman:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def tampilkan(self):
        print("\n===== ANTRIAN PEMINJAMAN =====")
        temp = self.head
        i = 1
        while temp:
            d = temp.data
            print(f"[{i}] {d['id']} - {d['nama']} | {d['kategori']}")
            temp = temp.next
            i += 1
        print("Total antrian:", self.hitung())

    def panggil_berikutnya(self):
        if not self.head:
            print("Antrian kosong")
            return

        print("\nMemanggil pengunjung berikutnya...")
        d = self.head.data
        print(f"Silakan masuk: {d['nama']} ({d['id']}) - {d['kategori']}")
        self.head = self.head.next

    def cari(self, nama):
        print(f"\nMencari '{nama}'...")
        temp = self.head
        i = 1
        while temp:
            if temp.data["nama"] == nama:
                d = temp.data
                print(f"Ditemukan: {d['id']} - {d['nama']} | {d['kategori']} (posisi ke-{i})")
                return
            temp = temp.next
            i += 1
        print("Tidak ditemukan")

    def hapus_berdasarkan_id(self, id):
        print(f"\nMenghapus pengunjung dengan ID {id}...")

        if not self.head:
            print("Antrian kosong")
            return

        if self.head.data["id"] == id:
            print(f"{self.head.data['nama']} ({id}) berhasil dihapus.")
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data["id"] == id:
                print(f"{curr.data['nama']} ({id}) berhasil dihapus.")
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print("ID tidak ditemukan")

    def hitung(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


# Main Program
if __name__ == "__main__":
    tampilkan_pengunjung()
    filter_belum_kembali()

    info_perpustakaan()
    rekap_kategori()

    print("\n===== OOP =====")
    p1 = Pengunjung("M001", "Rina", "Fiksi")
    p1.tampilkan_info()

    print()
    p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")
    p2.tampilkan_info()
    print("\nTotal pengunjung terdaftar:", Pengunjung.hitung_pengunjung())

    antrian = AntrianPeminjaman()
    antrian.tambah({"id": "M001", "nama": "Rina", "kategori": "Fiksi"})
    antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"})
    antrian.tambah({"id": "M003", "nama": "Siti", "kategori": "Fiksi"})
    antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"})

    antrian.tampilkan()
    antrian.panggil_berikutnya()
    antrian.tampilkan()
    antrian.hapus_berdasarkan_id("M003")
    antrian.tampilkan()
    antrian.cari("Taufik")
    print("\nTotal antrian:", antrian.hitung())