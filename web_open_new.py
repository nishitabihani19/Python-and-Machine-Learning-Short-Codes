from tkinter import *
import re,psutil,cv2,webbrowser,requests,json,math,wikipedia

root=Tk()
root.grid()
root.geometry("500x500")

def open_browser():
          webbrowser.open('https://www.google.com/')
butn=Button(root,text="submit",command=open_browser).place(x=50,y=300)
root.mainloop()
