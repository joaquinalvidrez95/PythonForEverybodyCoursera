import re

file = open("regex_sum_171283.txt")
sumOfNumbers = 0
for line in file:
    line = line.rstrip()
    numberList = re.findall('[0-9]+', line)
    if 0 == len(numberList):
        continue
    for stringNumber in numberList:
        sumOfNumbers = sumOfNumbers + int(stringNumber)

print(sumOfNumbers)
