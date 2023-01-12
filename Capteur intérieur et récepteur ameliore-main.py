# Imports go at the top
from microbit import *
import radio
radio.config(group=23)
radio.on()
outdoorTemp = '-'
T = temperature()
Tmin_int = 151
Tmax_int = -41
Tmin_ext = 151
Tmax_ext = -41

while True:
    message = radio.receive()
    if message:
        outdoorTemp = message
    if button_a.was_pressed():
        T=temperature()
        display.scroll(str(T))
    if button_b.was_pressed():
        display.scroll(outdoorTemp)
    if (Tmin_int > T) :
        Tmin_int=T
    if(Tmax_int < T):
        Tmax_int=T
    if (Tmin_ext > float(outdoorTemp)) :
        Tmin_ext=float(outdoorTemp)
    if(Tmax_ext < float(outdoorTemp)):
        Tmax_ext=float(outdoorTemp)  