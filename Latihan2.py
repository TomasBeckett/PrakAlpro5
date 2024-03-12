# LATIHAN 2
def ganjil(bawah, atas):
    a = bawah
    b = atas
    if a < b:
        for i in range (a, b + 1):
            if i % 2 == 1:
                print(i, end=' ')

    else:
        for i in range (a, b - 1, -1):
            if i % 2 == 1:
                print(i, end=' ')
    
ganjil(10, 30)
print()
ganjil(97, 82)


