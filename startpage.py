
import sys
import os
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

import startpage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    startpage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    startpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def buttonClick2(self):
        global root
        root.destroy()  #first destroy the window by clicking the button and then we are opening the filename
        #self.hide()
        #secframe=Toplevel2()
        filename='python login.py' #to open this file on clicking the button
        os.system(filename)
        
        
    def buttonClick1(self):
        global root
        root.destroy()
        #self.hide()
        #secframe=Toplevel2()
        filename='python signup.py'
        os.system(filename)
        
        

        

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font13 = "-family {Arial} -size 30 -weight bold -underline 1"
        font14 = "-family {Calibri} -size 14 -weight bold"

        top.geometry("730x312+215+141")
        top.title("Start Page")
        top.configure(background="#cc66ff") #----

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.137, rely=0.321, relheight=0.625
                , relwidth=0.719)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#CD5C5C") #------
        self.Frame1.configure(width=525)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.171, rely=0.41, height=44, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font14)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SIGNUP''')
        self.Button1.configure(width=97)
        self.Button1.configure(command=self.buttonClick1)


        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.667, rely=0.41, height=44, width=97)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''LOGIN''')
        self.Button2.configure(width=97)
        self.Button2.configure(command=self.buttonClick2)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.014, rely=0.096, height=61, width=714)
        #self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(background="#ffff00") #-----------
        #CD5C5C
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''ELECTION MANAGEMENT SYSTEM''')
        self.Label1.configure(width=714)

if __name__ == '__main__':
    vp_start_gui()





