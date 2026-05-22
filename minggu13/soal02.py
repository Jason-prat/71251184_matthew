Data='Matthew Jason Pratama', '71251184', 'Sleman, DI Yogyakarta'
NIM=Data[1]
Nama=Data[0]
Alamat=Data[2]

NIMS=tuple(NIM)
Namadpn=Nama.split()[0]
namabalik=Nama.split()
namabalik=tuple(reversed(namabalik))
print(f"NIM\t: {NIM}")
print(f"Nama\t: {Nama}")
print(f"Alamat\t: {Alamat}")
print()
print(f"NIM\t: {NIMS}")
print()
print(f"Nama Depan: {tuple(Namadpn)}")
print()
print(f"Nama Terbalik: {namabalik}")