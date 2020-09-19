"""
Aleksas Murauskas 260718389
Florence Diep     260727117
ECSE 416
Lab 1: Client/Server
Server Side 
"""

#import statements
import socket
import sys
from PIL import Image
import io
#Set server information 
ServerName = '127.0.0.2'
serverPort = 12345
#Create Socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind Socket to server name and Port number 
serverSocket.bind((ServerName, serverPort))
#Wait for a Client Request 
serverSocket.listen(1)
while True: #Infinite loop to listen
    connectionSocket, addr = serverSocket.accept()
    print("Client Request received.")
    filerequest = connectionSocket.recv(1024).decode()
    filename = filerequest
    try:
        if(filename.endswith(".txt")):
            file_content = open(filename, "r").read()
            print(type(file_content))
            mimetype = "text/html"
        elif(filename.endswith(".jpg")):
            img = Image.open(filename)
            file_content = img.tobytes()
            # file_content = Image.open(filename)
            mimetype = "image/jpg"
    except IOError:
        print("Unknown file, must send failed message")
        resp = "\HTTP/1.1 404 not found"
        connectionSocket.send(resp.encode())
        print("Server Response Sent.")
        connectionSocket.close()
        print("Socket closed and request cannot be completed.")
        continue
    resp = "HTTP/1.1 200 OK"
    connectionSocket.send(resp.encode())
    print("HTTP Response Sent.")
    connectionSocket.send(mimetype.encode("utf-8"))
    print("Content Type Response Sent.")
    # connectionSocket.send(file_content.encode())
    connectionSocket.send(file_content)
    print(img.size)
    print(type(img.size))
    print(tuple(bytes(img.size)))
    connectionSocket.send(bytes(img.size))
    print("File Content Response Sent.")
    #Send Server Response 
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