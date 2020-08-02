'''
class A():
    __z = 5
    def __init__(self):
        print('hi')
        print('this is class A')
    def a(self,z):
        print('a is ',z)
class C(A):
    def __init__(self):
        #A.__init__(self)
        print('this is class C')

S1=C()
S1.a(10)

'''
class car():
    __speed =0
    def __init__(self):
        self.__speed=12
    def checkspeed(self):
        return self.__speed
swift =car()
print(swift.checkspeed())
swift.__speed=40
print(swift.checkspeed())
