import re,psutil,cv2,webbrowser,requests,pyowm,json,math,wikipedia
from tkinter import *
from moviepy.editor import *
import xlwt,xlrd
from xlutils.copy import copy
import speech_recognition as sr
import cv2
from moviepy.editor import *
import ctypes
import os
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()

def raise_frame(frame):
    frame.tkraise()
    
root = Tk()

f1 = Frame(root,bg="pink")
f2 = Frame(root,bg="pink")
f3 = Frame(root,bg="pink")
f4 = Frame(root,bg="pink")
f5 = Frame(root,bg="pink")
f6 = Frame(root,bg="pink")
f7 = Frame(root,bg="pink")
f8 = Frame(root,bg="lightblue")
f9 = Frame(root,bg="pink")
f10 = Frame(root,bg="pink")
f11 = Frame(root,bg="pink")
f12 = Frame(root,bg="pink")
f13 = Frame(root,bg="lightblue")
f14 = Frame(root,bg="pink")
f15 = Frame(root,bg="pink")
f16 = Frame(root,bg="pink")
'''
f1.place(x=100,y=100)
f2.place(x=120,y=120)
f3.place(x=140,y=140)
f4.place(x=160,y=160)
f5.place(x=180,y=180)
f6.place(x=200,y=200)
f7.place(x=220,y=220)
f8.place(x=240,y=240)
f9.place(x=260,y=260)
f10.place(x=280,y=280)
f11.place(x=300,y=300)
f12.place(x=320,y=320)
f13.place(x=340,y=340)
f14.place(x=360,y=360)
f15.place(x=380,y=380)
f16.place(x=400,y=400)

'''
f1.grid(row=0, column=0, sticky='news')
f2.grid(row=0, column=0, sticky='news')
f3.grid(row=0, column=0, sticky='news')
f4.grid(row=0, column=0, sticky='news')
f5.grid(row=0, column=0, sticky='news')
f6.grid(row=0, column=0, sticky='news')
f7.grid(row=0, column=0, sticky='news')
f8.grid(row=0, column=0, sticky='news')
f9.grid(row=0, column=0, sticky='news')
f10.grid(row=0, column=0, sticky='news')
f11.grid(row=0, column=0, sticky='news')
f12.grid(row=0, column=0, sticky='news')
f13.grid(row=0, column=0, sticky='news')
f14.grid(row=0, column=0, sticky='news')
f15.grid(row=0, column=0, sticky='news')
f16.grid(row=0, column=0)

l1=Label(f16,text=' ').grid(row=1,column=8)
l1=Label(f16,text=' ').grid(row=2,column=8)
l1=Label(f16,text=' ').grid(row=3,column=8)
l1=Label(f16,text=' ').grid(row=4,column=8)
l1=Label(f16,text=' ').grid(row=5,column=8)
l1=Label(f16,text=' ').grid(row=6,column=8)
l1=Label(f16,text=' ').grid(row=7,column=8)

l1=Button(f16,text='Your Automation',bg='black',fg='white').grid(row=10,column=8)
l1=Label(f16,text=' ').grid(row=11,column=8)
l2=Button(f16,text='Your Easiness',bg='black',fg='white').grid(row=12,column=8)
button1=Button(f16,text='System Condition',fg='red',command=lambda:raise_frame(f1)).grid(row=20,column=1)
#system condition
def sys_cond():
          global out1
          battery = psutil.sensors_battery()
          plugged = battery.power_plugged
          percent = str(battery.percent)
          if plugged==False:
               plugged="Not Plugged In"
          else:
               plugged="Plugged In"
          #print(percent+'% | '+plugged)
          b=psutil.virtual_memory()
          #print(b[0])
          #print("total ram:",round(b[0]/(1024*1024*1024),2),"GB")
          ##print("available ram:",round(b[1]/(1024*1024*1024),2),"GB")
          #print("used ram:",round(b[3]/(1024*1024*1024),2),"GB")
          #print("free ram:",round(b[4]/(1024*1024*1024),2),"GB")
          out1=round(b[0]/(1024*1024*1024),2)
          out2=round(b[1]/(1024*1024*1024),2)
          out3=round(b[3]/(1024*1024*1024),2)
          out5=percent+'% | '+plugged
          out4=round(b[4]/(1024*1024*1024),2)
          head6=Label(f1,text="System Status",fg='#FFFF00').place(x=150,y=20)
          head6=Label(f1,text="Percentage",fg='#FFFF00').place(x=100,y=60)
          head7=Label(f1,text="total ram:",fg='#FFFF00').place(x=100,y=100)
          head8=Label(f1,text="available ram",fg='#FFFF00').place(x=100,y=140)
          head9=Label(f1,text="used ram:",fg='#FFFF00').place(x=100,y=180)
          head10=Label(f1,text="free ram:",fg='#FFFF00').place(x=100,y=220)
          head5=Label(f1,text=out5,fg='#FFFF00',bg='black').place(x=200,y=60)
          head1=Label(f1,text=out1,fg='#FFFF00',bg='black').place(x=200,y=100)
          head2=Label(f1,text=out2,fg='#FFFF00',bg='black').place(x=200,y=140)
          head3=Label(f1,text=out3,fg='#FFFF00',bg='black').place(x=200,y=180)
          head4=Label(f1,text=out4,fg='#FFFF00',bg='black').place(x=200,y=220)

