from tkinter import *
root=Tk()
root.geometry('400x400')

button2=Button(root,text='Sign-Up Here',fg='red',command=lambda:f1)
button2.grid(row=3,column=0)
button3=Button(root,text='Login Here',fg='red',command=lambda:f2)
button3.grid(row=3,column=5)

f1=Frame(root)
#signup

signup=Label(f1,text='Sign Up Here',fg='green')
fname=Label(f1,text='First Name')
lname=Label(f1,text='Last Name')
username=Label(f1,text='Username')
password=Label(f1,text='Password')
retype=Label(f1,text='Re-type')

entry1=Entry(f1)
entry2=Entry(f1)
entry3=Entry(f1)
entry4=Entry(f1)
entry5=Entry(f1)
signup.grid(columnspan=2,)
fname.grid(row=1,sticky='E')
entry1.grid(row=1,column=1)
lname.grid(row=2,column=0,sticky='E')
entry2.grid(row=2,column=1)
username.grid(row=3,column=0,sticky='E')
entry3.grid(row=3,column=1)
password.grid(row=4,column=0,sticky='E')
entry4.grid(row=4,column=1)
retype.grid(row=5,column=0,sticky='E')
entry5.grid(row=5,column=1)

d=Checkbutton(f1,text='All the information provided are correct',fg='blue')
d.grid(columnspan=2)

button1=Button(f1,text='Submit',bg='red')
button1.grid(row=7,column=1)
f1.grid()


f2=Frame(root)
#login
login=Label(f2,text='Login Here')
username=Label(f2,text='Username')
password=Label(f2,text='Password')
entry1=Entry(f2)
entry2=Entry(f2)
login.grid(columnspan=2)
username.grid(row=1,column=0,sticky='E')
entry1.grid(row=1,column=1)
password.grid(row=2,column=0,sticky='E')
entry2.grid(row=2,column=1)
button1=Button(f2,text='Submit',fg='red')
button1.grid(columnspan=3)
f2.grid()

root.mainloop()
