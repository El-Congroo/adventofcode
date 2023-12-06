import re

with open('2023/data/input06.txt') as f:
    content = [re.findall(r'\d+', line) for line in f.readlines()]

numbers = [(int(x),int(y)) for x, y in zip(content[0], content[1])]
number = [int(''.join(x)) for x in content]

def getDistance(msHeldDown, msWhole):
    return msHeldDown * (msWhole - msHeldDown)

def bbcnt(msWhole, bestDistace): # bigger best count
    for i in range(msWhole+1):
        if getDistance(i, msWhole) > bestDistace:
            return msWhole-i*2+1
    

prod1 = 1
for time, bestD in numbers:
    prod1 *= bbcnt(time, bestD) 

time, bestD = number

print("Part 1:", prod1)
print("Part 2:", bbcnt(time, bestD))