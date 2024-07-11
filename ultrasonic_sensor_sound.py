import time 
import board 
import adafruit_hcsr04
from adafruit_circuitplayground import cp


#Sonar's trigger pin should be connected to CPX's A0 connector 
#and echo pin should be connected to CPX's A1 connector
#If not, update this with the correct pin names
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A1)

while True:
    try:
        if sonar.distance < 5 :
            cp.play_tone(700,10)
        else :
            cp.play_tone(700,1)
        print(sonar.distance)
    except RuntimeError:
        print("Retrying!")
    time.sleep(2)
