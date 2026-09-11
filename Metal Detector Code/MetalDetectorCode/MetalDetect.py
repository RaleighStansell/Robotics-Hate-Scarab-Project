from machine import Pin
from utime import sleep
import time

class Metal_Detector:
    def __init__(self, out_pin):
        # Control pins
        self.sensor_pin = Pin(out_pin, Pin.IN)

    def read_metal(self):
        if self.sensor_pin.value() == 1:
            return True
        else:
            return False
        time.sleep(0.2)
        
