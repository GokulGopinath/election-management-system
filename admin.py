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

import admin_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    admin_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    admin_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:





    def edit_candidate(self):
        
        global root
        root.destroy()
        filename='python edit_candidate_name.py'
        os.system(filename)
 


   

    def clear_voters_table(self):
        db = sqlite3.connect('election.db')
        
        
        with db:
            cursor = db.cursor()
        cursor.execute("DELETE FROM voter")
        db.commit()
        messagebox.showinfo("INFORMATION","The voters table Cleared!!!")

#In start first voters table will be deleted and in the voters table and then start page will be opened. ALSO TEST CODE BELOW
    def start_election(self):
        db = sqlite3.connect('election.db')
        
        
        with db:
            cursor = db.cursor()
        cursor.execute("DELETE FROM voter")
        
        db.commit()
        db = sqlite3.connect('castyourvote.db')
        with db:
            cursor = db.cursor()
        cursor.execute( "update vote set votes=0")
        db.commit()
        global root
        root.destroy()
        filename='python startpage.py'
        os.system(filename)
 
        
    def display_result(self):
        global root
        root.destroy()
        filename='python Display_result.py'
        os.system(filename)












    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("606x450+374+142")
        top.title("Admin Page")
        top.configure(background="#cc66ff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.083, rely=0.111, relheight=0.762, relwidth=0.847)
        self.Canvas1.configure(background="#CD5C5C")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="#296357")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief='ridge')
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=513)

        self.Label1 = tk.Label(self.Canvas1)
        self.Label1.place(relx=0.39, rely=0.029, height=61, width=114)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffff00")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#2a5f63")
        self.Label1.configure(text='''Admin''')

        self.Button1 = tk.Button(self.Canvas1)
        self.Button1.place(relx=0.37, rely=0.598, height=24, width=131)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.clear_voters_table,text='''Clear Voters Table''')

        self.Button2 = tk.Button(self.Canvas1)
        self.Button2.place(relx=0.38, rely=0.437, height=24, width=125)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.edit_candidate,text='''Edit Candidate Name''')

        self.Button4 = tk.Button(self.Canvas1)
        self.Button4.place(relx=0.409, rely=0.787, height=24, width=84)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(command=self.display_result,text='''Display Result''')

        self.Button5 = tk.Button(self.Canvas1)
        self.Button5.place(relx=0.419, rely=0.277, height=24, width=87)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(command=self.start_election,text='''Start Election''')

if __name__ == '__main__':
    vp_start_gui()





