 # DAY 4 DSA
# Diagonal Difference Program
import os

def diagonalDifference(arr):

    sum1 = 0
    sum2 = 0

    n = len(arr)

    for i in range(n):
        sum1 = sum1 + arr[i][i]
        sum2 = sum2 + arr[i][n - 1 - i]

    return abs(sum1 - sum2)


if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
# -------------------------------------------------------------------------------------------------------------
    # Accending order bubble sort
def bubbleSort(arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1-i):
                if arr[j]>arr[j+1]:
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp

                    # arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__ == '__main__' :
    arr=[6,23,2,4,1,8,56,3]
    bubbleSort(arr)
    print(*arr)
# ---------------------------------------------------------------------------------------------------------------------
#  decending order bubble sort
def bubbleSort(arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1-i):
                if arr[j]<arr[j+1]:
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp

                    # arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__ == '__main__' :
    arr=[6,23,2,4,1,8,56,3]
    bubbleSort(arr)
    print(*arr)
# -----------------------------------------------------------------------------------------------------
#  Selection sort
def selectionSort(arr):
    for i in range(len(arr)):
        min=arr[i]
        loc=i
        for j in range(i+1,len(arr)):
            if min>arr[j]:
                min=arr[j]
                loc=j
        arr[i],arr[loc]=arr[loc],arr[i]
                
if __name__ == '__main__' :
    arr=[6,23,2,4,1,8,56,3]
    selectionSort(arr)
    print(*arr)
# -----------------------------------------------------------------------------------------------
#  Selection sort Descending order
def selectionSort(arr):
    for i in range(len(arr)):
        max=arr[i]
        loc=i
        for j in range(i+1,len(arr)):
            if max<arr[j]:
                max=arr[j]
                loc=j
        arr[i],arr[loc]=arr[loc],arr[i]
                
if __name__ == '__main__' :
    arr=[6,23,2,4,1,8,56,3]
    selectionSort(arr)
    print(*arr)
# __________________________________________________________________________________________________________________________

#  insertion sort: ascending order
def insertionsort(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        pos=i
        while current<arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
            arr[pos]=current
# ________________________________________________________________________________________________________________________
#  insertion sort: descending order
def insertionsort(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        pos=i
        while current>arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current           
                
    

                    
if __name__ == '__main__' :
    arr=[6,23,2,4,1,8,56,3]
    insertionsort(arr)
    print(*arr)
# _________________________________________________________________________________________________________________________
    # class and object
# class is the logical represtation of things it is like a blue print or template for object.
# object
# it is physical representation of class and physical reprentation of things.

# class student:
#     def show(self):
#         print("i am student")
# s=student();
# s.show();

# # student s=new student();
# # new student()
#      self---> instance method
#      no self pass---> staticmethod

# class student:
#     def __init__(self):
#         print("i am in show")
#     def show(self):
#         print("default constructor")

# s=student();
# s.show();

# class student:
#     def __init__()
# ____________________________________________________________________________________________________________________________

    # stack: push and pop
# Menu Driven Stack Program
import sys

class Stacks:

    def push(self):
        pass

    def pop(self):
        pass

    def traverse(self):
        pass

    def peek(self):
        pass


if __name__ == '__main__':

    obj = Stacks()

    while True:

        print("1. push")
        print("2. pop")
        print("3. peek")
        print("4. Traverse")
        print("0. exit")

        ch = int(input("Select any choice: "))

        if ch == 1:
            obj.push()

        elif ch == 2:
            obj.pop()

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            sys.exit(0)
# ---------------------------------------------------------------------------------------------
 # with size
import sys


class Stacks:

    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 5

    def isfull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False

    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, ele):
        if self.isfull():
            print("stack is full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")

    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            ele = self.stack.pop()
            self.top = self.top - 1
            print(ele, "is popped")

    def peek(self):
        if self.isempty():
            print("stack is empty")
        else:
            print("Top element is", self.stack[self.top])

    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])


if __name__ == '__main__':

    obj = Stacks()

    while True:

        print("1. push")
        print("2. pop")
        print("3. peek")
        print("4. Traverse")
        print("0. exit")

        ch = int(input("Select any choice: "))

        if ch == 1:
            ele = int(input("Enter data: "))
            obj.push(ele)

        elif ch == 2:
            obj.pop()

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            sys.exit(0)

# -------------------------------------------------------------------------------------------------
#  stack without  size
import sys

class Stacks:

    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 100

    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False

    def push(self, ele):
        if self.isFull():
            print("stack is full")
        else:
            self.top += 1
            self.stack.append(ele)
            print(ele, "is pushed")

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
            return ele

    def peek(self):
        print(self.stack[self.top])

    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])


if __name__ == '__main__':

    obj = Stacks()

    while True:

        print("1. push")
        print("2. pop")
        print("3. peek")
        print("4. Traverse")
        print("0. exit")

        ch = int(input("Select any choice: "))

        if ch == 1:
            ele = int(input("Enter data: "))
            obj.push(ele)

        elif ch == 2:
            ele = obj.pop()
            print(ele, "is popped")

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            sys.exit(0)   

# -------------------------------------------------------------------------------------------------
# revese array using stack
import sys

class Stacks:

    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 100

    def isfull(self):

        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False

    def isempty(self):

        if self.top == -1:
            return True
        else:
            return False

    def push(self, ele):

        if self.isfull():
            print("Stack is full")

        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")

    def pop(self):

        if self.isempty():
            print("Stack is empty")

        else:
            ele = self.stack.pop()
            self.top = self.top - 1
            return ele

    def traverse(self):

        for i in range(self.top, -1, -1):
            print(self.stack[i])


if __name__ == '__main__':

    obj = Stacks()

    arr = [1, 2, 3, 4, 5]

    for i in range(len(arr)):
        obj.push(arr[i])

    rev = []

    for i in range(len(arr)):
        ele = obj.pop()
        rev.append(ele)

    print(rev)
# --------------------------------------------------------------------------------------------------