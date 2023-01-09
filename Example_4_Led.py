from machine import Pin
import utime

pinNumber = 17
led = Pin(pinNumber, mode=Pin.OUT)

while True:
    led.toggle()
    utime.sleep(1)
    #led.on()
    #led.off()