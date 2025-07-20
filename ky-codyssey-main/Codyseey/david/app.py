# reuest : 클라이언트로부터 받은 HTTP 요청 정보를 담고 있는 객체 (get, post 등)
# Response : 클라이언트에게 응답할 HTTP 응답 정보를 담고 있는 객체 (예: 음성 파일, json 데이터 등)
from flask import Flask, request, Response
# os : 운영체제와 상호작용하기 위한 모듈 (환경변수,파일조작,경로관리 등)
import os
#메모리 사용을 위해 BytesIO를 사용 
from io import BytesIO
#Google Text-to-Speech 라이브러리
from gtts import gTTS

# 환경변수에서 기본 언어 설정, 없으면 'ko'로 설정
DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')

# Flask 애플리케이션 생성
app = Flask(__name__)

# Flask 애플리케이션의 루트 경로에 대한 라우트 설정
@app.route("/")

def home():

    # 음서으로 변환할 텍스트
    text = "Hello, DevOps"
    #text = "안녕하세요, DevOps"

    # 언어 설정, 쿼리 파라미터에서 'lang' 값을 가져오고, 없으면 기본 언어 사용
    lang = request.args.get('lang', DEFAULT_LANG)
    # BytesIO 객체 생성
    # gTTS를 사용하여 텍스트를 음성으로 변환하고 BytesIO 객체에 저장
    fp = BytesIO()

    #gTTS를 사용하여 텍스트를 음성으로 변환
    #text: 변환할 텍스트
    #com: 음성 합성 엔진 (예: 'com'은 Google TTS)
    #lang: 언어 코드 (예: 'ko'는 한국어, 'en
    gTTS(text, "com", lang).write_to_fp(fp)

    # 생성된 음성 파일을 HTTP 응답으로 반환
    # mimetype은 'audio/mpeg'로 설정 브라우저가 음성파일로 인식하도록 함
    #'video/mp4'         # MP4 비디오
    #'video/mpeg'        # MPEG 비디오
    #'video/webm'        # WebM 비디오
    return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생

if __name__ == '__main__':
    app.run('0.0.0.0', 80)