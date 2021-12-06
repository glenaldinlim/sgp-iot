from ds3231_port import DS3231 
from machine import Pin, SoftI2C
from utime import sleep, localtime
from config import i2cPins

i2c = SoftI2C(scl=Pin(i2cPins[1]), sda=Pin(i2cPins[0]), freq=100000)
ds = DS3231(i2c)
daysOfTheWeek = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"];

def getDateTime(option):
    rtc = ds.get_time()
    date = "{:0>2}".format(rtc[2])
    month = "{:0>2}".format(rtc[1])
    year = str(rtc[0])
    hour = "{:0>2}".format(rtc[3])
    minute = "{:0>2}".format(rtc[4])
    second = "{:0>2}".format(rtc[5])
    day = daysOfTheWeek[rtc[6]]
    
    if option == 1:
        return "{0}, {1}/{2}/{3}".format(day, date, month, year)
    elif option == 2:
        return "{1}/{2}/{3}".format(date, month, year)
    elif option == 3:
        return "{0}:{1}:{2}".format(hour, minute, second)
    elif option == 4:
        return "{0}:{1}".format(hour, minute)
    elif option == 5:
        return "{0}{1}{2}{3}{4}{5}".format(year, month, date, hour, minute, second)
    else:
        return "{0}, {1}/{2}/{3} {4}:{5}:{6}".format(day, date, month, year, hour, minute, second)
