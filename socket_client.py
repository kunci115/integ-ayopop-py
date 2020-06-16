import socket


def tcp_handler(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('hli-tcp-router-apim.apps.ocp-dev.hanabank.co.id', 32449))
    client_socket.send(bytes(data, encoding='utf-8'))
    reply = client_socket.recv(131072)
    return reply.decode()

