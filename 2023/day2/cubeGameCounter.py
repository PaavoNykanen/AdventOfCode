limits = {"red": 12, "green": 13, "blue": 14}

def isGameOk(gameInput):
    pulls = gameInput.split(": ")[1].split(";")
    for pull in pulls:
        dices = pull.split(", ")
        for dice in dices:
            num, color = dice.strip().split(" ")
            if (int(num) > limits[color]):
                return False
    return True


file = open("2023/day2/input.txt").read()
lines = file.split('\n')

sumOfIds = 0

for line in lines:
    if (line == ""):
        break
    gameId = line.split(":")[0].replace("Game ", "")
    gameIsOk = isGameOk(line)
    if (gameIsOk):
        sumOfIds += int(gameId)
            
    

print("Sum is: ", sumOfIds)
