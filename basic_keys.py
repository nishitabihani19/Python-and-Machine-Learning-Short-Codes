#Regular Expressions
#direct library:re
#use to search any extension file or any pattern
#compile
#search
#findall
#group:to seprate any devide
#match:confirm that  match is exist or not

import re

'''
#search
#re.search(pattern,string)
my_string="we are learning python"
result=re.search(r"are",my_string) #r.'python' is a pattern of row type
print(result)
'''
'''
#compile
my_str="my name is pradeep"
my_regux=re.compile(r'pradeep') #creating object of group
result=my_regux.search(my_str)  #search through object
if(result):
    print("found",result.group())
else:
    print("not found")
'''

'''
my_str="my name is pradeep and mobile is 987123 78"
#my_regux=re.compile(r'\d{6}') #creating object of group
#my_regux=re.compile(r'\d\d\d\d\d\d') #creating object of group
my_regux=re.compile(r'\d{0,2}') #creating object of group

#my_regux=re.compile(r'\w\w\w\w\w\w\w') #creating object of group

result=my_regux.search(my_str)  #search through object
if(result):
    print("found",result.group())
else:
    print("not found")
'''

'''
1.\w:-word line character(a-z and A-Z)
2.\d:- for digits
3.\s:- white line character(' ',tab,new line)
4.\D:-those are not digits
5.\W:-those are not words
6.\S:-those are not white space
7.+:-for one or more times
8.*:- for 0 or more
9.?:-for 0 or 1
10.{k}:-for repeat k times
11.{m,n}:-in between m and n
12..:- any character except new line

'''

my_str="my nameis pradeep  and mobile is 987123 78"
#my_regux=re.compile(r'pr(a)?(deep|cho|hello)')
#my_regux=re.compile(r'pr(a)+(deep|cho|hello)')
#result=my_regux.search(my_str) 
my_regux=re.compile(r' +(@)')

#my_regux=re.compile(r'(\W\d\d){0,80}')
result=my_regux.findall(my_str) 
if(result):
     print(result)
else:
     print("not found")
'''
if(result):
    print("found",result.group())
else:
    print("not found")
'''
'''
import re
my_mail="choudharypradeep663@gmail.com"
rg_ob=re.compile(r'(@)
'''
     
'''
#task
folder1:
    folder2:
        a:
            1
        b:
            2
        c:
            3
    folder3:
        d:
            4
        e:
            5
        f:
            6
     folder4:
        g:
            7
        h:
            8
        i:
            9
           
result:folder1>folder3>d.txt=4         
'''        
