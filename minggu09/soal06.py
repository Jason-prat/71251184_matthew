import re
import random

teks = input("Masukkan daftar email dan nama pemilik: ")

daftaremail = re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+',teks)

password='' 
karakter_password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
for j in range(8):
    rand = random.randint(0, len(karakter_password)-1)
    password += karakter_password[rand]

print("Hasil:")
for email in daftaremail:
    user = email.split("@")[0]
    print(f"{email} Username: {user}, Password: {password}")