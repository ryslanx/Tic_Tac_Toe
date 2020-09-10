def game_check():
    if inputted.count('X') - inputted.count('O') >= 2 or inputted.count('O') - inputted.count('X') >= 2:
        return "Impossible"
    counter = 0
    for combination in combinations:
        if all(inputted[number] == 'O' for number in combination):
            counter += 1
        elif all(inputted[number] == 'X' for number in combination):
            counter += 1
        if counter == 2:
            return "Impossible"
    counter = 0
    for combination in combinations:
        if not all(inputted[number] == 'O' for number in combination) and not all(
                inputted[number] == 'X' for number in combination) and '_' not in inputted:
            counter += 1
        if counter == 8:
            return "Draw"
    counter = 0
    for combination in combinations:
        if not all(inputted[number] == 'O' for number in combination) and not all(
                inputted[number] == 'X' for number in combination) and '_' in inputted:
            counter += 1
        elif all(inputted[number] == 'O' for number in combination):
            return 'O wins'
        elif all(inputted[number] == 'X' for number in combination):
            return 'X wins'
     # if counter == 8:
         # return "Game not finished"


def coordinates_check():
    turn = 0
    while True:
        global inputted
        if '_' not in inputted:
            break
        try:
            coordinates = input("Enter the coordinates:")
        except EOFError:
            continue
        if coordinates == '':
            continue
        coordinates = coordinates.split()
        counter = 0
        for number in coordinates:
            if number not in "1234567890":
                counter += 1
                print("You should enter numbers!")
                break
        if counter == 1:
            continue
        if int(coordinates[0]) > 3 or int(coordinates[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            counter += 1
        if counter == 1:
            continue
        # calculating the index
        coordinate_tuple = (int(coordinates[0]), int(coordinates[1]))
        coordinates_dict = {(1, 1): 6, (1, 2): 3, (1, 3): 0, (2, 1): 7, (2, 2): 4, (2, 3): 1, (3, 1): 8,
                            (3, 2): 5, (3, 3): 2}
        if inputted[coordinates_dict[coordinate_tuple]] == 'X' or inputted[coordinates_dict[coordinate_tuple]] == 'O':
            print("This cell is occupied! Choose another one!")
            counter += 1
            if counter == 1:
                continue
        elif turn % 2 == 0:
            inputted[coordinates_dict[(int(coordinates[0]), int(coordinates[1]))]] = 'X'
        else:
            inputted[coordinates_dict[(int(coordinates[0]), int(coordinates[1]))]] = 'O'
        print("---------")
        for x in range(0, 9, 3):
            print("| " + inputted[x] + " " + inputted[x + 1] + " " + inputted[x + 2] + " |")
        print("---------")
        turn += 1
        if game_check() == 'O wins' or game_check() == 'X wins' or game_check() == 'Draw':
            print(game_check())
            break



inputted = list(('_', '_', '_', '_', '_', '_', '_', '_', '_'))
combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
print("---------")
for i in range(0, 9, 3):
    print("| " + inputted[i] + " " + inputted[i + 1] + " " + inputted[i + 2] + " |")
print("---------")
coordinates_check()

# print(game_check())
