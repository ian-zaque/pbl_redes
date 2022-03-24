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
    
    def isLocked(self):
        return self.locked
    
    def setLocked(self):
        self.locked = not self.locked
        self.sendMessage("fechou man".encode("ascii"))
        # AVISAR AQUI QUE TRANCOU/DESTRANCOU
    
    def removeLixo(self):
        if self.locked == False and self.content > 0:
            self.content = 0
            self.sendMessage("tudo limpo por aqui".encode("ascii"))
            # AVISAR AQUI QUE ESVAZIOU
    
    def insertLixo(self):
        if self.locked == False:
            
            if self.content/self.capacidade < 0.9:
                self.content = self.content + 1
                
            elif self.content == self.capacidade:
                self.sendMessage("encheu pode parar".encode("ascii"))
                self.locked = True
            
            else:
                # AVISAR AQUI QUE BATEU O LIMITE, CHAMAR CAMINHÃO
                self.sendMessage("Ó o caminhao da merenda".encode("ascii"))
                
        else:
            self.sendMessage("lacrou".encode("ascii"))
            
lixeira = Lixeira(5)
print('AQUI 111111')
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
print('AQUI 2222222')
print(lixeira.getContent(), lixeira.isLocked())
lixeira.insertLixo()
lixeira.insertLixo()
print(lixeira.getContent(), lixeira.isLocked())
            