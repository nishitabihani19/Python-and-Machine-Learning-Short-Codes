a=input("enter value:")
i=0
for i in range(len(a)):
    while i<int(len(a)):
        print("first",end="")
        j=0
        while j<4:
            print("inner",end="")
            j+=1
        i+=1
        print()
        
