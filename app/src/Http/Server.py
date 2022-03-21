import socket

# class Server:
HOST = '127.0.0.1'
PORT = 65423
    # def __init__(self, host, port):
        # self.host = host
        # self.port = port
        # self.host = '127.0.0.1'
        # self.port = 65423
        
    # def startConnection(self):
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(5)
    conn, addr = server.accept()
    
    with conn:
        print("Connected by ", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        
        
        