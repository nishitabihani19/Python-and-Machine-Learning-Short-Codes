import requests,json,re
from tkinter import *
import re,psutil,cv2,webbrowser,requests,json,math,wikipedia
root=Tk()
root.grid()
root.geometry("500x500")
def fn_loc():
     send_url = "http://api.ipstack.com/check?access_key=c3da5c29b871d48c891e0bd39d77764e"
     geo_req = requests.get(send_url)
     geo_json = json.loads(geo_req.text)
     latitude = geo_json['latitude']
     longitude = geo_json['longitude']
     city = geo_json['city']
     print(latitude,longitude,city)
     head4=Label(root,text="Latitude",fg='black').place(x=10,y=100)
     head5=Label(root,text="Longitude",fg='black').place(x=10,y=140)
     head6=Label(root,text="City is",fg='black').place(x=10,y=180)
     head1=Label(root,text=latitude,fg='black').place(x=100,y=100)
     head2=Label(root,text=longitude,fg='black').place(x=100,y=140)
     head3=Label(root,text=city,fg='black').place(x=100,y=180)
fn_loc()


root.mainloop()
