# from Caminhao import Caminhao
# from Lixeira import Lixeira

class Api:
    
    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port
        self.BASE_URL = self.IP + '/' + str(self.PORT)
        
    
    def fetchMessage(self,data,client):
        message = data['message']
        
        if 'data' in data:
            data = data['data']
        
        ##### LIXEIRA BALANCER #####        
        if message == 'changeLixeiraStatus':
            self.changeLixeiraStatus(client,message)
    
        elif message == 'emptyLixeira':
            self.emptyLixeira(client,message)
            
        elif message == 'fullLixeira':
            self.fullLixeira(client,message)
            
        elif message == 'alertLixeiraLimit':
            self.alertLixeiraLimit(client,message,data)

        elif message == 'lockedLixeira':
            self.lockedLixeira(client,message)
        ##### LIXEIRA BALANCER #####   

    
    
    
    
    
    
    def changeLixeiraStatus(self,client,message,data):
        print(message,data)
    
    def emptyLixeira(self,client,message):
        print(message)
    
    def fullLixeira(self,client,message):
        print(message)
        
    def alertLixeiraLimit(self,client,message,data):
        print(message,data)
        
    def lockedLixeira(self,client,message):
        print(message)