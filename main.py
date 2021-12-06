# Device Configuration
from config import waterLevelPin, motorDriverPins, soilMoisturePins

# Module
from wifiManager import openWifiManager
from dhtSensor import readDhtValue
from soilMoisture import readSoilMoistureValue
from rtcSensor import getDateTime
from motorDriver import motorDriverControl
from waterLevel import readWaterLevel
from firebaseManager import getData, storeData, putData, deleteData

# Package
import json
from utime import sleep

# Initialize
print("Initialize System...")
openWifiManager()

print("Starting System in 5 Second...")
sleep(5)

# Main Loop
while True:
    configure = getData("/config")
    timeSettings = configure["timeSettings"]
    pompDuration = configure["pompDuration"]
    
    tempC = readDhtValue(1)
    humid = readDhtValue(2)
    soilMoisA = readSoilMoistureValue(soilMoisturePins[0], 10)
    soilMoisB = readSoilMoistureValue(soilMoisturePins[1], 10)
    waterHeight = readWaterLevel()
    
    data = {
      "humidity" : round(humid, 2),
      "soilMoistureA" : round(soilMoisA, 2),
      "soilMoistureB" : round(soilMoisB, 2),
      "temperature" : round(tempC, 2),
      "waterHeight" : waterHeight
    }
    
    if getDateTime(4) in timeSettings:
        motorDriverControl(motorDriverPins[:2], [1, 0])
        motorDriverControl(motorDriverPins[2:], [1, 0])
        sleep(pompDuration)
        motorDriverControl(motorDriverPins[:2], [0, 0])
        motorDriverControl(motorDriverPins[2:], [0, 0])
        sleep(1)
        data["pompDuration"] = pompDuration
        data["timestamp"] = getDateTime(0)
        print(putData("/dump/"+getDateTime(5), data))
    
    print(putData("/monitoring", data))
    sleep(10)
