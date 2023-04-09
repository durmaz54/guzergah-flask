
class AGV2FLUTTER():
    def __init__(self):
        self.motor1_temp = 0
        self.motor2_temp = 0
        self.motor3_temp = 0
        self.battery = 0
        self.speed = 5
        self.readQR = ["A", "B"]
        self.startTimeSecond = 0
        self.image = "http://127.0.0.1/map"

    def readJson(self):
        rslt = {
            "battery": self.battery,
            "speed": self.speed,
            "qrlist": self.readQR,
            "startTimeSecond": self.startTimeSecond,
            "temperature": [self.motor1_temp, self.motor2_temp, self.motor3_temp],
            "image":self.image
        }
        return rslt
