# circular linked list

# === Antrean Giliran Petugas Valet--Rotasi Melingkar ===
# buat struktur node CircularLinkedList di mana pointer next dari node terakhir menunjuk kembali ke head
# buat fungsi tambah_petugas(nama) untuk nambah petugas ke dalam list melingkar
# buat fungsi giliran_berikutnya(n) yang mensimulasikan n kali giliran dan mencetak nama petugas yang bertugas setiap gilirannya

class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_petugas(self, nama):
        new_node = Node(nama)

        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head # buat circular
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # buat tetap circular

    def giliran_berikutnya(self, n):
        if self.head is None:
            print('Tidak ada petugas dalam daftar')
            return

        current = self.head
        for i in range(1, n+1):
            print(f'Giliran {i}: {current.nama}')
            current = current.next

# Contoh Penggunaan Soal 3
print("=== Antrean Giliran Petugas Valet ===")
cll = CircularLinkedList()
cll.tambah_petugas('Andi')
cll.tambah_petugas('Budi')
cll.tambah_petugas('Citra')
cll.tambah_petugas('Dewi')
cll.giliran_berikutnya(6)   # Simulasi 6 giliran petugas
