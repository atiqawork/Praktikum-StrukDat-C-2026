class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, nama, keluhan):
        data = (nama, keluhan)
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.count += 1
        print(f'[DAFTAR] {nama} terdaftar dengan keluhan {keluhan} (No. Antrian: {self.count})')

    def dequeue(self):
        if self.is_empty():
            return 'Antrian Kosong! Tidak ada data untuk dihapus'
        temp_data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        self.count -= 1
        nama, keluhan = temp_data
        print(f'[PANGGIL] Dokter memanggil: {nama} (keluhan: {keluhan})')
        return temp_data
    
    def peek(self):
        if self.is_empty():
            return 'Antrian Kosong'
        nama, keluhan = self.front.data
        print(f'[PEEK] Pasien berikutnya: {nama}--{keluhan}')
        return self.front.data

    def size(self):
        return self.count
    
    def clear(self):
        self.front = None
        self.rear = None
        self.count = 0
        print(f'[CLEAR] Sesi Poliklinik selesai. Antrian dikosongkan')

    def tampilkan(self):
        if self.is_empty():
            print(f'[ANTRIAN KOSONG]')
            return
        print(f'[ANTRIAN SAAT INI]')
        current = self.front
        i = 1
        while current:
            nama, keluhan = current.data
            print(f'{i}. {nama} -> {keluhan}')
            current = current.next
            i += 1

print('======================================')
print('SISTEM ANTRIAN POLI UMUM')
print('RS Sehat Bersama')
print('======================================\n')

p1 = QueueLinkedList()
print('[CEK] Apakah antrian kosong? -> ', 'YA, Antrian masih kosong' if p1.is_empty() else 'TIDAK')

p1.enqueue('BUDI', 'Demam Tinggi')
p1.enqueue('ANI', 'Batuk Pilek')
p1.enqueue('Citra', 'Sakit Kepala')

print(f'[INFO] Jumlah Pasien Menunggu: {p1.size()} orang')

p1.peek()
print()
p1.dequeue()

p1.enqueue('DODI', 'Nyeri Perut')
print()
p1.tampilkan()
p1.dequeue()

print('[CEK] Apakah Antrian Kosong ->', 'YA Antrian masih kosong' if p1.is_empty() else 'TIDAK')

print('\n======================================')
print('SIMULASI SELESAI')
print('======================================')