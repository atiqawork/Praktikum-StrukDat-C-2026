# buat sebuah class, minimal 3 atribut/properti, 2 method
# 3 object lalu ubah salah satu atribut dari object tersebut

class JadwalBus:
    def __init__(self, nomor_bus, rute, waktu_berangkat):
        self.nomor_bus = nomor_bus
        self.rute = rute
        self.waktu_berangkat = waktu_berangkat

    def tampilkan_info(self):
        return f"Bus Nomor: {self.nomor_bus}, Rute: {self.rute}, Waktu Berangkat: {self.waktu_berangkat}"
    
    def ubah_waktu_berangkat(self, waktu_baru):
        self.waktu_baru = waktu_baru

    def waktu_berangkat_baru(self):
        return f"Bus Nomor: {self.nomor_bus}, Rute: {self.rute}, Waktu Berangkat Baru: {self.waktu_baru}"

p1 = JadwalBus("B001", "Marpoyan-Sudirman", "08:00")
print(p1.tampilkan_info())
p1.ubah_waktu_berangkat("09:00")
print(p1.waktu_berangkat_baru())

print("==========")

p2 = JadwalBus("B002", "Panam-Harapan Raya", "09:30")
print(p2.tampilkan_info())  
p2.ubah_waktu_berangkat("10:00")
print(p2.waktu_berangkat_baru())

print("==========")

p3 = JadwalBus("B003", "Tampan-Bukit Duri", "10:15")
print(p3.tampilkan_info())
p3.ubah_waktu_berangkat("11:00")
print(p3.waktu_berangkat_baru())