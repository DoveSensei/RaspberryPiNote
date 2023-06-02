import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO 모드 초기화
GPIO.setup(24,GPIO.OUT) # 24번 핀 OUT 모드 설정 / 메모리 할당

GPIO.output(24,GPIO.HIGH) # 24번 핀 1
time.sleep(1.0) # 1초 대기
GPIO.output(24,GPIO.LOW) # 24번 핀 0

GPIO.cleanup() # 모든 GPIO 메모리 할당 해제
