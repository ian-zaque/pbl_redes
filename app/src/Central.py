import imp
from client import Client
from lixeira import Lixeira

class Central(Client):
    
    def __init__(self, IP, PORT):
        super().__init__(IP)
        self.IP = IP
        self.PORT = PORT
        self.IP = '127.0.0.1'
        self.PORT = 64064
    
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
        self.createMessage('central/lixeiras')