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
 client_socket, client_address = server.accept()
 print 'Connection from: ', client_address
 data = client_socket.recv(1024)
 while not data == '':
   print 'Received: ', data
   client_socket.send(data.upper())
   data = client_socket.recv(1024)
 print 'Client disconnected'
 client_socket.close()
