from client import Client

class Lixeira(Client):
    
    def __init__(self, ip, capacidade):
        super().__init__(ip)
        self.capacidade = capacidade
        self.conteudo = 0
        self.locked = False
        
    def getCapacity(self):
        return self.capacidade
    
    def getContent(self):
        return self.conteudo
    
    def getPercentage(self):
        return self.conteudo/self.capacidade
    
    def isLocked(self):
        return self.locked
    
    def toString(self):
        lixeira = {
            'IP': self.IP, 
            'PORT':self.PORT,
            'isLocked': self.isLocked(),
            'capacidade': self.getCapacity(),
            'conteudo': self.getContent(),
            'porcentagem': self.getPercentage()
        }
        return lixeira
    
    def lock(self):
        self.locked = True
        self.createMessage('lockLixeira',self.toString())
        
    def unlock(self):
        self.locked = False
        self.createMessage('unlockLixeira',self.toString())
    
    def removeLixo(self):
        if self.locked == False and self.conteudo > 0:
            self.conteudo = 0
            self.createMessage('emptyLixeira',self.toString())
    
    def insertLixo(self):
        if self.locked == False:
            
            if self.getPercentage() < 0.75:
                self.conteudo = self.conteudo + 1
                
            elif self.conteudo == self.capacidade:
                self.locked = True
                self.createMessage('fullLixeira',self.toString())
            
            else:
                self.createMessage('alertLixeiraLimit',self.toString())
                
        else:
            self.createMessage('lockedLixeira',self.toString())
            
# lixeira = Lixeira(5)
# lixeira.startConnection()
# print(lixeira.getContent(), lixeira.isLocked())
# lixeira.insertLixo()
# lixeira.insertLixo()
# lixeira.removeLixo()
# print(lixeira.getContent(), lixeira.isLocked())
# lixeira.insertLixo()
# lixeira.insertLixo()
# lixeira.insertLixo()
# lixeira.insertLixo()
# print(lixeira.getContent(), lixeira.isLocked())
# lixeira.insertLixo()
# lixeira.insertLixo()
# print(lixeira.getContent(), lixeira.isLocked())
            