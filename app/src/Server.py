import json
import socket
from api import Api

class Server:
    
    def __init__(self):
        self.clientsArray = []
        self.IP = '127.0.0.1'
        self.PORT = 64064
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.API = Api(self.IP, self.PORT)
        
    def startConnection(self):
        self.serverSocket.bind((self.IP, self.PORT))
        self.serverSocket.listen()
        
        while True:
            conn, client = self.serverSocket.accept()
            # servidor_ip = conn.laddr
            # cliente_ip = conn.raddr
            # print("Connected by ", client)
            # print("CONN ", conn)
            
            # RECEIVING FROM CLIENT
            while True:
                data = conn.recv(8192)
                print('Data no Servidor',data, client)
                
                if data:
                    # client[0] is IP; client[1] is PORT
                    if client[0] not in self.clientsArray: self.clientsArray.append(client)
                    print("Lixeiras: ", self.clientsArray)
                    
                    data = json.loads(data)
                    self.API.fetchMessage(data,client)
                
                else: break
                
            conn.close()
    
    def disconnect(self):
        self.serverSocket.close()
    
server = Server()
server.startConnection()