class Television:
    def __init__(self, channel, volume, on):
        self.channel1 = channel
        self.volume = volume
        self.on = on

    def show(self):
        print(f"channel: {self.channel1}, volume: {self.volume}")

    def setChannel(self, channel):
        self.channel1 = channel

    def getChannel(self):
        return self.channel1


tv1 = Television(1, 10, True)
print(tv1)
tv1.show()    

tv1 = Television(5, 20, False)
tv1.show()    