file=input("Masukkan Nama File: ")
try:
    handle=open(file)
except:
    print("File Tidak Ditemukan")

hitung=dict()
for line in handle:
    if line.startswith("From "):
        kata=line.split()
        waktu = kata[5]
        jam = waktu.split(":")[0]
        hitung[jam]=hitung.get(jam,0) +1

for jam in sorted(hitung):
    print(jam, hitung[jam])