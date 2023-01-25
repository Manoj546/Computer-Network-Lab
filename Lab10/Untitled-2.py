from socket import *
serverName="Desktop"
serverPort=12530
serverSocket=socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print("ready to recieve")
while 1:
    ConnectionSocket,addr=serverSocket.accept()
    sentence=ConnectionSocket.recv(1024).decode()
    file=open(sentence,"r")
    l=file.read(1024)
    ConnectionSocket.send(l.encode())
    file.close()
    ConnectionSocket.close()



from socket import *
serverName="Desktop"
serverPort=12530
clientSocket=socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))
sentence=input("Enter file name")
clientSocket.send(sentence.encode())
filecontents=clientSocket.recv(1024).decode()
print('From server:', filecontents)
clientSocket.close()