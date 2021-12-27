import csv

def sorting():
    daftar=[]
    with open('DaftarNama.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=';')
        for row in csv_reader:
            daftar.append(row)
    choose1=str.lower(input('mau mengurutkan apa?(nama/nim) : '))
    if choose1=='nama':            
        choose2=str.lower(input('(ascending/descending)? : '))
        if choose2=='ascending':
            for i in range(len(daftar) - 1, 0, -1):
                for j in range(i):
                    if daftar[j][1].title() > daftar[j + 1][1].title():
                        tamp = daftar[j+1] 
                        daftar[j+1] = daftar[j]
                        daftar[j] = tamp
            print("NIM \t\t NAMA")
            print("-"*50)
            for i in range(len(daftar)):
                for j in range(len(daftar[0])):
                    if j==0:
                        print(daftar[i][j],end='\t')
                    else:
                        print(daftar[i][j])
                                          
        elif choose2=='descending':
            for i in range(len(daftar) - 1, 0, -1):
                for j in range(i):
                    if daftar[j][1].title() < daftar[j + 1][1].title():
                        tamp = daftar[j+1]
                        daftar[j+1] = daftar[j]
                        daftar[j] = tamp
            print("NIM \t\t NAMA")
            print("-"*50)
            for i in range(len(daftar)):
                for j in range(len(daftar[0])):
                    if j==0:
                        print(daftar[i][j],end='\t')
                    else:
                        print(daftar[i][j])
        else:
            print('pilihan tidak sesuai')
    elif choose1=='nim':
        choose2=str.lower(input('(ascending/descending)? : '))
        if choose2=='ascending':
            for i in range(len(daftar) - 1, 0, -1):
                for j in range(i):
                    if (int(daftar[j][0])) > (int(daftar[j + 1][0])):
                        tamp = daftar[j+1]
                        daftar[j+1] = daftar[j]
                        daftar[j] = tamp
            print("NIM \t\t NAMA")
            print("-"*50)
            for i in range(len(daftar)):
                for j in range(len(daftar[0])):
                    if j==0:
                        print(daftar[i][j],end='\t')
                    else:
                        print(daftar[i][j])
        elif choose2=='descending':
            for i in range(len(daftar) - 1, 0, -1):
                for j in range(i):
                    if (int(daftar[j][0])) < (int(daftar[j + 1][0])):
                        tamp = daftar[j+1] 
                        daftar[j+1] = daftar[j]
                        daftar[j] = tamp
            print("NIM \t\t NAMA")
            print("-"*50)
            for i in range(len(daftar)):
                for j in range(len(daftar[0])):
                    if j==0:
                        print(daftar[i][j],end='\t')
                    else:
                        print(daftar[i][j])
        else:
            print('pilihan tidak sesuai')