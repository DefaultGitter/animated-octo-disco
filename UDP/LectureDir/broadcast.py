import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('t:')
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(input().encode('utf-8'), ('255.255.255.255', 8888))
