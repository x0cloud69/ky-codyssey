def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

def calculate_expression():
    def get_precedence(op):
        if op in {'+', '-'}:
            return 1
        if op in {'*', '/'}:
            return 2
        return 0

    def apply_operator(operators, values):
        if not operators:
            return
        
        op = operators.pop()
        b = values.pop()
        a = values.pop()
        
        if op == '+':
            values.append(add(a, b))
        elif op == '-':
            values.append(subtract(a, b))
        elif op == '*':
            values.append(multiply(a, b))
        elif op == '/':
            values.append(divide(a, b))

    def evaluate_expression(expression):
        operators = []
        values = []
        i = 0
        
        # 공백 제거
        expression = expression.replace(" ", "")
        
        while i < len(expression):
            if expression[i].isdigit():
                # 숫자 파싱
                num = ""
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                values.append(float(num))
                i -= 1
            
            elif expression[i] == '(':
                operators.append(expression[i])
            
            elif expression[i] == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()  # '(' 제거
            
            elif expression[i] in {'+', '-', '*', '/'}:
                while (operators and operators[-1] != '(' and 
                       get_precedence(operators[-1]) >= get_precedence(expression[i])):
                    apply_operator(operators, values)
                operators.append(expression[i])
            
            i += 1
        
        while operators:
            apply_operator(operators, values)
        
        return values[0]

    while True:
        try:
            expression = input("계산식을 입력하세요 (종료하려면 'q' 입력): ")
            
            if expression.lower() == 'q':
                print("프로그램을 종료합니다.")
                break
            
            result = evaluate_expression(expression)
            print(f"결과: {result}")
            
        except Exception as e:
            print(f"오류가 발생했습니다: {e}")
            print("올바른 수식을 입력해주세요.")

# 프로그램 실행
if __name__ == "__main__":
    print("사칙연산 계산기 프로그램입니다.")
    print("사용 가능한 연산자: +, -, *, /")
    print("괄호 사용 가능: ()")
    print("예시: 5*3 + (8-3) * 3")
    calculate_expression()

