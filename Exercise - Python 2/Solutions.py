print("Question 1")
for i in range(0,7):
    if((i==3) or (i==6)):
        continue
    else:
        print(i)

print("")
print("Question 2")
x=int(input())
y=int(input())
a=[]
for i in range(x):
    b=[]
    for j in range(y):
        m=i*j
        b.append(m)
    #print(b)   
    a.append(b)
print(a)

print("")
print("Question 3")
l=[1,2,3,4,5,6,7,8,9,10]
answer=list(filter(lambda x:(x%2==0),l))
print(answer)

print("")
l=[1,2,3,4,5,6,7,8,9,10]
print("Question 4")
answer=list(map(lambda x:x*x,l))
print(answer)

print("")
print("Question 5")
def func(*argus):
    for key in argus:
        print('name:'+str(key['name']))
        print('age:'+str(key['age']))

func({"name":"aman","age":2},{"name":"deepak","age":0})
