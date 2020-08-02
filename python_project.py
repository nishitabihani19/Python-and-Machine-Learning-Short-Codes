import re,psutil,cv2,webbrowser,requests,pyowm,pygame,json,math,wikipedia
from moviepy.editor import *
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()

app_id = '1625ba25'
app_key = 'd915d2104f9e5a626dac165336c289b3'
language = 'en'


def fn_list():     
     print("please select any of them")
     print("1.System condition")
     print("2.change wallpaper")
     print("3.today's weather condition")
     print("4.wikipedia about any person")
     print("5.play background music")
     print("6.play video")
     print("7.performed calculator operation")
     print("8.send mail to your friend")
     print("9.send mobile message to your friend")
     print("10.make call to your friend")
     print("11.find  meaning of word")
     print("12.click your picture")
     print("13.check your location")
     print("14.move cursor according to your voice")
     print("15.open browser")


     def sys_cond():
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

     def change_wall():
          print("hello")
          
     def weather_cond():
          owm = pyowm.OWM('dc8c636c774e9480e689b16119a2dbf3')
          observation = owm.weather_at_place("alwar,india")
          w = observation.get_weather()
          temperature = w.get_temperature('celsius')
          wind = w.get_wind()
          print(wind)
          print(temperature)

     def wiki():
          word=input("enter  word..")
          complete_content=wikipedia.page(word)
          print(complete_content.images[0])
          print(complete_content.content)
          
     def music_play():
          print("hello")
          
     def video_play():
          dict={0:"720.mp4",
           1:"Daru_badnam_karti_dj_Remix.mp3",
           2:"HARYANVI_SONG_BY_LOKESH_GUJJER.mp3"
           }
          for i in range(3):
               print(dict[i])
               
          opn=int(input("select any of option..."))
          pygame.display.set_caption('Hello World!')
          clip = VideoFileClip(dict[opn])
          clip.preview()
          pygame.quit()

          
     def calc():         
          def Basic_cal():
              def Add():
                  x=int(input('Enter a number'))
                  y=int(input('Enter a number'))
                  print(x,"+",y,"=", x+y)
                  
              def Subtract():
                  x=int(input('Enter a number'))
                  y=int(input('Enter a number'))
                  print(x,"-",y,"=", x-y)
              
              def Multiply():
                  x=int(input('Enter a number'))
                  y=int(input('Enter a number'))
                  print(x,"*",y,"=", x*y)
              
              def Divide():
                  x=int(input('Enter a number'))
                  y=int(input('Enter a number'))
                  print(x,"/",y,"=", x/y)
              
              def Modulo():
                  x=int(input('Enter a number'))
                  y=int(input('Enter a number'))
                  print(x,"%",y,"=", x%y)
              
              def Back():
                  calculator()

              def Exit():
                  exit()

              print("Select operation.")
              print("1.Add")
              print("2.Subtract")
              print("3.Multiply")
              print("4.Divide")
              print("5.Modulo")
              print("6.Back")
              print("7.Exit")

              choice = int(input("Enter choice:"))
              dictionary={
                 1:Add,
                 2:Subtract,
                 3:Multiply,
                 4:Divide,
                 5:Modulo,
                 6:Back,
                 7:Exit}
              dictionary.get(choice)()
              Basic_cal()


          def Scientific_cal():
             
             def Back():
                 calculator()

             def Exit():
                 exit()
                  
             def Representation_Functions():
                  print('Choose one option')
                  print("1.ceil(x)")
                  print("2.copysign(x){Return a float with the magnitude (absolute value) of x but the sign of y}")
                  print("3.fabs(x){Return the absolute value of x}")
                  print("4.factorial(x)")
                  print("5.floor(x)")
                  print("6.isinfite(x){Return True if x is neither an infinity nor a NaN, and False otherwise}")
                  print("7.modf(x){Return the fractional and integer parts of x. Both results carry the sign of x and are floats}")
                  print("8.trunc(x){Return the Real value x truncated to an Integral }")
                  print("9.Back")
                  print("10.Exit")
              
                  def ceil():
                      x=float(input('Enter the value of x'))
                      print('ceil(',x,')=',math.ceil(x))

                  def copysign():
                      x=float(input('Enter the value of x'))
                      print('copysign(',x,')=',math.copysign(x))

                  def fabs():
                      x=float(input('Enter the value of x'))
                      print('fabs(',x,')=',math.fabs(x))

                  def fact():
                      x=float(input('Enter the value of x'))
                      print('factorial(',x,')=',math.factorial(x))

                  def floor():
                      x=float(input('Enter the value of x'))
                      print('floor(',x,')=',math.floor(x))

                  def isinf():
                      x=float(input('Enter the value of x'))
                      print('isinfinite(',x,')=',math.isinfinite(x))

                  def modf():
                      x=float(input('Enter the value of x'))
                      print('modf(',x,')=',math.modf(x))

                  def trunc():
                      x=float(input('Enter the value of x'))
                      print('trunc(',x,')=',math.trunc(x))

                  def Back():
                      Scientific_cal()


                  def Exit():
                      exit()

                  def opt():
                      print('Please enter correct option')
                      
                  choice = int(input("Enter choice:"))
                  dictionary={
                      1:ceil,
                      2:copysign,
                      3:fabs,
                      4:fact,
                      5:floor,
                      6:isinf,
                      7:modf,
                      8:trunc,
                      9:Back,
                      10:Exit}
                  dictionary.get(choice)()
                  Representation_Functions()

             def Trignometric_Functions():
                  print("Choose one option")
                  print("1.Sin(x)")
                  print("2.Cos(x)")
                  print("3.Tan(x)")
                  print("4.aSin(x)")
                  print("5.aCos(x)")
                  print("6.aTan(x)")
                  print("7.Back()")
                  print("8.Exit()")
                  #key1=input('')
                  
                  x=int(input("Enter the value of x"))
                  def Sin():
                        print('Sin(',x,')=',math.sin(x))

                  def Cos():
                        print('Cos(',x,')=',math.cos(x))

                  def Tan():
                       print('Tan(',x,')=',math.tan(x))

                  def aSin():
                       print('aSin(',x,')=',math.asin(x))

                  def aCos():
                       print('aCos(',x,')=',math.acos(x))

                  def aTan():
                       print('aTan(',x,')=',math.atan(x))

                  def Back():
                        Scientific_cal()

                  def Exit():
                        exit()

                  choice = int(input("Enter choice:"))
                  dictionary={
                      1:Sin,
                      2:Cos,
                      3:Tan,
                      4:aSin,
                      5:aCos,
                      6:aTan,
                      7:Back,
                      8:Exit}
                  dictionary.get(choice)()
                  
                  Trignometric_Functions()

             def Logarithmic_Functions():
                  print("Choose one option")
                  print("1.log(x,base)")
                  print("2.log1p(x)")
                  print("3.log2(x)")
                  print("4.log10(x)")
                  print("5.Back")
                  print("6.Exit")
                  key1=input('')

                  def log():
                      x=int(input("Enter the value of x"))
                      base=int(input('Enter the base'))
                      print('log(',x,',',base,')=',math.log(x,base))

                  def log1p():
                      print('log1p(',x,')=',math.log1p(x))

                  def log2():
                      x=int(input("Enter the value of x"))
                      print('log2(',x,')=',math.log2(x))

                  def log10():
                      x=int(input("Enter the value of x"))
                      print('log10(',x,')=',math.log10(x))

                  def Back():
                        Scientific_cal()

                  def Exit():
                          exit()

                  choice = int(input("Enter choice:"))
                  dictionary={
                      1:log,
                      2:log1p,
                      3:log2,
                      4:log10,
                      5:Back,
                      6:Exit}
                  dictionary.get(choice)()
                  
                  Exponential_Functions()

             def Angular_conversions():
                      print("Choose one option")
                      print("1.degrees(x)")
                      print("2.radians(x)")
                      print("3.Back")
                      print("4.Exit")
                      key1=input('')
                      
                      def degrees():
                              x=float(input('Enter the value of x'))
                              print('degrees(',x,')=',math.degrees(x))

                      def radians():
                              x=float(input('Enter the value of x'))
                              print('radians(',x,')=',math.radians(x))

                      def Back():
                              Scientific_cal()

                      def Exit():
                              exit()
                      choice = int(input("Enter choice:"))
                      dictionary={
                          1:degrees,
                          2:radians,
                          3:Back,
                          4:Exit}
                      dictionary.get(choice)()
                      
                      Angular_conversions()

             def Exponential_Functions():
                      print("Choose one option")
                      print("1.exp(x)")
                      print("2.expm1(x)")
                      print("3.pow(x,y)")
                      print("4.sqrt(x)")
                      print("5.Back")
                      print("6.Exit")
                      key1=int(input())
                      
                      def exp():
                              x=int(input('Enter the value of x'))
                              print('exp(',x,')=',math.exp(x))

                      def epml():
                              x=int(input('Enter the value of x'))
                              print('expm1(',x,')=',math.expm1(x))

                      def pow():
                              x=int(input('Enter the value of x'))
                              y=int(input('Enter the value of y'))
                              print('pow(',x,',',y,')=',math.expm1(x))

                      def sqrt():
                              x=int(input('Enter the value of x'))
                              print('expm1(',x,')=',math.expm1(x))

                      def Back():
                              Scientific_cal()

                      def Exit():
                              exit()

                      choice = int(input("Enter choice:"))
                      dictionary={
                          1:exp,
                          2:expml,
                          3:pow,
                          4:sqrt,
                          5:Back,
                          6:Exit}
                      dictionary.get(choice)()

                      Exponential_Functions()

             print("Choose one option")
             print("1.Representation Functions")
             print("2.Trignometric Functions")
             print("3.Logarithmic Functions")
             print("4.Angular Conversions")
             print("5.Exponential Functions")
             print("6.Back")
             print("7.Exit")
             key=int(input("Enter your choice"))

             dictionary={
                 1: Representation_Functions,
                 2: Trignometric_Functions,
                 3: Logarithmic_Functions,
                 4: Angular_conversions,
                 5: Exponential_Functions,
                 6: Back,
                 7: Exit
                 }
             dictionary.get(key)()
             
             Scientific_cal()


          def calculator():
              print("Choose one option")
              print("1.Basic Calculator")
              print("2.Scientific Calculator")
              print("3.Exit")
              num=input('')

              if num == '1':
                  Basic_cal()

              elif num == '2':
                  Scientific_cal()

              elif num == '3':
                  exit()

              else:
                  print("Please enter correct option")

              calculator()
          calculator()
                    

     def send_mail():
          username=input("enter your mail id:")
          password=input("enter password:")
          s.login(username,password)
          resp=input("enter other mail:")
          msg=input("enter text that u want to send")
          s.sendmail(username,resp,msg)
          print("mail send success")
          s.quit()
          print("logout")

          

     def send_msg():
          mob_no=input(" enter  mobile number")
          url = "https://www.fast2sms.com/dev/bulk"
          text=input("enter message:")
          payload = f"sender_id=FSTSMS&message={text}&language=english&route=p&numbers={mob_no}"
          headers = {
          'authorization': "7aEPsfe6YBxVS2AFR5zbZ08pD1MyLWu3HI9tJhnNkKTv4orcmX9l56RQr10eStLNMizaoyO8gWcnjPwT",
          'Content-Type': "application/x-www-form-urlencoded",
          'Cache-Control': "no-cache",
          }
          response = requests.request("POST", url, data=payload, headers=headers)
          print(response.text)

     def make_call():
          print("hello")

     def ox_dict():
          word_id = input("enter the word:")
          url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word_id.lower()
          urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()
          r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
          p=r.json()
          print(p['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])


     def camera():
          cam = cv2.VideoCapture(0)
          img_counter = 0
          while True:
              ret, frame = cam.read()
              cv2.imshow("test", frame)
              if not ret:
                  break
              k = cv2.waitKey(1)

              if k%256 == 27:
                  # ESC pressed
                  print("Escape hit, closing...")
                  break
              elif k%256 == 32:
                  # SPACE pressed
                  img_name = "opencv_frame_{}.png".format(img_counter)
                  cv2.imwrite(img_name, frame)
                  print("{} written!".format(img_name))
                  img_counter += 1
          cam.release()
          cv2.destroyAllWindows()

     def current_location():
          print("hello")
     def cursor_move():
          print("hello")
     def open_browser():
          webbrowser.open('https://www.google.com/')
      
     choice=int(input("enter choice:"))
     dict1={
          1:sys_cond, 
          2:change_wall,
          3:weather_cond,
          4:wiki,
          5:music_play,
          6:video_play, 
          7:calc,
          8:send_mail,
          9:send_msg,
          10:make_call,
          11:ox_dict,
          12:camera,
          13:current_location,
          14:cursor_move,
          15:open_browser}
     dict1.get(choice)()
     
fn_list()
