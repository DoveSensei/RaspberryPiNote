import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO 모드 초기화
GPIO.setup(24, GPIO.OUT) # 24번 핀 OUT 모드 설정 / 메모리 할당
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 23번 핀 IN 모드 설정 / 메모리 할당

try:
    while True:
        switch_state = GPIO.input(23) # 23번 스위치 값 읽기
        if switch_state:
            GPIO.output(24,GPIO.HIGH) # 24번 핀 1
        else:
            GPIO.output(24,GPIO.LOW) # 24번 핀 0


# Ctrl+C 입력시 프로그램 종료
except KeyboardInterrupt:
    pass

GPIO.cleanup()





