from tkinter import *
def raise_frame(frame):
    frame.tkraise()
root=Tk()
f1=Frame(root)
f2=Frame(root)
f3=Frame(root)
f4=Frame(root)

for frame in(f1,f2,f3,f4):
    frame.grid(row=1,column=1)
    
Label(f1,text='Frame 1').pack()
Button(f1,text='go to frame 2',command=lambda:raise_frame(f2)).pack()

Label(f2,text='Frame 2').pack()
Button(f2,text='go to frame 3',command=lambda:raise_frame(f3)).pack()

Label(f3,text='Frame 3').pack()
Button(f3,text='go to frame 4',command=lambda:raise_frame(f4)).pack()

Label(f4,text='Frame 4').pack()
Button(f4,text='go to frame 1',command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()
