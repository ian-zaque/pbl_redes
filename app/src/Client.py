import json
import socket

class Client:
    
    def __init__(self, ip):
        self.IP = ip
        self.IP = '127.0.0.1'
        self.PORT = 64064
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
    def startConnection(self):
        self.clientSocket.connect((self.IP, self.PORT))
    
    def createMessage(self,message, data):
        body = {'message': message, 'data': data}
        msg = json.dumps(body).encode("utf-8")
        self.sendMessage(msg)
    
    def sendMessage(self,message):
        print('Sending Message From client',message)
        self.clientSocket.sendall(message)
    
    def disconnect(self):
        self.clientSocket.close()