sys_cond()

n2=Button(f1, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=200,y=300)
l1=Label(f16,text=' ').grid(row=21,column=8)
button2=Button(f16,text='Change Wallpaper',fg='red',command=lambda:raise_frame(f2)).grid(row=22,column=2)
#wallpaper
SPI_SETDESKWALLPAPER = 20

dict={0:"0:r'C:\\spenish.jpg'",
           1:"1:r'C:\\pre_nis.jpg'",
           2:"2:r'C:\\photo.jpg'"
           }
p=StringVar()
l1=Label(f2,text='List Of Music ').place(x=300,y=10)

for i in range(3):
     #print(dict[i])
     head1=Label(f2,text=dict[i],fg='black').grid()
l1=Label(f2,text='Enter your choice: ').place(x=100,y=200)
word=Entry(f2,textvariable=p).place(x=250,y=200)
def fun_choice():
     try:
          #choice=int(input("enter your choice:"))
          
          #print(dict[p.get()])
          if(p.get()==0):
               ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,r'C:\\spenish.jpg')
          elif(p.get()==1):
               ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,r'C:\\pre_nis.jpg')
          elif(p.get()==2):
               ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,r'C:\\photo.jpg')
          else:
               ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,r'C:\\photo.jpg')
     except:
          #print("not valid input")
          l1=Label(f2,text='Invalid Input ').place(x=10,y=100)
          fun_choice()
butn=Button(f2,text="submit",command=fun_choice).place(x=200,y=400)
#fun_choice()

n2=Button(f2, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=200,y=450)
l1=Label(f16,text=' ').grid(row=23,column=8)
button3=Button(f16,text="Today's Weather",fg='red',command=lambda:raise_frame(f3)).grid(row=24,column=3)
#Weather temprature
root.title("whether forecasting")
lab1=Label(f3,text="Enter city name :",font=20).place(x=20,y=50) 
var1=StringVar()
ent_city=Entry(f3,textvariable=var1,font=18).place(x=180,y=55)

def fun_run():
          city_name=var1.get()
          #city_name = input("Enter city name : ") 
          api_key = "dc8c636c774e9480e689b16119a2dbf3"
          base_url = "http://api.openweathermap.org/data/2.5/weather?"
          complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
          response = requests.get(complete_url) 
          x = response.json() 
          if  x["cod"] != "404": 
                     y = x["main"]
                     current_temperature = (y["temp"] -(273.15))
                     current_pressure = y["pressure"]
                     current_humidiy = y["humidity"]
                     z = x["weather"]
                     weather_description = z[0]["description"]
                     '''
                     print(" Temperature (in celsius unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description))
                     '''
                     lab2=Label(f3,text="Temperature = ",font=15).place(x=20,y=100)
                     lab3=Label(f3,text=str(current_temperature),font=15).place(x=150,y=100)

                     lab4=Label(f3,text=" Atmospheric pressure = ",font=20).place(x=20,y=160)
                     lab5=Label(f3,text=str(current_pressure),font=15).place(x=240,y=160)
                     lab6=Label(f3,text="Humidity (in %) = ",font=20).place(x=20,y=220)
                     lab8=Label(f3,text=str(current_humidiy),font=15).place(x=180,y=220)
                     lab9=Label(f3,text="description =  ",font=20).place(x=20,y=280)
                     lab10=Label(f3,text=str(weather_description),font=15).place(x=140,y=280)
          else:
               lab11=Label(f3,text="City does not Exist",font=20,fg='red').place(x=100,y=340)
