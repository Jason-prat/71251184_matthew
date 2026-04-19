import re
jumlah=0
kalimat= input("Kalimat yang ingin dicek: ")
kata= input("Kata yang ini dicari jumlahnya: ")
kata=kata.lower()
kalimat = kalimat.lower().replace(",","")
kalimat = kalimat.replace(".","")
kalimat = kalimat.split()
for kal in kalimat:
    if kal == kata:
        jumlah+=1
print(f"kata '{kata}' ada {jumlah} buah")