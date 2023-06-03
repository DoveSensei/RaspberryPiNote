import time
import datetime
import os

# 파일 이름 설정
file_name = 'time_log.txt'

# 파일이 존재할 경우 삭제
if os.path.exists(file_name):
    os.remove(file_name)

try:
    while True:
        now_date_time = datetime.datetime.now() # 현재 시간 얻기
        now_linux_time = time.time() # 리눅스 현재 시간 얻기
        print('now_date_time : ', now_date_time) 
        print('now_linux_time: ', now_linux_time)
        print('')
        f = open(file_name,'a') # 파일 오픈
        f.write(str(now_date_time) + ' ' + str(now_linux_time) + '\n') #파일 쓰기
        f.close() #파일 닫기
        time.sleep(1.0)
    
except KeyboardInterrupt:
    pass


