import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('The OS assigned the address {} to me'.format(s.getsockname()))
