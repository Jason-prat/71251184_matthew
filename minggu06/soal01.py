def perkalian(bil1,x,bil2):
    hasil = bil1 * bil2
    print(bil1, x, bil2, "= ", end="")
    for i in range (1,bil1+1):
        if i < bil1:
            print(bil2,"+ ", end="")
        else:
            print(bil2, "=", hasil, end="")

try:
    bil1, x, bil2=input("Masukkan Perkalian (Contoh: 6 X 4): ").split()
    bil1=int(bil1)
    bil2=int(bil2)
    if x =="x" or x == "X":
        perkalian(bil1,x,bil2)
    else: 
        raise Exception
except:
    print("IKUTI INSTRUKSI INPUT")

