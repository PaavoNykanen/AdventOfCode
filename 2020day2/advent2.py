import array as arr

f = open("Day2Input.txt", "r")
minNumbs = []
maxNumbs = []
chars = []
strings = []
parts = [3]

for x in f:
    parts = x.split(" ", 3)
    minNumbs.append(parts[0].split("-")[0])
    maxNumbs.append(parts[0].split("-")[1])

    chars.append(parts[1][0])
    strings.append(parts[2])
    

valids = 0
numOfChars = 0
i=0

#part 1, from the string, find if given letter is in either of given places(minNumbs and maxNumbs) but not in both
while (i < len(minNumbs)):
    if (strings[i][int(minNumbs[i])-1] == chars[i] and strings[i][int(maxNumbs[i])-1] != chars[i]):
        valids = valids + 1
    if (strings[i][int(minNumbs[i])-1] != chars[i] and strings[i][int(maxNumbs[i])-1] == chars[i]):
        valids = valids + 1
    
    i=i+1


#part 1 find if number of given chars in a string is within boundaries minNumbs and maxNumbs
#while (i < len(minNumbs)):
#    numOfChars = strings[i].count(chars[i])
#    if (numOfChars <= int(maxNumbs[i]) and numOfChars >= int(minNumbs[i])):
#        valids = valids + 1 
#    i=i+1

print(valids)