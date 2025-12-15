# Imports go at the top
from microbit import *
import radio

start = 0
angle = 0
radio.config(group=5)
# Code in a 'while True:' loop repeats forever
radio.on()
while True:
    message = radio.receive()
    if message:
        angle = int(message)
        angle = angle * 0.06 + 30
    if button_a.is_pressed():
        start = 1
    if button_b.is_pressed():
        start = 0
    display.show(start)
