import socket

# class Client:
HOST = '127.0.0.1'
PORT = 65423
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
        
#     def connect(self):
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((HOST, PORT))
    server.sendall("GOJIRA MELHOR BANDA DO MUNDO AMO DE PAIXÃO!!")
    data = server.recv(1024)

print("Received ", data)