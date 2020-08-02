
class Bird:
    def __init__(self):
        print("Bird Initialized")
    def fly(self):
        print("Bird Can Fly")
class Crow(Bird):
    def __init__(self):
        Bird.__init__(self)
        print("Crow Initialized")
class Sparrow(Bird):
    def __init__(self):
        Bird.__init__(self)
        print("Sparrow Initialized")
    def jump(self):
        print("it can jump")
s1=Sparrow()
a=issubclass(Sparrow,Bird)
print(a)

#c1=Crow()


#super(self)
       
