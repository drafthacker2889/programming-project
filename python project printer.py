from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

win = Tk()

win.geometry("700x350")

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.txt')])
   if file:
      filepath = os.path.abspath(file.name)
      f=open(filepath,'r')
      t=f.read()
      Label(win, text=t , font=('Areial 11')).pack()
      f.close()


label = Label(win, text="select the file to print it", font=('Georgia 13'))
label.pack(pady=10)

ttk.Button(win, text="Browse", command=open_file).pack(pady=20)
win.mainloop()