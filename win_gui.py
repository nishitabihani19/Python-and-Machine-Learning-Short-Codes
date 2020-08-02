from tkinter import *

def fn_open():
     top=Toplevel()
     top.title("new window")
     top.geometry("300x300+120+120")
     button1=Button(top,text="close",command=top.destroy)
     button1.pack()
     
root=Tk()
button=Button(root,text="open window",command=fn_open)
button.pack()

root.geometry("300x300+120+120")
root.mainloop()
