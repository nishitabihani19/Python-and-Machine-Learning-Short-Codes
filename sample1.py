
def main_choice():
    option=int(input("press 1 for basic calc \n 2 for scientic calc:"))
    if(option==1):
        bas_calc()
    elif(option==2):
        sci_calc()
    else:
        print("please enter correct key") 

    
def bas_calc():
    global ip1,ip2,result,arg
    ip1=float(input("first value:"))
    ip2=float(input("second value:"))
    print("press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for division")
    choice=int(input("enter:"))
    def add():
        result=ip1+ip2
        print(result)
    def sub():
        result=ip1-ip2
        print(result)
    def multi():
        result=ip1*ip2
        print(result)
    def div():
        result=ip1/ip2
        print(result)

    dictionary={
        1 : add,
        2 : sub,
        3 : multi,
        4 : div}
    dictionary.get(choice)()

    cont1=int(input("for further continue press 0 \n to jump on main menu press 1"))
    if(cont1==0):
        bas_calc()
    elif(cont1==1):
        main_choice()
    else:
        exit()
                    


import math
def sci_calc():
    print("press 1 for trigonometric \n press: 1 for sine \n \t 2 for cos \n \t 3 for tan \n press 2 for power \n press 3 for squre root \n press 4 for logaritham")
    choice2=int(input("enter:"))
    def trigo():
        choice3=int(input("enter choice:"))
        angle=int(input("enter the value of angle"))
        def sine_fun():
            print("sin(",angle,")=",math.sin(angle))
        def cos_fun():
            print("cos(",angle,")=",math.cos(angle))
        def tan_fun():
            print("tan(",angle,")=",math.tan(angle))

        dict_trigo={
            1 : sine_fun,
            2 : cos_fun,
            3 : tan_fun}
        dict_trigo.get(choice3)()
    def power():
        x=float(input("enter first value"))
        y=float(input("enter second value"))
        print("power is:",math.pow(x,y))
        
    def squre_root():
        x=float(input("enter value:"))
        print("sqrt is:",math.sqrt(x))

    def logaritham_fun():
        x=float(input("enter value:"))
        print(math.log(x))
                
    dictionary2={
        1 : trigo,
        2 : power,
        3 : squre_root,
        4 : logaritham_fun}
    dictionary2.get(choice2)()
    count2=int(input("for further continue press 0 \n to jump on main menu press 1:"))
    if(count2==0):
        sci_calc()
    elif(count2==1):
        main_choice()
    else:
        exit()


def exit():
    print("thanks for use")

    
choice=int(input("press 1 for start: "))
if(choice==1):
    main_choice()
else:
    exit()

