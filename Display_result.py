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

import Display_result_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Display_result_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Display_result_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:




    def display(self):
        db = sqlite3.connect('castyourvote.db')
        print("hi")
            
            
        with db:
            cursor = db.cursor()
        cursor.execute("select candidate_name from vote where votes=(select max(votes) from vote);")
        content = cursor.fetchall()
        #print(content[0][0],content[1][0],len(content))
        self.text=""
        if not content:
            text="Please conduct the election "
        elif len(content)==1:
            text="The winner of election is "+content[0][0]
        elif len(content)>1:
            text="There is a tie"
            

        db.commit()
        print(text)
        return text;
        #messagebox.showinfo("INFORMATION","The voters table Cleared!!!")

    def end_election(self):
        global root
        root.destroy()
   

    





    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''


        #self.txt=self.display()


        
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("606x286+374+142")
        top.title("New Toplevel")
        top.configure(background="#cc66ff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.083, rely=0.105, relheight=0.78
                , relwidth=0.847)
        self.Canvas1.configure(background="#cd5c5c")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="#296357")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief='ridge')
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=513)

        self.Label1 = tk.Label(self.Canvas1)
        self.Label1.place(relx=0.214, rely=0.045, height=61, width=284)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffff00")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#2a5f63")
        self.Label1.configure(text='''Display Result''')

        self.Button1 = tk.Button(self.Canvas1)
        self.Button1.place(relx=0.419, rely=0.762, height=24, width=77)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.end_election,text='''End Election''')

        self.Label2 = tk.Label(self.Canvas1)
        self.Label2.place(relx=0.214, rely=0.404, height=51, width=284)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text=self.display())
        self.Label2.configure(width=284)

if __name__ == '__main__':
    vp_start_gui()





