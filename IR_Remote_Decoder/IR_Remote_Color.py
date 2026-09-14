from machine import Pin
import time

ir = Pin(15, Pin.IN)

YELLOW  = 0xffa25d   # btn 1
MAGENTA = 0xff629d   # btn 2
CYAN    = 0xffe21d   # btn 3

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
    leader_low = measure_low()
    if leader_low < 8000 or leader_low > 12000:
        return None

    leader_high = measure_high()
    if leader_high < 3000 or leader_high > 6000:
        return None

    bits = ""
    for _ in range(32):
        low = measure_low()
        high = measure_high()
        if high > 1000:
            bits += "1"
        else:
            bits += "0"

    return int(bits, 2)

print("Color IR Decoder Ready...")

last_time = 0

while True:
    code = decode_nec()
    if code is not None:
        now = time.ticks_ms()
        if time.ticks_diff(now, last_time) > 200:
            if code == YELLOW:
                print("YELLOW")
            elif code == MAGENTA:
                print("MAGENTA")
            elif code == CYAN:
                print("CYAN")
            else:
                print("Other:", hex(code))
            print("----------------------")
            last_time = now
     
















