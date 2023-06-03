import smbus
import time 

PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

bus = smbus.SMBus(1)    
Device_Address = 0x68

def MPU_Init():
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 0x07)
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 0x04)
    bus.write_byte_data(Device_Address, CONFIG, 0x00)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 0x00)
    bus.write_byte_data(Device_Address, INT_ENABLE, 0x01)

def read_raw_data(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    value = ((high << 8) | low)
    
    if(value > 32768):
        value = value - 65536
        
    return value

try:
    MPU_Init()

    calibration_number = 100
    avg_acc_x = 0
    avg_acc_y = 0
    avg_acc_z = 0
    avg_gyro_x = 0
    avg_gyro_y = 0
    avg_gyro_z = 0
        
    for i in range(calibration_number):
        acc_x = read_raw_data(ACCEL_XOUT_H) # 가속도 X 센서 값 읽기
        acc_y = read_raw_data(ACCEL_YOUT_H) # 가속도 Y 센서 값 읽기
        acc_z = read_raw_data(ACCEL_ZOUT_H) # 가속도 Z 센서 값 읽기
        gyro_x = read_raw_data(GYRO_XOUT_H) # 각속도 X 센서 값 읽기
        gyro_y = read_raw_data(GYRO_YOUT_H) # 각속도 Y 센서 값 읽기
        gyro_z = read_raw_data(GYRO_ZOUT_H) # 각속도 Z 센서 값 읽기
        
        avg_acc_x = avg_acc_x + acc_x # 가속도 X 센서 값 누적
        avg_acc_y = avg_acc_y + acc_y # 가속도 Y 센서 값 누적
        avg_acc_z = avg_acc_z + acc_z # 가속도 Z 센서 값 누적
        avg_acc_z = avg_acc_z - 16384.0 # 중력 값 보정
        avg_gyro_x = avg_gyro_x + gyro_x # 각속도 X 센서 값 누적
        avg_gyro_y = avg_gyro_y + gyro_y # 각속도 Y 센서 값 누적
        avg_gyro_z = avg_gyro_z + gyro_z # 각속도 Z 센서 값 누적
        time.sleep(0.1)
        print('Calibrating ' , i ,'/', calibration_number)
        
    avg_acc_x = avg_acc_x / calibration_number # 가속도 X 보정값 계산
    avg_acc_y = avg_acc_y / calibration_number # 가속도 Y 보정값 계산
    avg_acc_z = avg_acc_z / calibration_number # 가속도 Z 보정값 계산
    avg_gyro_x = avg_gyro_x / calibration_number # 각속도 X 보정값 계산
    avg_gyro_y = avg_gyro_y / calibration_number # 각속도 Y 보정값 계산
    avg_gyro_z = avg_gyro_z / calibration_number # 각속도 Z 보정값 계산
    
    while True:
        acc_x = read_raw_data(ACCEL_XOUT_H) # 가속도 X 센서 값 읽기
        acc_y = read_raw_data(ACCEL_YOUT_H) # 가속도 Y 센서 값 읽기
        acc_z = read_raw_data(ACCEL_ZOUT_H) # 가속도 Z 센서 값 읽기
        
        gyro_x = read_raw_data(GYRO_XOUT_H) # 각속도 X 센서 값 읽기
        gyro_y = read_raw_data(GYRO_YOUT_H) # 각속도 Y 센서 값 읽기
        gyro_z = read_raw_data(GYRO_ZOUT_H) # 각속도 Z 센서 값 읽기
        
        Ax = ((acc_x-avg_acc_x)/16384.0) * 9.80665 # 캘리브레이션 값 보정 후 가속도 X 센서 값 물리적인 값으로 변환
        Ay = ((acc_y-avg_acc_y)/16384.0) * 9.80665 # 캘리브레이션 값 보정 후 가속도 Y 센서 값 물리적인 값으로 변환
        Az = ((acc_z-avg_acc_z)/16384.0) * 9.80665 # 캘리브레이션 값 보정 후 가속도 Z 센서 값 물리적인 값으로 변환
        
        Gx = ((gyro_x-avg_gyro_x)/131.0) # 캘리브레이션 값 보정 후 각속도 X 센서 값 물리적인 값으로 변환 
        Gy = ((gyro_y-avg_gyro_y)/131.0) # 캘리브레이션 값 보정 후 각속도 Y 센서 값 물리적인 값으로 변환
        Gz = ((gyro_z-avg_gyro_z)/131.0) # 캘리브레이션 값 보정 후각속도 Z 센서 값 물리적인 값으로 변환
        
        print('Ax : ', Ax)
        print('Ay : ', Ay)
        print('Az : ', Az)
        print('Gx : ', Gx)
        print('Gy : ', Gy)
        print('Gz : ', Gz)
        print('')
        time.sleep(0.1)
    
except KeyboardInterrupt:
    pass
