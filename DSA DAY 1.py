# ********DSA DAY 1*********** 

# Last Digit Program
no = int(input("Enter the number: "))

res = no % 10

print("Last digit =", res)
# ________________________________________________________________________________________________
# Sum of Last Two Digits Program
no = int(input("Enter the number: "))

n1 = no % 10
no = no // 10

n2 = no % 10

res = n1 + n2

print("Sum =", res)
# _____________________________________________________________________________________________
# Sum of Three Digits Program
no = int(input("Enter the number: "))

n1 = no % 10
no = no // 10

n2 = no % 10
no = no // 10

n3 = no % 10

res = n1 + n2 + n3

print("Sum =", res)
#______________________________________________________________________________________________________________________

# reverse number
no = int(input("Enter the number: "))

n1 = no % 10
no = no // 10

n2 = no % 10
no = no // 10

n3 = no % 10

res = n1 * 100 + n2 * 10 + n3 * 1

print("Reverse Number =", res)
# --------------------------------------------------------------------------------------------------------------------------------

# no=123456789
# output = 10

no = int(input("Enter the no: "))
n1 = no%10
n2 = no//1000000
res(n1+n2)

print(res)

# ________________________________________________________________________________________________________________________________

# find max number
n1 =10
n2=20
n3=30

max=n1
if max<n2:
    max=n2
if max<n3:
    max=n3
print(max)

# _______________________________________________________________________________________________________________________
#  even and odd
no = 5

if no % 2 == 0:
    print(no, "is even")
else:
    print(no, "is odd"
        )
# ________________________________________________________________________________________________________________________

# per=75
# if per>=40 and per<=60:
#     print("take addmission in ABC clg")
# elif per>=61 and per<=80:
#     print("Take admmision in xyz clg")
# elif per>=80 and per<=100:
#     print("Take admission in RSQ clg")

# _______________________________________________________________________________________________________________________
cp = int(input("Enter cost price: "))
st = input("Are you student y/n: ")

if st == "y":
    if cp > 500:
        ds = cp * 0.10   # 10% discount
    else:
        ds = cp * 0.05   # 5% discount
else:
    if cp > 500:
        ds = cp * 0.08   # 8% discount
    else:
        ds = cp * 0.02   # 2% discount

net = cp - ds

print("Discount =", ds)
print("Net Amount =", net)

# _________________________________________________________________________________________________________________


# While loop with continue statement
i = 1
j = 10

while i < j:
    if i == 3:
        i = i + 1
        j = j - 1
        continue

    print(i, "\t", j)

    i = i + 1
    j = j - 1
# ________________________________________________________________________________________________________________________

# Looping Program

arr = [1, 2, 3, 4, 5]

for i in range(len(arr)):
    print(arr[i])

for x in arr:
    print(x)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

for j in range(10, 5, -1):
    if j == 8:
        continue
    print(j)

# ____________________________________________________________________________________________________________________________

# List Traversal and Slicing Program
arr = [11, 22, 33, 44, 55, 66, 77, 88]

print(arr)

# Using index
for i in range(len(arr)):
    print(arr[i], end=" ")

print()

# Using for-each loop
for x in arr:
    print(x, end=" ")

print()

# Indexing
print(arr[3])
print(arr[-1])

# Slicing
print(arr[1:5])
print(arr[:6])
print(arr[4:])
print(arr[:])
print(arr[::1])
print(arr[::2])
print(arr[::3])
print(arr[::-1])
print(arr[::-2])

# ________________________________________________________________________________________________________________________________

# Finding Maximum and Minimum Element in an Array/List
arr = [5, 3, 9, 2, 8]

maxi = arr[0]
mini = arr[0]

for i in range(1, len(arr)):
    if maxi < arr[i]:
        maxi = arr[i]

    if mini > arr[i]:
        mini = arr[i]

print("Maximum =", maxi)
print("Minimum =", mini)