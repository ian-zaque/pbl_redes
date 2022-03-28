from os import remove
import tkinter as tk
import tkinter.font as tkFont
# from Lixeira import Lixeira 

class App:
    def __init__(self, window):
        self.window = window
        self.lixeiras = []
        
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

        ipLixeiraButton=tk.Button(self.window)
        ipLixeiraButton["bg"] = "#efefef"
        ipLixeiraButton["font"] = tkFont.Font(family='Times',size=10)
        ipLixeiraButton["fg"] = "#000000"
        ipLixeiraButton["justify"] = "center"
        ipLixeiraButton["text"] = "Remover"
        ipLixeiraButton.place(x=10,y=70,width=55,height=25)
        ipLixeiraButton["command"] = self.ipLixeiraButton_command

        # Button that creates Lixeiras
        btnCreateLixeiras = tk.Button(self.window)
        btnCreateLixeiras=tk.Button(self.window)
        btnCreateLixeiras["bg"] = "#efefef"
        btnCreateLixeiras["font"] = tkFont.Font(family='Times',size=10)
        btnCreateLixeiras["fg"] = "#000000"
        btnCreateLixeiras["justify"] = "center"
        btnCreateLixeiras["text"] = "Add Lixeira"
        btnCreateLixeiras.place(x=10,y=460,width=75,height=25)
        btnCreateLixeiras["command"] = self.btnCreateLixeiras_command
    
    
    def createLixeira(self):
        if len(self.lixeiras) == 0:
            self.widthButton = 55; self.heightButton = 25;
            self.xImg = 70; self.yImg = 40; self.widthImg = 106; self.heightImg = 84;
            self.xAddButton = 10; self.yAddButton = 40;
            self.xRemoveButton = 10; self.yRemoveButton = 70;
            self.xBlockButton = 10; self.yBlockButton = 100;
            self.xPercentage = 90; self.yPercentage = 10; self.widthPercentage=70; self.heightPercentage=25
        
        else:
            print('SIZE SIZE',self.lixeiras)
            self.xImg = self.xImg+ 190;
            self.xAddButton = self.xAddButton + 190;
            self.xRemoveButton = self.xRemoveButton + 190;
            self.xBlockButton = self.xBlockButton + 190;
            self.xPercentage = self.xPercentage + 190;
         
        # img
        img=tk.Entry(self.window)
        img["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        img["font"] = ft
        img["fg"] = "#333333"
        img["justify"] = "center"
        # img["text"] = "Lixeira " + IP + ':' + str(PORT)
        img["text"] = "Lixeira "
        img.place(x = self.xImg, y = self.yImg, width = self.widthImg, height = self.heightImg)

        # Add Lixo Button
        addButton=tk.Button(self.window)
        addButton["bg"] = "#efefef"
        addButton["font"] = tkFont.Font(family='Times',size=10)
        addButton["fg"] = "#000000"
        addButton["justify"] = "center"
        addButton["text"] = "Add"
        addButton.place(x = self.xAddButton, y = self.yAddButton, width = self.widthButton, height =self.heightButton)
        addButton["command"] = self.GButton_655_command

        # Remove Lixo BUtton
        removeButton=tk.Button(self.window)
        removeButton["bg"] = "#efefef"
        removeButton["font"] = tkFont.Font(family='Times',size=10)
        removeButton["fg"] = "#000000"
        removeButton["justify"] = "center"
        removeButton["text"] = "Remover"
        removeButton.place(x=self.xRemoveButton, y=self.yRemoveButton, width=self.widthButton, height=self.heightButton)
        removeButton["command"] = self.GButton_311_command

        # Bloquear Lixeira Button
        blockButton=tk.Button(self.window)
        blockButton["bg"] = "#efefef"
        blockButton["font"] = tkFont.Font(family='Times',size=10)
        blockButton["fg"] = "#000000"
        blockButton["justify"] = "center"
        blockButton["text"] = "Bloquear"
        blockButton.place(x=self.xBlockButton, y=self.yBlockButton, width=self.widthButton, height=self.heightButton)
        blockButton["command"] = self.GButton_519_command

        # Percentage Label
        percentage=tk.Label(self.window)
        percentage["font"] = tkFont.Font(family='Times',size=10)
        percentage["fg"] = "#333333"
        percentage["justify"] = "center"
        percentage["text"] = "%"
        percentage["relief"] = "flat"
        percentage.place(x=self.xPercentage, y=self.yPercentage, width=self.widthPercentage, height=self.heightPercentage)        
        
        self.lixeiras.append({
            'img': img,
            'addButton' : addButton,
            'removeButton': removeButton,
            'blockButton' : blockButton,
            'percentage': percentage
        })

    def GButton_655_command(self):
        print("command")


    def GButton_311_command(self):
        print("command")


    def GButton_519_command(self):
        print("command")

    def btnCreateLixeiras_command(self):
        print('aaaaa',self.lixeiras)
        self.createLixeira()

if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()
