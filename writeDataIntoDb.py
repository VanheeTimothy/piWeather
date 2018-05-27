from DbClass import DbClass
import BMP280
from classMcp3008 import Mcp3008
from DHT11 import DHT11
from time import sleep



db = DbClass()
barometer = BMP280



humiditysensor = DHT11(pin=14)

mcp = Mcp3008()

invertedValues = {}
y = 1024
for i in range(0, 1024):
    y -= 1
    invertedValues[i] = y




def wegschrijvenVanSensorenNaarDb():

    tempWaarde = barometer.get_temperature()
    db.setTempValueToDatabase(tempWaarde)
    print("temp ok")

    pressureWaarde = barometer.get_pressure()
    db.setBarometerValuesToDatabase(pressureWaarde)
    print("pressure ok")

    humidityWaarde = humiditysensor.read().humidity
    if humidityWaarde != 0 and humidityWaarde != None:
        db.setHumidityValueToDatabase(humidityWaarde)
        print("humidty on")

    lichtwaarde = mcp.ReadChannel(0)
    db.setLightValueToDatabase(lichtwaarde)
    print("light ok")

    regenwaarde = mcp.ReadChannel(1)
    invertedRegenwaarde = invertedValues[regenwaarde]
    db.setRainValueToDatabase(invertedRegenwaarde)
    print("we did it")
    sleep(60)

try:
    count = 0
    while 1:
        wegschrijvenVanSensorenNaarDb()
        count +=1
        print(count)
except KeyboardInterrupt:
    print("End")

