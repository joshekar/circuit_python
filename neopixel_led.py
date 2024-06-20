import board
from digitalio import DigitalInOut, Direction, Pull
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

print("Switch value is :", switch.value)

while True:
    if (switch.value==True):
        led[0] = (255,0,0)
        
    else:
        led[0] = (0,255,0)
    
