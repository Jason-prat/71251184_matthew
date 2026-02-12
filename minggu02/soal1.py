print("List BMI:\nKekurangan BB: < 18.5\nNormal: 18.5-24.9\nKelebihan BB: 25-29.9\nObesitas: 30 <")
tinggi = float(input("Masukkan Tinggi Badan (Cm): "))
BMI = float(input("Masukkan BMI yang ingin dicapai: "))

BeratBadan = BMI * (tinggi/100)**2
print(f"Berat Badan yang ideal untuk mencapai BMI yang diinginkan adalah: {BeratBadan:.2f}Kg")