a=int(input("enter"))
try:
    a=a/0
except ZeroDivisionError:
    a=0.001
    print('hi')
except NameError:
    a=input("enter alpha")
    print('hlo')
except TypeError:
    a=int(input("value"))
    print('hello')
except:
    print("sshgh")
finally:
    print("Abir The Fav")
