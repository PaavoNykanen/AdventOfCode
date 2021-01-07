import array as arr

firstNum=0
secondNum=0
thirdNum=0

f = open("Day1Numbers.txt", "r")
numbers = arr.array('i', [])

for x in f:
    numbers.extend([int(x)])

firstNum = numbers[0]
secondNum = numbers[1]
i=0
k=1
j=len(numbers)-1


while (i < len(numbers)):
    if (i == (len(numbers)-1)):
        break
    if (k == (len(numbers)-1)):
        i=i+1
        k=i+1
        j=len(numbers)-1
    if (k==j):
        k=k+1
        j=len(numbers)-1
    
    if (numbers[i] + numbers[j] + numbers[k] == 2020):
        firstNum = numbers[i]
        secondNum = numbers[j]
        thirdNum = numbers[k]
        print(firstNum * secondNum*thirdNum)
        break
    j = j-1