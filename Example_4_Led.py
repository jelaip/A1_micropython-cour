from machine import Pin # importe dans le code la lib qui permet de gerer les Pin de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber = 17 # declaration d'une variable pinNumber à 17
led = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
                                   #et on prescise que c'est une pine de sortie de courant (OUT)

while True:          # boucle infini
    led.toggle()     # change l'etat de la led
    utime.sleep(1)   # attendre 1 seconde 
    #led.on()        allume la led 
    #led.off()       eteind la led 