import csv

def pencarian_data():
    daftar=[]
    with open('DaftarNama.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=';')
        for row in csv_reader:
            daftar.append(row)
    cari=str(input('nama/nim:'))
    tampung = []
    stop=False
    for i in range (len(daftar)):
        if cari in daftar[i][0]:
            tampung.append(daftar[i])
            cek='nim'
        elif cari.lower() in daftar[i][1].lower():
            tampung.append(daftar[i])
            cek='nama'
        else:
            stop=True
            
    for i in range(len(tampung)):
        if cek=='nim':
            for i in range(len(daftar) - 1, 0, -1):
                for j in range(i):
                    if (int(daftar[j][0])) > (int(daftar[j + 1][0])):
                        tamp = daftar[j+1]
                        daftar[j+1] = daftar[j]
                        daftar[j] = tamp       
                        
            left=0
            right=len(daftar)-1
            index=-1
            while (left<=right) and index==-1:
                mid=(left+right)//2
                if daftar[mid][0]==tampung[0][0]:
                    index= mid
                elif daftar[mid][0]>tampung[0][0]:
                    right=mid-1
                elif daftar[mid][0]<tampung[0][0]:
                    left=mid+1

        elif cek=='nama':
            for i in range(len(daftar) - 1, 0, -1):
                for j in range(i):
                    if daftar[j][1].title() > daftar[j + 1][1].title():
                        tamp = daftar[j+1] 
                        daftar[j+1] = daftar[j]
                        daftar[j] = tamp
            left=0
            right=len(daftar)-1
            index=-1
            while (left<=right) and index==-1:
                mid=(left+right)//2
                if daftar[mid][1]==tampung[0][1]:
                    index= mid
                elif daftar[mid][1]>tampung[0][1]:
                    right=mid-1
                elif daftar[mid][1]<tampung[0][1]:
                    left=mid+1
    
    print("NIM \t\t NAMA")
    print("-"*50)
    for i in range(len(tampung)):
        for j in range(len(tampung[0])):
            if j==0:
                print(tampung[i][j],end='\t')
            else:
                print(tampung[i][j])