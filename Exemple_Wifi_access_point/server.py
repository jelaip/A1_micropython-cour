from phew import server, access_point
import machine
import json

ap = access_point("raspi_ap", "123456789")  # ssid && mdp
ip = ap.ifconfig()[0]  
print(ip)  # debug ip address (to connect to the server)

page = open("index.html","r") # ouvre le fichier index.html (r = read)
indexhtml= page.read() # stock le contenu du fichier dans la variable indexhtml
page.close()  # ferme le fichier


led = machine.Pin(14, machine.Pin.OUT) 

@server.route("/", methods=["GET"]) # route de la page d'accueil, c'est un décorateur qui permet de lier une fonction à une route
def home(request): # fonction de la page d'accueil
    return str(indexhtml) # retourne le contenu de la variable indexhtml

@server.route("/led/<param>", methods=["GET"]) # route de la led avec un parametre ex : /led/on ou /led/off
def command(request, param):
    if param == "on":   # si le parametre est "on"
        led.on() # allume la led
        print("allume")
        return json.dumps({"status": "on"}) # retourne un json {"status": "on"} (return close la fonction)
    elif param == "off": # sinon si le parametre est "off"
        print("eteint")
        led.off() # sinon eteint la led
        return json.dumps({"status": "off"}) # retourne un json {"status": "off"}
    else: # sinon
        return "Not found", 404 # retourne "Not found" et le code 404

@server.catchall() # route par defaut
def catchall(request): 
  return "Not found", 404 # retourne "Not found" et le code 404

server.run() # lance le serveur


