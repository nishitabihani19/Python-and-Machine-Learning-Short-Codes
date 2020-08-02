class A():
    def __init__(self):
        print('hi')
        print('this is class A')
class B():
    def __init__(self):
        print('hlo')
        print('this is class B')
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('this is class C')

S1=C()

