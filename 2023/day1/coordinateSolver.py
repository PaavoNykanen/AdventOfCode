
file = open("2023/day1/input.txt").read()

lines = file.split('\n')

numbers = []
sumOfCalibration = 0

for line in lines:
    for char in line:
        if (char.isnumeric()):
            numbers.append(char)
    if (len(numbers) > 0):
        print("Found numbers: ", numbers)
        calibration = numbers[0] + numbers[len(numbers) - 1] 
        sumOfCalibration += int(calibration)
    print("Sum is: ", sumOfCalibration)
    numbers = []
    

print(sumOfCalibration)
