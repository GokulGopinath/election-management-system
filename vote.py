

from tkinter import*






import sys
import os
import sqlite3
from tkinter import*
from tkinter import messagebox

db = sqlite3.connect('castyourvote.db')
with db:
    cursor = db.cursor()
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

#---------------------------------------------------------------



import vote_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    vote_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    vote_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def submit(self):
        if self.count==1:
            cursor.execute("update vote set votes=votes+1 where candidate_no=1")
        if self.count==2:
            cursor.execute("update vote set votes=votes+1 where candidate_no=2")
        if self.count==3:
            cursor.execute("update vote set votes=votes+1 where candidate_no=3")
        if self.count==4:
            cursor.execute("update vote set votes=votes+1 where candidate_no=4")

        cursor.execute("SELECT * FROM vote")
        content=cursor.fetchall()
        self.count=self.count+1
        print(content)
        db.commit()
        messagebox.showinfo("","YOU HAVE VOTED SUCCESSFULLY")
        #GIVE LINK TO NEXT PG HERE
        global root

        root.destroy()
            
        filename='python startpage.py'  
        os.system(filename)             #after destroying the current window go to the filename
            
    def count1(self):
        self.count=1  #if the voter selected first candidate then count=1
    def count2(self):
        self.count=2  #if the voter selected first candidate then count=2
    def count3(self):
        self.count=3  #if the voter selected first candidate then count=3
    def count4(self):
        self.count=4  #if the voter selected first candidate then count=4
            
        

            


    


 #----------------------------------------------------------------------------------

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 9"

        top.geometry("566x555+385+139")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.v = IntVar()
        
        self.count = IntVar    # count variable is to keep track of the candidate the voter voted
        self.count = 0

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.124, rely=0.234, relheight=0.676
                , relwidth=0.751)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=425)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.082, rely=0.12, height=41, width=164)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(font="-family {Arial} -size 15")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Chetan Mukharjee''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.094, rely=0.307, height=31, width=144)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Arial} -size 15")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Saurabh Shukla''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.071, rely=0.493, height=31, width=158)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Arial} -size 15")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Sanchit Goyal''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.094, rely=0.653, height=31, width=146)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Arial} -size 15")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Harminder Singh''')

        self.Radiobutton1 = tk.Radiobutton(self.Frame1)
        self.Radiobutton1.place(relx=0.6, rely=0.133, relheight=0.093
                , relwidth=0.193)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font="-family {Arial} -size 15")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(command=self.count1,variable=self.v,value=1,text='''Vote''')
#-----------------------------------------------------------------------------------------------------
        self.Radiobutton2 = tk.Radiobutton(self.Frame1)
        self.Radiobutton2.place(relx=0.6, rely=0.307, relheight=0.093
                , relwidth=0.193)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font="-family {Arial} -size 15")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(command=self.count2,variable=self.v,value=2,text='''Vote''')

        self.Radiobutton3 = tk.Radiobutton(self.Frame1)
        self.Radiobutton3.place(relx=0.6, rely=0.467, relheight=0.12
                , relwidth=0.193)
        self.Radiobutton3.configure(activebackground="#ececec")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#d9d9d9")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(font="-family {Arial} -size 15")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify='left')
        self.Radiobutton3.configure(command=self.count3,variable=self.v,value=3,text='''Vote''')

        self.Radiobutton4 = tk.Radiobutton(self.Frame1)
        self.Radiobutton4.place(relx=0.612, rely=0.64, relheight=0.093
                , relwidth=0.169)
        self.Radiobutton4.configure(activebackground="#ececec")
        self.Radiobutton4.configure(activeforeground="#000000")
        self.Radiobutton4.configure(background="#d9d9d9")
        self.Radiobutton4.configure(disabledforeground="#a3a3a3")
        self.Radiobutton4.configure(font="-family {Arial} -size 15")
        self.Radiobutton4.configure(foreground="#000000")
        self.Radiobutton4.configure(highlightbackground="#d9d9d9")
        self.Radiobutton4.configure(highlightcolor="black")
        self.Radiobutton4.configure(justify='left')
        self.Radiobutton4.configure(command=self.count4,variable=self.v,value=4,text='''Vote''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.424, rely=0.84, height=34, width=79)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.submit,text='''Submit''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.115, rely=0.09, height=41, width=431)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial} -size 28 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#250f63")
        self.Label1.configure(text='''CAST YOUR VOTE''')

        self.menubar = tk.Menu(top, font=('Segoe UI', 9, ), bg=_bgcolor
                ,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()





