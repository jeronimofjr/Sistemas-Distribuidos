from time import sleep
from os import system
from select  import select
from socket import *
import sys

list_C = []
serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)



list_C.append(serverSocket)
list_C.append(sys.stdin)

print('The server is ready to receive') 
while 1:     
     r_sock = select(list_C, [], [])[0] 

     for sock in r_sock:
          if sock == serverSocket:
            
            connectionSocket, addr = serverSocket.accept()
            list_C.append(connectionSocket)
            print(f'Connected by {addr[0]}')
            sys.stdout.flush()
          
          elif sock == sys.stdin:
            
            message = input()
            sys.stdout.flush()
            for elem in list_C:
                if elem == connectionSocket:
                    connectionSocket.send(message.encode())
          else:

            try:                
               sentence = sock.recv(1024)	
               sentence = sentence.decode()	
               if sentence:
                    if sentence == 'end':
                         sock.close()
                         list_C.remove(sock)
                         print('connection terminated')
                         sleep(1)
                         system('clear')
                         print('The server is ready to receive') 
                    else:
                         sleep(0.5)
                         sys.stdout.write(sentence)	    
                         sys.stdout.flush()
            except:               
               sock.close()
               list_C.remove(sock)
               continue

          
