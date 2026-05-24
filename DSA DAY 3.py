
# DAY 3 DSA

# Addition Program using Function
def add():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    res=a+b
    print("addition is",res)
    if__name__== '__main__'
    add() 
# _________________________________________________________________________________________________________________________
# function with parameter
def add(a,b):
        res=a+b
        print("addition is", res)
if __name__=='__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    add(a,b)
#________________________________________________________________________________________________________________________________   
    # function with parameter and retrn value
def add(a, b):
    res = a + b
    return res

if __name__ == '__main__':
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    r = add(a, b)

    print("Addition is", r)
#  _______________________________________________________________________________________________________________   # 

def add(a,b):
    res=a+b
    print("addition is", res)
if __name__=='__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    add(a,b)
#_______________________________________________________________________________________________________________________________ 
    # Arithmetic Operations Program using Function
def add(a, b):

    res1 = a + b
    res2 = a - b
    res3 = a * b

    return res1, res2, res3


if __name__ == '__main__':

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    r1, r2, r3 = add(a, b)

    print("Addition =", r1)
    print("Subtraction =", r2)
    print("Multiplication =", r3)

#___________________________________________________________________________________________________________________________
# Linear Search Program

def linear_search(n, arr, target):
    flag = False

    for i in range(n):
        if target == arr[i]:
            flag = True
            loc = i
            break

    if flag == True:
        print("Search is successful and present at index", loc)
    else:
        print("Search is unsuccessful")


if __name__ == '__main__':

    n = int(input("Enter size: "))

    arr = []

    for i in range(n):
        arr.append(int(input()))

    target = int(input("Enter no which is to be search: "))

    linear_search(n, arr, target)
#_________________________________________________________________________________________________________________________________ 

# Binary Search Program

def binary_search(n, arr, target):

    flag = False
    low = 0
    high = n - 1

    while low <= high:

        mid = (low + high) // 2

        if target == arr[mid]:
            flag = True
            loc = mid
            break

        elif target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    if flag == True:
        print("Search is successful and present at index", loc)

    else:
        print("Search is unsuccessful")


if __name__ == '__main__':

    n = int(input("Enter size: "))

    arr = []

    for i in range(n):
        arr.append(int(input()))

    target = int(input("Enter no which is to be search: "))

    binary_search(n, arr, target)