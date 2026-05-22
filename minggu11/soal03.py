import re
berita=input("Masukkan nama file: ")

kataunik=[]
file=open(berita)
files=file.read()
kata=re.findall(r'[^\s]+',files)
kataunik.extend(list(dict.fromkeys(kata)))
print(f"isi file: \n{files}")
print()
print("Daftar Kata Unik:")
for line in kataunik:
    print(f"'{line}'",end=" ")
file.close()