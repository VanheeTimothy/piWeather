import smtplib

from DbClass import DbClass
from classMcp3008 import Mcp3008
import BMP280
import DHT11
db = DbClass()

barometer = BMP280

active = []

def checkWarningLight():
    lijst = db.getAllWarnings()
    licht = Mcp3008().ReadChannel(0)
    lichpercentage = (licht / 1023) * 100

    for tulpje in lijst:
        if tulpje[1] == 'light dependant resistor sensor':
            if tulpje[2] > lichpercentage or tulpje[3] < lichpercentage:
                if tulpje[0] not in active:
                    print(tulpje[2])
                    content = "This is an mail from piWheater. \nYou've set a warning for {}.\nThe sensor has reached {} out range: {} and {}".format(
                        tulpje[1], lichpercentage, tulpje[2], tulpje[3])
                    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('piweather1.0@gmail.com', 'raspberry')
                        smtp.sendmail('piweather1.0@gmail.com', 'Timothy_Vanhee@hotmail.com', content)
                        print(content)
                    active.append(tulpje[0])
            else:
                if tulpje[0] in active:
                    # send mail tis beter nu
                    content = "This is an email from piWeather. The sensor's value is between the warning set. Everything is alright now."
                    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('piweather1.0@gmail.com', 'raspberry')
                        smtp.sendmail('piweather1.0@gmail.com', 'Timothy_Vanhee@hotmail.com', content)
                        print(content)
                    active.remove(tulpje[0])



def checkWarningTemp():
    lijst = db.getAllWarnings()
    tempWaarde = barometer.get_temperature()
    for tulpje in lijst:
        if tulpje[1] == 'temperature sensor':
            if tulpje[2] > tempWaarde or tulpje[3] < tempWaarde:
                if tulpje[0] not in active:
                    content = "this a mail from piWheater. \nYou've set a warning for {}.\nThe sensor has reached {} out range: {} and {}".format(
                        tulpje[1], tempWaarde, tulpje[2], tulpje[3])
                    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('piweather1.0@gmail.com', 'raspberry')
                        smtp.sendmail('piweather1.0@gmail.com', 'Timothy_Vanhee@hotmail.com', content)
                        print(content)
                    active.append(tulpje[0])
            else:
                if tulpje[0] in active:
                    # send mail tis beter nu
                    content = "This is an email from piWeather. The sensor's value is between the warning set. Everything is alright now."
                    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('piweather1.0@gmail.com', 'raspberry')
                        smtp.sendmail('piweather1.0@gmail.com', 'Timothy_Vanhee@hotmail.com', content)
                        print(content)
                    active.remove(tulpje[0])


def checkWarningAirpressure():
    lijst = db.getAllWarnings()
    pressureValue = round(barometer.get_pressure(), 2)
    for tulpje in lijst:
        if tulpje[1] == 'air pressure sensor':
            if tulpje[2] > pressureValue or tulpje[3] < pressureValue:
                if tulpje[0] not in active:
                    content = "this a mail from piWheater. \nYou've set a warning for {}.\nThe sensor has reached {} out range: {} and {}".format(
                        tulpje[1], pressureValue, tulpje[2], tulpje[3])
                    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('piweather1.0@gmail.com', 'raspberry')
                        smtp.sendmail('piweather1.0@gmail.com', 'Timothy_Vanhee@hotmail.com', content)
                        print(content)
                    active.append(tulpje[0])
            else:
                if tulpje[0] in active:
                    # send mail tis beter nu
                    content = "This is an email from piWeather. The sensor's value is between the warning set. Everything is alright now."
                    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('piweather1.0@gmail.com', 'raspberry')
                        smtp.sendmail('piweather1.0@gmail.com', 'Timothy_Vanhee@hotmail.com', content)
                        print(content)
                    active.remove(tulpje[0])



def checkWarningHumidity():
    lijst = db.getAllWarnings()
    rain = Mcp3008().ReadChannel(1)
    for tulpje in lijst:
        if tulpje[1] == 'rain sensor':
            if tulpje[2] > rain or tulpje[3] < rain:
                if tulpje[0] not in active:
                    content = "this a mail from piWheater. \nYou've set a warning for {}.\nThe sensor has reached {} out range: {} and {}".format(
                        tulpje[1], rain, tulpje[2], tulpje[3])
                    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('piweather1.0@gmail.com', 'raspberry')
                        smtp.sendmail('piweather1.0@gmail.com', 'Timothy_Vanhee@hotmail.com', content)
                        print(content)
                    active.append(tulpje[0])
            else:
                if tulpje[0] in active:
                    # send mail tis beter nu
                    content = "This is an email from piWeather. The sensor's value is between the warning set. Everything is alright now."
                    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('piweather1.0@gmail.com', 'raspberry')
                        smtp.sendmail('piweather1.0@gmail.com', 'Timothy_Vanhee@hotmail.com', content)
                        print(content)
                    active.remove(tulpje[0])

def checkWarningRain():
    lijst = db.getAllWarnings()
    humiditysensor = DHT11.DHT11(pin=14)
    humidityWaarde = humiditysensor.read().humidity
    for tulpje in lijst:
        if tulpje[1] == 'humidity sensor':
            if tulpje[2] > humidityWaarde or tulpje[3] < humidityWaarde:
                if tulpje[0] not in active:
                    content = "this a mail from piWheater. \nYou've set a warning for {}.\nThe sensor has reached {} out range: {} and {}".format(
                        tulpje[1], humidityWaarde, tulpje[2], tulpje[3])
                    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('piweather1.0@gmail.com', 'raspberry')
                        smtp.sendmail('piweather1.0@gmail.com', 'Timothy_Vanhee@hotmail.com', content)
                        print(content)
                    active.append(tulpje[0])
            else:
                if tulpje[0] in active:
                    # send mail tis beter nu
                    content = "This is an email from piWeather. The sensor's value is between the warning set. Everything is alright now."
                    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login('piweather1.0@gmail.com', 'raspberry')
                        smtp.sendmail('piweather1.0@gmail.com', 'Timothy_Vanhee@hotmail.com', content)
                        print(content)
                    active.remove(tulpje[0])



try:
    while 1:
        checkWarningLight()
        checkWarningTemp()
        checkWarningAirpressure()
        checkWarningHumidity()
        checkWarningRain()
except KeyboardInterrupt:
    print("einde")