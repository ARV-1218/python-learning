import tkinter as tk


root = tk.Tk()
class game:

    def __init__(self,name):
        #initial widgets
        self.name = name
       
        ranTxt = tk.Label(root,text="Choose your character:",height=3,font=("Arial",10))
        ranTxt.pack()
        
        self.createChar()
        root.geometry("300x400")
        root.mainloop()
        
    def charName(self):
        return self.name

    def clear_screen(self):
        for widget in root.winfo_children():
            widget.destroy()

    def new_screen(self,lab):
         #new initial widgets
        hp = 500
        enemytxt = tk.Label(root,text=f"Dragon:{hp}",height=4 ,width=10,font=("Arial", 16, "bold"))
        enemytxt.pack()
        
        txt = tk.Label(root,text=f"You have choosen {lab} \n What would you like to do?")
        txt.pack()
           
    
    def createChar(self):
        for i in range(0,len(self.name)):
            lab = self.name[i]["Name"]
            the_Char = tk.Button(root,text=lab,command=lambda:[self.clear_screen(),self.new_screen(lab)])
            the_Char.pack(pady=2)
        print(len(self.name))

       