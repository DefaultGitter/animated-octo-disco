import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.3.80', 8000))


def receive():
    while True:
        data = s.recv(1024)
        print(data.decode('utf-8'))


receive()
