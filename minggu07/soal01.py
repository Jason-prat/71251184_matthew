n = input("Masukkan Bilangan: ")
try:    
    n = int(n)
    for i in range(n-1, 1,-1):
        prima = True
        for j in range(2,i):
            if i % j == 0:
                prima = False
                break
        if prima:
            print(f"Maka prima terdekat < {n} adalah {i}")
            break
except:
    print("Input Invalid")