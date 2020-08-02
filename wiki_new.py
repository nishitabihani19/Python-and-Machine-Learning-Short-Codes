from tkinter import *
import re,psutil,cv2,webbrowser,requests,json,math,wikipedia

root=Tk()
root.grid()
root.geometry("500x500")
p=StringVar()
l1=Label(root,text='Enter Word  ').place(x=10,y=100)
word=Entry(root,textvariable=p).place(x=100,y=100)

def wiki():
          #print(p.get())
          #word=input("enter  word..")
          complete_content=wikipedia.page(p.get())
          out1=complete_content.images[0]
          #out2=complete_content.content
          head2=Label(root,text=out1,fg='black').place(x=10,y=130)
          head1=Label(root,text=complete_content.summary,fg='black').place(x=10,y=160)

butn=Button(root,text="submit",command=wiki).place(x=200,y=200)
root.mainloop()



          
