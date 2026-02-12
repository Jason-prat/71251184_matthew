minggu = 5
gaji = float(input("Gaji yang diinginkan per jam: Rp"))
jamkerja = float(input("Jumlah jam kerja yang diinginkan dalam 1 minggu: "))

kotor = gaji * jamkerja * minggu
bersih = kotor - (kotor * 14/100)

pakaian = bersih * 10/100
alattulis = bersih * 1/100

setelah_belanja = bersih - pakaian - alattulis
sedekah = setelah_belanja * 25/100

anak_yatim = sedekah * 0.3
kaum_dhuafa = sedekah * 0.7

print(f"Pendapatan sebelum pajak:Rp {kotor:.0f}")
print(f"Pendapatan setelah pajak:Rp {bersih:.0f}\n")
print(f"Uang yang dihabiskan untuk pakaian dan aksesoris:Rp {pakaian:.0f}")
print(f"Uang yang dihabiskan untuk alat tulis:Rp {alattulis:.0f}\n")
print(f"Uang yang diberikan untuk sedekah:Rp {sedekah:.0f}")
print(f"Uang yang diberikan untuk anak yatim (30%):Rp {anak_yatim:.0f}")
print(f"Uang yang diberikan untuk kaum dhuafa (70%):Rp {kaum_dhuafa:.0f}")
