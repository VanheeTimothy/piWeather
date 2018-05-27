from RPi import GPIO
import time
from classMcp3008 import Mcp3008

GPIO.setmode(GPIO.BCM)


class Rgbled():
    def __init__(self, r, g, b):
        self.__leds = [r, g, b]
        for led in self.__leds:
            GPIO.setup(led, GPIO.OUT)

        self.__rood = GPIO.PWM(r, 50)
        self.__groen = GPIO.PWM(g, 50)
        self.__blauw = GPIO.PWM(b, 50)

    def roodWaarde(self):
        self.__rood.start(0)
        for i in range(100):
            self.__rood.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100):
            self.__rood.ChangeDutyCycle(100 - i)
            time.sleep(0.02)

    def groenWaarde(self):
        self.__groen.start(0)
        for i in range(100):
            self.__groen.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100):
            self.__groen.ChangeDutyCycle(100 - i)
            time.sleep(0.02)

    def blauwWaarde(self):
        self.__blauw.start(0)
        for i in range(100):
            self.__blauw.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100):
            self.__blauw.ChangeDutyCycle(100 - i)
            time.sleep(0.02)


try:
    led = Rgbled(13, 19, 26)

    while 1:
        led.roodWaarde()
        led.groenWaarde()
        led.blauwWaarde()
except KeyboardInterrupt:
    GPIO.cleanup()
