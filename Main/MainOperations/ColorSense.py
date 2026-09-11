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
    def read_signature(self):
        cyan = self.read_color("Cyan")
        magenta = self.read_color("Magenta")
        yellow = self.read_color("Yellow")

        return (cyan, magenta, yellow)

    # transforms the measured color signature to a normalized RGB value
    def normalize(self, sig):
        c, m, y = sig
        max_val = max(sig)

        if max_val == 0:
            return (0, 0, 0)

        return (
            int((c / max_val) * 255),
            int((m / max_val) * 255),
            int((y / max_val) * 255)
        )

    # compares the measured color signature to a target signature with a given tolerance
    def is_color(self, target_sig, tolerance=0.20):
        measured = self.normalize(self.read_signature())

        for i in range(3):
            if abs(measured[i] - target_sig[i]) > (target_sig[i] * tolerance):
                return False

        return True

# while True:
#     # Create a ColorSensor object with the appropriate pin numbers
#     color_sensor = ColorSensor(s0=2, s1=3, s2=4, s3=5, out_pin=6)

#     # Read the color values
#     yellow_value = color_sensor.read_color('Yellow')
#     cyan_value = color_sensor.read_color('Cyan')
#     magenta_value = color_sensor.read_color('Magenta')

#     # Print the color values
#     print("Yellow:", yellow_value)
#     print("Cyan:", cyan_value)
#     print("Magenta:", magenta_value)

#     # Wait for a second before the next reading
#     sleep(1)
