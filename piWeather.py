from flask import Flask, render_template, request
import BMP280
import DHT11
from classMcp3008 import Mcp3008
from DbClass import DbClass
import datetime



app = Flask(__name__)




def myround(x, base=5):
    return int(base * round(float(x) / base))


def getValue(data):
    waarden = []
    for x in data:
        for y in x:
            waarden.append(y)
    meetresultaat = []
    for x in waarden[0::2]:
        meetresultaat.append(x)
    return meetresultaat


def getTime(data):
    waarden = []
    for x in data:
        for y in x:
            waarden.append(y)
    date = []
    for y in waarden[1::2]:
        date.append(y)

    uren = []
    for x in date:
        tijdstring = str(x)
        uren.append(tijdstring[11:16])
    return uren


def getDay(data):
    waarden = []
    for x in data:
        for y in x:
            waarden.append(y)
    date = []
    for y in waarden[1::2]:
        date.append(y)

    uren = []
    for x in date:
        tijdstring = str(x)
        uren.append(tijdstring[5:10])
    return uren


def gemiddeldeWaarden(interval, listDays, listValues):
    datum = str(datetime.datetime.now() - datetime.timedelta(days=interval))[5:10]
    aantaldagen = len(listDays)
    aantalMeting = listDays.count(datum)
    somWaarden = 0
    if aantalMeting != 0:
        for i in range(0, aantaldagen):
            if listDays[i] == datum:
                somWaarden += int(listValues[i])
        result = round(somWaarden / aantalMeting, 2)
    else:
        result = 0
    return result


def gemiddeldeValueWeek(tijd, waarden):
    gemiddelde = []
    for i in range(7, 0, -1):
        waarde = gemiddeldeWaarden(i, tijd, waarden)
        gemiddelde.append(waarde)
    return gemiddelde


def gemiddeldeValueMaand(tijd, waarden):
    gemiddelde = []
    for i in range(31, 0, -1):
        waarde = gemiddeldeWaarden(i, tijd, waarden)
        gemiddelde.append(waarde)
    return gemiddelde






@app.route('/')
def home():
    db =DbClass()
    # inlezen barometer voor temperatuur
    barometer = BMP280
    tempWaarde = barometer.get_temperature()
    temperatuur = myround(tempWaarde)

    # inlezen barometer voor air pressure
    pressureValue = round(barometer.get_pressure(), 2)
    pressurepercentage = round((pressureValue / 1100) * 100, 2)
    pressureCircle = myround(pressurepercentage)

    # inlezen vochtigheidsgraad
    humiditysensor = DHT11.DHT11(pin=14)
    humidityWaarde = humiditysensor.read().humidity
    vochtigheidsWaarde = myround(humidityWaarde)
    if humidityWaarde == 0:
        waarde = db.getLatestRecordFromHumidity()
        humidityWaarde = waarde[0]
        vochtigheidsWaarde = myround(waarde[0])


    licht_sensor = 0
    regensensor = 1

    mcp = Mcp3008()
    lichtwaarde = mcp.ReadChannel(licht_sensor)
    licht_volt = mcp.convert_volts(lichtwaarde, 2)  # parameters zijn ingelezen waarde en afronding na de komma
    lichtpercentage = round((lichtwaarde / 1024) * 100, 2)
    cirkelwaarde = myround(lichtpercentage)
    # inlezen waarden van de regen sensor
    regenwaarde = mcp.ReadChannel(regensensor)
    regenprocent = round((regenwaarde / 1024) * 100, 0)
    invertedValues = {}
    y = 1024
    for i in range(0, 1024):
        y -= 1
        invertedValues[i] = y
    regenpercentage = round((invertedValues[regenwaarde] / 1024) * 100, 2)
    regencirkel = myround(regenpercentage)

    cirkelRegen = myround(regenprocent)

    if (regenwaarde >= 1010):
        toestand = "None"
    elif (regenwaarde < 1010 and regenwaarde > 768):
        toestand = "light"
    elif (regenwaarde < 768 and regenwaarde > 512):
        toestand = "medium"
    elif (regenwaarde < 512 and regenwaarde > 256):
        toestand = "light Heavy"
    else:
        toestand = "Heavy"

    return render_template('homepage.html', temp=temperatuur, waardeTemp=tempWaarde, humidity=vochtigheidsWaarde,
                           waardeHumidity=humidityWaarde, percentage=lichtpercentage, cirkelwaarde=cirkelwaarde,
                           lichtwaarde=lichtwaarde, regenwaarde=regenwaarde, toestand=toestand, cirkelRegen=regencirkel,
                           pressureValue=pressureValue, pressureCircle=pressureCircle)


@app.route('/graphs')
def graphs():
    db = DbClass()
    tempdata = db.getDailyDataFromTemperature()
    graden = getValue(tempdata)
    temptijd = getTime(tempdata)

    humdata = db.getDailyDataFromHumidity()

    vochtigheid = getValue(humdata)

    humtijd = getTime(humdata)

    lightdata = db.getDailyDataFromLight()
    lichtsterkte = getValue(lightdata)
    lichttijd = getTime(lightdata)

    airdata = db.getDailyDataFromAirpressure()
    luchtdruk = getValue(airdata)
    luchttijd = getTime(airdata)

    raindata = db.getDailyDataFromRain()
    rainfall = getValue(raindata)
    regentijd = getTime(raindata)

    return render_template('graphspage.html', graden=graden, temptijd=temptijd, vochtigheid=vochtigheid,
                           humtijd=humtijd, lichtsterkte=lichtsterkte, lichttijd=lichttijd, luchtdruk=luchtdruk,
                           luchttijd=luchttijd, rainfall=rainfall, regentijd=regentijd)


