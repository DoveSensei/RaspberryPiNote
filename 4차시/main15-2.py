import time
import datetime
from picamera2 import Picamera2

flag = 0

picam2 = Picamera2()

try:
    while True:
        now = datetime.datetime.now()
        nowMin = now.minute
        print(nowMin)
        if nowMin % 5 == 0:
            if flag == 0:
                flag = 1
                fileName = now.strftime('%Y-%m-%d %H:%M:%S')
                picam2.start_and_capture_file('timelabs_' + fileName + '.jpg')
                print("ok")
        else:
            flag = 0
        time.sleep(1)

except KeyboardInterrupt:
    pass




