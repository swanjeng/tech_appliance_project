angle1 = 0
radio.set_group(5)

def on_forever():
    global angle1
    angle1 = Math.constrain(input.acceleration(Dimension.Y), 0, 1000)
    radio.send_value("angle1", angle1)
    basic.pause(100)
basic.forever(on_forever)
