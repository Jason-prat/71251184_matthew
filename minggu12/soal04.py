import re
file=input("Masukkan Nama File:").strip()
try:
    emails={}
    with open(file, 'r', encoding='utf-8') as f:
        # for baris in f:
        #     if baris.startswith('From '):
        #         email = baris.split()[1]
        #         domain = email.split('@')[1]
        #         emails[domain] = emails.get(domain, 0) + 1
        for line in f:
            if line.startswith("From "):
                email=line.split()[1]
                domain=email.split("@")[1]
                emails[domain]=emails.get(domain,0)+1
    print(emails)
except:
    print("File Tidak Ditemukan")