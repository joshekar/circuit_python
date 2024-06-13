import board
from digitalio import DigitalInOut, Direction
import time


led = DigitalInOut(board.LED)


led.direction = Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
    
