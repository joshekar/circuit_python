from adafruit_circuitplayground import cp

while True:
    if cp.button_a:
        cp.play_file("smb_stage_clear.wav")
    elif cp.button_b:
        cp.play_file("smb_mariodie.wav")
