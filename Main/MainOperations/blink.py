from machine import Pin
from utime import sleep
import time

import ColorSense
import MetalDetect

colorSensor = ColorSense.ColorSensor(s0=2, s1=3, s2=4, s3=5, out_pin=6)
metalDetector = MetalDetect.Metal_Detector(out_pin=9)
Led=Pin(15, Pin.OUT)  # Assuming the LED is connected to pin 15

while True:
    # Read the color values
    yellow_value = colorSensor.read_color('Yellow')
    cyan_value = colorSensor.read_color('Cyan')
    magenta_value = colorSensor.read_color('Magenta')

    # Print the color values
    print("Yellow Value:", yellow_value)
    print("Cyan Value:", cyan_value)
    print("Magenta Value:", magenta_value)

    if(metalDetector.read_metal() and colorSensor.read_color('Yellow') > 1000):  # Adjust the threshold as needed
        print("Metal Detected!")
        Led.value(1)  # Turn on the LED
    else:
        Led.value(0)  # Turn off the LED
    # Wait for a short period before the next reading
    sleep(1)