import tkinter as tk


root = tk.Tk()

class game:
    hp = 500
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
    def letsAttack(self,ar,enemytext):
        
        self.hp -=ar
        enemytext.config(text=self.hp)
        
   
    
    def new_screen(self,lab):
        characters = {}

        for char in self.name:
           characters[char["Name"].upper()] = char
        dat = lab.upper()
        
        ar =characters[dat]["AR"]
        health = characters[dat]["HP"]
        
        #  #new initial widgets
        self.clear_screen()
        enemytxt = tk.Label(root,text=f"Dragon:{self.hp}",height=4 ,width=10,font=("Arial", 16, "bold"))
        enemytxt.pack()
        
        txt = tk.Label(root,text=f"You have choosen {lab} \n What would you like to do? \n ")
        txt.pack()
        
        yrhlth = tk.Label(root,text=f"\n Your HP:{health}")
        yrhlth.pack(pady=1)
        
         
        attack = tk.Button(root,text="Attack",command= lambda:self.letsAttack(ar,enemytxt,health,yrhlth))
        attack.pack(pady=1)
        
       

        print(lab)
        
   
        

            
                   
    def createChar(self):
        for i in range(0,len(self.name)):
            lab = self.name[i]["Name"]
            if(i == 0):
                wiz = tk.Button(root,text=lab,command=lambda:self.new_screen("Wizard"))
                wiz.pack(pady=1)
            elif(i == 1):    
                arch = tk.Button(root,text=lab,command=lambda:self.new_screen("Archer"))
                arch.pack(pady=1)
            elif(i == 2):
                war = tk.Button(root,text=lab,command=lambda:self.new_screen("Warrior"))
                war.pack(pady=1)

       