but_sub=Button(f3,text="submit",command=fun_run,font=20).place(x=100,y=300)

n2=Button(f3, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=200,y=350)
l1=Label(f16,text=' ').grid(row=25,column=8)
button4=Button(f16,text='Wikipidia Search',fg='red',command=lambda:raise_frame(f4)).grid(row=26,column=4)
#wikipedia
p=StringVar()
l1=Label(f4,text='Enter Word  ').place(x=10,y=100)
word=Entry(f4,textvariable=p).place(x=100,y=100)

def wiki():
          #print(p.get())
          #word=input("enter  word..")
          complete_content=wikipedia.page(p.get())
          out1=complete_content.images[0]
          #out2=complete_content.content
          head2=Label(f4,text=out1,fg='black').place(x=10,y=130)
          head1=Label(f4,text=complete_content.summary,fg='black').place(x=10,y=160)

butn=Button(f4,text="submit",command=wiki).place(x=100,y=300)
n2=Button(f4, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=100,y=330)
l1=Label(f16,text=' ').grid(row=27,column=8)
button5=Button(f16,text='Play Music',fg='red',command=lambda:raise_frame(f5)).grid(row=28,column=5)
n2=Button(f5, text='Go To Menu', command=lambda:raise_frame(f16))
n2.grid(columnspan=4)
l1=Label(f16,text=' ').grid(row=29,column=8)
button6=Button(f16,text='Play video',fg='red',command=lambda:raise_frame(f6)).grid(row=30,column=6)
#vedio
dict={0:"720.avi",
      1:"Daru_badnam_karti_dj_Remix.mp3",
      2:"HARYANVI_SONG_BY_LOKESH_GUJJER.mp3"
      }
     
var1=IntVar()
en=Entry(f6,textvariable=var1,font="bold").place(x=40,y=200)

def fn_list():
     for i in range(3):
          print(dict[i])

def fn_play():
     #print(dict[var1])
     
     pygame.display.set_caption(dict[var1.get()])
     clip = VideoFileClip(dict[var1.get()])
     clip.preview()
     pygame.quit()
     



Button(f6,text="Play",command=fn_play).place(x=200,y=400)
Button(f6,text="List",command=fn_list).place(x=100,y=400)

n2=Button(f6, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=200,y=450)

l1=Label(f16,text=' ').grid(row=31,column=8)
button7=Button(f16,text='Calculator',fg='red',command=lambda:raise_frame(f7)).grid(row=32,column=7)
n2=Button(f7, text='Go To Menu', command=lambda:raise_frame(f16))
n2.grid(columnspan=4)
l1=Label(f16,text=' ').grid(row=33,column=8)
button8=Button(f16,text='Send Mail',fg='red',command=lambda:raise_frame(f8)).grid(row=34,column=8)
#mail
p=StringVar()
n=StringVar()
resp=StringVar()
msg=StringVar()
head1=Label(f8,text="Enter Mail_id",fg='black').place(x=10,y=100)
head2=Label(f8,text="Enter password",fg='black').place(x=10,y=140)
en1=Entry(f8,textvariable=p).place(x=200,y=100)
en2=Entry(f8,textvariable=n).place(x=200,y=140)
head3=Label(f8,text="Enter Other mail",fg='black').place(x=10,y=180)
head4=Label(f8,text="Enter Message",fg='black').place(x=10,y=220)
en3=Entry(f8,textvariable=resp).place(x=200,y=180)
en4=Entry(f8,textvariable=msg).place(x=200,y=220)
def send_mail():
          #username=input("enter your mail id:")
          #password=input("enter password:")
          #print(p.get())
          #print(n.get())
          #print(resp.get())
          #print(msg.get())
          
          s.login(p.get(),n.get())
          #resp=input("enter other mail:")
          #msg=input("enter text that u want to send")
          s.sendmail(p.get(),resp.get(),msg.get())
          #print("mail send success")
          head1=Label(f8,text="mail send success",fg='black').place(x=100,y=240)

          s.quit()
          #print("logout")
          head2=Label(f8,text="LOgout",fg='black').place(x=100,y=280)
