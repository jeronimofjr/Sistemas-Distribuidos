from socket import *
from time import sleep
from select import *
import sys

list_C = []
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)


clientSocket.connect((gethostname(), serverPort))


list_C.append(clientSocket)
list_C.append(sys.stdin)

while 1:
    r_sock = select(list_C, [], [])[0]

    for sock in r_sock:
        if sock == clientSocket:
            response = sock.recv(1024)
            response = response.decode()
            if response == 'end':
                print('\nEnd chat...')
                sys.exit()   
            else:
                sleep(0.5)
                sys.stdout.write('Server => ' + response + '\n')
                sys.stdout.flush()
        else:
            message = input()
            if message == 'end':
                clientSocket.send(message.encode())
                sys.stdout.flush()
                print('\nEnd chat...')
                sys.exit() 
            clientSocket.send(('Client => ' + message + '\n').encode())
            sys.stdout.flush()
