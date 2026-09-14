from machine import Pin
from utime import sleep
import time

class Metal_Detector:
    # Constructor to initialize the metal detector with the specified output pin
    def __init__(self, out_pin):
        # Control pins
        self.sensor_pin = Pin(out_pin, Pin.IN)

    # Method to read the metal detection status
    def read_metal(self):
        if self.sensor_pin.value() == 1:
            time.sleep(0.2)
            return True
        else:
            time.sleep(0.2)
            return False

while True:
    metal_detector = Metal_Detector(15)
    if metal_detector.read_metal():
        print("Metal Detected")
    else:
        print("No Metal Detected")
        
