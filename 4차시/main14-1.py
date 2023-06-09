import RPi.GPIO as GPIO
import time
from picamera2 import Picamera2
import datetime


pirPin = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

picam2 = Picamera2()

try:
    while True:
        sensorValue = GPIO.input(pirPin)
        if sensorValue == 1:
            now = datetime.datetime.now()
            print(now)
            fileName = now.strftime('%Y-%m-%d %H:%M:%S')
            picam2.start_and_capture_file(fileName + '.jpg')
            time.sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
