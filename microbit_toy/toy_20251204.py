def cvtAng2Dir(ang: number):
    if ang < 45 or ang > 315:
        return 0
    elif 45 < ang and ang < 135:
        return 1
    elif 135 < ang and ang < 225:
        return 2
    elif 225 < ang and ang < 315:
        return 3
    return -1

def on_received_value(name, value):
    global _type, start, angle
    if name == "type":
        _type = value
    elif name == "start":
        start = value
        basic.show_number(value)
    elif start == 1 and name == "angle":
        angle = value
        if cvtAng2Dir(angle) == 0:
            music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
                music.PlaybackMode.IN_BACKGROUND)
            SuperBit.servo2(SuperBit.enServo.S1, 45)
            basic.pause(500)
            SuperBit.servo2(SuperBit.enServo.S1, 225)
            basic.pause(500)
            SuperBit.servo2(SuperBit.enServo.S1, 135)
        elif cvtAng2Dir(angle) == 1:
            music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
                music.PlaybackMode.IN_BACKGROUND)
            SuperBit.servo2(SuperBit.enServo.S1, 225)
            basic.pause(200)
            SuperBit.servo2(SuperBit.enServo.S1, 135)
        elif cvtAng2Dir(angle) == 3:
            music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
                music.PlaybackMode.IN_BACKGROUND)
            SuperBit.servo2(SuperBit.enServo.S1, 45)
            basic.pause(200)
            SuperBit.servo2(SuperBit.enServo.S1, 135)
        elif cvtAng2Dir(angle) == 2:
            music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
                music.PlaybackMode.IN_BACKGROUND)
            for index in range(3):
                SuperBit.servo2(SuperBit.enServo.S1, 225)
                basic.pause(500)
                SuperBit.servo2(SuperBit.enServo.S1, 45)
                basic.pause(500)
                SuperBit.servo2(SuperBit.enServo.S1, 135)
                basic.pause(500)
radio.on_received_value(on_received_value)

_type = 0
start = 0
angle = 0
angle = 400
start = 0
millis = input.running_time()
speed = 0
radio.set_group(5)
music.set_volume(150)
SuperBit.servo2(SuperBit.enServo.S1, 135)

def on_forever():
    global speed, _type
    if start == 1:
        if _type == 1:
            speed = Math.constrain(speed + 20, 0, 255)
        elif _type == 2:
            speed = Math.constrain(speed - 20, 0, 255)
        SuperBit.motor_run(SuperBit.enMotors.M2, speed)
    else:
        SuperBit.motor_stop_all()
        _type = 0
        speed = 0
basic.forever(on_forever)
