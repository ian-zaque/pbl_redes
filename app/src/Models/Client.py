import socket

class Client:
    
    def __init__(self):
        self.HOST = socket.gethostname()
        # self.IP = socket.gethostbyname(self.HOST)
        self.IP = '127.0.0.1'
        self.PORT = 65423
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
    def startConnection(self):
        self.clientSocket.connect((self.IP, self.PORT))
    
    def sendMessage(self,message):
        print('Sending Message From client',message)
        self.clientSocket.sendall(message)
    
    def disconnect(self):
        self.clientSocket.close()