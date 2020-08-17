from Tkinter import *

root = Tk()

def show_frame1():
    frame2.grid_forget()
    frame1.grid()

def show_frame2():
    frame1.grid_forget()
    frame2.grid()

frame1 = Frame(root)
Label(frame1, text="hello").grid(row=1, column=2)
Button(frame1, text='Go To Frame 2', command=show_frame2).grid(row=2, column=2)

frame2 = Frame(root)
Label(frame2, text="world").grid(row=1, column=2)
Button(frame2, text='Go To Frame 1', command=show_frame1).grid(row=2, column=2)


frame1.grid()

root.mainloop()
