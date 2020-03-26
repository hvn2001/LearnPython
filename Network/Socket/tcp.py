import argparse, socket

'''
bytes_sent = 0 # No bytes initially sent
while bytes_sent < len(message): # If number of bytes sent is less than the amount of data
  message_left = message[bytes_sent:] # Indexing and storing the part of the message remaining
  bytes_sent += sock.send(message_left) # Sending remaining message
  
  
Luckily,  Python has own implementation of this in a function called sendall(). 
It ensures that all of the data gets sent. 
Check out line 52 in the TCP server-client program above to see how it is used  
 sock.sendall(b'Greetings, server')
'''


def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', port))
    sock.listen(1)
    print('Listening at', sock.getsockname())
    while True:
        print('Waiting for a new connection')
        sc, sockname = sock.accept()
        print('Connection from', sockname)
        print('  Socket name:', sc.getsockname())
        print('  Socket peer:', sc.getpeername())
        message = recvall(sc, 16)
        print('  message from client:', repr(message))
        sc.sendall(b'Goodbye, client!')
        sc.close()
        print('  Closing socket')


def client(port):
    host = '127.0.0.1'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned the socket: ', sock.getsockname())
    sock.sendall(b'Greetings, server')
    reply = recvall(sock, 16)
    print('Server: ', repr(reply))
    sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000, help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
