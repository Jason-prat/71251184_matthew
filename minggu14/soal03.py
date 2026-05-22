import re
n1=input("Masukkan Nama File 1: ")
n2=input("Masukkan Nama File 2: ")
try:
    h1=open(n1).read()
    h2=open(n2).read()
    katta1=set(re.findall(r'\b[a-zA-Z]+\b', h1.lower()))
    katta2=set(re.findall(r'\b[a-zA-Z]+\b', h2.lower()))
    katasama=katta1&katta2
    if len(katta1)==0:
        print("Tidak ada kata pada file 1.")
    else:
        print(f"Kata pada teks 1 {katta1}")
    if len(katta2)==0:
        print("Tidak ada kata pada file 2.")
    else:
        print(f"Kata pada teks 2 {katta2}")
    if len(katasama) ==0:
        print("Tidak ada kata yang sama.")
    else:
        print(f"Kata yang sama pada kedua teks {katasama}")
except:
    print("File salah atau tidak ditemukan")

