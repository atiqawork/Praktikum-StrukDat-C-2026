class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None

class AntreanKendaraan:
    def __init__(self):
        self.head = None

    def tambah_belakang(self, plat):
        node_baru = Node(plat)

        if self.head is None:
            self.head = node_baru
            return

        sekarang = self.head
        while sekarang.next:
            sekarang = sekarang.next

        sekarang.next = node_baru

    def sisipkan_vip(self, plat_baru, plat_target):
        sekarang = self.head

        while sekarang:
            if sekarang.plat == plat_target:
                node_baru = Node(plat_baru)

                node_baru.next = sekarang.next
                sekarang.next = node_baru

                print("Kendaraan VIP berhasil disisipkan.")
                return

            sekarang = sekarang.next

        print("Plat target tidak ditemukan.")

    def tampilkan_antrean(self):
        sekarang = self.head

        if sekarang is None:
            print("Antrean kosong")
            return

        print("Antrean kendaraan:")
        while sekarang:
            print(sekarang.plat, end=" -> ")
            sekarang = sekarang.next
        print("None")


antrean = AntreanKendaraan()

antrean.tambah_belakang("B1234AA")
antrean.tambah_belakang("B5678BB")
antrean.tambah_belakang("B9999CC")
antrean.tampilkan_antrean()

antrean.sisipkan_vip("VIP777", "B5678BB")
antrean.tampilkan_antrean()