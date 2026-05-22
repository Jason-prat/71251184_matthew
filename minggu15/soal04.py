def digit(angka):
    if angka ==0:
        return 0
    return angka%10 + digit(angka//10)
angka=int(input("Masukkan angka: "))
print(digit(angka))