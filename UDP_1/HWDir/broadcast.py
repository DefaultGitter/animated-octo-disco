# Написати годинник з використанням UDP протоколу.
# На сервері встановлюється служба надсилання пакетів,
# що містять інформацію про поточний час у локальну мережу.
# Клієнти відображають поточний час.

import socket
from datetime import datetime
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

c_time = f'{datetime.now():%H:%M:%S}'

while True:
    while c_time[6:] != '00':
        c_time = f'{datetime.now():%H:%M:%S}'
        print(c_time)
        time.sleep(1)
    else:
        s.sendto(c_time[:5].encode('utf-8'), ('255.255.255.255', 8000))
        print('sended')
        time.sleep(1)
        c_time = f'{datetime.now():%H:%M:%S}'
