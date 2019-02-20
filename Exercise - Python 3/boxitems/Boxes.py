from abc import ABC, abstractmethod
class Box(ABC):
    
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def empty(self):
        pass
    @abstractmethod
    def count(self):
        pass

class item():
    def __init__(self,name,value):
        self.name=name
        self.value=value

class ListBox(Box):
    def __init__(self):
        #separate list for each instance of class
        lists=[]
        self.lists=lists
    def add(self,*items):
        """add items into a listbox"""
        for i in items:
            self.lists.append(i)
    def empty(self):
        """empties the box and returns the items as list"""
        l=[]
        for items in self.lists:
            l.append(items)
        self.lists.clear()#clears the list
        #print(self.lists)
        return l

    def count(self):
        """return count of number of items"""
        return len(self.lists)

class DictBox(Box):
    def __init__(self):
        """seperate dictionary for each object"""
        dicts={}
        self.dicts=dicts
    def add(self,*args):
        """adds all the argument items into dictionary"""
        for item in args:
            self.dicts.update({item.name:item.value})
       
    def empty(self):
        """empties the dictionary and returns the list to em"""
        l=[]
        for key,val in self.dicts.items():
            listitem=item(key,val)
            l.append(listitem)
        self.dicts.clear()#clears the dict
        return l

    def count(self):
        """count to no of items present"""
        return len(self.dicts.items())

def repack_boxes(*args):
    boxes=[]#list of boxes
    boxitems=[]#total number of items
    for values in args:#iterate to all boxes
        boxes.append(values)#get boxes to add into later
        for item in values.empty():
            boxitems.append(item)#add their items to a new list
    count=len(boxes)#total number of boxes
    itemperbox=int(len(boxitems)/count)#items per box
    modval=int(len(boxitems)%count)#if some extra value, then save to add that many later
    #print(modval)
    valindex=0
    #add equal amount of items to each of the box
    for valindex in range(count):
        for itemindex in range(itemperbox):
            boxes[valindex].add(boxitems[0])
            boxitems.remove(boxitems[0])
    
    #if more remain, add to the last box
    if(modval!=0):
        for i in range(modval):
            boxes[valindex].add(boxitems[0])
            boxitems.remove(boxitems[0])
    
    #print the items in each box
    for box in boxes:
        print('for box:'+str(box))
        x=box.empty()
        for i in x:
            print(i.value)




a=item('A',10)
b=item('B',20)
c=item('C',30)
d=item('D',40)
e=item('E',50)
f=item('F',60)
g=item('G',70)
h=item('H',80)
i=item('I',90)
j=item('J',100)
k=item('K',110)
l=item('L',120)
m=item('M',130)
n=item('N',140)
o=item('O',150)
p=item('P',160)
q=item('Q',170)
r=item('R',180)
s=item('S',190)
t=item('T',200)
u=item('U',210)
v=item('V',220)
w=item('W',230)
x=item('X',240)
y=item('Y',250)
z=item('Z',260)
aa=item('AA',270)
bb=item('BB',280)
cc=item('CC',290)
dd=item('DD',300)
ee=item('EE',310)
ff=item('FF',320)
gg=item('GG',330)
hh=item('HH',340)



#SAMPLE LISTBOX
"""lists=ListBox()
lists.add(a,b,c,d,d,d)"""
"""x=lists.empty()
for values in x:
    #print(values.name+":"+str(values.value))
    print(values)
#print(lists.count())"""

#SAMPLE DICTBOX
"""dicts=DictBox()
dicts.add(e,f,g,h)"""
"""x=dicts.empty()
for values in x:
    #print(values.name+":"+str(values.value))
    print(values)
#print(dicts.count())"""


#3 BOXES: 2 LISTBOXES OF 20 and 9 ITEM EACH
#1 DICTBOX OF SIZE 5
listA=ListBox()
listA.add(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t)
listB=ListBox()
listB.add(u,v,w,x,y,z,aa,bb,cc)
dictC=DictBox()
dictC.add(dd,ee,ff,gg,hh)

#EVENLY DISTRIBUTES THE ITEMS FROM BOXES
repack_boxes(listA,listB,dictC)
