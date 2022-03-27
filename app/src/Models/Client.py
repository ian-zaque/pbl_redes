import json
import socket

class Client:
    
    def __init__(self):
        self.HOST = socket.gethostname()
        print('CLIENT HOST: '+self.HOST)
        # self.IP = socket.gethostbyname(self.HOST)
        self.IP = '127.0.0.1'
        self.PORT = 64064
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
    def startConnection(self):
        self.clientSocket.connect((self.IP, self.PORT))
    
    def createMessage(self,message, data = None):
        if data == None:
            body = {'message': message}
            msg = json.dumps(body).encode("utf-8")
            self.sendMessage(msg)
        
        else:
            body = {'message': message, 'data': data}
            msg = json.dumps(body).encode("utf-8")
            self.sendMessage(msg)
    
    def sendMessage(self,message):
        print('Sending Message From client',message)
        self.clientSocket.sendall(message)
    
    def disconnect(self):
        self.clientSocket.close()