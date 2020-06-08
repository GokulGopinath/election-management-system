

import sys
import os

import sqlite3

from tkinter import*
from tkinter import messagebox



try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import login_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    login_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    login_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    #def error(self):



    def database(self):
        db = sqlite3.connect('election.db')
        username = self.Entry1.get()
        password1 = self.Entry2.get()
        with db:
            cursor = db.cursor()
        cursor.execute("SELECT * FROM voter where (u_name=? or password=? )and counter=0",(username,password1,))
        content = cursor.fetchall()
        print(content)

        if not content:
            messagebox.showerror("ERROR", "INVALID USERNAME OR PASSWORD OR YOU HAVE ALREADY VOTED ")
        else:
            cursor.execute("update voter set counter=1 where u_name=?",(username,))
            db.commit()
            global root
            root.destroy()
            filename='python vote.py'
            os.system(filename)
        





    # -------------------------------------

    def __init__(self, top=None):

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Courier New} -size 10"
        font13 = "-family {Arial} -size 24 -weight bold -underline 1"
        font15 = "-family {Times New Roman} -size 17 -weight bold"
        font17 = "-family {Segoe UI} -size 17 -weight bold"
        font18 = "-family {Times New Roman} -size 14 -weight bold"
        font9 = "-family {Segoe UI} -size 9"

        top.geometry("600x450+340+213")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.133, rely=0.2, relheight=0.656, relwidth=0.758)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=455)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.176, rely=0.237, height=31, width=108)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font15)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Username''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.165, rely=0.508, height=21, width=114)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font17)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Password''')
        self.Label3.configure(width=114)

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.484, rely=0.271,height=20, relwidth=0.36)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.495, rely=0.508,height=20, relwidth=0.36)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.352, rely=0.746, height=44, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font18)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.database,text='''LOGIN''')
        self.Button1.configure(width=97)

        self.menubar = tk.Menu(top, font=('Segoe UI', 9, ), bg=_bgcolor
                ,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.4, rely=0.044, height=48, width=119)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''SIGN IN''')
        self.Label1.configure(width=119)

if __name__ == '__main__':
    vp_start_gui()





