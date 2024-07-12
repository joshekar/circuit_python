import time 
import board 
import adafruit_hcsr04
from adafruit_circuitplayground import cp
import neopixel


#Sonar's trigger pin should be connected to CPX's A0 connector 
#and echo pin should be connected to CPX's A1 connector
#If not, update this with the correct pin names
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A1)

while True:
    try:
#get distance
        dist = sonar.distance
        print("Distance in cms", dist)
#convert to inches
        dist = dist / 2.54
        print("Distance in inches", dist)
#round to the nearest integer
        dist = round(dist)
        print("Rounded distance", dist)
#light up LEDs based on dist upto 10
        if dist < 10 :
            for i in range(dist):
                cp.pixels[i] =(225,255,255)
            time.sleep(2)
#light up LEDs red if dist >= 10
        else :
            for i in range(10):
                cp.pixels[i] =(255,0,0)
            time.sleep(2)
#switch off the LEDs and continue        
        cp.pixels.fill((0, 0, 0))

    except RuntimeError:
        print("Retrying!")
    time.sleep(2)
