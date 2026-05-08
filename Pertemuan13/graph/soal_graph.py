class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_kota(self, nama):
        if nama not in self.graph:
            self.graph[nama] = []

    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)     # u = kota asal
        self.tambah_kota(v)     # v = kota tujuan
        self.graph[u].append((v, jarak))    # nambahin kota tujuan dan jarak ke kota asal
        self.graph[v].append((u, jarak))    # nambahin kota asal dan jarak ke kota tujuan (karna jalan dua arah)
        print(f'[INPUT] Menambahkan jalan: {u} - {v} ({jarak} km)')

    def tampilkan_graph(self):
        print('\n[INFO] Struktur Jaringan Distribusi:')
        
        for kota in self.graph:
            print(f'- {kota} terhubung ke:', end=' ')
            
            tetangga = []   # tetangga untuk menyimpan kota tujuan dan jarak
            
            for tujuan, jarak in self.graph[kota]:
                tetangga.append(f'{tujuan} ({jarak} km)')   # nambahin kota tujuan dan jarak ke list tetangga
            print(', '.join(tetangga))  # gabungin semua tetangga

    def dijkstra(self, kota_asal):
        jarak = {}  # jarak untuk menyimpan jarak terpendek dari kota asal ke setiap kota lainnya
        for kota in self.graph:
            jarak[kota] = float('inf')      # inisialisasi jarak dengan tak hingga (infinity)
        jarak[kota_asal] = 0    # jarak dari kota asal ke dirinya sendiri adalah 0
        dikunjungi = []     # nyimpan kota yang sudah dikunjungi selama proses dijkstra
        while len(dikunjungi) < len(self.graph):    # periksa selama masih ada kota yang belum dikunjungi
            current_kota = None     # current_kota untuk nyimpan kota dengan jarak terpendek yang belum dikunjungi
            current_jarak = float('inf')    # current_jarak untuk nyimpan jarak terpendek yang ditemukan selama iterasi, diinisialisasi dengan tak hingga

            for kota in self.graph:     # cek setiap kota dalam graph      
                if kota not in dikunjungi and jarak[kota] < current_jarak:  # kalau kota belum dikunjungi dan jaraknya lebih kecil dari jarak terpendek saat ini
                    current_jarak = jarak[kota]   # update jarak terpendek
                    current_kota = kota     # kota yang sedang diperiksa menjadi kota dengan jarak terpendek saat ini (update kota terpendek)
            if current_kota is None:    # kalau kota dah habis, maka keluar dari loop
                break

            dikunjungi.append(current_kota)     # nambahin kota yang sedang diperiksa ke daftar kota yang sudah dikunjungi
            for tetangga, bobot in self.graph[current_kota]:   # cek setiap tetangga dari kota yang sedang diperiksa, tetangga => kota tujuan, bobot => jarak ke kota tujuan
                jarak_baru = jarak[current_kota] + bobot    # hitung jarak baru ke tetangga melalui kota yang sedang diperiksa
                if jarak_baru < jarak[tetangga]:    # kalo jarak baru lebih kecil dari jarak tetangga, update jarak ke tetangga
                    jarak[tetangga] = jarak_baru
        print(f'\n[HASIL] Jarak Terpendek dari {kota_asal}:')

        nomor = 1
        for kota, total_jarak in jarak.items():     # nampilin jarak terpendek ke setiap kota dari kota asal
            if kota != kota_asal:       # kalau kota bukan kota asal, tampilkan jarak ke kota tersebut
                print(f'{nomor}. Ke {kota}: {total_jarak} km')
                nomor += 1


print('SISTEM NAVIGASI LOGISTIK "KILAT MAJU"')
print('=========================================')

p1 = Graph()

p1.tambah_jalan('Jakarta', 'Bandung', 150)
p1.tambah_jalan('Jakarta', 'Cirebon', 200)
p1.tambah_jalan('Bandung', 'Tasikmalaya', 100)
p1.tambah_jalan('Bandung', 'Cirebon', 130)
p1.tambah_jalan('Cirebon', 'Semarang', 250)
p1.tambah_jalan('Tasikmalaya', 'Semarang', 200)
p1.tampilkan_graph()

print('\n[PROSES] Menghitung Rute Terpendek Dari: Jakarta...')
p1.dijkstra('Jakarta')

print('==========================================')
print('Simulasi Navigasi Selesai!')