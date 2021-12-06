import network
from utime import sleep

def openWifiConnection(ssid, password):
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    print("Connecting to {} network".format(ssid), end="")
    while not wifi.isconnected():
        wifi.connect(ssid, password)
        print(".", end="")
        sleep(1)
    print("\nSuccess to connect with {} network!".format(ssid))
    config = wifi.ifconfig()
    print("Device IP: {}".format(config[0]))
