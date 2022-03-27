import tkinter as tk
import tkinter.font as tkFont
# from Lixeira import Lixeira 

class App:
    def __init__(self, root):        
        #setting title
        root.title("Coleta de Lixo")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        btnCreateLixeiras = tk.Button(root)
        btnCreateLixeiras=tk.Button(root)
        btnCreateLixeiras["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        btnCreateLixeiras["font"] = ft
        btnCreateLixeiras["fg"] = "#000000"
        btnCreateLixeiras["justify"] = "center"
        btnCreateLixeiras["text"] = "Add Lixeira"
        btnCreateLixeiras.place(x=10,y=460,width=75,height=25)
        btnCreateLixeiras["command"] = self.btnCreateLixeiras_command(root)
        
    
    def createLixeira(self,root):
        GLineEdit_514=tk.Entry(root)
        GLineEdit_514["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_514["font"] = ft
        GLineEdit_514["fg"] = "#333333"
        GLineEdit_514["justify"] = "center"
        GLineEdit_514["text"] = "Lixeira N"
        GLineEdit_514.place(x=70,y=40,width=106,height=84)

        GButton_655=tk.Button(root)
        GButton_655["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_655["font"] = ft
        GButton_655["fg"] = "#000000"
        GButton_655["justify"] = "center"
        GButton_655["text"] = "Add"
        GButton_655.place(x=10,y=40,width=55,height=25)
        GButton_655["command"] = self.GButton_655_command

        GButton_311=tk.Button(root)
        GButton_311["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_311["font"] = ft
        GButton_311["fg"] = "#000000"
        GButton_311["justify"] = "center"
        GButton_311["text"] = "Remover"
        GButton_311.place(x=10,y=70,width=55,height=25)
        GButton_311["command"] = self.GButton_311_command

        GButton_519=tk.Button(root)
        GButton_519["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_519["font"] = ft
        GButton_519["fg"] = "#000000"
        GButton_519["justify"] = "center"
        GButton_519["text"] = "Bloquear"
        GButton_519.place(x=10,y=100,width=55,height=25)
        GButton_519["command"] = self.GButton_519_command

        GLabel_551=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_551["font"] = ft
        GLabel_551["fg"] = "#333333"
        GLabel_551["justify"] = "center"
        GLabel_551["text"] = "%"
        GLabel_551["relief"] = "flat"
        GLabel_551.place(x=90,y=10,width=70,height=25)
    

    def GButton_655_command(self):
        print("command")


    def GButton_311_command(self):
        print("command")


    def GButton_519_command(self):
        print("command")

    def btnCreateLixeiras_command(self,root):
        self.createLixeira(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
