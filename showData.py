import csv

def menampilkan_data():
    daftar=[]
    with open('DaftarNama.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=';')
        for row in csv_reader:
            daftar.append(row)
    print("NIM \t\t NAMA")
    print("-"*50)
    for i in range(len(daftar)):
        for j in range(len(daftar[0])):
            if j==0:
                print(daftar[i][j],end='\t')
            else:
                print(daftar[i][j])