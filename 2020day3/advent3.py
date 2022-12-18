import array as arr

f = open("Day3Input.txt", "r")
strings=[]
trees = 0
trees2 = 0
trees3 = 0
trees4 = 0
trees5 = 0


for x in f:
    strings.append(x)

# length of row 31
# number of columns 323

index = 1
row = 1

while(row < len(strings)):

    if (index > 30):
        index = index - 31

    if (strings[row][index] == "#"):
        trees = trees + 1

    index = index + 1
    row = row + 1

index = 3
row = 1

while(row < len(strings)):

    if (index > 30):
        index = index - 31

    if (strings[row][index] == "#"):
        trees2 = trees2 + 1

    index = index + 3
    row = row + 1

index = 5
row = 1

while(row < len(strings)):

    if (index > 30):
        index = index - 31

    if (strings[row][index] == "#"):
        trees3 = trees3 + 1

    index = index + 5
    row = row + 1

index = 7
row = 1

while(row < len(strings)):

    if (index > 30):
        index = index - 31

    if (strings[row][index] == "#"):
        trees4 = trees4 + 1

    index = index + 7
    row = row + 1

index = 1
row = 2

while(row < len(strings)):

    if (index > 30):
        index = index - 31

    if (strings[row][index] == "#"):
        trees5 = trees5 + 1

    index = index + 1
    row = row + 2

print(trees*trees2*trees3*trees4*trees5)

#258, 232, 64, 259 