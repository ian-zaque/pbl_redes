import socket

class Server:
    
    def __init__(self):
        self.IP = '127.0.0.1'
        self.PORT = 65423
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def startConnection(self):
        self.serverSocket.bind((self.IP, self.PORT))
        self.serverSocket.listen()
        
        while True:
            conn, client = self.serverSocket.accept()
            # servidor_ip = conn.laddr
            # cliente_ip = conn.raddr
            # print("Connected by ", client)
            # print("CONN ", conn)
            
            while True:
                data = conn.recv(4096)
                print('Data no Servidor',data)
                
                if not data: break
                
                # conn.sendall(data)
                print(data)
                
            conn.close()
    
    def disconnect(self):
        self.serverSocket.close()
    
server = Server()
server.startConnection()