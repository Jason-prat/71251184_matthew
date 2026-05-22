from datetime import date, datetime
import re
sekarang = date.today()
tanggal=input("Masukkan tanggal yang ingin dicek dengan format YYYY-MM-DD: ")
bagian = tanggal.split("-")
tahun = bagian[0]
bulan = bagian[1]
hari = bagian[2]
bulan31= int(bulan) in [12, 1, 3, 5,7 ,8 ,10]
bulan30 = int(bulan) in [4, 6, 9, 11]
kabisat= (int(tahun) % 4 == 0 and int(tahun) % 100 != 0) or (int(tahun) % 400 == 0)
if (bulan31 and int(hari) <= 31) or (bulan30 and int(hari) <= 30) or (int(bulan) == 2 and int(hari) <= (29 if kabisat else 28)):
    tanggal1 = datetime.strptime(tanggal, "%Y-%m-%d").date()
    selisih = sekarang - tanggal1

    if selisih.days>0:
        print(f"{hari}-{bulan}-{tahun} 00:00:00 selisih {selisih.days} hari")
    else:
        print(f"{hari}-{bulan}-{tahun} 00:00:00 {abs(selisih.days)} hari dari sekarang")
else:
    print("Tanggal yang dimasukkan tidak valid")