butn=Button(f8,text="submit",command=send_mail) .place(x=50,y=300)

n2=Button(f8, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=200,y=500)

button9=Button(f16,text='Send Message',fg='red',command=lambda:raise_frame(f9)).grid(row=32,column=9)
#msg

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
app_id = '1625ba25'
app_key = 'd915d2104f9e5a626dac165336c289b3'
language = 'en'
pr=StringVar()
ni=Entry(f9,textvariable=pr).place(x=130,y=50)
ch=StringVar()
bi=Entry(f9,textvariable=ch).place(x=130,y=100)
head1=Label(f9,text="Enter Mobile No.",fg='black').place(x=10,y=50)
head2=Label(f9,text="Enter Message",fg='black').place(x=10,y=100)

def send_msg():
          #mob_no=input(" enter  mobile number")
          url = "https://www.fast2sms.com/dev/bulk"
          #text=input("enter message:")
          payload = f"sender_id=FSTSMS&message={ch.get()}&language=english&route=p&numbers={pr.get()}"
          headers = {
          'authorization': "7aEPsfe6YBxVS2AFR5zbZ08pD1MyLWu3HI9tJhnNkKTv4orcmX9l56RQr10eStLNMizaoyO8gWcnjPwT",
          'Content-Type': "application/x-www-form-urlencoded",
          'Cache-Control': "no-cache",
          }
          response = requests.request("POST", url, data=payload, headers=headers)
          #print(response.text)
          Label(f9,text=response.text).place(x=20,y=150)

Button(f9,text="send ",command=send_msg).place(x=30,y=200)

n2=Button(f9, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=100,y=330)

button10=Button(f16,text='Make Call',fg='red',command=lambda:raise_frame(f10)).grid(row=30,column=10)
#call
lab_head=Label(f10,text="Calling",font="bold").place(x=100,y=20)
var1=StringVar()
ent1=Entry(f10,text=var1,font="bold").place(x=200,y=100)
lab_entry=Label(f10,text="enter mobile no:",font="bold").place(x=10,y=100)

def fn_calling():
     global lab_info
     from twilio.rest import TwilioRestClient
     TWILIO_PHONE_NUMBER = "+19105063051"
     DIAL_NUMBERS = ["919664149754"]
     TWIML_INSTRUCTIONS_URL = \
                            "http://static.fullstackpython.com/phone-calls-python.xml"

     client = TwilioRestClient("AC4aaecc06b047d246e4b9cbdc1e419104", "cc93934fe711b89f3ce821ad0b912b76")

     if(var1.get()=="919664149754"):
          def dial_numbers(numbers_list):
              for number in numbers_list:
                  lab_dial=Label(root,text="Dialing"+number,font="bold").place(x=40,y=200)
                  #print("Dialing " + number)
                  client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                                      url=TWIML_INSTRUCTIONS_URL, method="GET")

          if __name__ == "__main__":
              dial_numbers(DIAL_NUMBERS)
     else:
          lab_info=Label(f10,text="please enter registered mobile  number",font="bold").place(x=20,y=300)
          #print("not registered mobile number:")
