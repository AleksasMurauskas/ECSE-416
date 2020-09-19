"""
Aleksas Murauskas 260718389
Florence Diep     260727117
ECSE 416
Lab 1: Client/Server
Client Side 
"""
#import statements
import socket
import sys
from PIL import Image
import io

#Standard Server Name and Port Numbers and timeout 
serverName = '127.0.0.2'
serverPort = 12345
timeout= 5
#Parse command line inputs

if(len(sys.argv)==5): #In case of 5 aruments 0. client.py 1. [-host] 2. [-port] 3. [-filename] 4. [-timeout]
	serverName= str(sys.argv[1])
	serverPort = int(sys.argv[2])
	filename = str(sys.argv[3])
	timeout = int(sys.argv[4])


elif (len(sys.argv)==4): #In case of 4 aruments 0. client.py 1. [-host] 2. [-port] 3. [-filename]
	serverName= str(sys.argv[1])
	serverPort = int(sys.argv[2])
	filename = str(sys.argv[3])

else: #Incorrect Number of arguments
	print("Incorrect number of arguments, exiting program")
	sys.exit(1)

#Create Socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#set the timeout to the 
clientSocket.settimeout(timeout)
#Connect Socket
try:
	clientSocket.connect((serverName, serverPort))
except socket.error:
	print("Client Socket could not connect to server")
	sys.exit(1)

#Create File request
fileRequest = filename
clientSocket.send(fileRequest.encode())
print("Request Message Sent")

# receive server response
serverResponse = clientSocket.recv(1024)
print('Server HTTP Response: ', serverResponse.decode())
if(serverResponse=="\HTTP/1.1 404 not found"):
	print("404 Not Found")
	clientSocket.close()
	sys.exit(1)

# receive file content
mimetypeResponse = clientSocket.recv(1024).decode("utf-8")
print("Content-type: ", mimetypeResponse)
if(mimetypeResponse=="text/html"):
	file_content = clientSocket.recv(1024).decode("utf-8")
	print(file_content)
elif(mimetypeResponse=="image/jpg"):
	raw_img = clientSocket.recv(1024)
	size = tuple(clientSocket.recv(1024).decode("utf-8"))
	print(type(size))
	print(size)
	file_content = Image.frombytes('RGB', size, raw_img)
	Image.open(file_content).show()
clientSocket.close()
print("Socket Closed")
sys.exit(0)


"""
import socket

serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()
"""