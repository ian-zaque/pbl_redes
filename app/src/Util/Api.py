
import imp
from Models.Caminhao import Caminhao
from Models.Lixeira import Lixeira


class Api:
    
    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port
        self.BASE_URL = self.IP + '/' + self.PORT
        
        
    #### ROUTES FOR LIXEIRA ####
    # def clearLixeira(self):
        # if 
    
    #### ROUTES FOR LIXEIRA ####