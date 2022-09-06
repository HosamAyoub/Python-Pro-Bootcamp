#Calculator
from art import logo
#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtact(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtact,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    for operation in operations:
        print(operation)
    cont = True
    while (cont):
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        operation_function = operations[operation_symbol]
        result = operation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            cont = False
            calculator()

calculator()