sub_button=Button(f10,text="submit",command=fn_calling).place(x=100,y=400)
n2=Button(f10, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=200,y=450)
button11=Button(f16,text='Find Word',fg='red',command=lambda:raise_frame(f11)).grid(row=28,column=11)
#dictonary
'''
r=sr.Recognizer()

app_id = '1625ba25'
app_key = 'd915d2104f9e5a626dac165336c289b3'
language = 'en'
f11.title("dictionary search")
f11.geometry('800x400+0+0')
patt2=xlwt.easyxf("font:name Times New Roman,color-index red,bold on",num_format_str='#,##0.00')

label1=Label(f11,text="enter the word: ",font=("arial",15,"bold"))
label1.place(x=50,y=80)
name=StringVar()
entry_box=Entry(f11,textvariable=name,width=25,bg="white",font=("arial",12,"bold"))
entry_box.place(x=220,y=85)
label3=Label(f11,text="meaning:",font=("arial",15,"bold"))
label3.place(x=10,y=250)

def temp():
    print(word_id)
    print(name.get())


def fn_do():
    global label4
    global a
    global word_id
    word_id=name.get()
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word_id.lower()
    urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()
    
    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
    p=r.json()
    a=p['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
    if(a):
        label4=Label(f11,text=a,font=("arial",15))
        label4.place(x=100,y=250)
    else:
        label7=Label(f11,text="word not found",font=("arial",12,"bold"))
        label7.place(x=100,y=250)             
        
def fn_reset():
    label4.destroy()
    label7.destroy()
    entry_box.delete(0,END)

def fn_save():
    wb=xlrd.open_workbook('dict.xls')
    ws=copy(wb)
    w_sheet=ws.get_sheet(0)
    sheet=wb.sheet_by_index(0)
    l=len(sheet.col_values(0))
    w_sheet.write(l,0,word_id)
    w_sheet.write(l,2,a,patt2)
    ws.save('dict.xls')

def fn_speak():
    global word_id
    with sr.Microphone() as source:
          #print("listening")
          audio=r.listen(source)
          #print("fatching string")
          word_id=r.recognize_google(audio)
          #print(word_id)
          fn_do()
           #print("your voice not recognise properly")
search_button = Button(f11,text="search",width=10,height=2,bg="white",command=fn_do).place(x=150,y=150)
reset_button = Button(f11,text="reset",width=10,height=2,bg="white",command=fn_reset).place(x=280,y=150)
save_button = Button(f11,text="save",width=10,height=2,bg="white",command=fn_save).place(x=410,y=150)
audio_button = Button(f11,text="speak..",width=10,height=2,bg="white",command=fn_speak).place(x=500,y=80)
f11.bind('<Return>',lambda event: fn_do())
'''
n2=Button(f11, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=300,y=350)

button12=Button(f16,text='Click Picture',fg='red',command=lambda:raise_frame(f12)).grid(row=26,column=12)
#camera capture
head1=Label(f12,text="press Space to click",fg='black').place(x=10,y=100)
head2=Label(f12,text="Escape to Terminate",fg='black').place(x=10,y=140)
def camera():
    cam = cv2.VideoCapture(0)
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k == 27:
            # ESC pressed
            #print("Escape hit, closing...")
            break
        elif k == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            #print("{} written!".format(img_name))
            img_counter += 1
    cam.release()

    cv2.destroyAllWindows()
butn=Button(f12,text="Switch Camera",command=camera).place(x=100,y=200)


n2=Button(f12, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=200,y=500)
button13=Button(f16,text='Check Location',fg='red',command=lambda:raise_frame(f13)).grid(row=24,column=13)
#mylocation
def fn_loc():
     send_url = "http://api.ipstack.com/check?access_key=c3da5c29b871d48c891e0bd39d77764e"
     geo_req = requests.get(send_url)
     geo_json = json.loads(geo_req.text)
     latitude = geo_json['latitude']
     longitude = geo_json['longitude']
     city = geo_json['city']
     #print(latitude,longitude,city)
     head4=Label(f13,text="Latitude",fg='black').place(x=10,y=100)
     head5=Label(f13,text="Longitude",fg='black').place(x=10,y=140)
     head6=Label(f13,text="City is",fg='black').place(x=10,y=180)
     head1=Label(f13,text=latitude,fg='black').place(x=100,y=100)
     head2=Label(f13,text=longitude,fg='black').place(x=100,y=140)
     head3=Label(f13,text=city,fg='black').place(x=100,y=180)
fn_loc()
n2=Button(f13, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=100,y=250)
button14=Button(f16,text='Move Cursor',fg='red',command=lambda:raise_frame(f14)).grid(row=22,column=14)
n2=Button(f14, text='Go To Menu', command=lambda:raise_frame(f16))
n2.grid(columnspan=4)
button15=Button(f16,text='Open Browser',fg='red',command=lambda:raise_frame(f15)).grid(row=20,column=15)
#open google
def open_browser():
          webbrowser.open('https://www.google.com/')
butn=Button(f15,text="submit",command=open_browser).place(x=50,y=300)
n2=Button(f15, text='Go To Menu', command=lambda:raise_frame(f16))
n2.place(x=100,y=350)

root.attributes("-fullscreen",True)

raise_frame(f16)
root.mainloop()
