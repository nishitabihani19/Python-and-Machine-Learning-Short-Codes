from tkinter import *
import re,psutil,cv2,webbrowser,requests,pyowm,pygame,json,math,wikipedia

root=Tk()
root.grid()
root.geometry("500x500")
def sys_cond():
          global out1
          battery = psutil.sensors_battery()
          plugged = battery.power_plugged
          percent = str(battery.percent)
          if plugged==False:
               plugged="Not Plugged In"
          else:
               plugged="Plugged In"
          print(percent+'% | '+plugged)
          b=psutil.virtual_memory()
          #print(b[0])
          print("total ram:",round(b[0]/(1024*1024*1024),2),"GB")
          print("available ram:",round(b[1]/(1024*1024*1024),2),"GB")
          print("used ram:",round(b[3]/(1024*1024*1024),2),"GB")
          print("free ram:",round(b[4]/(1024*1024*1024),2),"GB")
          out1=round(b[0]/(1024*1024*1024),2)
          out2=round(b[1]/(1024*1024*1024),2)
          out3=round(b[3]/(1024*1024*1024),2)
          out5=percent+'% | '+plugged
          out4=round(b[4]/(1024*1024*1024),2)
          head6=Label(root,text="System Status",fg='#FFFF00').place(x=150,y=20)
          head6=Label(root,text="Percentage",fg='#FFFF00').place(x=100,y=60)
          head7=Label(root,text="total ram:",fg='#FFFF00').place(x=100,y=100)
          head8=Label(root,text="available ram",fg='#FFFF00').place(x=100,y=140)
          head9=Label(root,text="used ram:",fg='#FFFF00').place(x=100,y=180)
          head10=Label(root,text="free ram:",fg='#FFFF00').place(x=100,y=220)


          head5=Label(root,text=out5,fg='#FFFF00',bg='black').place(x=200,y=60)
          head1=Label(root,text=out1,fg='#FFFF00',bg='black').place(x=200,y=100)
          head2=Label(root,text=out2,fg='#FFFF00',bg='black').place(x=200,y=140)
          head3=Label(root,text=out3,fg='#FFFF00',bg='black').place(x=200,y=180)
          head4=Label(root,text=out4,fg='#FFFF00',bg='black').place(x=200,y=220)

sys_cond()
root.mainloop()
