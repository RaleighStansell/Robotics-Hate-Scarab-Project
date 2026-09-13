from machine import Pin
from utime import sleep
import time

import ColorSense
import MetalDetect

colorSensor = ColorSense.ColorSensor(s0=2, s1=3, s2=4, s3=5, out_pin=6)
metalDetector = MetalDetect.Metal_Detector(out_pin=9)
Led=Pin(15, Pin.OUT)  # Assuming the LED is connected to pin 15

yellow = (colorSensor.read_color('Yellow'), 0, 0)  # Initialize with the yellow color signature
cyan = (0, colorSensor.read_color('Cyan'), 0)  # Initialize with the cyan color signature
magenta = (0, 0, colorSensor.read_color('Magenta'))  # Initialize with the magenta color signature

detected_color = "Yellow"  # Start with yellow as the detected color

while True:
    # Read the color values
    if(metalDetector.read_metal() and colorSensor.read_color(detected_color) > 300):
        Led.value(1)  # Turn on the LED
        print("Metal Detected!")
    # Wait for a short period before the next reading
    sleep(1)