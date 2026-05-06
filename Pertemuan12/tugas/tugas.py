class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class Binarysearch_Tree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)
        if self.root is None:
            self.root = new_node
            print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}')
            return
        
        current = self.root
        ditambahkan = False
        while not ditambahkan:
            if id_buku < current.id_buku:
                if current.left is None:
                    current.left = new_node
                    ditambahkan = True
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    ditambahkan = True
                else:
                    current = current.right
        print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}')

    def search(self, id_buku):
        current = self.root
        while current:
            if id_buku == current.id_buku:
                return current
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        return None
    
    def traversal_inorder(self):
        hasil = []
        
        def inorder_help(node):
            if node:
                inorder_help(node.left)
                hasil.append((node.id_buku, node.judul))
                inorder_help(node.right)
        
        inorder_help(self.root)
        return hasil
    
    def get_min(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current
    
    def get_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current
    
    def height(self):
        def height_help(node):
            if not node:
                return -1
            left_height = height_help(node.left)
            right_height = height_help(node.right)
            return 1 + max(left_height, right_height)
        return height_help(self.root)
    
def main():
    print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
    print('=========================================\n')

    katalog= Binarysearch_Tree()
    buku = [
        (50, 'Dasar Pemrograman'),
        (30, 'Struktur Data'),
        (70, 'Kecerdasan Buatan'),
        (20, 'Matematika Diskrit'),
        (40, 'Basis Data'),
        (60, 'Jaringan Komputer'),
        (80, 'Sistem Operasi')
    ]
    for id_buku, judul in buku:
        katalog.insert(id_buku, judul)
    print()

    print('[INFO] Koleksi Buku (In-Order Traversal):')
    buku_sorted = katalog.traversal_inorder()
    for i, (id_buku, judul) in enumerate(buku_sorted, 1):
        print(f'{i}. {id_buku} - {judul}')
    print()

    print('[SEARCH] Mencari ID 60...', end='')
    ditemukan = katalog.search(60)
    if ditemukan:
        print(f'Ditemukan! Judul: {ditemukan.judul}')
    else:
        print(f'Data tidak ditemukan')

    print('[SEARCH] Mencari ID 100...', end='')
    ditemukan = katalog.search(100)
    if ditemukan:
        print(f'Ditemukan! Judul: {ditemukan.judul}')
    else:
        print(f'Data tidak ditemukan')
    print()

    min_node = katalog.get_min()
    max_node = katalog.get_max()
    print(f'[STATISTIK] ID Terkecil: {min_node.id_buku}')
    print(f'[STATISTIK] ID Terbesar: {max_node.id_buku}')

    print(f'[INFO] Tinggi (Height) Tree: {katalog.height()}')

    print('\n============================================')
    print('Simulasi Selesai!')


if __name__ == '__main__':
    main()