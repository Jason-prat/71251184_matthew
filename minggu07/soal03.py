tinggi = int(input("Masukkan tinggi= "))
lebar = int(input("Masukkan lebar= "))
total_angka = tinggi * lebar
lebar_awal=lebar
for i in range(1,total_angka+1,lebar):
    for j in range(i,lebar+1):
        print(j,end=" ")
    lebar = lebar+lebar_awal
    print()