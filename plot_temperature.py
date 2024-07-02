import time
from adafruit_circuitplayground import cp


print("startplot:","Temperature Sensor")

while True:
    print(cp.temperature * 1.8 +32)
    time.sleep(5)
