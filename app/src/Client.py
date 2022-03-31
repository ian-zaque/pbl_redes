import json
import socket

class Client:
    
    def __init__(self):
        self.IP = '127.0.0.1'
        self.PORT = 64064
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    def getIP(self):
        return self.IP
    
    def startConnection(self):
        self.clientSocket.connect((self.IP, self.PORT))
    
    def createMessage(self,message, data):
        body = {'message': message, 'data': data}
        msg = json.dumps(body).encode("utf-8")
        print('Sending Message From client',msg)
        self.clientSocket.sendall(msg)
    
    def disconnect(self):
        self.clientSocket.close()