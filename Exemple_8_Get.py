import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = ''
password = ''
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://jsonplaceholder.typicode.com/posts/1"

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()) # traite sa reponse en Json
        r.close() # ferme la demande
        utime.sleep(1)  
    except Exception as e:
        print(e)
    
