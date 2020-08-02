import math
from math import tan
from math import sin
from math import cos
from math import log
from math import log10
from math import pi
from math import pow
def call():
    val1=int(input("1. Basic calculater \n 2. Scientific Calculator \n 3.Exit \n Enter:"))
    if(val1==1):
        Basic_Calculator()
    elif(val1==2):
        sci_cal()
    elif(val1==3):
        task
    else:
        print("Enter Correct Value")
            
def Basic_Calculator():
    print("1. + \n 2. - \n 3. * \n 4. / \n 5. % \n ")
    val2=int(input("Enter:"))
    if(val2==1):
        add()
    elif(val2==2):
        sub()
    elif(val2==3):
        mult()
    elif(val2==4):
        div()
    elif(val2==5):
        per()
    else:
        print("Please Enter Valid Key")
    call()
global val5
def add():
    print("Enter the Values ")
    val3=float(input("Enter:"))
    val4=float(input("Enter:"))
    val5=val3+val4
    print("Result is :",val5)
def sub():
    print("Enter the Values ")
    val3=float(input("Enter:"))
    val4=float(input("Enter:"))
    val5=val3-val4
    print("Result is :",val5)
def mult():
    print("Enter the Values ")
    val3=float(input("Enter:"))
    val4=float(input("Enter:"))
    val5=val3*val4
    print("Result is :",val5)
def div():
    print("Enter the Values ")
    val3=float(input("Enter:"))
    val4=float(input("Enter:"))
    val5=val3/val4
    print("Result is :",val5)
def per():
    print("Enter the Values ")
    val3=float(input("Enter:"))
    val5=val3/100
    print("Result is :",val5)
def sci_cal():
    print("1. tan \n 2. cos \n 3. sin \n 4. log \n 5. x^y \n 6. 1/x \n 7.PI ")
    val2=int(input("Enter:"))
    if(val2==1):
        tan()
    elif(val2==2):
        cos()
    elif(val2==3):
        sin()
    elif(val2==4):
        log()
    elif(val2==5):
        power()
    elif(val2==6):
        divi()
    elif(val2==7):
        pie()
    else:
        print("Please Enter Valid Key")
    call()
def tan():
    print("Enter value of angle")
    val3=float(input())
    print("Result is ",math.tan(val3))

def cos():
    print("Enter value of angle")
    val3=int(input("cos("))
    print("Result is ",math.cos(val3))

def sin():
    print("Enter value of angle")
    val3=int(input("sin("))
    print("Result is ",math.sin(val3))

def log():
    print("Enter value for log")
    val3=int(input("log("))
    print("Result is ",math.log(val3))

def log10():
    print("Enter value for log")
    val3=int(input("("))
    print("Result is ",math.log10(val3))

def power():
    print("Enter values")
    val3=int(input("Enter : "))
    val4=int(input("Enter : "))
    print("Result is ",math.pow(val3,val4))
def divi():
    print("Enter value")
    val3=int(input("Enter : "))
    print("Result is ",1/val3)

def pie():
    print("Enter value")
    val3=int(input("Enter : "))
    print("Result is ",val3*3.14)

   
call()



    
