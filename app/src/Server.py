import json
import select, socket, sys, queue
from api import Api

class Server:
    
    def __init__(self):
        self.clientsArray = []
        self.IP = '127.0.0.1'
        self.PORT = 64064
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.API = Api(self.IP, self.PORT)
        
    def startConnection(self):
        # self.serverSocket.bind((self.IP, self.PORT))
        # self.serverSocket.listen()
        
        # while True:
        #     conn, client = self.serverSocket.accept()
        #     # servidor_ip = conn.laddr
        #     # cliente_ip = conn.raddr
        #     # print("Connected by ", client)
        #     # print("CONN ", conn)
            
        #     # RECEIVING FROM CLIENT
        #     while True:
        #         data = conn.recv(8192)
        #         print('Data no Servidor',data, client)
                
        #         if data:
        #             # client[0] is IP; client[1] is PORT
        #             if client[0] not in self.clientsArray: self.clientsArray.append(client)
        #             # print("Lixeiras: ", self.clientsArray)
                    
        #             data = json.loads(data)
        #             self.API.fetchMessage(data,client)
                
        #         else: break
                
        #     conn.close()
        
        self.serverSocket.setblocking(0)
        self.serverSocket.bind(('127.0.0.1', 64064))
        self.serverSocket.listen(5)
        inputs = [self.serverSocket]
        outputs = []
        message_queues = {}

        while inputs:
            readable, writable, exceptional = select.select(inputs, outputs, inputs)
            print('111111111111',readable)
            print('222222222222',writable)
            print('333333333333',exceptional)
            for s in readable:
                if s is self.serverSocket:
                    connection, client_address = s.accept()
                    # connection.setblocking(1)
                    inputs.append(connection)
                    message_queues[connection] = queue.Queue()
                else:
                    data = s.recv(1024)
                    print('Data no Servidor: ',data, client_address)
                    print('\n')
                    if data:
                        message_queues[s].put(data)
                        data = json.loads(data)
                        
                        # client_address[0] is IP; client_address[1] is PORT
                        if client_address[0] not in self.clientsArray: self.clientsArray.append({client_address: data['data'] })
                        print("Lixeiras: ", self.clientsArray)
                        print('\n')
                        
                        apiResponse = self.API.fetchMessage(data,client_address, self.clientsArray)
                        if apiResponse != None: self.serverSocket.sendto(json.dumps(apiResponse).encode("utf-8"), client_address)
                        
                        print('API RESPONSE: ', apiResponse)
                        print('\n')
                        
                        if s not in outputs:
                            outputs.append(s)
                            
                    else:
                        if s in outputs:
                            outputs.remove(s)
                        inputs.remove(s)
                        s.close()
                        del message_queues[s]

            for s in writable:
                try:
                    print('----------',s)
                    next_msg = message_queues[s].get_nowait()
                except queue.Empty:
                    outputs.remove(s)
                else:
                    # if apiResponse != None: self.serverSocket.sendto(json.dumps(apiResponse).encode("utf-8"), client_address)
                    s.send(next_msg)

            for s in exceptional:
                inputs.remove(s)
                if s in outputs:
                    outputs.remove(s)
                s.close()
                del message_queues[s]
    
    def disconnect(self):
        self.serverSocket.close()
    
server = Server()
server.startConnection()