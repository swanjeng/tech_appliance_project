def on_button_pressed_a():
    global start
    start = 1
    basic.show_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global start
    start = 0
    basic.show_number(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global angle
    if name == "angle1":
        angle = Math.map(value, 0, 1000, 30, 90)
radio.on_received_value(on_received_value)

angle = 0
start = 0
start = 0
radio.set_group(5)

def on_forever():
    if start == 1:
        SuperBit.servo(SuperBit.enServo.S1, angle)
        SuperBit.servo(SuperBit.enServo.S2, Math.map(angle, 30, 90, 90, 30))
    else:
        SuperBit.motor_stop_all()
basic.forever(on_forever)
