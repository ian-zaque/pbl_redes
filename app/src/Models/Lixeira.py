from Client import Client
class Lixeira(Client):
    
    def __init__(self, capacidade):
        super().__init__()
        self.capacidade = capacidade
        self.content = 0
        self.locked = False
        
    def getCapacidade(self):
        return self.capacidade
    
    def getContent(self):
        return self.content
    
    def getPercentage(self):
        return self.content/self.capacidade
    
    def isLocked(self):
        return self.locked
    
    def setLocked(self):
        self.locked = not self.locked
        self.createMessage('changeLixeiraStatus',self.isLocked())
    
    def removeLixo(self):
        if self.locked == False and self.content > 0:
            self.content = 0
            self.createMessage('emptyLixeira')
    
    def insertLixo(self):
        if self.locked == False:
            
            if self.getPercentage() < 0.9:
                self.content = self.content + 1
                
            elif self.content == self.capacidade:
                self.locked = True
                self.createMessage('fullLixeira')
            
            else:
                self.createMessage('alertLixeiraLimit',self.getPercentage())
                
        else:
            self.createMessage('lockedLixeira')
            
lixeira = Lixeira(5)
lixeira.startConnection()
print(lixeira.getContent(), lixeira.isLocked())
lixeira.insertLixo()
lixeira.insertLixo()
lixeira.removeLixo()
print(lixeira.getContent(), lixeira.isLocked())
lixeira.insertLixo()
lixeira.insertLixo()
lixeira.insertLixo()
lixeira.insertLixo()
print(lixeira.getContent(), lixeira.isLocked())
lixeira.insertLixo()
lixeira.insertLixo()
print(lixeira.getContent(), lixeira.isLocked())
            