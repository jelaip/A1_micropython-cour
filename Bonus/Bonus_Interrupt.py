from machine import Pin
import utime
pin = Pin(14,Pin.IN,Pin.PULL_UP)
led = Pin(17,Pin.OUT)
def ChangeLed(pin):
    print(pin)
    led.toggle()

pin.irq(trigger=Pin.IRQ_FALLING, handler=ChangeLed)
while True:
    utime.sleep(1)
    
    

    