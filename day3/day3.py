file = open("day3input.txt", 'r')
lines = file.readlines()
file.close()

# Create matrix of every character split
matrix = []
for line in lines:
#    matrix.append([*line.strip("\n")])
    matrix.append(line.strip("\n"))


# Function which checks if part number is valid:
def isValidPart(row: int, startIndex: int, endIndex: int, matrix) -> bool:
    isValid = False

    # Set the search window
    minSearchRow = max(0, row - 1)
    maxSearchRow = min(len(matrix)-1, row + 1)
    minSearchCol = max(0, startIndex -1)
    maxSearchCol = min(len(matrix[0])-1, endIndex)

    for i in range(minSearchRow, maxSearchRow + 1):
        for j in range(minSearchCol, maxSearchCol + 1):
            if (not matrix[i][j].isnumeric()) and matrix[i][j] != ".":
                isValid = True

    return isValid

# Iterate through each space and see if it is adjacent to a symbol
total = 0
lengthOfEachLine = len(matrix[0])
for row in range(len(matrix)):
    startIndex = -1
    endInex = -1
    leftPtr = 0

    # Get the part numbers
    while leftPtr < lengthOfEachLine:

        if matrix[row][leftPtr].isdigit():
            rightPtr = leftPtr + 1

            for rightPtr in range(leftPtr + 1, lengthOfEachLine + 1):

                if not matrix[row][leftPtr: rightPtr+1].isnumeric():
                    break
            # At this point, matrix[row][leftPtr: rightPtr]) = the string of the part number


            # Once we have the part number, add to the total if it is next to a symbol
            if isValidPart(row, leftPtr, rightPtr, matrix):
                total += int(matrix[row][leftPtr: rightPtr])
            leftPtr = rightPtr

        else:

            leftPtr += 1

print(total)


# Part 2

## Function to return the gear ratio
def gearRatio(row, col, matrix) -> int:
    gearRatioVal = 0

    # Set search the 3x3 window around gear
    minRow = max(0, row-1)
    maxRow = min(row, len(matrix)-1)
    minCol = max(0, col-1)
    maxCol = min(col, len(matrix[0])-1)

    ## Iterate through each row surrounding the gear to find the number of digits
    numCount = 0
    for i in range(minRow, maxRow+1):
        
        symbolCount = 0
        
        # Find how many symbols are not digits in each row--this will give total count of part numbers
        # surrounding the gear
        for j in range(minCol, maxCol+1):
            
            # If we are looking at the same row as the gear, just check if the left and right are numeric
            if i == row:
                if matrix[i][j].isnumeric():
                    numCount += 1
            else:
                if not matrix[i][j].isnumberic():
                    symbolCount += 1
        
        # Add the number of unique numbers to the total count of numbers surrounding the gear
        numCount += 3-symbolCount

    # If there are less or more than 2 part number surrounding the gear, return 0
    if numCount != 2:

        return 0

    else: 

    return gearRatioVal    
