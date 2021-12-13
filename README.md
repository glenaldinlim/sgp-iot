## About SGP ( Smart Greenhouse Pesticide)
SGP a.k.a Smart Greenhouse Pesticide is a IoT project about Controlling and Monitoring Greenhouse. In this project, user can controlling the watering time also the pomp duration; user can monitoring humidity and temperature of greenhouse, soil moisture, and height of pesticide. This is a Final Project of TEK304 - Sistem Tertanam (Embedded System).

### Team
- J3D119016 - Arief Kurnia Ananda
- J3D119039 - Dwi Yulinar
- J3D119021 - Bagus Raspati
- J3D119052 - Glenaldin Halim
- J3D119072 - Meihair Alfianzen
- J3D119101 - Nur Tri Wahyudiningsih
- J3D119110 - Ramadhan Kukuh Prakoso
- J3D119119 - Safrizal Abdul Latief

## Component Used
| Name                            | Functionality | Qty   |
| ------------------------------- | ------------- | ----- |
| NodeMCu Ai-Thinker ESP32-S      | Board         | 1 pcs |
| Capacitive Soil Moisture Sensor | Sensor        | 2 pcs |
| DHT22                           | Sensor        | 1 pcs |
| Water Level Sensor              | Sensor        | 1 pcs |
| RTC DS3231                      | Sensor        | 1 pcs |
| Water Pump 5V                   | Actuator      | 2 pcs |
| L298N Motor Driver Module       | Module        | 1 pcs |
| GX16 Connector (2 pin & 3 pin)  | Connector     | 6 pcs |
| Molex Mini JST (3 pin)          | Connector     | 4 pcs |
| Printed 3D Case                 | Case          | 1 pcs |
| Printed PCB Board               | PCB           | 1 pcs |

## Library / Package Used
| Name        | Source                                                                         |
| ----------- | ------------------------------------------------------------------------------ |
| RTC DS3231  | [Github](https://github.com/peterhinch/micropython-samples/tree/master/DS3231) |
| uFirebase   | [Github](https://github.com/ckoever/micropython-firebase-realtime-database)    |
| WifiManager | [Github](https://github.com/tayfunulu/WiFiManager)                             |

## Wiring
Soon Will Update

## Development Environment
This Project is develop with MicroPython (Firmware version: 1.17) as a Programming Language, Thonny as IDE, Firebase as Database and NextJS as web framework. You can visit the web repo's at [SGP IoT - Web](https://github.com/glenaldinlim/sgp-iot-web)

## How to Use
1. Install CH340 Driver and Thonny IDE in your PC
2. Download MicroPython firmware from [MicroPython Official Website](https://micropython.org/download/)
3. Flash MicroPython firmware to your board via Thonny IDE
5. Download this repo to your local computer or you can copy one-by-one the file then save it to your board directly
6. Change pin configuration and other config in config.py
7. Run and Test it!
