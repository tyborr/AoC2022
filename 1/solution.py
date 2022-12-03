calories = []

with open("./input.txt", 'r') as f:
    data = [x for x in f.read().strip().split("\n")]

print(data)
max1, max2, max3, count = 0, 0, 0, 0
for x in data:
    if x == '':
        count = 0 #skip to next elf
    else:
        count += int(x)
    calories.append(count)
sorted_data = sorted(calories, reverse=True)
print(sorted_data[1:4])
print(sum(sorted_data[1:3]))