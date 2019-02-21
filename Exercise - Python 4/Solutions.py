
#QUESTION 1
"""def fib(n):
    val1=0
    val2=1
    val3=val1+val2
    while(val1+val2<n):
        val3=val1+val2
        yield val3  
        val1=val2
        val2=val3

f=fib(100)
for values in f:
    print(values)"""


#QUESTION 2
"""def do_twice(func):
    func()
    func()

@do_twice
def sampefunc():
    print("This function will be executed twice")"""



#QUESTION 3
"""from collections import Counter
with open("samplef.txt","r") as file:
    content=file.readlines()
    words=[]
    for line in content:
        wordperline=line.split(" ")
        for word in wordperline:
            words.append(word)
        
    frequency=Counter(words).most_common(1)#print how many entries from it
    for key,val in frequency:
        print(key.capitalize()+" occured "+str(val)+" times")"""


#QUESTION 4
"""def isprime(value):
    num=value
    flag=True
    i=1
    for i in range(2,num):
        if(num%i==0):
            flag=False  
            break;
    return flag

def primefunction():
    i=2
    while(True):
        if(isprime(i)==True):
            print(i)
            yield 
        i+=1
        

value=2
primenum=primefunction()
a=str(input("Print prime number (y/n)?:"))
while(a=='y'):
    next(primenum)
    a=str(input("Print prime number (y/n)?:"))"""


#QUESTION 6 INCOMPLETE?
"""import re
string=str(input("Enter string:"))
regex=str(input("Enter regex"))
#regsearch
rm=re.findall(regex,string)
if(len(rm)==0):
    print("No match found")
else:
    print(rm)"""

    



