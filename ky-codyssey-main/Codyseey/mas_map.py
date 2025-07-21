"""
✅ 1. 음성출력 웹 애플리케이션 구현 (app.py)
적절한 위치에 david라는 이름으로 디렉토리(이하 작업 디렉토리)를 생성한다.

작업 디렉토리에 app.py라는 이름으로 파일을 추가하고 아래 코드로 저장한다.

from flask import Flask, request, Response
import os
from io import BytesIO
from gtts import gTTS

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/")
def home():

    text = "Hello, DevOps"

    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, "com", lang).write_to_fp(fp)

    return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생

if __name__ == '__main__':
    app.run('0.0.0.0', 80)
	
	
Python 패키지 관리자로 gTTS 패키지를 설치한다.
Visual Studio Code를 실행해서 작업 디렉토리를 오픈 한다.
Visual Studio Code에서 app.py를 실행한다.
웹브라우저로 접속하여 음성 출력을 확인한다.


✅ 2. 계산기 프로그램 구현 (calculator.py)
david라는 디렉토리에 작업한다.
다음 요구사항에 맞는 파이썬 계산기 프로그램을 calculator.py라는 이름의 파일로 작성한다:

📌 기능 요구사항

사용자 입력 받기
실수형 숫자 2개 입력
연산자 입력 (+, -, *, /)
기본 연산 기능
함수 이름	동작 설명
add(a, b)	덧셈
subtract(a, b)	뺄셈 (a - b)
multiply(a, b)	곱셈
divide(a, b)	나눗셈 (a / b)
예외 처리
b == 0일 때 "Error: Division by zero." 출력
잘못된 연산자는 "Invalid operator." 출력
출력 형식
"Result: &lt;계산결과&gt;"

🧱 구현 방식
모든 연산은 별도의 함수로 정의
input()으로 사용자 입력 처리
if __name__ == "__main__": 블록에서 실행
입력받은 숫자는 반드시 정수형 변환합니다.

개발환경	
개발환경
터미널에서 명령어를 이용해서 실행하지 않는다.
flask run 명령어를 사용하지 않는다.
Visual Studio Code만을 사용해서 코드 편집 및 실행한다.

제약조건	
제약사항
터미널에서 명령어를 이용해서 실행하지 않는다.
flask run 명령어를 사용하지 않는다.
Visual Studio Code만을 사용해서 코드 편집 및 실행한다.

보너스 과제
Python에서 안정적인 개발 환경을 구성하기 위해서 venv를 이용해서 가상환경을 구성하고 실행해 본다.
문자열 수식 입력 방식 계산기 기능 추가
사용자가 한 줄로 수식을 입력하면 해당 수식을 해석하여 계산 결과를 출력하는 기능을 구현합니다.

예시 입력:
Enter expression: 2 + 3
Result: 5.0

✅ 구현 요구사항
Python 파일: 기존 calculator.py에 기능 추가
사용자 입력 형식: "숫자 연산자 숫자" 형태 (공백 포함)
연산자는 하나만 허용
허용 연산자: +, -, *, /
예외 처리 포함:
잘못된 입력 형식
0으로 나누는 경우
"""

import pandas as pd

