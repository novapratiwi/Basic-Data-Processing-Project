import csv

def menghapus_data():
    spasi=' '
    daftar=[]
    with open('DaftarNama.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=';')
        for row in csv_reader:
            daftar.append(row)
    hapus = input("Masukan nama/nim yang akan di dihapus : ")
    with open('DaftarNama.csv', mode="w",newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        for i in range(len(daftar)):
            if hapus==daftar[i][0] or spasi+hapus.lower()==daftar[i][1].lower():
                daftar.remove(daftar[i])
                print("\n ====================Data berhasil dihapus===================")
            else:
                ("data yang ingin dihapus tidak ada di dalam daftar")
        writer.writerows(daftar) 