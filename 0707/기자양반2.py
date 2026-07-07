from datetime import datetime
import pyttsx3

# TTS 엔진은 한 번만 초기화 (반복문 안에서 매번 만들 필요 없음)
engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    if 'ko' in voice.id.lower() or 'korean' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

count = 1  # mp3 파일 이름이 겹치지 않도록 번호 붙이기

while True:
    print("\n===== 새 경기 기사 작성 (그만 두려면 '그만' 입력) =====")

    place = input("경기가 열린 곳은? ")
    if place == "그만":
        break

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

    # 음성 파일 이름을 매번 다르게 저장 (news_Son_1.mp3, news_Son_2.mp3, ...)
    file_name = f"news_Son_{count}.mp3"
    engine.save_to_file(news, file_name)
    engine.say(news)
    engine.runAndWait()

    print(f"음성 파일이 생성되었습니다: {file_name}")
    count += 1

print("\n프로그램을 종료합니다.")
