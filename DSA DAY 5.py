#  DAY 5 DSA
# simple manu drivan queue code  
import sys
class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5

    def isFull(self):
        if self.rear==self.CAPACITY-1:
            return True
        else:
            return False

    def insert(self,ele):
        pass

    def traverse(self):
        pass

    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False

    def delete(self):
        pass
        
    
    def peek(self):
        pass

if __name__ == '__main__':
    obj=Queue()
    while True:
        print("1. insert")
        print("2. delete")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch=int(input("select any choice"))
        if ch==1:
            ele=int(input("Enter data: "))
            obj.insert(ele)
        elif ch==2:
            obj.delete()
        elif ch==3:
            obj.peek()
        elif ch==4:
            obj.traverse()
        elif ch==0:
            sys.exit(0)    
# _________________________________________________________________________________________________________________________
# insert , Delete
import sys
class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5

    def isFull(self):
        if self.rear==self.CAPACITY-1:
            return True
        else:
            return False

    def insert(self,ele):
        if self.isFull():
            print("queue is full")
        else:
            self.rear=self.rear+1
            self.queue.append(ele)
            print("ele is inserted")


    def traverse(self):
        if self.isEmpty():
            print("queue is Empty")
        else:
            for i in range(self.rear+1):
                print(self.queue[i])


    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False

    def delete(self):
        if self.isEmpty():
            print("queue is Empty")
        else:
            ele= self.queue[self.rear]
            for i in range(1,rear+1):
                Queue[i-1]=Queue[i]
            self.front-=1   
                
    def peek(self):
        if self.isEmpty():
            print("queue is Empty")
        else:            
            print(self.queue[self.rear])

if __name__ == '__main__':
    obj=Queue()
    while True:
        print("1. insert")
        print("2. delete")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch=int(input("select any choice"))
        if ch==1:
            ele=int(input("Enter data: "))
            obj.insert(ele)
        elif ch==2:
            obj.delete()
        elif ch==3:
            obj.peek()
        elif ch==4:
            obj.traverse()
        elif ch==0:
            sys.exit(0)
# ______________________________________________________________________________________________________________________

# Reverse queue using stack
class Stacks:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5
    def isfull(self):
         if self.top==self.CAPACITY-1:
             return True
         else:
             return False
    def push(self,ele):
        if self.isfull():
            print("stack is full")
        else:
            self.top=self.top+1
            self.stack.append(ele)
            print(ele, "is pushed")
    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])

if  __name__ == '__main__':
     obj=Stacks()
     while True:
         print('1. push')
         print("2. pop")
         print("3. peek")
         print("4. Traverse")
         print("0. exit")
         ch=int(input("Select any choice"))
         if ch==1:
             ele=int(input("Enter data: "))     
             obj.push(ele)
         elif ch==2:
             obj.pop()
         elif ch==3:
             obj.peek()
         elif ch==4:
             obj.traverse()
         elif ch==0:
             sys.exit(0)    
# _________________________________________________________________________________________________________________________________
class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5

    def isFull(self):
        if self.rear==self.CAPACITY-1:
            return True
        else:
            return False

    def insert(self,ele):
        if self.isFull():
            print("queue is full")
        else:
            self.rear=self.rear+1
            self.queue.append(ele)
            print("ele is inserted")


    def traverse(self):
        if self.isEmpty():
            print("queue is Empty")
        else:
            for i in range(self.rear+1):
                print(self.queue[i])


    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False

    def delete(self):
        if self.isEmpty():
            print("queue is Empty")
        else:
            ele= self.queue[self.rear]
            for i in range(1,rear+1):
                Queue[i-1]=Queue[i]
            self.front-=1   
                
    def peek(self):
        if self.isEmpty():
            print("queue is Empty")
        else:            
            print(self.queue[self.rear])

if __name__==' __main__':
    obj1=Queue()
    obj2=Stack()
    n=(input("Enter number of element"))
    for i in range(obj1.CAPACITY):
        ele=int(input("Enter element"))
        obj1.insert(ele)
    for x in range(obj1.CAPACITY):
         ele=obj1.delete()
         obj2.push(ele)
  
    for x in range(obj1.CAPACITY):
        ele=obj2.pop()
        obj1.insert(ele) 

    obj1.traverse()           
# __________________________________________________________________________________________________________________________________
# insert element in the Array

arr=[1,2,3,4,5,6,7]
key=22
loc=3
arr.append(0)
print(arr)

for i in range(len(arr)-1,loc,-1):
    arr[i]=arr[i-1] 
arr[loc]=key    
print(arr)    
# ________________________________________________________________________________________________________________________
# delete key element from array
arr=[1,2,3,4,5,6,7]
loc=1
print(*arr)


for i in range(loc+1,len(arr)):
    arr[i-1]=arr[i] 
arr.pop()
print(arr) 
# _______________________________________________________________________________________________________________________
# Array Rotation:
arr=[1,2,3,4,5]

print(*arr)



for j in range(len(arr)-1,0,-1):
     temp=arr[-1]
     for i in range(len(arr)-1,0,- 1):
        arr[i]=arr[i-1]
        arr[0]=temp    
print(arr)
# __________________________________________________________________________________________________________________________
# Intersection of two Arrays:
arr1=[1,2,2,1]
arr2=[2,2]
arr3=[]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        arr1=arr2
        
        
        
#  ____________________________________________________________________________________________________________________ 

# Rearrange positive and Negative Number:

arr1=[-1,2,-3,4,5,-6]
neg=[]
pos=[]
res=[]
for i in range(len(arr)):
    if arr[i]<0:
        neg.append(arr[i])
    else:
        pos.append(arr[i])
for i in range(len(arr)):
     res.append(neg[i])
     res.append(pos[i])
# _________________________________________________________________________________________________________________________
    # string reverse
s="hello"
rev=" "
for x in s:
    rev=x+rev
print(rev)
# ___________________________________________________________________________________________________________________
# check for a valid palindromic strig:
#  question: write a program to check if a given string is a valid
# pallidromic string after ignoring non alphanumeric character.
# sample input: "A man, a plan, a canal: panama"
# expected ouput: valid palindrome

s= "A man, a plan, a canal: panama"
str=" "
for x in s:
    if x.isalpha():
        str=str+x
print(str)
str=str.lower()
print(str)
rev=str[: : -1]
if rev==str:
    print("pallindrome")
else:
    print("Not")
#_______________________________________________________________________________________________________________________ 

    #  check for Anagram:
    # write a program to check if two strings are anagrams of each other.
    # logic: check if the character counts in both strings are the same.
    # sample input: "listen" and "silent"
    # Expected output: Anagrams
# Check for Anagram

s1 = "Listen"
s2 = "Silent"

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")

  




    
