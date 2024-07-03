from adafruit_circuitplayground import cp

note = [262,262,392,392,440,440,392,392,440,262]
duration = [1,0.5,1,2,0.5,1,1,0.5,1,2]

for i in range(10):
    cp.pixels[i] =(255,0,0)
    cp.play_tone(note[i], duration[i])
    cp.pixels[i] =(0,0,0)
