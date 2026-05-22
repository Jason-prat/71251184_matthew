def palindrom(kata):
    if len(kata) <=1:
        return "Kata Palindrome"
    if kata[0] != kata[-1]:
        return "Kata bukan Palindrome"
    return palindrom(kata[1:-1])
kata=input("Masukkan Kata: ")
print(palindrom(kata))