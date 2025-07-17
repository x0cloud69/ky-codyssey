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
    raise ValueError("Invalid number input.")

def main():
    result = 0
    try:
        a = float(input("Enter first numner:"))
        b = float(input("Enter second number:"))
        a = int(a)
        b = int(b)
        operator = input("Enter operator (+, -, *, /): ")
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator input.")
            return
        result = calculate(a, b, operator)
        print(f"Result:  <{result}>")
        # except ValueError as e:
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
