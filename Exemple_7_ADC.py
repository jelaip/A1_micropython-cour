from machine import Pin, ADC # importe dans le code la lib qui permet de gerer les Pin de sortie et de reception de signaux analogique
import time # importe dans le code la lib qui permet de gerer le temps

adc = ADC(Pin(26, mode=Pin.IN)) # on prescise au programme que la pin 26 est une entré de type ADC

while True:# boucle infini
    val = adc.read_u16() # elle lit la valeur converti entre 0 et 65535 
    val = val * (3.3 / 65535) # produit en crois pour retrouver le voltage
    print(round(val, 2), "V") # ecrire la valeur de val en arrondisant à deux chiffres apres la virgule
    time.sleep_ms(100) # attendre 100ms => 0.1 seconde