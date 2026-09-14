from machine import Pin
from utime import sleep

class ReflectiveSensorArray:
    # Constructor to initialize the reflective sensor array with the specified pin numbers
    def __init__(self, pin_num1, pin_num2, pin_num3, pin_num4, pin_num5, pin_num6, pin_num7, pin_num8):
        self.pins = [
            Pin(pin_num1, Pin.IN),
            Pin(pin_num2, Pin.IN),
            Pin(pin_num3, Pin.IN),
            Pin(pin_num4, Pin.IN),
            Pin(pin_num5, Pin.IN),
            Pin(pin_num6, Pin.IN),
            Pin(pin_num7, Pin.IN),
            Pin(pin_num8, Pin.IN)
        ]

    # Method to read the value of a specific sensor in the array
    def read(self, index):
        return self.pins[index].value()

    # Methods to check if a specific sensor is reflective (returns 1) or non-reflective (returns 0)
    def is_reflective(self, index):
        return self.read(index) == 1

    def is_non_reflective(self, index):
        return self.read(index) == 0

    # Method to read the values of all sensors in the array
    def read_all(self):
        return [pin.value() for pin in self.pins]

    # Methods to read the reflective status of all sensors in the array
    def read_all_reflective(self):
        return [self.is_reflective(i) for i in range(len(self.pins))]

    def read_all_non_reflective(self):
        return [self.is_non_reflective(i) for i in range(len(self.pins))]


while True:
    sensor_array = ReflectiveSensorArray(16, 17, 18, 19, 20, 21, 22, 26)  # Replace with actual GPIO pin numbers
    readings = sensor_array.read_all()
    print("Sensor Readings:", readings)
    sleep(1)
