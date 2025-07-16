""" def find_min_max(numbers):
    if not numbers:  # 빈 리스트 체크
        return None, None
    
    min_val = numbers[0]  # 첫 번째 숫자를 최소값으로 초기화
    max_val = numbers[0]  # 첫 번째 숫자를 최대값으로 초기화
    
    for num in numbers:
        if num < min_val:  # 현재 숫자가 최소값보다 작으면
            min_val = num
        if num > max_val:  # 현재 숫자가 최대값보다 크면
            max_val = num
            
    return min_val, max_val

def main():
    try:
        # 입력 받기
        input_str = input()
        
        # 입력된 문자열을 공백으로 분리하고 float로 변환
        numbers = [float(x) for x in input_str.split()]
        
        # 최소값과 최대값 찾기
        min_val, max_val = find_min_max(numbers)
        
        # 결과 출력
        print(f"Min: {min_val}, Max: {max_val}")
        
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main() """

def find_min_max(numbers):
    if not numbers: # 빈 리스트 체크
        return None, None
    
    min_val = numbers[0]  # 첫 번째 숫자를 최소값으로 초기화
    max_val = numbers[0]  # 첫 번째 숫자를 최대값으로 초기화
    
    for num in numbers:
        if num < min_val:  # 현재 숫자가 최소값보다 작으면
            min_val = num
        if num > max_val:  # 현재 숫자가 최대값보다 크면
            max_val = num
            
    return min_val, max_val

def main():
    try:
        # 입력받기
        input_str = input("숫자를 입력 해주세요 : ")
        # 입력된 문자열을 공백으로 분리하고 float로 변환
        numbers = [float(x) for x in (input_str.split())]
        # 최소값과 최대값 찾기
        min_val, max_val = find_min_max(numbers)
        # 결과 출력
        print(f"Min: {min_val}, Max: {max_val}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()



