# Add your Python code here. E.g.
from microbit import *


while True:
    if button_a.is_pressed():
        display.show('a')
   
    if button_b.is_pressed():
        display.show(Image.HEART_SMALL)
        
    if button_a.is_pressed() and button_b.is_pressed():
        display.show('o')
        sleep(2000)
    