import sys
sys.path.append('../')

import tkinter as tk
import tkinter.font as tkFont 
from src import lixeira, central

class View:
    def __init__(self, window):
        self.window = window
        self.lixeiras = []; self.index = 0
        self.central = central.Central('127.0.0.1',64064)
        
        # Variables to control itens placement
        self.widthButton = 55; self.heightButton = 25;
        self.xImg = 70; self.yImg = 40; self.widthImg = 106; self.heightImg = 84;
        self.xAddButton = 10; self.yAddButton = 40;
        self.xRemoveButton = 10; self.yRemoveButton = 70;
        self.xBlockButton = 10; self.yBlockButton = 100;
        self.xPercentage = 90; self.yPercentage = 10; self.widthPercentage=70; self.heightPercentage=25
        
        #setting title
        self.window.title("Coleta de Lixo")
        #setting self.window size
        width=600; height=500
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)

        self.ipLabel=tk.Label(self.window, name = "ipLabel")
        self.ipLabel["font"] = tkFont.Font(family='Times',size=10)
        self.ipLabel["fg"] = "#333333"
        self.ipLabel["justify"] = "center"
        self.ipLabel["text"] = "IP"
        self.ipLabel.place(x=10,y=460,width=35,height=25)

        self.ipInput=tk.Entry(self.window, name = "ipInput")
        self.ipInput.bind('<Enter>',self.bindCreateLixeirasEvent)
        self.ipInput["bg"] = "#ffffff"
        self.ipInput["borderwidth"] = "1px"
        self.ipInput["font"] = tkFont.Font(family='Times',size=10)
        self.ipInput["fg"] = "#333333"
        self.ipInput["justify"] = "center"
        self.ipInput["text"] = ""
        self.ipInput.place(x=40,y=460,width=90,height=25)

        self.capacidadeLabel=tk.Label(self.window, name = "capacidadeLabel")
        self.capacidadeLabel["font"] = tkFont.Font(family='Times',size=10)
        self.capacidadeLabel["fg"] = "#333333"
        self.capacidadeLabel["justify"] = "center"
        self.capacidadeLabel["text"] = "Capacidade"
        self.capacidadeLabel.place(x=150,y=460,width=70,height=25)

        self.capacidadeInput=tk.Entry(self.window, name = "capacidadeInput")
        self.capacidadeInput.bind('<Enter>',self.bindCreateLixeirasEvent)
        self.capacidadeInput["bg"] = "#f8f8f8"
        self.capacidadeInput["borderwidth"] = "1px"
        self.capacidadeInput["font"] = tkFont.Font(family='Times',size=10)
        self.capacidadeInput["fg"] = "#333333"
        self.capacidadeInput["justify"] = "center"
        self.capacidadeInput["text"] = ""
        self.capacidadeInput.place(x=220,y=460,width=50,height=25)

        # Button that creates Lixeiras
        self.btnCreateLixeiras = tk.Button(self.window, name = "btnCreateLixeiras")
        self.btnCreateLixeiras.bind('<Enter>',self.bindCreateLixeirasEvent)
        self.btnCreateLixeiras["bg"] = "#efefef"
        self.btnCreateLixeiras["font"] = tkFont.Font(family='Times',size=10)
        self.btnCreateLixeiras["fg"] = "#000000"
        self.btnCreateLixeiras["justify"] = "center"
        self.btnCreateLixeiras["text"] = "Add Lixeira"
        self.btnCreateLixeiras.place(x=290,y=460,width=75,height=25)
        self.btnCreateLixeiras["command"] = self.btnCreateLixeiras_command

    
    def createLixeira(self, IP, capacidade):
        
        if len(self.lixeiras) == 0:
            # print('1111111111111111111',self.lixeiras)
            self.widthButton = 55; self.heightButton = 25;
            self.xAddButton = 10; self.yAddButton = 40;
            self.xRemoveButton = 10; self.yRemoveButton = 70;
            self.xBlockButton = 10; self.yBlockButton = 100;
            self.xPercentage = 70; self.yPercentage = 50; self.widthPercentage=70; self.heightPercentage=25
            self.xIp = 70; self.yIp = 90; self.widthIp = 70; self.heightIp = 25;
        
        else:
            # print('2222222222222222222',self.lixeiras)
            self.xAddButton = self.xAddButton + 190;
            self.xRemoveButton = self.xRemoveButton + 190;
            self.xBlockButton = self.xBlockButton + 190;
            self.xPercentage = self.xPercentage + 190;
            self.xIp = self.xIp + 190;

        # Add Lixo Button
        addButton=tk.Button(self.window, name = "addButton" + str(self.index))
        addButton["bg"] = "#efefef"
        addButton["font"] = tkFont.Font(family='Times',size=10)
        addButton["fg"] = "#000000"
        addButton["justify"] = "center"
        addButton["text"] = "Add"
        addButton.place(x = self.xAddButton, y = self.yAddButton, width = self.widthButton, height =self.heightButton)

        # Remove Lixo BUtton
        removeButton=tk.Button(self.window, name = "removeButton" + str(self.index))
        removeButton["bg"] = "#efefef"
        removeButton["font"] = tkFont.Font(family='Times',size=10)
        removeButton["fg"] = "#000000"
        removeButton["justify"] = "center"
        removeButton["text"] = "Remover"
        removeButton.place(x=self.xRemoveButton, y=self.yRemoveButton, width=self.widthButton, height=self.heightButton)
        # removeButton["command"] = self.GButton_311_command

        # Bloquear Lixeira Button
        blockButton=tk.Button(self.window, name = "blockButton" + str(self.index))
        blockButton["bg"] = "#efefef"
        blockButton["font"] = tkFont.Font(family='Times',size=10)
        blockButton["fg"] = "#000000"
        blockButton["justify"] = "center"
        blockButton["text"] = "Bloquear"
        blockButton.place(x=self.xBlockButton, y=self.yBlockButton, width=self.widthButton, height=self.heightButton)
        # blockButton["command"] = self.GButton_519_command

        ipLabel=tk.Label(self.window)
        ipLabel["font"] = tkFont.Font(family='Times',size=10)
        ipLabel["fg"] = "#333333"
        ipLabel["justify"] = "center"
        ipLabel["text"] = IP
        ipLabel.place(x= self.xIp, y=self.yIp, width= self.widthIp, height= self.heightIp)

        # Percentage Label
        percentage=tk.Label(self.window, name = "percentage" + str(self.index))
        percentage["font"] = tkFont.Font(family='Times',size=10)
        percentage["fg"] = "#333333"
        percentage["justify"] = "center"
        percentage["text"] = str(0) + " % (" + str(capacidade) + ")"
        percentage["relief"] = "flat"
        percentage.place(x=self.xPercentage, y=self.yPercentage, width=self.widthPercentage, height=self.heightPercentage)        
        
        lixeiraModel = lixeira.Lixeira(IP, capacidade)
        lixeiraModel.startConnection()
        
        self.lixeiras.append({
            'addButton' : addButton,
            'removeButton': removeButton,
            'blockButton' : blockButton,
            'percentage': percentage,
            'self.index': self.index,
            'IP': IP,
            'Capacidade': capacidade,
            'ID': hash(IP + str(self.index)),
            'lixeira': lixeiraModel
        })
        
        self.index = self.index + 1
        self.capacidadeInput.delete(0,tk.END); self.capacidadeInput.insert(0,'')
        self.ipInput.delete(0,tk.END); self.ipInput.insert(0,'')
        
        addButton["command"] = self.addButtonCommand(lixeiraModel.IP, hash(IP + str(self.index-1)))
        

    def btnCreateLixeiras_command(self):      
        self.createLixeira(self.ipInput.get(),self.capacidadeInput.get())

    def bindCreateLixeirasEvent(self,event):
        if self.ipInput.get() == '' or self.capacidadeInput.get() == '': self.btnCreateLixeiras['state'] = 'disabled'
        elif self.ipInput.get() != '' and self.capacidadeInput.get() != '': self.btnCreateLixeiras['state'] = 'normal'

    def addButtonCommand(self, lixeiraIp, lixeiraId):
        self.central.addLixo(lixeiraIp, lixeiraId)
        self.central.getLixeira(lixeiraIp, lixeiraId)

if __name__ == "__main__":
    window = tk.Tk()
    app = View(window)
    window.mainloop()