@app.route('/graphsWeek')
def graphsWeek():
    db = DbClass()

    tempdata = db.getWeeklyDataFromTemperature()
    graden = getValue(tempdata)
    temptijd = getDay(tempdata)
    gemiddeldetemp = gemiddeldeValueWeek(temptijd, graden)

    humdata = db.getWeeklyDataFromHumidity()
    vochtigheid = getValue(humdata)
    humtijd = getDay(humdata)
    gemiddeldehum = gemiddeldeValueWeek(humtijd, vochtigheid)

    lightdata = db.getWeeklyDataFromLight()
    lichtsterkte = getValue(lightdata)
    lichttijd = getDay(lightdata)
    gemiddeldelight = gemiddeldeValueWeek(lichttijd, lichtsterkte)

    airdata = db.getWeeklyDataFromAirpressure()
    luchtdruk = getValue(airdata)
    luchttijd = getDay(airdata)
    gemiddeldeair = gemiddeldeValueWeek(luchttijd, luchtdruk)

    raindata = db.getWeeklyDataFromRain()
    rainfall = getValue(raindata)
    regentijd = getDay(raindata)
    gemiddelderain = gemiddeldeValueWeek(regentijd, rainfall)

    laatste7dagen = []
    for i in range(7, 0, -1):
        datum = str(datetime.datetime.now() - datetime.timedelta(days=i))[5:10]
        laatste7dagen.append(datum)

    return render_template('graphsWeek.html', gemiddeldetemp=gemiddeldetemp, laatste7dagen=laatste7dagen,
                           gemiddeldehum=gemiddeldehum, gemiddeldelight=gemiddeldelight, gemiddeldeair=gemiddeldeair,
                           gemiddelderain=gemiddelderain)


@app.route('/graphsMonth')
def graphsMonth():
    db = DbClass()
    tempdata = db.getMonthlyDataFromTemperature()
    graden = getValue(tempdata)
    temptijd = getDay(tempdata)
    gemiddeldetemp = gemiddeldeValueMaand(temptijd, graden)
    print(gemiddeldetemp)

    humdata = db.getMonthlyDataFromHumidity()
    vochtigheid = getValue(humdata)
    humtijd = getDay(humdata)
    gemiddeldehum = gemiddeldeValueMaand(humtijd, vochtigheid)

    lightdata = db.getMonthlyDataFromLight()
    lichtsterkte = getValue(lightdata)
    lichttijd = getDay(lightdata)
    gemiddeldelight = gemiddeldeValueMaand(lichttijd, lichtsterkte)

    airdata = db.getWeeklyDataFromAirpressure()
    luchtdruk = getValue(airdata)
    luchttijd = getDay(airdata)
    gemiddeldeair = gemiddeldeValueMaand(luchttijd, luchtdruk)

    raindata = db.getMonthlyDataFromRain()
    rainfall = getValue(raindata)
    regentijd = getDay(raindata)
    gemiddelderain = gemiddeldeValueMaand(regentijd, rainfall)

    laatste7dagen = []
    for i in range(31, 0, -1):
        datum = str(datetime.datetime.now() - datetime.timedelta(days=i))[5:10]
        laatste7dagen.append(datum)

    return render_template('graphsmonth.html', gemiddeldetemp=gemiddeldetemp, laatste7dagen=laatste7dagen,
                           gemiddeldehum=gemiddeldehum, gemiddeldelight=gemiddeldelight, gemiddeldeair=gemiddeldeair,
                           gemiddelderain=gemiddelderain)


@app.route('/sensors')
def sensors():
    return render_template('sensorspage.html')


@app.route('/photos')
def photos():
    return render_template('photopage.html')


@app.route('/about')
def about():
    return render_template('aboutpage.html')


@app.route('/settings')
def settings():
    tijdnu = datetime.datetime.now()
    db = DbClass()
    listOfWarnings = db.getAllWarnings()
    return render_template('settingspage.html', listOfWarnings=listOfWarnings, tijdnu=tijdnu)


@app.route('/check', methods=["POST"])
def setwarningcheck():
    db = DbClass()
    sensoren = request.form['sensor']
    minValue = request.form['minValue']
    maxValue = request.form['maxValue']
    db.setWarning(sensoren, minValue, maxValue)

    return render_template('setwarningcheck.html')


@app.route('/triggercheck', methods=["POST"])
def cameratrigger():
    db = DbClass()
    sensor = request.form['camera-group']
    triggervalue = request.form['triggervalue']

    db.setCameraTrigger(sensor, triggervalue)

    return render_template('setwarningcheck.html')


@app.route('/delete', methods=["POST"])
def deletecheck():
    db = DbClass()
    lijst = db.getAllWarnings()
    for x in lijst:
        try:
            delon = request.form[str(x[0])]
            db.deleteWarning(x[0])
        except:
            pass

    return render_template('deletecheck.html')









if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

