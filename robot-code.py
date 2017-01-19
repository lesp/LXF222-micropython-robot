from microbit import *
import radio
radio.on()

for i in range(3):
    display.show(Image.HEART_SMALL)
    sleep(500)
    display.show(Image.HEART)
    sleep(500)
while True:
    incoming = radio.receive()
    if incoming == 'left':
        display.show(Image.ARROW_E)
        pin8.write_digital(0)
        pin12.write_digital(1)
        pin16.write_digital(0)
        pin0.write_digital(1)
    elif incoming == 'right':
        display.show(Image.ARROW_W)
        pin12.write_digital(0)
        pin8.write_digital(1)
        pin16.write_digital(1)
        pin0.write_digital(0)
    elif incoming == 'forward':
        display.show(Image.ARROW_N)
        pin12.write_digital(1)
        pin8.write_digital(0)
        pin16.write_digital(1)
        pin0.write_digital(0)
    elif incoming == 'reverse':
        display.show(Image.ARROW_S)
        pin12.write_digital(0)
        pin8.write_digital(1)
        pin16.write_digital(0)
        pin0.write_digital(1)    
    elif incoming == 'brakes':
        display.show(Image.SURPRISED)
        pin12.write_digital(0)
        pin8.write_digital(0)
        pin16.write_digital(0)
        pin0.write_digital(0) 
