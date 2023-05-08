# def calculator(a,b,n):
#     if n=="+":
#         return a+b
#     elif n=="-":
#         return a-b
#     elif n=="*":
#         return a*b
#     elif n=="/":
#         return a/b
#     else:
#         return "this operation is not allowed"
# a=float(input("Enter first number\n"))
# b=float(input("Enter second number\n"))
# n=input("Enter the operation(+,-,*,/)\n")
# print(calculator(a,b,n))


#Basic calculator using class and objects

class BasicCalculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        try:
            return self.a / self.b
        except:
            return "This operation is not allowed"


print("Welcome to Basic Calculator")
while (True):
    a = input("Enter first number\n")
    b = input("Enter second number\n")
    if a.isdigit() != True or b.isdigit() != True:
        print("This is not supported.Enter valid digit")
        continue
    operation = input(
        "Choose from the operation\n1.Addition\n2.Substration\n3.Multiplication\n4.Division\nTo leave calculator type 'Exit'\n")
    calculator_obj = BasicCalculator(int(a), int(b))
    if operation == "1":
        print(calculator_obj.add())
    elif operation == "2":
        print(calculator_obj.sub())
    elif operation == "3":
        print(calculator_obj.mul())
    elif operation == "4":
        print(calculator_obj.div())
    elif operation.lower() == "exit":
        print("Exited!!")
        break
    else:
        print("This operation not supported,Choose from the options")

