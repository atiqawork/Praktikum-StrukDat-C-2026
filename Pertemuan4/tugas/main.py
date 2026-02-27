from kurs import mata_uang
from konverter import idr_ke_lain, asing_ke_idr
from tabulate import tabulate

def tampilan():
    print("\n========================")
    print("   KONVENTER MATA UANG")
    print("========================\n")

    data = [[kode, f"{nilai:,.0f}"] for kode, nilai in mata_uang.items()]
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    tampilan()

    arah_convert = input("Apakah ingin melakukan konversi dari IDR? (y/n): ").lower()
    if arah_convert == "y":
        try:
            jumlah_rupiah = float(input("Masukkan jumlah dalam IDR: "))
        except ValueError:
            print("Input harus berbentuk angka!")
            return
        
        kode = input("Masukkan kode mata uang yang ingin di-convert (USD/EUR/SGD/JPY/MYR/SAR): ").upper()
        if kode not in mata_uang:
            print("Kode mata uang tidak tersedia...")
            return
        
        hasil = idr_ke_lain(jumlah_rupiah, kode)
        print(f"Hasil Konversi dari IDR ke {kode} adalah {hasil:.2f} {kode}")

    else:
        try:
            jumlah_asing = float(input("Masukkan jumlah mata uang asing: "))
        except ValueError:
            print("Input harus berbentuk angka!")
            return
        
        kode = input("Masukkan kode mata uang asal (USD/EUR/SGD/JPY/MYR/SAR): ").upper()
        if kode not in mata_uang:
            print("Kode mata uang tidak tersedia...")
            return
        
        hasil = asing_ke_idr(jumlah_asing, kode)
        print(f"Hasil Konversi {kode} ke IDR adalah Rp {hasil:.2f}")

if __name__ == "__main__":
    main()