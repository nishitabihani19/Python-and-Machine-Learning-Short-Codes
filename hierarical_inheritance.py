class D():
     def __init__(self):
         print("this is class D")
class A(D):
    
    def __init__(self):
        D.__init__(self)
        print('this is class A')
        print('\n')
class B(D):
    def __init__(self):
        D.__init__(self)
        print('this is class B')
        print('\n')
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('this is class C')
        print('\n')

S1=C()

