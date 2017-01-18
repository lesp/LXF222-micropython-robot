from microbit import *
import radio
radio.on()

while True:
    incoming = radio.receive()
    if incoming == 'left':
        pin8.write_digital(0)
        pin12.write_digital(1)
        pin16.write_digital(0)
        pin0.write_digital(1)
    elif incoming == 'right':
        pin12.write_digital(0)
        pin8.write_digital(1)
        pin16.write_digital(1)
        pin0.write_digital(0)
    elif incoming == 'forward':
        pin12.write_digital(1)
        pin8.write_digital(0)
        pin16.write_digital(1)
        pin0.write_digital(0)
    elif incoming == 'reverse':
        pin12.write_digital(0)
        pin8.write_digital(1)
        pin16.write_digital(0)
        pin0.write_digital(1)    
    elif incoming == 'brakes':
        pin12.write_digital(0)
        pin8.write_digital(0)
        pin16.write_digital(0)
        pin0.write_digital(0) 
        #sleep(1000)
        #pin12.write_digital(0)
        #sleep(1000)
