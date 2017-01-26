from microbit import *
import radio
radio.on()
display.scroll("Turn the wheel to drive the robot",delay=50)
while True:
    gesture = accelerometer.current_gesture()
    print(gesture)
    if gesture == "left":
        display.show(Image.ARROW_W)
        radio.send('left')
    elif gesture == "right":
        display.show(Image.ARROW_E)
        radio.send('right')
    elif gesture == "up":
        display.show(Image.ARROW_N)
        radio.send('forward')
    elif gesture == "down":
        display.show(Image.ARROW_S)
        radio.send('reverse')
    elif button_b.was_pressed():
        display.show(Image.SURPRISED)
        radio.send('brakes')
        