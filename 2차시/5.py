import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) #GPIO 메모리 초기화
GPIO.setmode(GPIO.BCM) #GPIO 모드 초기화
GPIO.setup(16,GPIO.OUT) #GPIO 16번핀 OUT 모드 설정 / 메모리 할당

p = GPIO.PWM(16,1) # 16번핀 PWM 모드 설정

try:
    while True: # 무한 반복
        p.start(50) # 초기 PWM 50% / 부저 사운드 50%
        p.ChangeFrequency(262) # 부저 주파수 262Hz 설정
        time.sleep(1.0) # 1초 대기
        p.ChangeFrequency(294) # 부저 주파수 294Hz 설정
        time.sleep(1.0) # 1초 대기
        p.ChangeFrequency(330) # 부저 주파수 330Hz 설정
        time.sleep(1.0) # 1초 대기
        p.ChangeFrequency(349) # 부저 주파수 349Hz 설정
        time.sleep(1.0) # 1초 대기
        p.ChangeFrequency(392) # 부저 주파수 392Hz 설정
        time.sleep(1.0) # 1초 대기
        p.stop() # PWM 정지 / 부저 사운드 0%
        time.sleep(1.0) # 1초 대기

# Ctrl + C 입력시 프로그램 종료
except KeyboardInterrupt:
    pass

p.stop() # PWM 정지 / 부저 사운드 0%
GPIO.cleanup() # GPIO 메모리 할당 해제

