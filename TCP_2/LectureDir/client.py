import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))


def receive():
    while True:
        data = client.recv(1024)
        print(data.decode('utf-8'))


Thread(target=receive).start()

while True:
    client.send(input('Enter your message: ').encode('utf-8'))
