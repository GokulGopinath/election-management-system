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

import edit_candidate_name_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    edit_candidate_name_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    edit_candidate_name_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:


    def database(self):
        #try:
        db = sqlite3.connect("castyourvote.db")
        
        candidate1  = self.c1.get()
        candidate2  = self.c2.get()
        candidate3  = self.c3.get()
        candidate4  = self.c4.get()


        if not(candidate1) or not(candidate2) or not(candidate3) or not(candidate4):
            messagebox.showerror("ERROR","Please fillup the details and then submit")
        else:
            with db:
                cursor = db.cursor()
           
            cursor.execute("update vote set candidate_name=? where candidate_no=1",(candidate1,))
            #cursor.execute("update vote set candidate_name={} where candidate_no=1".format(candidate1,))
            cursor.execute("update vote set candidate_name=? where candidate_no=2",(candidate2,))
            cursor.execute("update vote set candidate_name=? where candidate_no=3",(candidate3,))
            cursor.execute("update vote set candidate_name=? where candidate_no=4",(candidate4,))
            db.commit()



            global root
            root.destroy()
            filename='python admin.py'
            os.system(filename)
            











    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("623x450+391+160")
        top.title("Edit Candidate Name page")
        top.configure(background="#cc66ff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.144, rely=0.222, relheight=0.656, relwidth=0.73)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#CD5C5C")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#646464")
        self.Frame1.configure(width=455)

        self.l1 = tk.Label(self.Frame1)
        self.l1.place(relx=0.132, rely=0.237, height=21, width=71)
        self.l1.configure(activebackground="#f9f9f9")
        self.l1.configure(activeforeground="black")
        self.l1.configure(background="#d9d9d9")
        self.l1.configure(disabledforeground="#a3a3a3")
        self.l1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.l1.configure(foreground="#000000")
        self.l1.configure(highlightbackground="#d9d9d9")
        self.l1.configure(highlightcolor="black")
        self.l1.configure(text='''Candidate 1''')

        self.l2 = tk.Label(self.Frame1)
        self.l2.place(relx=0.132, rely=0.373, height=21, width=74)
        self.l2.configure(activebackground="#f9f9f9")
        self.l2.configure(activeforeground="black")
        self.l2.configure(background="#d9d9d9")
        self.l2.configure(disabledforeground="#a3a3a3")
        self.l2.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.l2.configure(foreground="#000000")
        self.l2.configure(highlightbackground="#d9d9d9")
        self.l2.configure(highlightcolor="black")
        self.l2.configure(text='''Candidate 2''')

        self.l3 = tk.Label(self.Frame1)
        self.l3.place(relx=0.121, rely=0.508, height=21, width=71)
        self.l3.configure(activebackground="#f9f9f9")
        self.l3.configure(activeforeground="black")
        self.l3.configure(background="#d9d9d9")
        self.l3.configure(disabledforeground="#a3a3a3")
        self.l3.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.l3.configure(foreground="#000000")
        self.l3.configure(highlightbackground="#d9d9d9")
        self.l3.configure(highlightcolor="black")
        self.l3.configure(text='''Candidate 3''')

        self.l4 = tk.Label(self.Frame1)
        self.l4.place(relx=0.121, rely=0.644, height=21, width=71)
        self.l4.configure(activebackground="#f9f9f9")
        self.l4.configure(activeforeground="black")
        self.l4.configure(background="#d9d9d9")
        self.l4.configure(disabledforeground="#a3a3a3")
        self.l4.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.l4.configure(foreground="#000000")
        self.l4.configure(highlightbackground="#d9d9d9")
        self.l4.configure(highlightcolor="black")
        self.l4.configure(text='''Candidate 4''')

        self.c1 = tk.Entry(self.Frame1)
        self.c1.place(relx=0.352, rely=0.237,height=20, relwidth=0.36)
        self.c1.configure(background="white")
        self.c1.configure(disabledforeground="#a3a3a3")
        self.c1.configure(font="TkFixedFont")
        self.c1.configure(foreground="#000000")
        self.c1.configure(highlightbackground="#d9d9d9")
        self.c1.configure(highlightcolor="black")
        self.c1.configure(insertbackground="black")
        self.c1.configure(selectbackground="#c4c4c4")
        self.c1.configure(selectforeground="black")

        self.c2 = tk.Entry(self.Frame1)
        self.c2.place(relx=0.352, rely=0.373,height=20, relwidth=0.36)
        self.c2.configure(background="white")
        self.c2.configure(disabledforeground="#a3a3a3")
        self.c2.configure(font="TkFixedFont")
        self.c2.configure(foreground="#000000")
        self.c2.configure(highlightbackground="#d9d9d9")
        self.c2.configure(highlightcolor="black")
        self.c2.configure(insertbackground="black")
        self.c2.configure(selectbackground="#c4c4c4")
        self.c2.configure(selectforeground="black")

        self.c3 = tk.Entry(self.Frame1)
        self.c3.place(relx=0.352, rely=0.508,height=20, relwidth=0.36)
        self.c3.configure(background="white")
        self.c3.configure(disabledforeground="#a3a3a3")
        self.c3.configure(font="TkFixedFont")
        self.c3.configure(foreground="#000000")
        self.c3.configure(highlightbackground="#d9d9d9")
        self.c3.configure(highlightcolor="black")
        self.c3.configure(insertbackground="black")
        self.c3.configure(selectbackground="#c4c4c4")
        self.c3.configure(selectforeground="black")

        self.c4 = tk.Entry(self.Frame1)
        self.c4.place(relx=0.352, rely=0.644,height=20, relwidth=0.36)
        self.c4.configure(background="white")
        self.c4.configure(disabledforeground="#a3a3a3")
        self.c4.configure(font="TkFixedFont")
        self.c4.configure(foreground="#000000")
        self.c4.configure(highlightbackground="#d9d9d9")
        self.c4.configure(highlightcolor="black")
        self.c4.configure(insertbackground="black")
        self.c4.configure(selectbackground="#c4c4c4")
        self.c4.configure(selectforeground="black")

        self.submit = tk.Button(self.Frame1)
        self.submit.place(relx=0.462, rely=0.814, height=24, width=49)
        self.submit.configure(activebackground="#ececec")
        self.submit.configure(activeforeground="#000000")
        self.submit.configure(background="#d9d9d9")
        self.submit.configure(disabledforeground="#a3a3a3")
        self.submit.configure(foreground="#000000")
        self.submit.configure(highlightbackground="#d9d9d9")
        self.submit.configure(highlightcolor="black")
        self.submit.configure(pady="0")
        self.submit.configure(command=self.database,text='''Submit''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.128, rely=0.044, height=71, width=465)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ffff00")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 23 -weight bold -underline 1")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Enter Name of the Candidates''')

if __name__ == '__main__':
    vp_start_gui()





