# from Caminhao import Caminhao
# from Lixeira import Lixeira

class Api:
    
    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port
        self.BASE_URL = self.IP + '/' + str(self.PORT)
        
    
    def fetchMessage(self,data,client):
        message = data['message']
        if 'data' in data: data = data['data']
        
        ##### LIXEIRA BALANCER #####        
        if message == 'changeLixeiraStatus':
            self.changeLixeiraStatus(client,message,data)
    
        elif message == 'emptyLixeira':
            self.emptyLixeira(client,message,data)
            
        elif message == 'fullLixeira':
            self.fullLixeira(client,message,data)
            
        elif message == 'alertLixeiraLimit':
            self.alertLixeiraLimit(client,message,data)

        elif message == 'lockLixeira':
            self.lockLixeira(client,message,data)
        
        elif message == 'unlockLixeira':
            self.unlockLixeira(client,message,data)    
        ##### LIXEIRA BALANCER #####   

    
    
    
    
    
    
    def changeLixeiraStatus(self,client,message,data):
        print(client,message,data)
    
    def emptyLixeira(self,client,message,data):
        print(client,message,data)
    
    def fullLixeira(self,client,message,data):
        print(client,message,data)
        
    def alertLixeiraLimit(self,client,message,data):
        print(client,message,data)
        
    def lockLixeira(self,client,message,data):
        print(client,message,data)
        
    def unlockLixeira(self,client,message,data):
        print(client,message,data)