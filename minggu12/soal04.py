import re
file=input("Masukkan Nama File:").strip()
try:
    emails={}
    with open(file, 'r', encoding='utf-8') as handle:

        for line in handle:
            if line.startswith("From "):
                email=line.split()[1]
                domain=email.split("@")[1]
                emails[domain]=emails.get(domain,0)+1
    print(emails)
    handle.close()
except:
    print("File Tidak Ditemukan")