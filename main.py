from showData import menampilkan_data
from addData import menambahkan_data
from searchData import pencarian_data
from deleteData import menghapus_data
from sortingData import sorting

def menu():            
    print("========MENU========")
    print("1. Menampilkan Data")
    print("2. Menambahkan Data")
    print("3. Mencari Data")
    print("4. Menghapus Data")
    print("5. Sorting Data")

    menu=str(input("\nPilih Menu Keberapa?\n"))
    if menu=="1":
        menampilkan_data()
    elif menu=="2":
        menambahkan_data()
    elif menu=="3":
        pencarian_data()
    elif menu=="4":
        menghapus_data()
    elif menu=='5':
        sorting()
    else:
        print("menu yang anda pilih tidak tersedia")

menu()
choose=str(input('\nkembali ke menu awal?(y/n)\n'))
while choose.lower()=='y':
    menu()
    choose=str(input('\nkembali ke menu awal?(y/n)\n'))
if choose.lower()=='n':
    print('='*65,'SELESAI','='*65)