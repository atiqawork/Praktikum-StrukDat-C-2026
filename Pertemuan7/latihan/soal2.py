class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None

class Antrean:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def tambah(self, plat):
        baru = Node(plat)
        if self.head is None:
            self.head = baru
            self.tail = baru
        else:
            self.tail.next = baru
            self.tail = baru
        print(f"{plat} masuk")
    
    def hapus(self, plat):
        now = self.head
        prev = None
        
        while now:
            if now.plat == plat:
                if prev is None:
                    self.head = now.next
                else:
                    prev.next = now.next
                print(f"{plat} dihapus (mogok)")
                return
            prev = now
            now = now.next
        print(f"{plat} tidak ditemukan")
    
    def tampil(self):
        print("\nAntrean:", end=" ")
        now = self.head
        while now:
            print(f"[{now.plat}]", end=" -> ")
            now = now.next
        print("Kosong")

antrean = Antrean()

antrean.tambah("B 1234 ABC")
antrean.tambah("D 8888 XYZ")
antrean.tambah("A 111 TUV")

antrean.tampil()
antrean.hapus("D 8888 XYZ")
antrean.tampil()

