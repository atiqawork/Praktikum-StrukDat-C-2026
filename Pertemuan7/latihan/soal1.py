plat_mobil = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

plat_ganjil = [] 
plat_genap = [] 

for plat in plat_mobil:
    bagian = plat.split()
    angka_string = bagian[1]  
    angka_terakhir = int(angka_string[-1])  
    
    if angka_terakhir % 2 == 0:
        plat_genap.append(plat)
    else:
        plat_ganjil.append(plat)
        
print("Plat dengan angka terakhir GENAP:", plat_genap)
print("Plat dengan angka terakhir GANJIL:", plat_ganjil)