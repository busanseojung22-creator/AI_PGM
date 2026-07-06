class Television:
    serialnumber = 0  # 클래스 변수 (모든 TV가 공유하는 카운터)

    def __init__(self, channel, volume, on):
        Television.serialnumber += 1  # TV가 만들어질 때마다 카운트 1 증가
        self.serialnumber = Television.serialnumber  # 개별 TV의 고유 시리얼 번호로 저장
        self.channel = channel
        self.volume = volume
        self.is_on = on

    def __str__(self):
        # 오타 수정: serialNumber -> serialnumber
        # 문법 수정: 문자열 끝에 닫는 따옴표와 괄호 추가
        return f"Television(serial_number={self.serialnumber}, channel={self.channel}, volume={self.volume}, is_on={self.is_on})"
        
    def set_channel(self, channel):
        self.channel = channel

    def get_channel(self):
        return self.channel


# 객체 생성
tv1 = Television(11, 10, True)
tv2 = Television(22, 20, False)
tv3 = Television(33, 30, True)

# 출력 확인
print(tv1)
print(tv2)
print(tv3)