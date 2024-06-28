import time
from adafruit_circuitplayground import cp

left_light = False
right_light = False

while True:
    if cp.button_a:
        while (cp.button_a):
            pass
       
        left_light = not left_light
        

        while left_light==True:
            for i in range(5):
     	        cp.pixels[i] =(228,20,10)
                time.sleep(0.1)
                
            for i in range(5): 
                cp.pixels[i] =(0,0,0)
                
            if cp.button_a:
                while (cp.button_a):
                    pass
                left_light = False


    if cp.button_b:
        while (cp.button_b):
            pass
       
        right_light = not right_light
       
        while right_light==True:
            for i in range(9,4,-1):
     	        cp.pixels[i] =(228,20,10)
                time.sleep(0.1)
                
            for i in range(9,4,-1): 
                cp.pixels[i] =(0,0,0)
                
            if cp.button_b:
                while (cp.button_b):
                    pass
                right_light = False
