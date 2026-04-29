def hitung_komisi(total_penjualan, skema, index=0):
    if (total_penjualan >= skema[index][0]
            or index >= len(skema) - 1):
        return skema[index][1]
    else:
        return hitung_komisi(total_penjualan, skema, index + 1)

def main():
    skema_komisi = (
    100000000, 10, # penjualan >= 100 jt -> komisi 10%
    50000000, 5, # penjualan >= 50 jt -> komisi 5 %
    20000000, 2, # penjualan >= 20 jt -> komisi 2 %
    0, 0 # di bawah 20 jt -> tidak ada komisi
)
    
    nama_sales = input("Masukkan nama sales: ")
    total_penjualan = int(input("Masukkan total penjualan: "))
    komisi = hitung_komisi(total_penjualan, skema_komisi, 0)
    print(f"Nama Sales: {nama_sales}")
    print(f"Komisi    : {total_penjualan * (komisi / 100)}")


if __name__ == "__main__":
    main()