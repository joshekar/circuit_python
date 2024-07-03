from adafruit_circuitplayground import cp


for x in range(2):
    cp.pixels[0] =(255,0,0)
    cp.play_tone(262, 1) # note c
    cp.pixels[0] =(0,0,0)

for x in range(2):
    cp.pixels[4] =(0,0,255)
    cp.play_tone(392, 1) # note g
    cp.pixels[4] =(0,0,0)

for x in range(2):
    cp.pixels[5] =(255,0,255)
    cp.play_tone(440, 1) # note a
    cp.pixels[5] =(0,0,0)

cp.pixels[4] =(0,0,255)
cp.play_tone(392, 1) # note g
cp.pixels[4] =(0,0,0)

