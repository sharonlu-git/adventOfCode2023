actualCubes = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

# Open input file and store each line's hands in linstList
# Ex. linesList = ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
file = open("day2input.txt", "r")
linesList = []
for line in file.readlines():
    linesList.append(line.strip("\n").split(": ")[1].split("; "))
file.close()

# Iterate through each game
dictLines = {}
total = 0
partTwoTotal = 0
gameNumber = 1

for game in linesList:

    # Create dictionary of colors and their counts for each hand
    dictColors = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    # Iterate through each hand and get the max count of each color from each hand
    for cubeSet in game:
        cubes = cubeSet.split(", ") # [3 blue][4 red]
        for cube in cubes:
            color = cube.split(" ")
            dictColors[color[1]] = max(dictColors[color[1]], int(color[0]))


    # Part 1: Check to see if the game is possible based on actualCubes
    isPossible = True
    for color in actualCubes:
        if dictColors[color] > actualCubes[color]:
            isPossible = False
    
    power = 1
    # Part 2: Get the power and add
    for color in actualCubes:
        power *= dictColors[color]
    partTwoTotal += power

    # If it the game is possible, add to the total
    if isPossible:
        total += gameNumber
    
    gameNumber += 1
    
print(total)
print(partTwoTotal)
