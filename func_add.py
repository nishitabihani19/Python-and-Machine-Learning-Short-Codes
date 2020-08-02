
def addition(v1,v2):
    global sum
    v5=8
    sum=v1+v2
    print("a+b=",sum)
    write()
    return sum,v5
'''
def sub():
    global sum
    sum=val1-val2
    print("a-b=",sum)
    write()
def mult():
    global sum
    sum=val1*val2
    print("a*b=",sum)
    write()
def div():
    global sum
    sum=val1/val2
    print("a/b=",sum)
    write()
'''

def write():
    print("result is",sum)
def square(s1=0):
    area=s1*s1
    print('area is',area)
def read(n1,n2,n3=0):
    print("n1",n1)
    print("n2",n2)
    print("n3",n3)
    print(str(n1)+n2)

val1=int(input("a:"))
val2=int(input("b:"))
str1=input("string :")
val3,val4=addition(val1,val2)
print("output is",val3)
print("output is",val4)
#sub()
#mult()
#div()
#square()
#square(val1)
#read(val1,str1,val2)
#read(val1,str1)
#read(n2=val1,n3=val2,n1=str1)
