#  ++++++++++++++++++++++ 2 days(DSA)+++++++++++++++++++++++++++++++++++++++++++++++++++

arr=[11,22,33]
print(arr)
for i in range(len(arr)):
    print(arr[i])

arr=[[1,2,3], 22,[4,5]]
print(arr)
for x in range(len(arr)):
    print(arr[x])

arr=[[1,2,3],[4,5,6],[7,8,9]]
print(arr)
for x in range(len(arr)):
    print(arr[x])
    print()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end="  ")
    print()
# _______________________________________________________________________________________________________________________________


s=set()

print(s)
print(type(s))

s={1,2,3,4,5,3,2,4,3,2,4,4}
print(s)

arr=[1,2,3,4,5,3,2,4,3,2,4,4]
s=set(arr)
arr=list(s)
print(arr)

# ______________________________________________________________________________________________________________________________

# accept value from user and print it
n=int(input("Enter the size"))

arr=[]
for i in range(n):
    ele=int(input("Enter the element: "))
    arr.append(ele)

    for i in range(len(arr)):
        print(arr[i])
# _____________________________________________________________________________________________________________________________        # 
        
# accept value from user && find sum of list
n=int(input("Enter the size: "))
print("Enter the element: ")
arr=[]
sum=0
for i in range(n):
    ele=int(input("Enter the element: "))
    arr.append(ele)
    for i in range(len(arr)):
        sum=sum+arr[i]
        print(sum)
        
# ______________________________________________________________________________________________________________________

# sum of even && odd

n=int(input("Enter the size: "))
print("Enter the element: ")
arr=[]
even=0
odd=0
for i in range(n):
    ele=int(input("Enter the element: "))
    arr.append(ele)
for i in range(len(arr)):
    if arr[i]%2==0:
        even=even+arr[i]
    else:
        
        odd=odd+arr[i]
        print(even)
        print(odd)
# ____________________________________________________________________________________________________________________________

# Even Odd Sum Array Program

n = int(input("Enter the size: "))
print("Enter the element: ")

arr = []
even = 0
odd = 0
e1 = 0
o1 = 0

for i in range(n):
    ele = int(input("Enter the element: "))
    arr.append(ele)

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even = even + arr[i]
        e1 = e1 + 1
    else:
        odd = odd + arr[i]
        o1 = o1 + 1

print(even)
print(odd)
# ___________________________________________________________________________________________________________________________________

# Special Number Program
n = 2025
a = 20
b = 25

sq = a + b
sq = sq ** 2

if n == sq:
    print("2025 is a special number")
else:
    print("2025 is not a special number")

# ______________________________________________________________________________________________________________________

# Tech Number Program
no = 2025

n1 = no % 100
n2 = no // 100

sum = n1 + n2
sq = sum ** 2

if sq == no:
    print("tech no")
else:
    print("not tech no")
#____________________________________________________________________________________________________________________________ 

#  Tech Number Program using While Loop    
no = 2025
save = no
count = 0

while no > 0:
    no = no // 10
    count = count + 1

no = save

if count % 2 == 0:
    mid = count // 2

    n1 = no % 10 ** mid
    n2 = no // 10 ** mid

    sum = n1 + n2
    sq = sum ** 2

    if sq == no:
        print("tech no")
    else:
        print("not tech no")
else:
    print("not tech no")

# ________________________________________________________________________________________________________________________


# sum of even && odd
n=int(input("Enter the size: "))
print("Enter the element: ")
arr=[]
even=0
odd=0
for i in range(n):
    ele=int(input("Enter the element: "))
    arr.append(ele)
for i in range(len(arr)):
    if arr[i]%2==0:
        even=even+arr[i]
    else:
        
        odd=odd+arr[i]
        print(even)
        print(odd)
#_______________________________________________________________________________________________________________________________ 

n = int(input("Enter the size: "))
print("Enter the elements: ")
arr = []
even = 0
odd = 0
e1 = 0
o1 = 0

for i in range(n):
    ele = int(input("Enter element {i+1}: "))
    arr.append(ele)

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even = even + arr[i]
        e1 = e1 + 1
    else:
        odd = odd + arr[i]
        o1 = o1 + 1

print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)
print("Count of even numbers:", e1)
print("Count of odd numbers:", o1)
# ____________________________________________________________________________________________________________________________

