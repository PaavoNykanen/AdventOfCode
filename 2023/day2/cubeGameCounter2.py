limits = {"red": 0, "green": 0, "blue": 0}

def resetLimits():
    limits["blue"] = 0
    limits["green"] = 0
    limits["red"] = 0


def countGamePower(gameInput):
    pulls = gameInput.split(": ")[1].split(";")
    for pull in pulls:
        dices = pull.split(", ")
        for dice in dices:
            num, color = dice.strip().split(" ")
            if (int(num) > limits[color]):
                limits[color] = int(num)
    sum = limits["blue"] * limits["green"] * limits["red"]
    resetLimits()
    return sum


file = open("2023/day2/input.txt").read()
lines = file.split('\n')

sumOfPowers = 0

for line in lines:
    if (line == ""):
        break
    sumOfPowers += countGamePower(line)
            
    

print("Sum is: ", sumOfPowers)
