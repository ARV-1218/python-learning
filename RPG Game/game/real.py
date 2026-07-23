import tkinter as tk

root = tk.Tk()

lab = tk.Label(root,text="Choose your character",width=20,padx=80)
lab.pack()

characters =[
    {
        "ID":1,
        "Name":"Archer",
        "HP":200,
        "ROF":25
    },
    {
        "ID":2,
        "Name":"Warrior",
        "HP":200,
        "ROF":30
    }
]
hp = 500
char_instances = []
def choosechar():
    clear_screen()
    playgame()
    for i in characters:
        char = tk.Button(root,text=i["Name"])
        char.pack()
        char_instances.append(char)
        char.add
    
        
def playgame():
    dragHp = tk.Label(root,text=f"Dragon HP:{hp}")
    dragHp.pack()

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


btn  = tk.Button(root,text="CLICK",command=lambda:choosechar())

btn.pack()

root.geometry('300x400')
root.mainloop()
