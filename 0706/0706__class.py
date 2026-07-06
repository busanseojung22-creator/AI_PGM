class Television:  # 3. 클래스 첫 글자는 대문자로 권장
    def __init__(self, channel, volume, on): 
        
        self.channel = channel
        self.volume = volume
        self.on = on 

    def set_channel(self, channel):
        
        self.channel = channel
        
    def get_channel(self):
        return self.channel
    def __str__(self):
        return f"Television(channel={self.channel}, volume={self.volume}, on={self.on}"

# 객체 생성 및 테스트
tv1 = Television(1, 10, True)
tv2 = Television(2, 20, False)

print(tv1.get_channel())
print(tv1.channel)



