import math

class BasicCalculator():
    def __init__(self, *args):
        self.args = list(args)

    def addition(self):
        sum = 0
        for i in self.args[0]:
            sum += i
        return sum

    def substraction(self):
        sub = self.args[0][0]  # substrating from first number
        t = self.args[0]
        for i in t[1:]:  # iterating through the remaining
            sub -= i
        return sub

    def multiplication(self):
        mult = 1
        for i in self.args[0]:
            mult *= i
        return mult

    def division(self):
        try:
            div = self.args[0][0]  # divides the first number
            t = self.args[0]
            for i in t[1:]:  # iterating through the rest
                div /= i
            return div
        except:
            return "This operation is not allowed"

    def power(self):
        exponent = int(input("Enter the power\n"))
        p = []
        for i in self.args[0]:
            p.append(pow(i, exponent))
        return p

    def sine(self):
        sine_values = []
        for i in self.args[0]:
            sine_values.append(math.sin(i))
        return sine_values


print("Welcome to calculator")
while (True):
    try:  # to catch non numbers
        n = int(input("Enter no. of values\n"))
        values = [int(input("Enter number-{}\n".format(i + 1))) for i in range(n)]
    except:
        print("This is not supported enter numbers")
        continue
    operation = input(
        "Choose the operation\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Power\n6.sine\n7.To exit\n")

    calculator_obj = BasicCalculator(values)
    if operation == "1":
        print(calculator_obj.addition())
    elif operation == "2":
        print(calculator_obj.substraction())
    elif operation == "3":
        print(calculator_obj.multiplication())
    elif operation == "4":
        print(calculator_obj.division())
    elif operation == "5":
        print(calculator_obj.power())
    elif operation == "6":
        print(calculator_obj.sine())
    elif operation == "7":
        print("Exited!!")
        break
    else:
        print("This operation not supported,Choose from the options")