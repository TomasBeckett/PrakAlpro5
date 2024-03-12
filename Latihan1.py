# LATIHAN 1
def perkalian(angka1, angka2):
    total = 0
    penjumlahan_str = ""

    for i in range(angka1):
        total += angka2
        if i < angka1 - 1:
            penjumlahan_str += str(angka2) + " + "
        else:
            penjumlahan_str += str(angka2)

    print(str(angka1) + " x " + str(angka2) + " = " + penjumlahan_str + " = " + str(total))

perkalian(6, 5)  
perkalian(7, 10) 

