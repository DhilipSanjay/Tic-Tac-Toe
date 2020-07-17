import socket
import time

s = socket.socket()
host = input("Enter the server IP:")
port = 9999

def print_matrix(matrix):
    #print(matrix)
    for i in range(3):
        for j in range(3):
            current = "_"
            if matrix[i][j] == 1:
                current = "X"
            elif matrix[i][j] == 2:
                current = "O"
            print(current, end = "\t")
        print("")

def start_player():
    try:
        s.connect((host, port))
        print("Connected to :", host, ":", port)
        start_game()
        s.close()
    except socket.error as e:
        print("Socket connection error:", e) 

def start_game():
    welcome = s.recv(2048 * 10)
    print(welcome.decode())

    name = input("Enter Player name:")
    s.send(name.encode())

    while True:
        try: 
            recvData = s.recv(2048 * 10)
            recvDataDecode = recvData.decode()

            if recvDataDecode == "Input":
                x = int(input("Enter the x coordinate:"))
                y = int(input("Enter the y coordinate:"))
                coordinates = str(x)+"," + str(y)
                s.send(coordinates.encode())

            elif recvDataDecode == "Error":
                print("Error occured! Try again..")
            
            elif  recvDataDecode == "Matrix":
                print(recvDataDecode)
                matrixRecv = s.recv(2048 * 100)
                matrixRecvDecoded = matrixRecv.decode("utf-8")
                print_matrix(eval(matrixRecvDecoded))

            elif recvDataDecode == "":
                time.sleep(10)
                break

            else:
                print(recvDataDecode)
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt")
            time.sleep(2)
            break

start_player()