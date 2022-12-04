with open("./input.txt", 'r') as f:
    data = [x for x in f.read().strip().split("\n")]
count = 0
for x in data:
    sets = x.split(',')
    splitted_set1 = sets[0].split('-')
    splitted_set2 = sets[1].split('-')
    set1 = set(range(int(splitted_set1[0]), int(splitted_set1[1]) + 1))
    set2 = set(range(int(splitted_set2[0]), int(splitted_set2[1]) + 1))
    #if set1.issubset(set2) or set1.issuperset(set2): #part 1
    if set1.intersection((set2)): #part2
        count +=1

print(count)