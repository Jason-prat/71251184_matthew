import re
namafile=input('Masukan file:')
try:
    handle=open(namafile)
    file=handle.read()
    for line in file.strip().split('\n'):
        if '||' in line:
            bagian = line.split("||",1)
            soal=bagian[0].strip()
            jawaban=bagian[1].strip()
            print(soal)
            jawabanuser=input("Masukkan Jawaban: ")
            if jawaban.lower() == jawabanuser.lower():
                print("Jawaban Benar!")
            else:
                print("Jawaban Salah")
except:
    print("Nama file salah")