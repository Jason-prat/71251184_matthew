n = input("Masukkan Bilangan: ")
n = int(n)
for i in range (n,0,-1):
    ya=1
    for j in range (i ,0 ,-1):
        ya = j * ya
    print(ya,end=" ")
    for k in range(i,0,-1):
        print(k, end =" ")
    print()