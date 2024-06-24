import board
import analogio
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 10)
light = analogio.AnalogIn(board.LIGHT)

while True:
    if light.value < 3000:
        for i in range(3,9):
            led[i] = (255,255,255)

        time.sleep(10)
    else:
        for i in range(3,9):
            led[i] = (0,0,0)
            
        time.sleep(10)
        
