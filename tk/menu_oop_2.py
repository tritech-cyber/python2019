import tkinter as tk

class MintApp(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.columnconfigure(0, weight = 0)
        self.root.rowconfigure(0, weight = 0)


        main_frame = tk.Frame(self.root, width = 385, height = 460, background = "black")
        main_frame.columnconfigure(0, weight = 0)
        main_frame.rowconfigure(0, weight = 0)
        main_frame.grid(row  = 0, column = 0)

        label_frame = tk.Frame(main_frame, width = 375, height = 115, background = "blue")
        label_frame.grid(row  = 0, column = 0)

        button_frame = tk.Frame(main_frame, width = 375, height = 330, background = "green")
        button_frame.grid(row  = 1, column = 0)



if __name__ == "__main__":
    root = tk.Tk()
    MyApp = MintApp(root)

    tk.mainloop()
