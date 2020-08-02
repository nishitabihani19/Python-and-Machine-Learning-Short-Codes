from tkinter import *
def raise_frame(frame):
    frame.tkraise()
    
root = Tk()
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)

f1.grid(row=0, column=0, sticky='news')
f2.grid(row=0, column=0, sticky='news')
f3.grid(row=0, column=0, sticky='news')

Label(f1, text='FRAME 1').pack()
Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
Button(f1, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()


lab1=Label(f2,text='signup page')
lab1.pack()
en=Entry(f2)
en.pack()
Button(f2, text='Go to frame 1', command=lambda:raise_frame(f1)).pack()


lab2=Label(f3,text='login page')
lab2.pack()
Button(f3, text='Go to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()
