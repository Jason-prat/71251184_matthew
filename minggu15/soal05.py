def kombinasi(n,m):
    if m == 0 or m == n:
        return 1
    else:
        return kombinasi(n-1,m-1)+ kombinasi(n-1,m)
n=int(input("Masukkan jumlah keseluruhan: "))
m=int(input("Masukkan yang ingin dicari: "))
if n>m:
    print(kombinasi(n,m))
else: 
    print("Jumlah variabel yang memenuhi terlalu banyak")