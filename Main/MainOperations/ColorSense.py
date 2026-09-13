from machine import Pin
from utime import sleep
import time

class ColorSensor:
    def __init__(self, s0, s1, s2, s3, out_pin):
        # Control pins
        self.s0 = Pin(s0, Pin.OUT) # Magenta Color
        self.s1 = Pin(s1, Pin.OUT) # Cyan Color
        self.s2 = Pin(s2, Pin.OUT) # Green Color
        self.s3 = Pin(s3, Pin.OUT) # Red Color
        # Output pin from sensor
        self.out_pin = Pin(out_pin, Pin.IN)

        # Set scaling to 20% (recommended for stability)
        self.s0.value(1)
        self.s1.value(0)

    def read_color(self, color):
        # Set the filter for the specified color
        if(color == 'Yellow'):
            self.s1.value(1)
            self.s2.value(1)
            self.s3.value(0)
        elif(color == 'Cyan'):
            self.s1.value(0)
            self.s2.value(1)
            self.s3.value(1)
        elif(color == 'Magenta'):
            self.s1.value(1)
            self.s2.value(0)
            self.s3.value(1)
        else:
            self.s1.value(0)
            self.s2.value(0)
            self.s3.value(0)

        # Wait for the sensor to stabilize
        sleep(0.1)
        # Measure the frequency of the output signal
        start_time = time.ticks_us()
        count = 0
        while time.ticks_diff(time.ticks_us(), start_time) < 100000:  # Measure for 100ms
            if self.out_pin.value() == 1:
                count += 1
                while self.out_pin.value() == 1:
                    pass  # Wait for the signal to go low
        return count

