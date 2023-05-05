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
        return "this operation is not allowed"
a=float(input("Enter first number\n"))
b=float(input("Enter second number\n"))
n=input("Enter the operation(+,-,*,/)\n")
print(calculator(a,b,n))