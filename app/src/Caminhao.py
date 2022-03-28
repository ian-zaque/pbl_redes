from client import Client
class Caminhao(Client):
    
    def __init__(self, capacidade):
        super().__init__()
        self.lixeiras = []
        self.conteudo = 0
        self.locked = False