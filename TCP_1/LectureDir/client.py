import socket

# Client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8888))

# data = client_socket.recv(256)

# print(data.decode('utf-8'))

# client_socket.close()
# input()
while True:
    data = client_socket.recv(512)
    print(data.decode('utf-8'))

    client_socket.send(input('Enter your message: ').encode('utf-8'))

