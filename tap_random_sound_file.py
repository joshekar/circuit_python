import random
from adafruit_circuitplayground import cp

files = ["smb_stage_clear.wav", "smb_mariodie.wav"]


while True:
    if cp.tapped==True:
        pick = random.choice(files)
        print("Randomly chosen file value is", pick)
        cp.play_file(pick)
