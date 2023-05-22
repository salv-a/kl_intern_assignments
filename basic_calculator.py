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


# Basic calculator using class and objects

class BasicCalculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def add(self):
        return self.num_1 + self.num_2

    def sub(self):
        return self.num_1 - self.num_2

    def mul(self):
        return self.num_1 * self.num_2

    def div(self):
        try:
            return self.num_1 / self.num_2
        except ValueError:
            return "This operation is not allowed"


print("Welcome to Basic Calculator")
while True:
    num1 = input("Enter first number\n")
    num2 = input("Enter second number\n")
    if num1.isdigit() is not True or num2.isdigit() is not True:
        print("This is not supported.Enter valid digit")
        continue
    print("Choose from the options")
    operation = input("1.Addition\n2.Substration\n3.Multiplication\n4.Division\nTo leave calculator type 'Exit'\n")
    calculator_obj = BasicCalculator(int(num1), int(num2))

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
