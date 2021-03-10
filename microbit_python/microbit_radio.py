# Add your Python code here. E.g.
from microbit import *
import audio, speech
import radio

radio.config(group=23)
radio.on()

i = 0
while True:
    message = radio.receive()
    if message:
        display.show(i)
        if i >= 9:
            i = 0
        else:
            i += 1
    if accelerometer.was_gesture('shake'):
        display.clear()
        radio.send('duck')
