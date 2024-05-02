from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1) # ServerSocket listens to incoming requests
print('The server is ready to receive')
while True:
  connectionSocket, addr = serverSocket.accept() # ConnectionSocket is created once TCP handshake is completed
  message = connectionSocket.recv(1024).decode()
  connectionSocket.send(message.upper().encode())
  connectionSocket.close()
