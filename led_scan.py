import board
from digitalio import DigitalInOut, Direction, Pull
import time

#define LEDs that are connected to CPX connectors
red = DigitalInOut(board.A0) 
blue = DigitalInOut(board.A1) 
green = DigitalInOut(board.A2) 

#configure LEDs as output
red.direction = Direction.OUTPUT
blue.direction = Direction.OUTPUT
green.direction = Direction.OUTPUT

while True:
    #ALL ON
    red.value = True
    time.sleep(1)
    red.value = False
    blue.value = True
    time.sleep(1)
    blue.value = False
    green.value = True
    time.sleep(1)
    green.value = False
    blue.value = True
    time.sleep(1)
    blue.value = False
    
    
