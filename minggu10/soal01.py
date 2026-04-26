file1=input("Masukkan file pertama : ")
file2=input("Masukkan file kedua   : ")
try:
    handle1=open(file1).read().strip().split('\n')
    handle2 = open(file2).read().strip().split('\n')

    for i in range(max(len(handle1), len(handle2))):
        
        if i < len(handle1):
            baris1= handle1[i]
        else :
            print(f"Tidak ada line {i}")
        if i < len(handle2):
            baris2 = handle2[i]
        else:
            print(f"Tidak ada line {i}")

        if baris1 != baris2:
            print(f"Baris {i+1} berbeda:")
            print(f"File 1 : {baris1}")
            print(f"File 2 : {baris2}")
except:
    print("Nama file salah")