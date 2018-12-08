from argparse import ArgumentParser
from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep

parser = ArgumentParser()
parser.add_argument("serverIP")
parser.add_argument("serverPort", type=int)
args = parser.parse_args()

s = socket(AF_INET, SOCK_DGRAM)
# server IP and port
dest_ip = '127.0.0.1'
dest_port = 12345
msg = 'A'
# send message to the server
s.sendto(msg, (args.serverIP, args.serverPort))
s.sendto(msg, (args.serverIP, args.serverPort))
sleep(2)
for x in range(0, 10):
    s.sendto(msg, (args.serverIP, args.serverPort))
    s.sendto(msg, (args.serverIP, args.serverPort))
# receive message from the server
data, sender_info = s.recvfrom(2048)
print "Server sent: ", data
# close client socket
s.close()



