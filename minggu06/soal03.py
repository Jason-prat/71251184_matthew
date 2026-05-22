jumlah = input("Berapa Jumlah Mata Kuliah? ")
nilai = 0
try:
    jumlah=int(jumlah)
    for i in range (1,jumlah+1):
        mk = input(f"Nilai MK {i}: ")
        if mk == "A":
            nilai = nilai + 4
        elif mk == "B":
            nilai = nilai + 3
        elif mk == "C":
            nilai = nilai +2
        elif mk == "D":
            nilai = nilai +1
        else:
            print("Bukan Nilai Valid")
            break
    nilai_akhir = nilai / jumlah
    print(f"Nilai IPS anda semester ini: {nilai_akhir:.2f}")
except:
    print("INPUT TIDAK VALID")