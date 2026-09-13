from machine import Pin
from utime import sleep
import time

from ColorSense import ColorSensor
from MetalDetect import Metal_Detector

colorSensor = ColorSensor(s0=2, s1=3, s2=4, s3=5, out_pin=6)
metalDetector = Metal_Detector(out_pin=9)

yellow = (colorSensor.read_color('Yellow'), 0, 0)  # Initialize with the yellow color signature
cyan = (0, colorSensor.read_color('Cyan'), 0)  # Initialize with the cyan color signature
magenta = (0, 0, colorSensor.read_color('Magenta'))  # Initialize with the magenta color signature

detected_color = "Yellow"  # Start with yellow as the detected color

while True:
    # Read the color values
    if(colorSensor.read_color('Yellow') > yellow[0]):
        detected_color = "Yellow"
    elif(colorSensor.read_color('Cyan') > cyan[1]):
        detected_color = "Cyan"
    elif(colorSensor.read_color('Magenta') > magenta[2]):
        detected_color = "Magenta"
    print("Detected Color:", detected_color)