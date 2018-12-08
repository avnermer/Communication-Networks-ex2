from socket import socket, AF_INET, SOCK_STREAM
import os.path
from argparse import ArgumentParser
#parser = ArgumentParser()
#parser.add_argument("myPort", type=int)
#args = parser.parse_args()

found_msg = 'HTTP/1.1 200 OK'
not_found_msg = 'HTTP/1.1 404 Not Found'
close_msg = 'Connection: close'
moved_msg = 'HTTP/1.1 301 Moved Permanently'
location_msg = 'Location: /result.html'


server = socket(AF_INET, SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 12345
# if specified as argument
#if (args.myPort):
 #   server_port = args.myPort
server.bind((server_ip, server_port))
server.listen(5)

while True:
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    data = client_socket.recv(1024)
    if not data:
        continue
    while not '\r\n\r\n' in data:
        data += client_socket.recv(1024)
        print 'Received: ', data
    data = data.strip().split(' ')[1]
    if data == '/':
        data = 'index.html'
    elif data == '/redirect':
        client_socket.send(moved_msg + '\r\n' + close_msg + '\r\n' + location_msg + '\r\n\r\n')
        client_socket.close()
        continue

    data = 'files/' + data

    answer = ''
    if not os.path.isfile(data):
        client_socket.send(not_found_msg + '\r\n' + close_msg + '\r\n\r\n')
        client_socket.close()
        continue
    file = open(data, 'rb')
    answer = found_msg

    answer += '\r\n' + close_msg + '\r\n\r\n'
    answer += file.read()
    client_socket.send(answer)
    file.close()
    print 'Client disconnected'
    client_socket.close()