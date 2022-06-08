#calculator
from replit import clear
from art import logo


def add(n1, n2):
    return(n1 + n2)
def multiply(n1, n2):
    return(n1 * n2)
def subtract(n1, n2):
    return(n1 - n2)
def divide(n1, n2):
    return(n1 / n2)

operations = {
"+": add,
"*": multiply,
"-": subtract,
"/": divide
}
def calculator():
    print(logo)
    num1 = float(input("What would you like the first number to be? "))
    for symbol in operations:
        print(symbol)

    keep_going = True
    while keep_going:
        operation_symbol = input("What operation would you like to perform? ")
        num2 = float(input("What would you like the next number to be? "))
        equation = operations[operation_symbol]
        answer = equation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        input_var = input(f"Type 'y' to contiue calculating with {answer}, or type 'n' to zero. ") 
        if input_var == "y":
            clear()
            print(logo)
            print(answer)
            num1 = answer
        elif input_var == "n":
            clear()
            calculator()
        else:
            print("Invalid input")
            

calculator()