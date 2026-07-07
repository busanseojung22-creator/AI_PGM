from datetime import datetime
import pyttsx3

# 경기 결과 입력 받는 곳
place = input("경기가 열린 곳은? ")
time = input("경기가 열린 시간은? ")
opponent = input("상대 팀은? ")
goals = input("손흥민은 몇 골을 넣었나요? ")
aids = input("도움은 몇 개인가요? ")
score_me = int(input("손흥민 팀이 넣은 골 수는? "))
score_you = int(input("상대 팀이 넣은 골 수는? "))

# 기사 작성하는 곳
news = "[프리미어 리그 속보(" + str(datetime.now()) + ")]\n"
news = news + "손흥민 선수는 " + place + "에서 " + time + "에 열린 경기에 출전하였습니다. "
news = news + "상대 팀은 " + opponent + "입니다. "

if score_me > score_you:
    news = news + "손흥민 선수의 팀이 " + str(score_me) + "골을 넣어 " + str(score_you) + "골을 넣은 상대 팀을 이겼습니다. "
elif score_me < score_you:
    news = news + "손흥민 선수의 팀이 " + str(score_me) + "골을 넣어 " + str(score_you) + "골을 넣은 상대 팀에게 졌습니다. "
else:
    news = news + "두 팀은 " + str(score_me) + "대" + str(score_you) + "로 비겼습니다. "

if int(goals) > 0 and int(aids) > 0:
    news = news + "손흥민 선수는 " + goals + "골에 도움 " + aids + "개로 승리를 크게 이끌었습니다. "
elif int(goals) > 0 and int(aids) == 0:
    news = news + "손흥민 선수는 " + goals + "골로 승리를 이끌었습니다. "
elif int(goals) == 0 and int(aids) > 0:
    news = news + "손흥민 선수는 골은 없지만 도움 " + aids + "개로 승리하는 데 공헌하였습니다. "
else:
    news = news + "아쉽게도 이번 경기에서 손흥민의 발끝은 침묵을 지켰습니다. "

print(news)

# ---------------- 음성으로 들려주는 곳 (오프라인 TTS) ----------------
# pyttsx3 는 인터넷 연결 없이 OS에 내장된 음성 엔진을 사용합니다.
#   - Windows : SAPI5
#   - macOS   : NSSpeechSynthesizer
#   - Linux   : espeak / espeak-ng (별도 설치 필요: sudo apt install espeak)
#
# 설치: pip install pyttsx3
# (Python 3.14는 아직 pyttsx3의 공식 지원 목록에는 없지만, 순수 파이썬으로
#  OS API를 감싸는 라이브러리라 대부분 문제없이 동작합니다. 설치 후 오류가
#  나면 pip install --upgrade pyttsx3 로 최신 버전을 받아보세요.)

engine = pyttsx3.init()

# 한국어 음성이 설치되어 있다면 자동으로 선택 (없으면 시스템 기본 음성 사용)
for voice in engine.getProperty('voices'):
    if 'ko' in voice.id.lower() or 'korean' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 170)   # 말하기 속도
engine.setProperty('volume', 1.0) # 음량 (0.0 ~ 1.0)

engine.save_to_file(news, "news_Son.mp3")  # 파일로 저장
engine.say(news)                            # 바로 음성 재생
engine.runAndWait()

print("음성 파일이 생성되었습니다: news_Son.mp3")
