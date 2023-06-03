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
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    bus.write_byte_data(Device_Address, CONFIG, 0)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    value = ((high << 8) | low)
    
    if(value > 32768):
        value = value - 65536
        
    return value

try:
    MPU_Init() # 자이로센서 초기화
    while True:
        acc_x = read_raw_data(ACCEL_XOUT_H) # 가속도 X 센서 값 읽기
        acc_y = read_raw_data(ACCEL_YOUT_H) # 가속도 Y 센서 값 읽기
        acc_z = read_raw_data(ACCEL_ZOUT_H) # 가속도 Z 센서 값 읽기
        
        gyro_x = read_raw_data(GYRO_XOUT_H) # 각속도 X 센서 값 읽기
        gyro_y = read_raw_data(GYRO_YOUT_H) # 각속도 Y 센서 값 읽기
        gyro_z = read_raw_data(GYRO_ZOUT_H) # 각속도 Z 센서 값 읽기
        
        print('acc_x : ', acc_x)
        print('acc_y : ', acc_y)
        print('acc_z : ', acc_z)
        print('gyro_x : ', gyro_x)
        print('gyro_y : ', gyro_y)
        print('gyro_z : ', gyro_z)
        print('')
        time.sleep(0.1)
    
except KeyboardInterrupt:
    pass

