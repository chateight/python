# Add your Python code here. E.g.
from microbit import *
import radio

radio.config(group=23)
radio.on()

while True:
    message = radio.receive()
    if message:
        display.scroll(temperature())
