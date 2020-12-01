import tkinter as tk
from tkinter import ttk

def calc():
    if user_op.get()=='+':
        print('Result :',user_num.get()+user_num1.get())
    if user_op.get()=='-':
        if user_num.get()>user_num1.get():
            print('Result : ',user_num.get()-user_num1.get())
        elif user_num.get()<user_num1.get():
            print('Result : ',user_num1.get()-user_num.get())
    if user_op.get()=='*':
        print('Result :',user_num.get()*user_num1.get())
    if user_op.get()=='/':
        if user_num.get()>user_num1.get():
            print('Result :',user_num.get()/user_num1.get())
        elif user_num1.get()>user_num.get():
            print('Result : ',user_num1.get()/user_num.get())
            

root = tk.Tk()
root.title('Calculator part1')



user_num = tk.IntVar()
name_num = ttk.Label(root,text="First number : ")
name_num.pack(side="left",padx=(0,10))
name_entry = ttk.Entry(root,width=15,textvariable=user_num)
name_entry.pack(side="left")
name_entry.focus()

user_num1 = tk.IntVar()
name_num1 = ttk.Label(root,text="Second number : ")
name_num1.pack(side="left",padx=(0,10))
name_entry1 = ttk.Entry(root,width=15,textvariable=user_num1)
name_entry1.pack(side="left")
name_entry1.focus()

user_op = tk.StringVar()
op = ttk.Label(root,text="Enter operator : ")
op.pack(side="left",padx=(0,10))
op_entry =  ttk.Entry(root,width=15,textvariable=user_op)
op_entry.pack(side="left")
op_entry.focus()

button = ttk.Button(root,text="Calculate",command=calc)
button.pack(side="left",fill="x",expand=True)

root.mainloop()

