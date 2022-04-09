from client import Client

class Central(Client):
    
    def __init__(self):
        super().__init__()
        self.lixeiras = {}
        self.startConnection()
    
    def lockLixeira(self,lixeiraIp, lixeiraID):
        self.createMessage('central/LockLixeira',{'IP': lixeiraIp, 'ID': lixeiraID})
        
    def unlockLixeira(self,lixeiraIp, lixeiraID):
        self.createMessage('central/unLockLixeira',{'IP': lixeiraIp, 'ID': lixeiraID})
    
    def addLixo(self, lixeiraIp, lixeiraID):
        self.createMessage('central/addLixo',{'IP': lixeiraIp, 'ID': lixeiraID})
    
    def removeLixo(self, lixeiraIp, lixeiraID):
        self.createMessage('central/removeLixo',{'IP': lixeiraIp, 'ID': lixeiraID})
    
    def getLixeira(self, lixeiraIP, lixeiraID):
        self.createMessage('central/getLixeira',{'IP': lixeiraIP, 'ID': lixeiraID})
    
    def getAllLixeiras(self):
        self.createMessage('central/lixeiras',{})
        
central = Central()
central.getAllLixeiras()