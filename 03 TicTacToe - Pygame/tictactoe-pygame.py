import pygame

i = 0
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(matrix)

playerOne = 1
playerOneColor = (255, 0, 0)
playerTwo = 2
playerTwoColor = (0, 0, 255)

#initialize
pygame.init()

width = 600
height = 550
screen = pygame.display.set_mode((width, height))

#set title
pygame.display.set_caption("Tic Tac Toe")

#set icon
icon = pygame.image.load("tictactoe.png")
pygame.display.set_icon(icon)

#fonts
bigfont = pygame.font.Font('freesansbold.ttf', 64)
smallfont = pygame.font.Font('freesansbold.ttf', 32)
backgroundColor = (255, 255, 255)
titleColor = (0, 0, 0)
subtitleColor = (128, 0, 255)
lineColor = (0, 0, 0)

def buildScreen(string, playerColor = subtitleColor):
    screen.fill(backgroundColor)
    
    #vertical lines
    pygame.draw.line(screen, lineColor, (250-2, 150), (250-2, 450), 4)
    pygame.draw.line(screen, lineColor, (350-2, 150), (350-2, 450), 4)
    #horizontal lines
    pygame.draw.line(screen, lineColor, (150, 250-2), (450, 250-2), 4)
    pygame.draw.line(screen, lineColor, (150, 350-2), (450, 350-2), 4)

    title = bigfont.render("TIC TAC TOE", True, titleColor)
    screen.blit(title, (110, 0))
    subtitle = smallfont.render(str.upper(string), True, playerColor)
    screen.blit(subtitle, (150, 70))

def centerMessage(msg, color = titleColor):
    pos = (100, 480)
    # screen.fill(backgroundColor)
    msgRendered = smallfont.render(msg, True, color)
    screen.blit(msgRendered, pos)

def printCurrent(current, pos, color):
    currentRendered = bigfont.render(str.upper(current), True, color)
    screen.blit(currentRendered, pos)

def printMatrix(matrix):
    for i in range(3):
        #When row increases, y changes
        y = int((i + 1.75) * 100) 
        for j in range(3):
            #When col increases, x changes
            x =  int((j + 1.75) * 100)
            current = " "
            color = titleColor
            if matrix[i][j] == playerOne:
                current = "X"
                color = playerOneColor
            elif matrix[i][j] == playerTwo:
                current = "O"
                color = playerTwoColor
            printCurrent(current, (x, y), color)

def handleMouseEvent(matrix, pos):
    global i
    x = pos[0]
    y = pos[1]
    if(x < 150 or x > 450 or y < 150 or y > 450 or result != 0 or i >= 9):
        return
    else:
        # When x increases, column changes
        col = int(x/100 - 1.5)
        # When y increases, row changes
        row = int(y/100 - 1.5)
        print("({}, {})".format(row,col))
        if validate_input(row, col):
            if i%2 == 0:
                matrix[row][col] = playerOne
            else: 
                matrix[row][col] = playerTwo
            i = i + 1

def validate_input(x, y):
    if x > 3 or y > 3:
        print("\nOut of bound! Enter again...\n")
        return False
    elif matrix[x][y] != 0:
        print("\nAlready entered! Try again...\n")
        return False
    return True
                

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

def buildFinalScreen(result):
    buildScreen("~~~Game Over~~~")
    if result == 1:
        centerMessage("Player one is the winner!!", playerOneColor)
    elif result == 2:
        centerMessage("Player two is the winner!!", playerTwoColor)
    elif i >= 9:
        centerMessage("Draw game!! Try again later!")

if __name__ == "__main__":
    result = 0
    i = 0
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                handleMouseEvent(matrix, pos)
        if i%2 == 0:
            buildScreen("Player One's Turn", playerOneColor)
        else:
            buildScreen("Player Two's Turn", playerTwoColor)

        result = check_winner()
        if i >= 9 or result != 0:
            buildFinalScreen(result)
                              
        printMatrix(matrix) 
        pygame.display.update()