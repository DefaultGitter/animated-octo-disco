import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('192.168.3.80', 8887))


# def receive():
# while True:
#         data = s.recv(1024)
#         print(data.decode('utf-8'))


# thread = Thread(target=receive).start()

while True:
    print('t:')
    s.sendto(input().encode('utf-8'), ('192.168.3.80', 8888))
