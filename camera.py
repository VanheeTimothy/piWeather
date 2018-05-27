from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180



try:
    fotonummer = 1
    while 1:
        camera.start_preview()
        sleep(2)

        camera.capture('/home/timo/Documents/weatherstation/static/img/foto{}.jpg'.format(fotonummer))
        fotonummer +=1
        camera.stop_preview()
        sleep(2)
        print(fotonummer)
except KeyboardInterrupt:
    print("einde")

