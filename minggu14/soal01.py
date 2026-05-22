n = int(input("Masukkan jumlah kategori: "))
data_app={}
for i in range(n):
    nama_kat=input("Masukkan nama kategori: ")
    print("Masukkan 5 nama aplikasi di kategori", nama_kat)
    app=[]
    for j in range(5):
        nama_app=input("Nama aplikasi: ")
        app.append(nama_app)
    data_app[nama_kat]=app
daftar_app_list=[]
for app in data_app.values():
    daftar_app_list.append(set(app)) 



muncul={}
satu=set()
dua=set()
for i in (data_app):
    for j in data_app[i]:
        muncul[j]=muncul.get(j,0)+1
for i in muncul:
    if muncul[i]==1:
        satu.add(i)
    elif muncul[i] ==2:
        dua.add(i)
print(f"App yang mucul pada 1 kategori {satu}")
print(f"App yang mucul pada 2 kategori {dua}")