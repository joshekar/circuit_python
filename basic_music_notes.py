from adafruit_circuitplayground import cp


cp.pixels[0] =(255,0,0)
cp.play_tone(262, 1) # note c
cp.pixels[0] =(0,0,0)

cp.pixels[1] =(255,255,0)
cp.play_tone(294, 1) # note d
cp.pixels[1] =(0,0,0)

cp.pixels[2] =(0,255,0)
cp.play_tone(330, 1) # note e
cp.pixels[2] =(0,0,0)

cp.pixels[3] =(0,255,255)
cp.play_tone(349, 1) # note f
cp.pixels[3] =(0,0,0)

cp.pixels[4] =(0,0,255)
cp.play_tone(392, 1) # note g
cp.pixels[4] =(0,0,0)

cp.pixels[5] =(255,0,255)
cp.play_tone(440, 1) # note a
cp.pixels[5] =(0,0,0)

cp.pixels[6] =(255,255,255)
cp.play_tone(494, 1) # note b
cp.pixels[6] =(0,0,0)

cp.pixels[7] =(150,122,255)
cp.play_tone(523, 1) # note c
cp.pixels[7] =(0,0,0)
