from tkinter import *
def bulb_on():
    print("bulb is on")
def bulb_off():
    print("bulb is off")
def fan_on():
    print("fan is on")
def fan_off():
    print("fan is off")

root=Tk()
root.grid()
v=IntVar()
w=IntVar()
root.geometry('600x480+100+200')
root.title("first gui")
#label
    
head=Label(text="Bulb",fg='#FFFF00',bg='black').grid(row=0,column=0)
#button
button=Radiobutton(text="ON",variable=v,value=1,command=bulb_on)
button.grid(row=1,column=0)
button=Radiobutton(text="OFF",variable=v,value=2,command=bulb_off)
button.grid(row=1,column=1)

head=Label(text="Fan",fg='#FFFF00',bg='black').grid(row=3,column=0)
button=Radiobutton(root,text="ON",variable=w,value=1,command=fan_on)
button.grid(row=4,column=0)
button=Radiobutton(root,text="OFF",variable=w,value=2,command=fan_off)
button.grid(row=4,column=1)

en=Entry(text="enter your name",font=100).grid(row=5,column=0)
en1=Entry(text="enter your name",font=200).grid(row=6,column=0)

temp=Button(text="submit",bd=4,activebackground="red",activeforeground="yellow",font=20,relief="sunken",bg="white",fg="black",command=fan_on).grid(row=8,column=0)

#task
#create gui to search any word from dictionary and show there result in gui
