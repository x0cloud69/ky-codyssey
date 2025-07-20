""" 
✅ 2. 복잡한 사칙연산 프로그램 구현하기 - **priority_calculator.py**
문제 3번에서 만들어진 **calculator.py 를 개선한다.**
입력된 문자열의 사칙연산(+,-,*,/) 우선순위를 고려하여 계산하는 프로그램을 작성한다.
괄호((, ))는 처리하지 않는다.
사칙연산의 일반적인 우선순위(,/ > +,-)를 적용하여 정확히 계산한다.

📌 기능 요구사항
입력 예시
4 + 5 * 3 - 2
사칙연산 우선순위에 따라 계산하여 올바른 결과 출력

예외 처리
0으로 나누는 경우 "Error: Division by zero." 출력
잘못된 입력 형식 시 "Invalid input." 출력
출력 예시

Result: 17.0
🧱 구현 방식 및 기술 요구사항
입력 문자열은 터미널에서 input()으로 입력받는다.
문자열을 공백 기준으로 나누어(split()) 처리한다.
기존 문제 3번 calculator.py의 연산 함수(add, subtract, multiply, divide)를 반드시 재사용한다.
Python 내장 함수 eval() 사용을 금지한다.
다음의 형식을 반드시 따른다.
if __name__ == "__main__":
    main()
개발환경	
개발환경
Visual Studio Code만을 사용해서 코드 편집 및 실행한다.
Git에서 기본 제공되는 명령어로 터미널에서 실행하며 별도의 도구를 사용하지 않는다.
커밋 명령어 사용시 에디터 없이 명령어로만 메시지를 입력한다.
revert 명령어를 사용해서 되돌리기 한다.
제약조건	
제약사항
Visual Studio Code만을 사용해서 코드 편집 및 실행한다.
Git에서 기본 제공되는 명령어로 터미널에서 실행하며 별도의 도구를 사용하지 않는다.
커밋 명령어 사용시 에디터 없이 명령어로만 메시지를 입력한다.
revert 명령어를 사용해서 되돌리기 한다.
보너스 과제
reset과 revert의 차이점과 협업시 revert를 추천하는 이유를 Markdown 문서로 제출한다.

문서의 이름은 reset_vs_revert.md로 저장해서 제출한다.

문자열의 사칙연산(+,-,*,/) 우선순위에 더하여 괄호(**(**, **)**)의 우선순위를 정확히 고려하여 계산하는 프로그램을 작성한다.

예를 들어, 다음과 같은 입력이 있을 때:

( 4 + 5 ) * ( 3 - 2 )
프로그램은 괄호 및 연산자의 우선순위를 적용하여 정확한 결과를 출력해야 한다.

Result: 9.0 """

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
    # 사칙연산 우선순위를 고려하여 계산하는 함수
    def get_precedence(op):
        if op in {'+', '-'}:
            return 1
        if op in {'*', '/'}:
            return 2
        return 0

    # 연산자 우선순위에 따라 연산을 수행 하는 함수
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

    # 문자열을 계산하는 하는 함수
    def evaluate_expression(expression):
        operators = []
        values = []
        i = 0
        
        # 공백 제거
        expression = expression.replace(" ", "")
        
        # 문자열을 순회하며 숫자와 연산자를 처리
        while i < len(expression):
            if expression[i].isdigit():
                # 숫자 파싱
                num = ""
                # 숫자가 소수점이 포함된 경우도 처리
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                values.append(float(num))
                i -= 1
            # 연산자 "(, ), +, -, *, /" 처리
            # 연산자 "("을 만나면 스택에 추가 
            # 연산자 ")"을 만나면 스택에서 연산자를 꺼내어 계산
            # 연산자 +, -, *, /을 만나면 우선순위에 따라 계산
            elif expression[i] == '(':
                operators.append(expression[i])
            
            elif expression[i] == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()  # '(' 제거
            
            elif expression[i] in {'+', '-', '*', '/'}:
                # opeaotors 연산자 처리 -1 은 맨뒤, 현재 연산자와 우선순위 비교
                # 현재 연산자보다 우선순위가 높은 연산자가 스택에 있는 경우
                # 스택에서 연산자를 꺼내어 계산하고 현재 연산자를 스택에 추가
                # 현재 연산자와 우선순위가 같거나 낮은 연산자가 스택에 있는 경우
                # 현재 연산자를 스택에 추가 
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

