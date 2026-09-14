from machine import Pin
import time

ir= Pin(15, Pin.IN)

# Values derived from Remote_Decoder.py
yellow  = 0xffa25d   #btn 1
magenta = 0xff629d   #btn 2
cyan    = 0xffe21d   #btn 3 

# start of pulse
def sense_for_low():
    while ir.value() == 1:
        pass
# end of pulse
def sense_for_high():
    while ir.value() == 0:
        pass    

def low_detected():
    sense_for_low()
    start= time.ticks_us()
    sense_for_high()
    end= time.ticks_us()
    return time.ticks_diff(end, start)

def high_detected():
    sense_for_high()
    start= time.ticks_us()
    sense_for_low()
    end= time.ticks_us()
    return time.ticks_diff(end, start)

def decode_NEC():
    lead_low = low_detected()
    if lead_low < 8000 or lead_low > 12000:
        return None

    lead_high = high_detected()
    if lead_high < 3000 or lead_high > 6000:
        return None

    bits = ""
    for _ in range (32):
        low = low_detected()
        high = high_detected()

        if high > 1000:
            bits += "1"

        else: bits += "0"

    return int(bits, 2)

print ("Press remote to change color.")

last_time = 0 
while True:
    button = decode_NEC()
    if button is not None:
        now = time.ticks_ms()
        if time.ticks_diff(now, last_time) > 200:
            if button == yellow:
                print("YELLOW")
            elif button == magenta:
                print("MAGENTA")
            elif button == cyan:
                print("CYAN")
            else: 
                print ("Unknown Button Pressed:", hex(button))

            print("-------------------")

            last_time = now
     
















