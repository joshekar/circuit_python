import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1

while True:
    for i in range(10):
     	cp.pixels[i] =(225,0,0)
        time.sleep(0.1)
        
    for i in range(10):
     	cp.pixels[i] =(0,0,0)
        time.sleep(0.1)
        
