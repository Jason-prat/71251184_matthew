def primas(n,x=1,prima=0):
    if x>n:
        return prima
    if n%x==0:
        prima+=1
    return primas(n,x+1,prima)

n=int(input("Masukkan Bilangan: "))

p=primas(n)

if p ==2:
    print(f"Bilangan {n} adalah Prima")
else:
    print(f"Bilangan {n} bukan bilangan Prima")