def add(a,b):
    return a+b

def subtract(a, b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculate(a,b,operator):
    if operator == '+':
        return add(a,b)
    if operator == '-':
        return subtract(a,b)
    if operator == '*':
        return multiply(a,b)
    if operator == '/':
        if b == 0:
            raise ValueError("Error: Division by zero.")
        return divide(a,b)

def main():
    result = 0
    try:
       a = int(input("Enter first numner:"))
    except ValueError:
        print("Invalid number inpit:")
        return
    
    try:
        b = int (input("Enter second number:"))
    except ValueError:
        print("Invalid number input.")
        return
    
    operator = input("Enter operator (+, -, *, /): ")
    if operator not in ['+', '-', '*', '/']:

        print("Invalid operator input.")
        return

    try:
        result = calculate(a,b, operator)
        print(f"Result:  <{result}>")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
