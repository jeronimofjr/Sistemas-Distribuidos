from socket import *
from time import sleep

serverName = 'localhost'

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

# é feita a leitura da expressão matemática
message = input('Enter your operation: ')

clientSocket.sendto(message.encode(), (serverName, serverPort))

# resultado enviado pelo server
result, serverAddress = clientSocket.recvfrom(2048)

sleep(1)
print(f'Operation result: {result.decode()}')
clientSocket.close()
