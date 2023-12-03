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

# print(total)

## Part 2:

spellings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

total = 0
for line in lines:
    firstDigitIndex = len(line)
    lastDigitIndex = 0

    # Get index of first character that is a digit
    for i in range(len(line)):
        if line[i].isdigit():
            firstDigitIndex = i
            firstDigit = line[i]
            lastDigitIndex = i
            break
    
    # Get index of last character that is a digit
    for i in range(len(line)-1, firstDigitIndex-1, -1):
        if line[i].isdigit():
            lastDigitIndex = i
            lastDigit = line[i]
            break
    if firstDigitIndex > 2:
        for spelling in spellings:
            currentIndex = line[0:len(line)].find(spelling)
            if currentIndex != -1:
                if currentIndex < firstDigitIndex:
                    firstDigitIndex = currentIndex
                    firstDigit = spellings[spelling]
                if currentIndex > lastDigitIndex:
                    lastDigitIndex = currentIndex
                    lastDigit = spellings[spelling]

    # Search for spelling in last substring:
    if lastDigitIndex < len(line) - 3:
        lastDigitNotFound = 0
        while (lastDigitNotFound == 0):
            lastDigitNotFound = 1
            for spelling in spellings:
                currentIndex = line[lastDigitIndex + 1: len(line)].find(spelling)
                if currentIndex != -1:
                    lastDigitIndex = lastDigitIndex + 1 + currentIndex
                    lastDigit = spellings[spelling]
                    lastDigitNotFound = 0
    
    total += int(firstDigit + lastDigit)
print(total)
