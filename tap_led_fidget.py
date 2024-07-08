import time
from adafruit_circuitplayground import cp

# set tapped to true if tapped once
#cp.detect_taps = 1

while True:

    if cp.tapped:    
        position = 0
        sleeptime = 0.01

        #blink an LED 25 times
        for i in range(25):
            cp.pixels[position] = (164, 50, 168)
            time.sleep(sleeptime)
            cp.pixels[position] = (0, 0, 0)
            time.sleep(sleeptime)

            position = position + 1
            if position == 10:
                position = 0

            sleeptime = sleeptime + 0.02


