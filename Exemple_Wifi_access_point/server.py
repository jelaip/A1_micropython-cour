from phew import server, access_point
import machine
import json

ap = access_point("raspi_ap", "123456789")  # ssid && mdp
ip = ap.ifconfig()[0]  
print(ip)  # debug ip address (to connect to the server)

page = open("index.html","r")
indexhtml= page.read()
page.close()


led = machine.Pin(14, machine.Pin.OUT)

@server.route("/", methods=["GET"])
def home(request):
    return str(indexhtml)

@server.route("/led/<param>", methods=["GET"])
def command(request, param):
    if param == "on":
        led.on()
        print("allume")
        return json.dumps({"status": "on"}) 
    led.off()
    return json.dumps({"status": "off"})

@server.catchall()
def catchall(request):
  return "Not found", 404

server.run()


