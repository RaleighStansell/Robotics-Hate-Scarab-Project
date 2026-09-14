#DECODER:
from machine import Pin
import time

ir = Pin(16, Pin.IN)

def wait_for_low():
    while ir.value() == 1:
        pass

def wait_for_high():
    while ir.value() == 0:
        pass

def measure_low():
    wait_for_low()
    start = time.ticks_us()
    wait_for_high()
    end = time.ticks_us()
    return time.ticks_diff(end, start)

def measure_high():
    wait_for_high()
    start = time.ticks_us()
    wait_for_low()
    end = time.ticks_us()
    return time.ticks_diff(end, start)

def decode_nec():
    # Leader LOW (~9000–11000)
    leader_low = measure_low()
    if leader_low < 8000 or leader_low > 12000:
        return None

    # Leader HIGH (~4500)
    leader_high = measure_high()
    if leader_high < 3000 or leader_high > 6000:
        return None

    bits = ""

    # NEC encodes bits in HIGH duration
    for _ in range(32):
        low = measure_low()
        high = measure_high()

        if high > 1000:
            bits += "1"
        else:
            bits += "0"

    return bits

def bits_to_hex(bits):
    return hex(int(bits, 2))

print("NEC Decoder Ready...")

last_code = None
last_time = 0

while True:
    bits = decode_nec()
    if bits:
        code = bits_to_hex(bits)

        # ignores all extra codes sent by various pulses sent by buttons 
        now = time.ticks_ms()
        if time.ticks_diff(now, last_time) > 200:
            print("Hex:", code)
            print("----------------------")
            last_code = code
            last_time = now