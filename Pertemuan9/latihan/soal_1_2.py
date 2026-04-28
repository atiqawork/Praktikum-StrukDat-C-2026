# double linked list

# === Parkir Dua Arah--Penelusuran maju & mundur ===
# buat struktur node dan double linked list dengan pointer next dan prev
# buat fungsi tambah_kendaraan(plat) untuk nambah kendaraan ke akhir list
# buat fungsi tampilkan_maju() untuk cetak semua kendaraan dari head ke tail
# buat fungsi tampilkan_mundur() untuk cetak semua kendaraan dari tail ke head

class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def tambah_kendaraan(self, plat):   # fungsi untuk menambah kendaraan ke akhir list
        new_node = Node(plat)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def tampilkan_maju(self):   # fungsi untuk cetak semua kendaraan dari head ke tail
        current = self.head
        while current:
            print(current.plat)
            current = current.next

    def tampilkan_mundur(self):     # fungsi untuk cetak semua kendaraan dari tail ke head
        current = self.tail
        while current:
            print(current.plat)
            current = current.prev
    

# === Hapus Kendaraan dari Tengah--Update Dua Arah ===
# gunakan struktur Double Linked List dari soal sebelumnya
# buat fungsi hapus_kendaraan(plat) yang mencari node berdasarkan plat lalu menghapusnya dengan memperbarui pointer next dan prev dari node tetangga
# Tampilkan list sebelum dan sesudah penghapusan menggunakan tampilkan_maju()
    def hapus_kendaraan(self, plat):
        current = self.head
        while current:
            if current.plat == plat:

                if current.prev and current.next:   # jika node di tengah
                    current.prev.next = current.next
                    current.next.prev = current.prev

                elif current.prev is None:  # jika node adalah head
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                elif current.next is None:  # jika node adalah tail
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                return
            current = current.next

# Contoh Penggunaan Soal 1
print('=== Parkir Dua Arah ===')
dll = DoublyLinkedList()
dll.tambah_kendaraan('B 1234 ABC')
dll.tambah_kendaraan('D 5678 XYZ')
dll.tambah_kendaraan('A 9999 TUV')
dll.tambah_kendaraan('F 1111 DEF')
print('[MAJU]')
dll.tampilkan_maju()
print('\n[MUNDUR]')
dll.tampilkan_mundur()

# Contoh Penggunaan Soal 2
print('\n=== Hapus Kendaraan dari Tengah ===')
dll = DoublyLinkedList()
dll.tambah_kendaraan('B 1111 AA')
dll.tambah_kendaraan('D 2222 BB')
dll.tambah_kendaraan('A 3333 CC')
dll.tambah_kendaraan('B 4444 DD')
print('[SEBELUM HAPUS]')
dll.tampilkan_maju()
dll.hapus_kendaraan('A 3333 CC')
print('\n[SESUDAH HAPUS]')
dll.tampilkan_maju()