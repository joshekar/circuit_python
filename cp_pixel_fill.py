import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1

while True:
    cp.pixels.fill((255, 0, 0))
    time.sleep(1)
    cp.pixels.fill((0, 255, 0))
    time.sleep(1)
    cp.pixels.fill((0, 0, 255))
    time.sleep(1)
