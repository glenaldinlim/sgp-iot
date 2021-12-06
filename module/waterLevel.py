from machine import Pin
from config import waterLevelPin

def readWaterLevel():
    waterPin = Pin(waterLevelPin, Pin.IN)
    
    levelValue = waterPin.value()
    return levelValue
