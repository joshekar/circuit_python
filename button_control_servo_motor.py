from adafruit_motor import servo
from adafruit_circuitplayground import cp
import time
import board
import pwmio


# create a PWMOut object on Pin A2.
# make sure the motor's orange wire is connected to A2
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo
my_servo = servo.Servo(pwm)

#go to 0
my_servo.angle = 0
#give it some time to get there
time.sleep(1) 

while True :
    if cp.button_a :
            my_servo.angle = 90

    elif cp.button_b :
            my_servo.angle = 0
