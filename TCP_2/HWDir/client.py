import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))


def receive():
    while True:
        data = client.recv(1024)
        if not data:
            exit()
        print(data.decode('utf-8'))


Thread(target=receive).start()

while True:
    try:
        message = input('Enter your message: ')
        client.send(message.encode('utf-8'))
    except ValueError:
        print()
        exit('You are disconnected')
