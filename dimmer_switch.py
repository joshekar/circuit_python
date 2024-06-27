from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.5
cp.pixels.fill((255, 255, 255))


while True:
    if cp.button_a:
        while (cp.button_a):
            pass
        print("pressed a")
        cp.pixels.brightness -= 0.1
        print("decreased brightness", cp.pixels.brightness)
        
    if cp.button_b:
        while (cp.button_b):
            pass
        print("pressed b")
        cp.pixels.brightness += 0.1
        print("increased brightness", cp.pixels.brightness)
