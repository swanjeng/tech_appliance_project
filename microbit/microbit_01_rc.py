from microbit import *
import radio
import time

def constrain(value, lower, upper):
    if value < lower:
        return lower
    elif value > upper:
        return upper
    return value

radio.config(group=5)
radio.on()

while True:
    angle = accelerometer.get_y()
    angle = constrain(angle, 0, 1000)
    radio.send(str(angle))
    
    time.sleep(0.1)
