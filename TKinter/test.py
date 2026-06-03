import tkinter as tk

root = tk.Tk() 

tk.Label(root,text="First Name:").grid(row=0,column=0)
tk.Label(root,text="Last Name:").grid(row=1,column=0)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)


lab = tk.Label(root,text="Hello! I am Aarav")
lab.grid(row=3,column=0)

button = tk.Button(root,text="Stop",width=10,command=root.destroy)
button.grid(row=4,column=0)
root.geometry("400x300") 
root.mainloop()