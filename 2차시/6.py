import RPi.GPIO as GPIO
import time

TrigPin = 16
EchoPin = 20

GPIO.setwarnings(False) #GPIO 메모리 초기화
GPIO.setmode(GPIO.BCM) #GPIO 모드 초기화
GPIO.setup(TrigPin,GPIO.OUT) #GPIO TrigPin(16번핀) OUT 모드 설정 / 메모리 할당
GPIO.setup(EchoPin, GPIO.IN) #GPIO EchoPin(20번핀) OUT 모드 설정 / 메모리 할당

try:
    while True: # 무한 반복
        GPIO.output(TrigPin, True) # TrigPin(16번핀) 핀 1
        time.sleep(0.00001) # 0.00001초 대기
        GPIO.output(TrigPin, False) # TrigPin(16번핀) 핀 0

        # 초음파 센서 수신 대기, 수신 후 시간 체크
        while GPIO.input(EchoPin) == 0 :
            start_time = time.time()

        while GPIO.input(EchoPin) == 1 :
            end_time = time.time()

        duration = end_time - start_time # 걸린 시간 계산
        distanceCm = duration * 17000 # 걸린 시간(s) * [초음파 센서 속도(34000cm/s) / 2 ]
        distanceCm = round(distanceCm, 2) # 소수 두번째 자리 반올림

        print("cm:",distanceCm) #distanceCm값 출력
        time.sleep(0.5) #0.5초 대기

# Ctrl + C 입력시 프로그램 종료
except KeyboardInterrupt:
    pass
    
