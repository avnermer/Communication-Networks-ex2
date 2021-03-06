from socket import socket, AF_INET, SOCK_STREAM
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("myPort", type=int)
args = parser.parse_args()

server = socket(AF_INET, SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 12345
server.bind((server_ip, args.myPort))
server.listen(5)

while True:
    isAlreadySend = False
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    count = 0
    data = client_socket.recv(1024)
    count += len(data)
    while not data == '':
        print 'Received: ', data
        data = client_socket.recv(1024)
        # count the len of all data
        count += len(data)
    if count == 22 and not isAlreadySend:
        # send to client one time
        client_socket.send('B')
        isAlreadySend = True
    print 'Client disconnected'
    client_socket.close()