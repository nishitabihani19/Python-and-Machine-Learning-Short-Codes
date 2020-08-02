class A():
    def __init__(self):
        print('this is class A')
        print('\n')
class B(A):
    def __init__(self):
        A.__init__(self)
        print('this is class B')
        print('\n')
class C(B):
    def __init__(self):
        B.__init__(self)
        print('this is class C')
        print('\n')

S1=C()
