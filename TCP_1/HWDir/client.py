import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

while True:
    data = client_socket.recv(512)
    print(data.decode('utf-8'))

    client_socket.send(f'signal'.encode('utf-8'))
