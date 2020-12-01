import tkinter as tk
import logging
import sqlite3 as database
from tkinter import ttk
root = tk.Tk()
root.title('Quotes everyday')
logger = logging.getLogger('Gui_logger')
logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)s %(message)s',level=logging.DEBUG)
def Login():
    newroot = tk.Tk()
    newroot.title('Login window')
    user_password = tk.IntVar()
    password_label = ttk.Label(newroot,text="Password")
    password_label.pack(side="left",padx=(0,10))
    entry1 = ttk.Entry(newroot,width=20,textvariable=user_password)
    entry1.pack(side="left")
    entry1.focus()
    
    user_email = tk.StringVar()
    user = ttk.Label(newroot,text="Email")
    user.pack(side="left")
    new  = ttk.Entry(newroot,width=20,textvariable=user_email)
    new.pack(side="left")
    new.focus()

    connection = database.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS user_info(password,email)')
    logger.debug("This will create a database")
    connection.commit()
    connection.close()
    print("Database created !")

    connection = database.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO user_info VALUES(?,?)',(user_password.get(),user_email.get()))
    logger.debug("This will insert into database")
    connection.commit()
    connection.close()
    print("Inserted into database !")

    connection = database.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user_info')
    logger.debug("This will print all the inserted data")
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    print(data)


    
login_button = ttk.Button(root,text='Login',command=Login).pack(side='top',
                                                                fill='both')


