import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO 모드 초기화
GPIO.setup(24, GPIO.OUT) # 24번 핀 OUT 모드 설정 / 메모리 할당

ledWhitePwm = GPIO.PWM(24,500) # 24번 핀 PWM 500Hz 설정
ledWhitePwm.start(0) # 24번 핀 PWM LOW
            
ledWhitePwm.ChangeDutyCycle(0) # 24번 핀 PWM 시작 0% Duty 설정
time.sleep(1.0) # 1초 대기
ledWhitePwm.ChangeDutyCycle(30) # 24번 핀 PWM 시작 30% Duty 설정
time.sleep(1.0) # 1초 대기
ledWhitePwm.ChangeDutyCycle(60) # 24번 핀 PWM 시작 60% Duty 설정
time.sleep(1.0) # 1초 대기
ledWhitePwm.ChangeDutyCycle(100) # 24번 핀 PWM 시작 100% Duty 설정

GPIO.cleanup() # 모든 GPIO 메모리 할당 해제
