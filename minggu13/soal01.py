cek=eval(input("Masukkan tuple yang ingin dicek(pisahkan dengan koma): "))
if len(cek) == 1:
    print("Isi harus lebih dari 1")
else:
    if len(set(cek))==1:
        print(True)
    else:
        print(False)