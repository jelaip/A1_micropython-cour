from machine import Pin, Timer # Import Pin and Timer class from machine module
import utime # Import utime module
bt = Pin(14, Pin.IN, Pin.PULL_UP) # Create a Pin object called bt for button
led = Pin(17,mode=Pin.OUT) # Create a Pin object called led for LED
timer = Timer() # Create a Timer object called timer
timer2 = Timer()    # Create a Timer object called timer2

def buttonTimer(t): # Define a function called buttonTimer
    if bt.value() == 0: 
        print("ok")

timer.init(period=100, mode=Timer.PERIODIC, callback=lambda t: buttonTimer(t)) # Call buttonTimer every 100ms
timer2.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: led.toggle()) # Call led.toggle every 1000ms

while True:
    utime.sleep(1)
    print('1')