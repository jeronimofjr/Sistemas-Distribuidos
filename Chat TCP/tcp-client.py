from socket import *
from time import sleep

serverName = 'localhost'

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)


clientSocket.connect((serverName, serverPort))

while 1:
    message = input('Client=> ')

    # encerra a conexão
    if message == 'end':
        break
        
    clientSocket.send(message.encode())

    response = clientSocket.recv(1024)

    sleep(0.5)
    print(f'Server=> {response.decode()}')

clientSocket.close()
print('End chat...')