from machine import Pin
from utime import sleep_us, sleep
import time

class TCS3200:
    def __init__(self, s0, s1, s2, s3, out_pin):
        self.s0 = Pin(s0, Pin.OUT)
        self.s1 = Pin(s1, Pin.OUT)
        self.s2 = Pin(s2, Pin.OUT)
        self.s3 = Pin(s3, Pin.OUT)
        self.out_pin = Pin(out_pin, Pin.IN)

        # 20% scaling for stability
        self.s0.value(1)
        self.s1.value(0)

    def _set_filter(self, color):
        # Correct TCS3200 truth table
        if color == "RED":
            self.s2.value(0)
            self.s3.value(0)
        elif color == "BLUE":
            self.s2.value(0)
            self.s3.value(1)
        elif color == "CLEAR":
            self.s2.value(1)
            self.s3.value(0)
        elif color == "GREEN":
            self.s2.value(1)
            self.s3.value(1)

    def _read_frequency(self):
        start = time.ticks_us()
        count = 0
        while time.ticks_diff(time.ticks_us(), start) < 100000:  # 100 ms
            if self.out_pin.value() == 1:
                count += 1
                while self.out_pin.value() == 1:
                    pass
        return count

    def read_rgb(self):
        rgb = {}

        for color in ["RED", "GREEN", "BLUE"]:
            self._set_filter(color)
            sleep(0.02)
            rgb[color] = self._read_frequency()

        return rgb

    def detect_color(self, rgb):
        red = rgb["RED"]
        green = rgb["GREEN"]
        blue = rgb["BLUE"]
        if(red<150 and blue<100 and green<100):
            return "Black"
        else:
            if((red*0.75) > blue*1.25 and green > blue*1.25):
                return "Yellow"
            elif((blue*1.25) > (red*0.75) and blue*1.25 > green):
                return "Cyan"
            elif((red*0.75) > green and blue*1.25 > green):
                return "Magenta"
            else:
                return "Unknown"


sensor = TCS3200(s0=2, s1=3, s2=4, s3=5, out_pin=6)

Team1 = Pin(7, Pin.OUT)
Team2 = Pin(8, Pin.OUT)
Team3 = Pin(9, Pin.OUT)

while True:

    rgb = sensor.read_rgb()
    color = sensor.detect_color(rgb)
    if(Team1.value() == 1):
        detected_color = "Yellow"
    elif(Team2.value() == 1):
        detected_color = "Cyan"
    elif(Team3.value() == 1):
        detected_color = "Magenta"
    else:
        detected_color = "Unknown"
    if(color == detected_color):
        print("color found, color:", color, "RGB:", rgb)
    else:
        print("color not found, color:", color, "RGB:", rgb)
    sleep(0.2)
