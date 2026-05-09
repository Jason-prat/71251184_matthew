Dictionary = {7: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Keys\tValue\tItems")
for i in range(len(Dictionary)):
    keys,value=list(Dictionary.items())[i]
    print(f"{keys}\t{value}\t{i+1}")