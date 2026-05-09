import re
file=input("Masukkan Nama File: ")

emails={}
try:
    handle=open(file).read().strip()
    daftaremail=re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', handle)
    for email in daftaremail:
        if email not in emails:
            emails[email]=1
        else:
            emails[email]+=1
    print(emails)
except:
    print("File tidak ditemukan")

handle.close()