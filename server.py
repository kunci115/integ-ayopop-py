import socket

# Create a TCP/IP socket
from core import inquiry_req
from core import payment_req
from core import status_req

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 10000)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    print('connection from', client_address)

    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(1024)
        print('received {!r}'.format(data))
        if data[34:41].decode() == 'AYOPINQ':
            status = inquiry_req(data)
            print('sending data back to the client')
            connection.sendall(bytes(status.text, encoding='utf8'))
        elif data[34:41].decode() == 'AYOPYMN':
            status = payment_req(data)
            print('not sending back, please make sure your callback active to receive the response reply')
            connection.sendall(bytes(status.text, encoding='utf8'))
        elif data[34:41].decode() == 'AYOPSTS':
            status = status_req(data)
            print('sending data back to the client')
            connection.sendall(bytes(status.text, encoding='utf8'))
        else:
            print('no data from', client_address)
