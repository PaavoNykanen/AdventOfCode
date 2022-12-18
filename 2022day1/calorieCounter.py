

file = open("calories.txt").read()

elfs = file.split('\n\n')

summedCalories = []

for elf in elfs:
    caloriesStrings = elf.split('\n')
    if (caloriesStrings.count('') != 0):
        caloriesStrings.remove('')
    calories = list(map(int, caloriesStrings))
    summedCalories.append(sum(calories))

summedCalories.sort(reverse = True)
print(summedCalories)

topThree = summedCalories[0] + summedCalories[1] + summedCalories[2]

print(topThree)
