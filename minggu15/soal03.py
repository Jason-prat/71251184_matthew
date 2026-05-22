def deret_ganjil(n,x=1,m=0,h=0):
    x=2**m-1
    h+=x
    if m==n:
        return h
    else:
        return deret_ganjil(n,x,m+1,h)

n=int(input("Masukkan berapa kali perulangan: "))

print(deret_ganjil(n))