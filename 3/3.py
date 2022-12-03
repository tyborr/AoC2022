import string

with open("./input.txt", 'r') as f:
    data = [x for x in f.read().strip().split("\n")]

scores = dict(zip(string.ascii_lowercase, range(1,27)), **dict(zip(string.ascii_uppercase, range(27,53))))
print(scores)
score = 0
for items in data:
    string1 = items[slice(0,len(items)//2)]
    string2 = items[slice(len(items)//2, len(items))]
    common = ''.join(set(string1).intersection(string2))
    score += scores[common]

score2 = 0
lines = []

def process(data):
    common2 = ''.join(set(data[0]).intersection(data[1]).intersection(data[2]))
    print(common2, scores[common2])
    return scores[common2]

for line in data:
    lines.append(line)
    if len(lines) >= 3:
        score2 += process(lines)
        lines = []
if len(lines) > 0:
    process(lines)

print(score2)