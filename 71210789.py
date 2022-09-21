import json

karyawan = int(input('Masukkan jumlah karyawan baru : '))
for i in range(karyawan):
    nama = input('Masukkan nama : ')
    l = list()
    d = dict()
    dalamat = dict()
    dkolega = dict()
    alamat = input('Masukkan alamat : ')
    dalamat['Alamat'] = alamat
    kolega = int(input('Masukkan jumlah kolega : '))
    listkolega = list()
    for j in range (kolega):
        jmlhKolega = input('Masukkan nama kolega ke-{} : '.format(str(j + 1)))
        listkolega.append(jmlhKolega)
    dkolega['Kolega'] = listkolega
    l.append(dalamat)
    l.append(dkolega)
    with open('karyawan.json', 'r') as datafile:
        data = json.load(datafile)
        data[nama] = l
    with open('karyawan.json', 'w') as datafile:
        json.dump(data, datafile)
    print('=== Data berhasil ditambahkan ===\n')