from adafruit_circuitplayground import cp
import time
import random

#Dice Game with Player A and Player B

while True:
    # When Player A presses button_a
    if cp.button_a==True:
        while(cp.button_a==True):
            pass
        # click detected

	#generate a random number between 1 and 5
        playerA_roll = random.randint(1,5)
        print("PlayerA dice roll is:",playerA_roll)
        
    #light up LEDs on Player A side based on the random number    
        for i in range(playerA_roll):
            cp.pixels[i] =(255,0,0)
            time.sleep(0.1)


    # When Player B presses button_b    
    if cp.button_b==True:
        while(cp.button_b==True):
            pass
        # click detected    
        
        
	#generate a random number between 1 and 5
        playerB_roll = random.randint(1,5)
        print("PlayerB dice roll is:",playerB_roll)
        
    #light up LEDs on Player B side based on the random number       
        for i in range(5,5+playerB_roll):
            cp.pixels[i] =(0,0,255)
            time.sleep(0.1)

#If Player A number is > Player B, blink LEDs 3 times on Player A side        
        if playerA_roll > playerB_roll:
            for x in range(3):
                for i in range(playerA_roll):
                    cp.pixels[i] =(255,0,0)
                time.sleep(0.2)
                
                cp.pixels.fill((0,0,0))
                time.sleep(0.1)

#If Player B number is > Player A, blink LEDs 3 times on Player B side    
        elif playerB_roll > playerA_roll:
            for x in range(3):
                
                for i in range(5,5+playerB_roll):
                    cp.pixels[i] =(0,0,255)
                time.sleep(0.1)            
        
                cp.pixels.fill((0,0,0))
                time.sleep(0.1)
    
#If Player A number is = Player B, blink LEDs 3 times on both Player A and Player B sides
        else:
            for x in range(3):
                for i in range(playerA_roll):
                    cp.pixels[i] =(255,0,0)
                time.sleep(0.1)
        
     
                for i in range(5,5+playerB_roll):
                    cp.pixels[i] =(0,0,255)
                time.sleep(0.1)
                
                cp.pixels.fill((0,0,0))
                time.sleep(0.1)
                
                
