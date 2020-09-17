"""
Aleksas Murauskas 260718389
Florence Diep 
ECSE 416
Lab 1: Client/Server
Server Side 
"""

#import statements
import socket

#Set server information 
ServerName = '127.0.0.1'
serverPort = 12345

#Create Socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind Socket to server name and Port number 
serverSocket.bind((ServerName, serverPort))
#Wait for a Client Request 
serverSocket.listen(1)
print('Server is awaiting Input')
while True: #Infinite loop to listen
    connectionSocket, addr = serverSocket.accept()
    print("Client Request recieved.")
    request = connectionSocket.recv(1024).decode()  
    filename = request
    #capitalizedSentence = request.upper()
    try:
		file = open(filename, "r")
	except IOError:
		print("File Does Not Exist, must send failed message")
		resp = "\HTTP/1.1 404 not found"

	file_content = file.read()
    
    #Send Server Response 
    #connectionSocket.send(capitalizedSentence.encode())
    print("Server Response Sent")
    connectionSocket.close()
    print("Socket closed and request completed.")


"""
import socket
serverPort = 12345
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()"""