#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 28, 2019 09:38:52 PM IST  platform: Windows NT

#first open support and then otherfile
import sys
import sqlite3
from tkinter import *
import os

from tkinter import messagebox


#db.execute("CREATE TABLE IF NOT EXISTS voters (voter_no. int NOT NULL AUTO INCREMENT,voter_uname varchar(255),voter_pass varchar")


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

import signup_support
# nm=stringvar()
# unm=stringvar()
# password=stringvar()
# mob=intvar()







def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    signup_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    signup_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def database(self):
        #try:
        db = sqlite3.connect("election.db")
        #except Exception:
         #   tkMessageBox.showerror('Error', 'Error while connecting sqlite')
        name1 = self.nm.get()
        username1 =self.unm.get()
        password1 =self.password.get()
        mobile =self.mob.get()


       # with sqlite3.connect("election.sqlite") as db:
        with db:
            cursor = db.cursor()
       # cursor.execute('CREATE TABLE IF NOT EXISTS voter(name varchar(255) NOT NULL,u_name varchar(255) NOT NULL,password varchar(255) NOT NULL,Mobile_no int)')
        #try:
        cursor.execute("SELECT *FROM  voter WHERE u_name=?",(username1,))
        #note the coma after username1 above.it is to make it a tuple
        data=cursor.fetchall()
        if data:
             messagebox.showerror("ERROR","USERNAME ALREADY EXISTS")
        else:
            cursor.execute('INSERT INTO voter(name ,u_name,password,Mobile_no,counter) VALUES(? ,? ,? , ?,0)',(name1,username1, password1, mobile,))
            global root
            root.destroy()
            
            filename='python startpage.py'
            os.system(filename)
        #except Exception:
       #     tkMessageBox.showerror('Error', 'Error while connecting sqlite')

        db.commit()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''



        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+391+160")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.15, rely=0.222, relheight=0.656, relwidth=0.758)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#646464")
        self.Frame1.configure(width=455)

        self.l1 = tk.Label(self.Frame1)
        self.l1.place(relx=0.176, rely=0.237, height=21, width=39)
        self.l1.configure(activebackground="#f9f9f9")
        self.l1.configure(activeforeground="black")
        self.l1.configure(background="#d9d9d9")
        self.l1.configure(disabledforeground="#a3a3a3")
        self.l1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.l1.configure(foreground="#000000")
        self.l1.configure(highlightbackground="#d9d9d9")
        self.l1.configure(highlightcolor="black")
        self.l1.configure(text='''Name''')

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
        self.l2.configure(text='''Username''')

        self.l3 = tk.Label(self.Frame1)
        self.l3.place(relx=0.154, rely=0.508, height=21, width=58)
        self.l3.configure(activebackground="#f9f9f9")
        self.l3.configure(activeforeground="black")
        self.l3.configure(background="#d9d9d9")
        self.l3.configure(disabledforeground="#a3a3a3")
        self.l3.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.l3.configure(foreground="#000000")
        self.l3.configure(highlightbackground="#d9d9d9")
        self.l3.configure(highlightcolor="black")
        self.l3.configure(text='''Password''')

        self.l4 = tk.Label(self.Frame1)
        self.l4.place(relx=0.154, rely=0.644, height=21, width=64)
        self.l4.configure(activebackground="#f9f9f9")
        self.l4.configure(activeforeground="black")
        self.l4.configure(background="#d9d9d9")
        self.l4.configure(disabledforeground="#a3a3a3")
        self.l4.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.l4.configure(foreground="#000000")
        self.l4.configure(highlightbackground="#d9d9d9")
        self.l4.configure(highlightcolor="black")
        self.l4.configure(text='''Mobile no.''')

        self.nm = tk.Entry(self.Frame1)
        self.nm.place(relx=0.352, rely=0.237,height=20, relwidth=0.36)
        self.nm.configure(background="white")
        self.nm.configure(disabledforeground="#a3a3a3")
        self.nm.configure(font="TkFixedFont")
        self.nm.configure(foreground="#000000")
        self.nm.configure(highlightbackground="#d9d9d9")
        self.nm.configure(highlightcolor="black")
        self.nm.configure(insertbackground="black")
        self.nm.configure(selectbackground="#c4c4c4")
        self.nm.configure(selectforeground="black")

        self.unm = tk.Entry(self.Frame1)
        self.unm.place(relx=0.352, rely=0.373,height=20, relwidth=0.36)
        self.unm.configure(background="white")
        self.unm.configure(disabledforeground="#a3a3a3")
        self.unm.configure(font="TkFixedFont")
        self.unm.configure(foreground="#000000")
        self.unm.configure(highlightbackground="#d9d9d9")
        self.unm.configure(highlightcolor="black")
        self.unm.configure(insertbackground="black")
        self.unm.configure(selectbackground="#c4c4c4")
        self.unm.configure(selectforeground="black")

        self.password = tk.Entry(self.Frame1)
        self.password.place(relx=0.352, rely=0.508,height=20, relwidth=0.36)
        self.password.configure(background="white")
        self.password.configure(disabledforeground="#a3a3a3")
        self.password.configure(font="TkFixedFont")
        self.password.configure(foreground="#000000")
        self.password.configure(highlightbackground="#d9d9d9")
        self.password.configure(highlightcolor="black")
        self.password.configure(insertbackground="black")
        self.password.configure(selectbackground="#c4c4c4")
        self.password.configure(selectforeground="black")

        self.mob = tk.Entry(self.Frame1)
        self.mob.place(relx=0.352, rely=0.644,height=20, relwidth=0.36)
        self.mob.configure(background="white")
        self.mob.configure(disabledforeground="#a3a3a3")
        self.mob.configure(font="TkFixedFont")
        self.mob.configure(foreground="#000000")
        self.mob.configure(highlightbackground="#d9d9d9")
        self.mob.configure(highlightcolor="black")
        self.mob.configure(insertbackground="black")
        self.mob.configure(selectbackground="#c4c4c4")
        self.mob.configure(selectforeground="black")

        self.submit = tk.Button(self.Frame1)
        self.submit.place(relx=0.418, rely=0.814, height=24, width=49)
        self.submit.configure(activebackground="#ececec")
        self.submit.configure(activeforeground="#000000")
        self.submit.configure(background="#d9d9d9")
        self.submit.configure(disabledforeground="#a3a3a3")
        self.submit.configure(foreground="#000000")
        self.submit.configure(highlightbackground="#d9d9d9")
        self.submit.configure(highlightcolor="black")
        self.submit.configure(pady="0")
       #------------------------------------
        self.submit.configure(command=self.database,text='''Submit''' )

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.367, rely=0.044, height=71, width=145)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 23 -weight bold -underline 1")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Sign up''')

if __name__ == '__main__':
    vp_start_gui()





