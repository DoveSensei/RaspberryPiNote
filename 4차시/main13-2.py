import RPi.GPIO as GPIO
import time
from picamera2 import Picamera2


import datetime

swPin = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

oldSw = 0
newSw = 0

picam2 = Picamera2()

try:
    while True:
        newSw = GPIO.input(swPin)
        if newSw != oldSw:
            oldSw = newSw
            
            if newSw == 1:
                now = datetime.datetime.now()
                print(now)
                fileName = now.strftime('%Y-%m-%d %H:%M:%S')
                picam2.start_and_capture_file(fileName + '.jpg')
                
            time.sleep(0.2)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

