angka=input("Masukkan angka(beri spasi antar angka): ").split()
data=[]
for i in angka:
    try:
        data.append(int(i))
    except ValueError:
        print(f"{i}, bukan angka")
if len(data)<3:
    print("Jumlah data Kurang")
else:
    angka=sorted(data)
    angka.reverse()
    print(f"3 Bilangan Terbaik: {angka[0]}, {angka[1]}, {angka[2]}")