import socket

'''
Creating a socket Object

socket.socket(family, type, proto, fileno)

Family:
- AF_INET. This family is used with IPV4 addresses. When we first introduced IP addresses, 
we were talking about IPV4 addresses. IP addresses are most commonly used.
- AF_INET6
- AF_UNIX

Type. The type specifies the transport layer protocol:
- SOCK_DGRAM specifies that the application is to use User UDP. Recall that UDP is less reliable but 
requires no initial connection establishment. We are building these server and client programs pair in UDP
- SOCK_STREAM specifies that the application is to use TCP
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(s)

# Binding The Socket #
port = 3000
hostname = '127.0.0.1'
s.bind((hostname, port))
