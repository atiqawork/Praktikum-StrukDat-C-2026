class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        total = sum(ord(char) for char in key)  # hitung jumlah nilai unicode dari karakter dalam kode buku
        return total % self.size    # rumus hash: total unicode mod ukuran hash
    
    def insert(self, kode, judul):
        index = self.hash_function(kode)    # hitung index menggunakan fungsi hash
        bucket = self.table[index]      # ambil bucket yang sesuai dengan index
        for item in bucket:     # periksa apakah kode sudah ada di bucket
            if item[0] == kode:
                item[1] = judul  # update judul jika kode sudah ada
                print(f'Data dengan kode {kode} berhasil di-update')
                return
        bucket.append([kode, judul])    # nambahin kode dan judul ke bucket 
        print(f'Data dengan kode {kode} berhasil ditambahkan')

    def search(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for item in bucket:     
            if item[0] == kode:
                print(f'{kode} : {item[1]}')
                return item[1]
        print(f'Buku tidak ditemukan')
        return None
    
    def delete(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for i, item in enumerate(bucket):   # periksa setiap item di bucket untuk menemukan kode yang cocok, enumerate untuk mendapatkan indeks item
            if item[0] == kode:
                del bucket[i]
                print(f'Data dengan kode {kode} berhasil dihapus')
                return
        print(f'Buku tidak ditemukan')

    def display(self):
        print('===============================')
        print('ISI HASH TABLE')
        print('===============================')

        for i, bucket in enumerate(self.table):
            print(f'Bucket {i}:', end=' ')  
            if not bucket:
                print('Kosong')
            else:
                for item in bucket:
                    print(f'[{item[0]} : {item[1]}]', end=' ')
                print()


perpus = HashTable()

perpus.insert('BK111', 'Mahir C++ Dalam Satu Jam')
perpus.insert('BK222', 'Python Dasar')
perpus.insert('BK333', 'Matematika Diskrit')
perpus.insert('BK444', 'Atomic Habits')
perpus.insert('BK555', 'Sepuluh Dosa Besar Soeharto')
print('\n[DISPLAY]')
perpus.display()

print('')
perpus.insert('BK045', 'Mein Kampf')
perpus.insert('BK111', 'Bumi Manusia')
print('\n[DISPLAY UPDATE]')
perpus.display()

print('\n[SEARCH] Mencari Buku Berdasarkan Kode')
perpus.search('BK444')
perpus.search('BK201')

print('\n[DELETE] Menghapus Buku Berdasarkan Kode')
perpus.delete('BK555')

print('\n[DISPLAY UPDATE]')
perpus.display()