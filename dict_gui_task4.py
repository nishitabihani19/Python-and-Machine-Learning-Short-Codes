import xlwt
import xlrd
import  requests
import json
import vlc
from xlutils.copy import copy
app_id = '1625ba25'
app_key = 'd915d2104f9e5a626dac165336c289b3'
language = 'en'
from tkinter import *
root=Tk()
root.title("dictionary search")
root.geometry('800x400+0+0')
label1=Label(root,text="enter the word: ",font=("arial",10,"bold")).place(x=10,y=10)
name=StringVar()
entry_box=Entry(root,textvariable=name,width=25,bg="Lightgreen").place(x=120,y=10)
from win32com.client import Dispatch
s=Dispatch("SAPI.SpVoice")
           
def fn_do():
    word_id=name.get()
    
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word_id.lower()
    urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()
    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
    p=r.json()
    print(p)
    a=p['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
    label3=Label(root,text="meaning:",font=("arial",10,"bold")).place(x=10,y=100)
    label4=Label(root,text=a,font=("arial",10,"bold")).place(x=10,y=120)
    q=vlc.MediaPlayer('http://audio.oxforddictionaries.com/en/mp3/hello_gb_1.mp3')
    q.play()
    #s.Speak(p['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])

work = Button(root,text="submit",width=30,height=2,bg="white",command=fn_do).place(x=250,y=250)


#root.mainloop()

#sticky="E"(give the direction)
#p=vlc.MediaPlayer(path)
#p.play()
#,show="*"
