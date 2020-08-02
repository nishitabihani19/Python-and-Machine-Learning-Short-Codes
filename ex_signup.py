def generate():
    global val4
    import random
    for x in range(1):
        val4=(random.randint(1,1000)*2)
        print(val4)
    return val4
def call():
    global val1
    print("1. Sign up")
    print("2. Sign in")
    val1=int(input("Enter:"))

def check(Username,Password,val5):
        import smtplib
        s=smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        password2="nishita19"
        s.login(Username,password2)
        print("hehe")
        message=str(val5)
        print("hehe1",message)
        #type(val5)
        s.sendmail(Username,Username,message)
        print("hehe2")
        s.quit()
def signin():
    global Username1
    global Password1
    global val5
    Username1=input("Enter Username:")
    Password1=input("Enter Password:")
    if(Username==Username1 and Password==Password1):
        print("id pass are correct")
        val5=generate()
        check(Username,Password,val5)
        OTP=input("Enter OTP:")
        if(OTP==str(val5)):
            print("You are Logged In")
        else:
            print("Wrong OTP")
    else:
        print("Please Enter Correct Value")    
def signup():
             First_name=input("Enter First name:")
             Last_name=input("Enter Last name:")
             global alt_email
             alt_email=input("Enter altername Email:")
             print("Date of Birth")
             Day=int(input("Enter Day:"))
             Month=int(input("Enter Month:"))
             Year=int(input("Enter Year:"))
             global Username
             Username=input("Enter Username:")
             global Password
             Password=input("Enter Password:")
             reenter_Pass=input("Re-enter password")
             print("1. Sign in")
             global val2
             val2=int(input("Enter:"))
             if(val2==1):
                 signin()
                
    
    
    

call()
if(val1==1):
    signup()
elif(val1==2):
    signin()
else:
    print("Please Enter Correct Value") 




    
                        
        
    
