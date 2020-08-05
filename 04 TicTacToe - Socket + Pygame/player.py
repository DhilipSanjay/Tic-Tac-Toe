import pygame
import socket
import time
import threading
from queue import Queue

s = socket.socket()
host = input("Enter the server IP:")
port = 9999

playerOne = 1
playerOneColor = (255, 0, 0)
playerTwo = 2
playerTwoColor = (0, 0, 255)
player = ""
msg = ""
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#Threads
numOfThreads = 2
jobNumber = [1, 2] 
queue = Queue()

#Create worker threads
def create_workers():
    for _ in range(numOfThreads):
        t = threading.Thread(target=work) #argument - target function
        t.daemon = True
        t.start()


def create_jobs():
    for x in jobNumber:
        queue.put(x)
    
    queue.join()

#performs the next job in the queue
def work():
    while True:
        currentJob = queue.get()
        if currentJob == 1:
            start_player()
        if currentJob == 2:
            accept_msg()
        queue.task_done()


#initialize
pygame.init()

width = 600
height = 550
screen = pygame.display.set_mode((width, height))

#set title
pygame.display.set_caption("Tic Tac Toe")

#set icon
# icon = pygame.image.load("tictactoe.png")
# pygame.display.set_icon(icon)

#fonts
bigfont = pygame.font.Font('freesansbold.ttf', 64)
smallfont = pygame.font.Font('freesansbold.ttf', 32)
backgroundColor = (255, 255, 255)
titleColor = (0, 0, 0)
subtitleColor = (0, 0, 0)
lineColor = (0, 0, 0)

def buildScreen(player, string, playerColor = titleColor):
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
    centerMessage(player, playerColor)

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

def handleMouseEvent(pos):
    x = pos[0]
    y = pos[1]
    if(x < 150 or x > 450 or y < 150 or y > 450):
        return
    else:
        # When x increases, column changes
        col = int(x/100 - 1.5)
        # When y increases, row changes
        row = int(y/100 - 1.5)
        print("({}, {})".format(row,col))
        return row,col

def buildFinalScreen(msg):
    color = (0, 255, 0)
    # if result == 1:
    #     msg = "Player one is the winner!!"
    #     color = playerOneColor
    # elif result == 2:
    #     msg = "Player two is the winner!!"
    #     color = playerTwoColor
    # elif i >= 9:
    #     msg = "Draw game!! Try again later!"
    buildScreen(msg, "~~~Game Over~~~", color)

def start_player():
    global player
    try:
        s.connect((host, port))
        print("Connected to :", host, ":", port)
        recvData = s.recv(2048 * 10)
        player = recvData.decode()
        start_game()
        s.close()
    except socket.error as e:
        print("Socket connection error:", e) 



def start_game():
    running = True
    global msg
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x, y = handleMouseEvent(pos)
    
        buildScreen(player, msg)                      
        printMatrix(matrix) 
        pygame.display.update()


def accept_msg():
    global matrix
    global msg
    try: 
        recvData = s.recv(2048 * 10)
        recvDataDecode = recvData.decode()
        buildScreen(player, recvDataDecode)

        if recvDataDecode == "Input":
            failed = 1
            x = None
            y = None
            while failed:
                try:
                    coordinates = str(1)+"," + str(2)
                    s.send(coordinates.encode())
                    failed = 0
                except:
                    print("Error occured....Try again")

        elif recvDataDecode == "Error":
            print("Error occured! Try again..")
        
        elif recvDataDecode == "Matrix":
            print(recvDataDecode)
            matrixRecv = s.recv(2048 * 100)
            matrixRecvDecoded = matrixRecv.decode("utf-8")
            matrix = eval(matrixRecvDecoded)

        elif recvDataDecode == "Over":
            msgRecv = s.recv(2048 * 100)
            msgRecvDecoded = msgRecv.decode("utf-8")
            msg = msgRecvDecoded

    except:
        print("Error occured")


create_workers()
create_jobs()