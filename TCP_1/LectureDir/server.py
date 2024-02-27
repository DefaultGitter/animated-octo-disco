import socket
# telnet IP port in cmd
# Server
# 1
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2
# server_socket.bind(('127.0.0.1', 8888))
server_socket.bind(('192.168.1.3', 8888))
# 3
server_socket.listen()
# 4
while True:
    client_socket, addr = server_socket.accept()
    print('Connected by', addr)

    # client_socket.send(f'Hello, {addr}'.encode('utf-8'))
    client_socket.send(input('Enter your message: ').encode('utf-8'))

    data = client_socket.recv(512)
    print(data.decode('utf-8'))

    # client_socket.close()
    # server_socket.close()

    # input()
