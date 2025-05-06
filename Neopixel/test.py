import time
from neopixel import Neopixel

numpix = 8*8
pixels = Neopixel(numpix, 0, 0, "GRB")
pixels.brightness(50)
pixels.fill((0,0,0))
pixels.set_pixel(0, (0, 0, 0))
pixels.show()
time.sleep(1)

while True:
    pixels.fill((0,0,0))
    for i in range(0, numpix, 2):
        pixels.set_pixel(i, (255, 0, 0))
    pixels.show()
    time.sleep(1)
    pixels.fill((0,0,0))
    for i in range(1, numpix, 2):
        pixels.set_pixel(i, (0, 255, 0))
    pixels.show()
    time.sleep(1)


    




