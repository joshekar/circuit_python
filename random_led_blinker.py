from adafruit_circuitplayground import cp
import time
import random


while True:
	#generate a random number between 0 and 9
    i = random.randint(0,9)

	#blink led[i] for 0.1 sec
    cp.pixels[i] =(225,50,155)
    time.sleep(0.1)

    cp.pixels[i] =(0,0,0)
    time.sleep(0.1)

        
