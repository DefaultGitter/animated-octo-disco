import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen()
server_clients = []


def receive(_user):
    while True:
        try:
            data = _user.recv(1024)
            if data.decode('utf-8').lower() == 'exit':
                server_clients.remove(_user)
                _user.close()

            print(data.decode('utf-8'))

            for client in server_clients:
                try:
                    client.send(data)
                except ConnectionError:
                    server_clients.remove(_user)

        except OSError:
            print('User disconnected')
            break


while True:
    user, addr = server.accept()
    server_clients.append(user)
    print('Connected by', addr)
    Thread(target=receive, args=(user,)).start()
