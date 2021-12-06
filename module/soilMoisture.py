from machine import Pin, ADC
from utime import sleep
from averageSample import averageSample

def readSoilMoistureValue(sensorPin, sample):
    soilPin = ADC(Pin(sensorPin))
    rawValue = []
    
    for i in range(sample):
        rawValue.append(soilPin.read())
        sleep(0.1)
    
    avgVal = averageSample(sorted(rawValue))
    
    moisValue = 100 - ((avgVal/4096) * 100)
    return round(moisValue, 2)
