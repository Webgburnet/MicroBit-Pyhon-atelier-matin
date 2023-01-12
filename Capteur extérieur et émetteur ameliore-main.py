from microbit import *
import radio
radio.config(group=23)
radio.on()

while True:
    T=str(temperature())
    if (T != str(temperature())):
        radio.send(T)