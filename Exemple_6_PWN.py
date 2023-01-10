from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import time # importe dans le code la lib qui permet de gerer le temps

pwm_led = PWM(Pin(15,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_led.freq(1_000) # dont la frequence est de 1000 (default)
pwm_led.duty_u16(13000) # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3v
