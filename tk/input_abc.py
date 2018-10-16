from tkinter import *
from tkinter import ttk

root=Tk()
mainframe = ttk.Frame(root, padding="30 30 30 30 ")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

avar=StringVar() # Value saved here
bvar=StringVar()
def plot():
  print(avar.get())
  print(bvar.get())
  return ''

ttk.Entry(mainframe, width=7, textvariable=avar).grid(column=2, row=1)
ttk.Label(mainframe, text="a=").grid(column=1, row=1)
ttk.Entry(mainframe, width=7, textvariable=avar).grid(column=2, row=1)
ttk.Label(mainframe, text="b=").grid(column=1, row=2)
ttk.Entry(mainframe, width=7, textvariable=bvar).grid(column=2, row=2)
ttk.Button(mainframe, text="Calculate", command=plot).grid(column=2, row=13)
root.mainloop()
