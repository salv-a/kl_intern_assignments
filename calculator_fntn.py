def calculator(a,b,n):
    if n=="+":
        return a+b
    elif n=="-":
        return a-b
    elif n=="*":
        return a*b
    elif n=="/":
        return a/b
    else:
        print("this operation is not allowed")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
n=input("Enter the operation")
print(calculator(a,b,n))