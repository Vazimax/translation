from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Dictionary')

connect = sqlite3.connect("database\dictionary.db")
cursor = connect.cursor()

Label(root , text= "Enter word :").grid(column=0,row=0)
Label(root , text= "Translation :").grid(column=0,row=1)

word = ttk.Entry(root , width = 40)
word.grid(column=1,row=0)

translation = ttk.Entry(root , width = 40)
translation.grid(column=1,row=1)

def looking_for(event):
    the_word = word.get()
    x = cursor.execute('select * from en2cn')
    for row in x :
        if the_word = row[1]:
            translation.delete(0,"end")
            translation.insert("end",row[2])
            break


word.bind("<Return>" , looking_for)

root.mainloop()


