from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort)) # Establish TCP connection with server - 3 way handshake
message = input('Input lowercase sentence:')
clientSocket.send(message.encode()) # Once TCP connection is established, client can simply drop messages into the socket, without specifying address like UDP.
modifiedMessage = clientSocket.recv(1024)
print('From Server: ', modifiedMessage.decode())
clientSocket.close()