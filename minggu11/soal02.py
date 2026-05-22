angka=[]
while True:
    inputuser=input("Masukkan angka, jika sudah ketik 'done': ")
    if inputuser.lower()=="done":
        break
    try:
        nilai=int(inputuser)
        angka.append(nilai)
    except:
        print("Input bukan angka")
total=0
for i in angka:
    total+=int(i)
rata=total/len(angka)
print(f"List angka yang ingin dicari rata-rata: {angka}")
print(f"Rata Ratanya adalah: {rata}")