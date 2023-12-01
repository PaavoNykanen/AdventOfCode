
numberWords = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

file = open("2023/day1/input.txt").read()

lines = file.split('\n')

numbers = []
sumOfCalibration = 0

for line in lines:
    for count, char in enumerate(line):
        if (char.isnumeric()):
            numbers.append(char)
        else:
            for word in numberWords:
                if (line.startswith(word, count)):
                    numbers.append(numberWords[word])
                    
            
    if (len(numbers) > 0):
        print("Found numbers: ", numbers)
        calibration = numbers[0] + numbers[len(numbers) - 1] 
        sumOfCalibration += int(calibration)
    print("Sum is: ", sumOfCalibration)
    numbers = []
    

print(sumOfCalibration)
