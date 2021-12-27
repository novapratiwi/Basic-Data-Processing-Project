import csv

def menambahkan_data():
    spasi=" "
    daftar=[]
    with open('DaftarNama.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=';')
        for row in csv_reader:
            daftar.append(row)
    with open('DaftarNama.csv', mode='a', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        nim = input("MASUKAN NIM :")
        nama = str.title(input("MASUKAN NAMA :"))
        nama = spasi+nama
        new = [nim,nama,'']
        writer.writerow(new)
        print("\n=====data berhasil ditambahkan=====")