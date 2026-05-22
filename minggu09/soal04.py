import re
kalimat = input("Masukkan kalimat yang ingin dicari kata terpendek dan terpanjang: ")
kata = kalimat.split()
terpendek = kata[0]
terpanjang =kata[0]

for i in range (len(kata)):
    if len(kata[i]) >= len(terpanjang):
        terpanjang = kata[i]
    elif len(terpanjang) >= len(kata[i]):
        terpanjang = terpanjang
    if len(terpendek) <= len(kata[i]):
        continue
    elif len(kata[i]) <= len(terpendek):
        terpendek = kata[i]

print(f"Kata terpendek: '{terpendek}' dan kata terpanjang: '{terpanjang}'")
