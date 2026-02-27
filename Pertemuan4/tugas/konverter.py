# method/fungsi konversi IDR ke mata uang lain pada kurs.py

from kurs import mata_uang

def idr_ke_lain(jumlah_rupiah, kode):
    return jumlah_rupiah / mata_uang[kode]
def asing_ke_idr(jumlah_asing, kode):
    return jumlah_asing * mata_uang[kode]