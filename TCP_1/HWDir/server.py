# Завдання 1.
# Створіть сервер, який слухає певний порт.
# Створіть клієнт, який підключається до порту.
# Сервер повинен приймати повідомлення від клієнта і відправляти назад відлуння.
# Клієнт повинен надсилати повідомлення серверу та виводити відповідь.

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen()
while True:
    client_socket, addr = server_socket.accept()
    print('Connected by', addr)

    client_socket.send(f'{addr} connected'.encode('utf-8'))

    data = client_socket.recv(512)
    print(data.decode('utf-8'))