no=2025
n1=no%100
n2=no//100

sum=n1+n2
sq=sum**2
if  sq==no:
   print("tech no") 
else:
     print("no tech no")

#_______________________________________________________________________________________________________________________



#            j1 j2 j3 j4
# i=1      1  1   1  1
# i=2     2  2  2   2
# i=3    3   3  3  3
# i=4   4   4  4  4

for i in range(1,5):
    for j in range(1,5): 
        print(i,end=" ")
    print()

n=1
for i in range(1,5):
    for j in range(1,5): 
        print(n,end="\t ")
        n=n+1
    print()

# output:
# 1	 2	 3	 4	 
# 5	 6	 7	 8	 
# 9	 10	 11	 12	 
# 13	 14	 15	 16
# ____________________________________________________________________________________________________________________________________
n=1
for i in range(1,5):
    for j in range(1,5): 
        print(chr(n),end="\t ")
        n=n+1
    print()

    # OUTPUT:
# ABCD
# EFGH
# IJKL
# MNOP
# _______________________________________________________________________________________________________________________

for i in range(1,5):
    for j in range(1,i+1):
         print(chr(n),end="\t ")
    n=n+1
    print()


for i in range(4,0,-1):
    for j in range(1,i+1):
         print("*",end=" ")

    print()
    
# output:
# * * * * 
# * * * 
# * * 
# * 
# _______________________________________________________________________________________________________________________

sp=0
for i in range(4,0,-1):
    for x in range(sp):
        print("  ",end="")
        for j in range(1,i+1):
         print("*",end=" ")
         print()
         sp=sp+1
# __________________________________________________________________________________________________________________________
s="Learning python is very easy from rudhali mam"
print(s.find("python"))   
print(s.find("java")) 
print(s.find("r")) 
print(s.rfind("r")) 
# _____________________________________________________________________________________________________________________

s="abcabcabcabcadda"
print(s.count("a"))
print(s.count('ab'))
print(s.count('a',3,10))

# ______________________________________________________________________________________________________________________________
s="Learning python is very difficult from rudhali mam"
s1=s.replace("difficult","easy")
print(s1)
# ___________________________________________________________________________________________________________________________
s="Learning python is very difficult from rudhali mam"
ls=s.split()
print(ls)
print(len(ls))
# _____________________________________________________________________________________________________________________________

s="www.ashish.com"
ls=s.split(",")
print(ls)
# _____________________________________________________________________________________________________________________________
l=['Nagpur','Pune','Mumbai','delhi']
s=' '.join(l)
print(s)
# ________________________________________________________________________________________________________________________
# String Reverse Program
s = input("Enter string: ")

print(s[::-1])
# _______________________________________________________________________________________________________________________

s="Learning python is very easy from rudhali mam"
ls=s.split()
print(ls)
ls=ls[: :-1]
print(ls)
s=' '.join(ls)
print(s)

# ___________________________________________________________________________________________________________________________

s="Learning python is very easy from rudhali mam"
ls=s.split()
print(ls)
ans=" "
for x in ls:
    ans=ans+ls[x][: :-1]+" "
    print(ans)
# ________________________________________________________________________________________________________________________

# remove duplicate alphabets
s='ABCDABBBCCCDDEFEEF'
ans=" "
for i in range(len(s)):
    if i not in ans:
        ans=ans+i
        print(ans)
# ___________________________________________________________________________________________________________________________

no = input("Enter the number: ")

if no.isdigit():

    if len(no) == 10:

        if no.startswith("6") or no.startswith("7"):
            print("Valid Mobile Number")
        else:
            print("Invalid Starting Digit")

    else:
        print("Please enter 10 digit only")

else:
    print("Please enter number in digit format only")

# ______________________________________________________________________________________________________________________
d = {}

d[100] = 'raj'
d[200] = 'poonam'
d[300] = 'rudhali'

print(d)

# output:
# {100: 'raj', 200: 'poonam', 300: 'rudhali'}

print(d[100])

# output
# raj
# ____________________________________________________________________________________________________________________________
rec={}
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter name: ")
    per=float(input("Enter perc: "))
    rec[name]=per

    print(rec)
    for x in rec:
        print(x,'\t',rec[x])

