import tkinter as tk
import turtle
from random import randint
from chaoscode import *
from spiralcode import *
# *************************************************************************
#main tk (the menu starts below)

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.option_add("*Font", "courier")
        self.wm_title("MENU - CWC PYTHON PRESENTATION")
        self.minsize(400, 200)
        self.button1 = tk.Button(self.frame, text = 'Choas', width = 25, command = self.new_window)
        self.button1.pack()
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

        root.option_add("*Font", "courier")
        root.wm_title("MENU - CWC PYTHON PRESENTATION")
        root.minsize(400, 200)
        a = tk.Button(root, text="random chaos",font=('courier', '20') ,command=chaos)
        b = tk.Button(root, text="recursion   ",font=('courier', '20') ,command=callSpiral)
        t1 = tk.Label(root, text="Chaos (Sierpinski Triangle) : CW Coleman",font=('courier', '10'))
        t2 = tk.Label(root, text="Resursion (Pop S0AR): CW Coleman : CW Coleman",font=('courier', '10'))
        t3 = tk.Label(root, text = "SOAR (Stack of Activation Records)",font=('courier', '10'))
        a.pack()
        b.pack()
        t1.pack()
        t2.pack()
        t3.pack()

def main():
    root = tk.Tk()
    app = MainManu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
