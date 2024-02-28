import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen()
server_clients = []


def receive(_user):
    while True:
        data = _user.recv(1024)
        print(data.decode('utf-8'))
        for client in server_clients:
            client.send(data)


while True:
    user, addr = server.accept()
    server_clients.append(user)
    print('Connected by', addr)
    Thread(target=receive, args=(user,)).start()

    # user.send(input('Enter your message: ').encode('utf-8'))
