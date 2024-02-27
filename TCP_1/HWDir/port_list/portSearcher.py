# Створіть програму, яка приймає IP-адресу як вхідні дані.
# Використовуйте сокети для спроби підключення до різних портів цієї IP-адреси. Виведіть список відкритих портів.
import socket

port = 0
open_port_list = []
ip = input('Enter your IP: ')
lm = int(input('Enter search limit (9999 or 65535): '))
if lm > 9999:
    print('Warning! The search limit is very big. Program execution time can be quite long.')
    input('Press enter to continue...')
while port <= lm:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port))
        print(f'{port} is open')
        open_port_list.append(port)
        port += 1
    except OSError:
        print(f'{port} CLOSED')
        port += 1

print('Empty ports:')
print(open_port_list)
