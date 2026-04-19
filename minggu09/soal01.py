import re
kata1 = input("Masukkan kata pertama yang ingin dicek: ")
kata2 = input("Masukkan kata kedua yang ingin dicek: ")

lower1 = kata1.lower().replace(" ","")
lower2 = kata2.lower().replace(" ","")

urutan1 = "".join(sorted(lower1))
urutan2 = "".join(sorted(lower2))

if urutan1 == urutan2:
    print("Kata 1 dan Kata 2 adalah Anagram")
else:
    print("Kata 1 dan Kata 2 bukan Anagram")