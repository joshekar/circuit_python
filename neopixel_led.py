import board
from digitalio import DigitalInOut, Direction, Pull
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

print("Switch value is :", switch.value)

while True:
    if (switch.value==True):
        for i in range(10) :   
            led[i] = (255,0,0)
            time.sleep(0.1)
            led[i] = (0,0,0)
    
        for i in range(10) :   
            led[i] = (0,255,0)
            time.sleep(0.1)
            led[i] = (0,0,0)
    
        for i in range(10) :   
            led[i] = (0,0,255)
            time.sleep(0.1)
            led[i] = (0,0,0)
