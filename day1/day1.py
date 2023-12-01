file = open('day1input.txt', 'r')
lines = file.readlines()
file.close()

## Part 1:
total = 0
## Iterate through lines to make an ordered list of digits for each line
for line in lines:
    firstDigit = "0"
    lastDigit = "0"
    for i in range(len(line)):
        if line[i].isdigit():
            currentDigit = int(line[i])
            if int(firstDigit) <= 0:
                firstDigit = line[i]
                lastDigit = line[i]
            elif lastDigit != line[i]:
                lastDigit = line[i]
    total += int(firstDigit + lastDigit)

print(total)

## Part 2:
spellings = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "night": 9,
}
for line in lines:
    firstDigit = "0"
    lastDigit = "0"
    for i in range(len(line)):

