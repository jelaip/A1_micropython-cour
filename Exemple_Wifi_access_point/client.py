import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
import machine

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'raspi_ap'
password = '123456789'
wlan.connect(ssid, password) # connecte la raspi au réseau
urlon = "http://192.168.4.1/led/on"
urloff = "http://192.168.4.1/led/off"

led = machine.Pin(14, machine.Pin.OUT)

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("try on GET")
        r = urequests.get(urlon) # lance une requete sur l'url
        print(r.json()) # traite sa reponse en Json
        # le json c'est {"status": "on"} ou {"status": "off"}
        if r.json()["status"] == "on":
            led.on()
        r.close() # ferme la demande 
    except Exception as e:
        print(e)
    utime.sleep(1)
    try:
        print("try off GET")
        r = urequests.get(urloff) # lance une requete sur l'url
        print(r.json()) # traite sa reponse en Json
        if r.json()["status"] == "off":
            led.off()
        r.close() # ferme la demande
        utime.sleep(1)  
    except Exception as e:
        print(e)
    utime.sleep(1)
