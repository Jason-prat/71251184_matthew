def ganjil(bawah, atas):
    if bawah < atas:
        print(f"Bawah = {bawah}, atas = {atas}. Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya adalah: ", end="")
        if atas%2 !=0:
            for i in range (bawah, atas+1):
                if i %2!=0:
                    if i<atas:
                        print(f"{i},",end=" ")
                    else:
                        print(f"{i}.")
        else:
            for i in range (bawah, atas+1):
                if i %2!=0:
                    if i<(atas-1):
                        print(f"{i},",end=" ")
                    else:
                        print(f"{i}.")
    elif bawah>atas:
        print(f"Bawah = {bawah}, atas = {atas}. Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya adalah: ", end="")
        for i in range (bawah, atas-1,-1):
            if i % 2 != 0:
                if atas % 2 == 0:
                    if i >atas +1:
                        print(f"{i},", end=" ")
                    else:
                        print(f"{i}.")
                else:
                    if i > atas:
                        print(f"{i},", end=" ")
                    else:
                        print(f"{i}.", end="")
                
bawah = input("Masukkan Batas Bawah: ")
atas = input("Masukkan Batas Atas: ")
try: 
    bawah=int(bawah)
    atas=int(atas)
    ganjil(bawah,atas)
except:
    print("INPUTNYA SALAH WOI")