def load_and_analyze_data():
    """데이터 파일들을 불러와서 분석하는 함수"""
    
    print("=" * 60)
    print("📂 1단계: 데이터 수집 및 분석")
    print("=" * 60)
    
    # 1. CSV 파일들 불러오기
    print("\n1️⃣ CSV 파일 불러오기...")
    try:
        area_map = pd.read_csv('C:/codyssey/ky-codyssey-main/Codyseey/area_map.csv')
        area_struct = pd.read_csv('C:/codyssey/ky-codyssey-main/Codyseey/area_struct.csv')
        area_category = pd.read_csv('C:/codyssey/ky-codyssey-main/Codyseey/area_category.csv')
        
        print("✅ 모든 CSV 파일을 성공적으로 불러왔습니다.")
    except FileNotFoundError as e:
        print(f"❌ 파일을 찾을 수 없습니다: {e}")
        return None
    
    # 2. 각 파일의 내용 출력 및 분석
    print("\n2️⃣ 각 파일 내용 분석...")
    
    print("\n📊 area_map.csv 분석:")
    print(f"   - 행 수: {len(area_map)}")
    print(f"   - 열 수: {len(area_map.columns)}")
    print(f"   - 열 이름: {list(area_map.columns)}")
    print("\n   처음 5행:")
    print(area_map.head())
    
    print("\n📊 area_struct.csv 분석:")
    print(f"   - 행 수: {len(area_struct)}")
    print(f"   - 열 수: {len(area_struct.columns)}")
    print(f"   - 열 이름: {list(area_struct.columns)}")
    print("\n   처음 5행:")
    print(area_struct.head())
    
    print("\n📊 area_category.csv 분석:")
    print(f"   - 행 수: {len(area_category)}")
    print(f"   - 열 수: {len(area_category.columns)}")
    print(f"   - 열 이름: {list(area_category.columns)}")
    print("\n   전체 내용:")
    print(area_category)
    
    # 3. 구조물 ID를 이름으로 변환
    print("\n3️⃣ 구조물 ID를 이름으로 변환...")
    
    # area_category를 딕셔너리로 변환하여 매핑
    category_dict = dict(zip(area_category['category'], area_category['struct']))
    
    # area_struct에 구조물 이름 추가
    area_struct['struct_name'] = area_struct['category'].map(category_dict)
    
    print("✅ 구조물 ID를 이름으로 변환 완료")
    print("\n   변환된 area_struct (처음 5행):")
    print(area_struct.head())
    
    # 4. 세 데이터를 하나의 DataFrame으로 병합
    print("\n4️⃣ 데이터 병합...")
    
    # area_map과 area_struct를 x, y 좌표 기준으로 병합
    merged_data = pd.merge(area_map, area_struct, on=['x', 'y'], how='inner')
    
    # area 기준으로 정렬
    merged_data = merged_data.sort_values('area')
    
    print("✅ 데이터 병합 및 정렬 완료")
    print(f"   - 병합된 데이터 행 수: {len(merged_data)}")
    print(f"   - 병합된 데이터 열 수: {len(merged_data.columns)}")
    print("\n   병합된 데이터 (처음 5행):")
    print(merged_data.head())
    
    # 5. area 1에 대한 데이터만 필터링
    print("\n5️⃣ area 1 데이터 필터링...")
    
    area1_data = merged_data[merged_data['area'] == 1]
    
    print(f"✅ area 1 데이터 필터링 완료")
    print(f"   - area 1 데이터 행 수: {len(area1_data)}")
    print("\n   area 1 데이터:")
    print(area1_data)
    
    # 6. 보너스: 구조물 종류별 요약 통계를 리포트로 출력
    print("\n6️⃣ 보너스: 구조물 종류별 요약 통계...")
    
    # 전체 데이터에서 구조물 종류별 통계
    print("\n📈 전체 지역 구조물 종류별 통계:")
    struct_summary = merged_data['struct_name'].value_counts()
    print(struct_summary)
    
    # area 1에서 구조물 종류별 통계
    print("\n📈 area 1 구조물 종류별 통계:")
    area1_struct_summary = area1_data['struct_name'].value_counts()
    print(area1_struct_summary)
    
    # 구조물별 상세 통계
    print("\n📊 구조물별 상세 통계:")
    struct_detailed = merged_data.groupby('struct_name').agg({
        'area': ['count', 'nunique'],
        'x': ['mean', 'min', 'max'],
        'y': ['mean', 'min', 'max']
    }).round(2)
    print(struct_detailed)
    
    return area1_data, merged_data

def main():
    """메인 함수"""
    print("☕ 반달곰 커피 데이터 분석 프로그램")
    print("=" * 60)
    
    # 데이터 분석 실행
    result = load_and_analyze_data()
    
    if result:
        area1_data, merged_data = result
        print("\n" + "=" * 60)
        print("✅ 1단계 데이터 수집 및 분석 완료!")
        print("=" * 60)
        print(f"📊 분석 결과:")
        print(f"   - 전체 데이터: {len(merged_data)}개 행")
        print(f"   - area 1 데이터: {len(area1_data)}개 행")
        print(f"   - 구조물 종류: {merged_data['struct_name'].nunique()}개")
    else:
        print("\n❌ 데이터 분석 중 오류가 발생했습니다.")

if __name__ == "__main__":
    main() 