def cek_angka(bil1,bil2,bil3):
    if bil1!=bil2!=bil3:
        if bil1+bil2 == bil3 or bil1+bil3 == bil2 or bil2+bil3 == bil1:
            return "True"
        else:
            return"False"
    else:
        return "False"
    pass

bil1 = input("Masukkan Bilangan 1: ")
bil2 = input("Masukkan Bilangan 2: ")
bil3 = input("Masukkan Bilangan 3: ")
try:
    bil1 = int(bil1)
    bil2 = int(bil2)
    bil3 = int(bil3)
    print(cek_angka(bil1,bil2,bil3))
except:
    print("INPUT SALAH")