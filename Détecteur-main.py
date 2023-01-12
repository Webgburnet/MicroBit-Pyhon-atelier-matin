from microbit import *
import radio
radio.config(group=1)
radio.on()

display.clear()
signal=0

while True:
    message = radio.receive_full()
    if message:
        signal=message[1]
        if signal<=85:
            display.show(Image('00000:'
                               '00000:'
                               '00600:'
                               '00000:'
                               '00000'))
        elif signal <=70:
            display.show(Image('00000:'
                               '00600:'
                               '06960:'
                               '00600:'
                               '00000'))
        elif signal <-55:
            display.show(Image('00600:'
                               '03930:'
                               '69996:'
                               '03930:'
                               '00600'))
        elif signal >=-55:
            display.show(Image('99999:'
                               '99999:'
                               '99999:'
                               '99999:'
                               '99999'))
    if button_a.was_pressed():
        display.scroll(str(signal))