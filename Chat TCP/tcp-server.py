from time import sleep
from os import system
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

# loop que faz o servidor ficar esperando requisições
while 1:  
     print('The server is ready to receive')   
     connectionSocket, addr = serverSocket.accept()
     if connectionSocket:
          print(f'Connected by {addr[0]}')
          while 1:
               sentence = connectionSocket.recv(1024)
               if sentence:
                    sleep(0.5)

                    print(f'Client=> {sentence.decode()}')
                    sentence = input('Server=> ')
                    connectionSocket.send(sentence.encode())
               else:
                    break
     connectionSocket.close()
     print('connection terminated')
     sleep(2)
     system('clear')
          
#connectionSocket.close()

