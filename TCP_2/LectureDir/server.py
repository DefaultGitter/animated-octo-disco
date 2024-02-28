import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 8888))

server.listen()

user, addr = server.accept()
print('Connected by', addr)


def receive():
    while True:
        data = user.recv(1024)
        print(data.decode('utf-8'))


Thread(target=receive).start()

while True:
    user.send(input('Enter your message: ').encode('utf-8'))
