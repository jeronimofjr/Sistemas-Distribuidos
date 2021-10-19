from socket import *
from time import sleep

# calculadora que executa as 4 funções básicas (+,-,∙,÷)
from calc import calculator

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print('The server is ready to receive')

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(f'Connected by {clientAddress[0]}')

    sleep(1)
    # desempacota a mensagem
    num1, op, num2 = message.decode().split(' ')

    # resultado da operação
    result = calculator(num1, num2, op)

    serverSocket.sendto(str(result).encode(), clientAddress)
    print(f'result sent to {clientAddress[0]}')
    #break
serverSocket.close()
