
# DAY 3 DSA
# def add():
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     res=a+b
#     print("addition is",res)
#     if__name__== '__main__':
#     add()

# function with parameter
def add(a,b):
        res=a+b
        print("addition is", res)
if __name__=='__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    add(a,b)
    
    # function with parameter and retrn value
# def add(a,b):
#         res=a+b
#         return res
#         if __name__=='__main__':
#             a=int(input("Enter a: "))
# b=int(input("Enter b: "))
#    r= add(a,b)
# print("Addition is", r)
    
# def add(a,b):
#     res=a+b
#     print("addition is", res)
# if __name__=='__main__':
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     add(a,b)
    
def add(a,b):
    res1=a+b
    res2=a-b
    res3=a*b
    return res1,res2,res3
if __name__=='__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    r1,r2,r3=add(a,b)
    print("addition",r1)
    print("multiplication",r2)
    print("division",r3)