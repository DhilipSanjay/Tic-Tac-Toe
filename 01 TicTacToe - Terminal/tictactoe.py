matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(matrix)

playerOne = 1
playerTwo = 2

def print_matrix():
    print(matrix)
    for i in range(3):
        for j in range(3):
            current = "_"
            if matrix[i][j] == playerOne:
                current = "X"
            elif matrix[i][j] == playerTwo:
                current = "O"
            print(current, end = "\t")
        print("")

def validate_input(x, y):
    if x > 3 or y > 3:
        print("\nOut of bound! Enter again...\n")
        return False
    elif matrix[x][y] != 0:
        print("\nAlready entered! Try again...\n")
        return False
    return True
         
    
def get_input(currentPlayer):
    if currentPlayer == playerOne:
        print("\nPlayer One's Turn")
    else:
        print("\nPlayer Two's Turn")
    failed = 1
    while failed:
        try:
            x = int(input("Enter the x coordinate:"))
            y = int(input("Enter the y coordinate:"))
            if validate_input(x, y):
                matrix[x][y] = currentPlayer
                failed = 0
                print_matrix()
        except:
            print("Error occured! Try again..")
        

def check_rows():
    # print("Checking rows")
    result = 0
    for i in range(3):
        if matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2]:
            result = matrix[i][0]
            if result != 0:
                break
    return result

def check_columns():
    # print("Checking cols")
    result = 0
    for i in range(3):
        if matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i]:
            result = matrix[0][i]
            if result != 0:
                break
    return result

def check_diagonals():
    # print("Checking diagonals")
    result = 0
    if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
        result = matrix[0][0]
    elif matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
        result = matrix[0][2]
    return result

def check_winner():
    result = 0
    result = check_rows()
    if result == 0:
        result = check_columns()
    if result == 0:
        result = check_diagonals()
    return result

def main():
    result = 0
    i = 0
    while result == 0 and i < 9 :
        if (i%2 == 0):
            get_input(playerOne)
        else:
            get_input(playerTwo)
        result = check_winner()
        i = i + 1
        # print("Current count", i ,result == 0 and i < 9, "Result = ", result)
    
    if result == 1:
        print("Player one is the winner")
    elif result == 2:
        print("Player two is the winner")
    else:
        print("Draw")

main()
    

