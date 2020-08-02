from tkinter import *
import requests, json 
root=Tk()
root.geometry("500x500")
root.title("whether forecasting")
lab1=Label(root,text="Enter city name :",font=20).place(x=20,y=50) 
var1=StringVar()
ent_city=Entry(root,textvariable=var1,font=18).place(x=180,y=55)

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
                     lab2=Label(root,text="Temperature = ",font=15).place(x=20,y=100)
                     lab3=Label(root,text=str(current_temperature),font=15).place(x=150,y=100)

                     lab4=Label(root,text=" Atmospheric pressure = ",font=20).place(x=20,y=160)
                     lab5=Label(root,text=str(current_pressure),font=15).place(x=240,y=160)

                     lab6=Label(root,text="Humidity (in %) = ",font=20).place(x=20,y=220)
                     lab8=Label(root,text=str(current_humidiy),font=15).place(x=180,y=220)

                     lab9=Label(root,text="description =  ",font=20).place(x=20,y=280)
                     lab10=Label(root,text=str(weather_description),font=15).place(x=140,y=280)
                     

          else:
               lab11=Label(root,text="City does not Exist",font=20,fg='red').place(x=100,y=340)
                     
               
 
     

but_sub=Button(root,text="submit",command=fun_run,font=20).place(x=100,y=400)
