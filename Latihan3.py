# LATIHAN 3
def matakuliah():
    jumlah = 0
    nilai = {"A": 4, "B": 3, "C": 2, "D": 1}
    sks = 3

    matkul = int(input("Masukan Jumlah Mata kuliah: "))

    for i in range(matkul):
        while True:
            nilai_matkul = input("Nilai MK {}: ".format(i + 1))
            if nilai_matkul in nilai:
                jumlah = jumlah + nilai[nilai_matkul] * sks
                break
            else:
                print("nilai tidak valid")
                break
        
    if jumlah > 0:
        rata_rata = jumlah / (matkul * sks)
        print("Nilai IPS anda sementara ini adalah:", round(rata_rata, 2))
    else:
        print("Kesalahan")
    
matakuliah()

