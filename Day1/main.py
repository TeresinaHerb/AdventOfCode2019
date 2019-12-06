import math
totalFuel = 0

file = open('input.txt', 'r')
temp = file.read().strip()
file.close()

masses = list()
for x in temp.split():
    masses.append(int(x))

# part 1
for mass in masses:
    totalFuel += math.floor(mass/3) - 2
    
print (totalFuel)

# part 2
totalFuel = 0

for mass in masses:
    temp = mass
    while (math.floor(temp/3)-2 > 0):
        temp = math.floor(temp/3) - 2
        totalFuel += temp

print (totalFuel)