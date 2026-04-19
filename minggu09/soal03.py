import re
kalimat = input("Masukkan kalimat yang ingin dihapus spasi berlebihan: ")
hasil =""
for i in range (len(kalimat)):
    if i>0 and kalimat[i] == " " and kalimat[i-1] == " ":
        continue
    hasil += kalimat[i]
print(hasil)