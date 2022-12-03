with open("./input.txt", 'r') as f:
    data = [x.replace(" ", "") for x in f.read().strip().split("\n")]


outcomes = {
    "AX": 4 , "AY": 8, "AZ": 3,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 7, "CY": 2, "CZ": 6
}

test=["AY","BX","CZ"]
total = 0
for x in data:
    total += outcomes[x]

#print(total)

outcomes2 = {
    "AX": 3, "AY": 4, "AZ": 8,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 2, "CY": 6, "CZ": 7
}
total2=0
for x in data:
    total2 += outcomes2[x]

print(total2)