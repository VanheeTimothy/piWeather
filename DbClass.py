import mysql.connector as connector


class DbClass:
    def __init__(self):

        self.__dsn = {
            "host": "localhost",
            "user": "yourName",
            "passwd": "passwf",
            "db": "dbName"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getDataFromDatabase(self):
        # Query zonder parameters
        cursor = self.__connection.cursor()
        sqlQuery = "SELECT sensoren.naam, meting.tijdstip, meting.waarde, eenheid.eenheid FROM meting JOIN eenheid on meting.eenheidID = eenheid.eenheidID JOIN sensoren on meting.sensorID = sensoren.sensorID order by tijdstip;"
        cursor.execute(sqlQuery)
        result = cursor.fetchall()
        cursor.close()

        return result

    def getAllData(self):
        cursor = self.__connection.cursor()
        query = "SELECT * FROM meting"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getAllDataFromTemperature(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM meting WHERE sensorID = 1"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getDailyDataFromTemperature(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 1 AND DATE(`tijdstip`) = CURDATE()"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    def getWeeklyDataFromTemperature(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 1 AND DATE_SUB(now(), INTERVAL 7 DAY)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    def getMonthlyDataFromTemperature(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 1 AND DATE_SUB(now(), INTERVAL 1 MONTH)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result


    def getLatestRecordFromHumidity(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde FROM piWeather.meting WHERE sensorID = 2 order by metingID DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result




    def getAllDataFromHumidity(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM meting WHERE sensorID = 2 "
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    def getDailyDataFromHumidity(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 2 AND DATE(`tijdstip`) = CURDATE()"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    def getMonthlyDataFromHumidity(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 2 AND DATE_SUB(now(), INTERVAL 1 MONTH)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result


    def getWeeklyDataFromHumidity(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 2 AND DATE_SUB(now(), INTERVAL 7 DAY)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getMonthlyDataFromHumidity(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 2 AND DATE_SUB(now(), INTERVAL 1 MONTH)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result


    def getAllDataFromLight(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM meting WHERE sensorID = 5 "
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getDailyDataFromLight(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 5 AND DATE(`tijdstip`) = CURDATE()"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getWeeklyDataFromLight(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 5 AND DATE_SUB(now(), INTERVAL 7 DAY)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getMonthlyDataFromLight(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 5 AND DATE_SUB(now(), INTERVAL 1 MONTH)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getAlldataFromAirpressure(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM meting WHERE sensorID = 4 "
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getDailyDataFromAirpressure(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 4 AND DATE(`tijdstip`) = CURDATE()"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getWeeklyDataFromAirpressure(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 4 AND DATE_SUB(now(), INTERVAL 7 DAY)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getMonthlyDataFromAirpressure(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 4 AND DATE_SUB(now(), INTERVAL 1 MONTH)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result


    def getAlldataFromRain(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM meting WHERE sensorID = 3 "
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getDailyDataFromRain(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 3 AND DATE(`tijdstip`) = CURDATE()"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getWeeklyDataFromRain(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 3 AND DATE_SUB(now(), INTERVAL 7 DAY)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getMonthlyDataFromRain(self):
        cursor = self.__connection.cursor()
        query = "SELECT waarde, tijdstip FROM `meting` WHERE sensorID = 3 AND DATE_SUB(now(), INTERVAL 1 MONTH)"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result



    def getDataFromSensor(self, sensorName):
        cursor = self.__connection.cursor()
        # Query met parameters
        sqlQuery = "SELECT sensoren.naam as 'sensor', meeting.tijdstip, meeting.waarde, eenheid.eenheid FROM meeting JOIN eenheid on meeting.eenheidID = eenheid.eenheidID JOIN sensoren on meeting.sensorID = sensoren.sensorID  WHERE sensoren.naam = '{param}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param=sensorName)
        
        cursor.execute(sqlCommand)
        result = cursor.fetchall()
        cursor.close()
        return result

    def setDataToDatabase(self, value1):
        cursor = self.__connection.cursor()
        # Query met parameters
        sqlQuery = "INSERT INTO tablename (columnname) VALUES ('{param1}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        cursor.execute(sqlCommand)
        self.__connection.commit()
        cursor.close()


    def setHumidityValueToDatabase(self, value):
        cursor = self.__connection.cursor()

        query = "INSERT INTO meting (sensorID, tijdstip, waarde, eenheidID) VALUES(2,NOW(), '{param}',2)"
        #combineren van de query en parameter
        command = query.format(param=value)
        cursor.execute(command)
        self.__connection.commit()
        cursor.close()




    def setTempValueToDatabase(self, value):
        cursor = self.__connection.cursor()
        query = "INSERT INTO meting(sensorID, tijdstip, waarde, eenheidID) VALUES(1, NOW(),'{param}', 1)"
        command = query.format(param=value)
        cursor.execute(command)
        self.__connection.commit()
        cursor.close()


    def setRainValueToDatabase(self, value):
        cursor = self.__connection.cursor()
        query = "INSERT INTO meting(sensorID, tijdstip, waarde, eenheidID) VALUES(3, NOW(),'{param}', 4)"
        command = query.format(param=value)
        cursor.execute(command)
        self.__connection.commit()
        cursor.close()


    def setBarometerValuesToDatabase(self,value):
        cursor = self.__connection.cursor()
        query = "INSERT INTO meting(sensorID, tijdstip, waarde, eenheidID) VALUES(4, NOW(),'{param}',3)"
        command = query.format(param=value)
        cursor.execute(command)
        self.__connection.commit()
        cursor.close()


    def setLightValueToDatabase(self, value): #value = percentage
        cursor = self.__connection.cursor()
        value = ((value /1024) *100)
        query = "INSERT INTO meting(sensorID, tijdstip, waarde, eenheidID) VALUES(5, NOW(),'{param}',2)"
        command = query.format(param=value)
        cursor.execute(command)
        self.__connection.commit()
        cursor.close()


    def uploadPhotoToDatabase(self, value):
        cursor = self.__connection.cursor()
        query = "INSERT INTO meting(sensorID, tijdstip, waarde, eenheidID) VALUES(6, NOW(), '{param}', 4)"
        command = query.format(param=value)
        cursor.execute(command)
        self.__connection.commit()
        cursor.close()


    def setWarning(self, sensor, minValue, maxValue):
        cursor = self.__connection.cursor()
        controle = "SELECT * FROM piWeather.settings WHERE sensorName = '{param}'"
        controleformat = controle.format(param=sensor)
        controleUitvoering = cursor.execute(controleformat)
        controleresultaat = cursor.fetchall()
        if (controleresultaat)== []:
            query = "INSERT INTO settings(sensorName, minimumValue, maximumValue) VALUES('{param1}','{param2}','{param3}')"
        else:
            query = "UPDATE settings SET sensorName = '{param1}', minimumValue = '{param2}', maximumValue = '{param3}' WHERE sensorName = '{param1}';"

        command = query.format(param1=sensor, param2=minValue, param3=maxValue)
        cursor.execute(command)
        self.__connection.commit()


    def getAllWarnings(self):
        cursor = self.__connection.cursor()
        query = "SELECT * FROM piWeather.settings"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def deleteWarning(self, warningID):
        cursor = self.__connection.cursor()
        self.__connection = connector.connect(**self.__dsn)
        cursor = self.__connection.cursor()
        query = "DELETE FROM settings where settingsID = '{param}';"
        command = query.format(param=warningID)
        cursor.execute(command)
        self.__connection.commit()


    def setCameraTrigger(self, sensorName, triggerValue):
        cursor = self.__connection.cursor()
        query = "INSERT INTO cameraTriggers(sensorName, triggerValue) VALUES('{param1}', '{param2}');"
        command = query.format(param1=sensorName, param2=triggerValue)
        cursor.execute(command)
        self.__connection.commit()
        cursor.close()



    def close_cursor(self):
        self.__cursor.close()



