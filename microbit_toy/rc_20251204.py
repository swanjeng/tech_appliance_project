def on_on_start():
    radio.send_value("type", 0)
ml.on_start(ml.event.still, on_on_start)

def on_on_start2():
    radio.send_value("type", 1)
ml.on_start(ml.event.acce, on_on_start2)

def on_button_pressed_a():
    radio.send_value("start", 1)
    basic.show_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_value("start", 0)
    basic.show_number(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    radio.send_value("angle", input.compass_heading())
    while input.logo_is_pressed():
        pass
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_on_start3():
    radio.send_value("type", 2)
ml.on_start(ml.event.event, on_on_start3)

radio.set_group(5)
input.calibrate_compass()
