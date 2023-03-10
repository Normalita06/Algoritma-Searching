name = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
def linearsearch(nama,x):
    for l in range(len(nama)):
        if type(nama[l]) == list:
            hasil_x = linearsearch(nama[l],x)
            if hasil_x == -1:
                return -1
            else:
                print(f'{x} ditemukan pada indeks {l} kolom {hasil_x}')
                exit()
        elif nama[l] == x:
            return l
    return -1
print(name)
x = input('Masukan nama yang ingin dicari: ')
hasil_y = linearsearch(name,x)
if hasil_y == -1:
    print(f'{x} ditemukan pada indeks {hasil_y}')
else:
    print(f'{x} ditemukan pada indeks {hasil_y}')

# def jumpsearch():