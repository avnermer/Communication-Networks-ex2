from socket import socket, AF_INET, SOCK_STREAM
from argparse import ArgumentParser
from time import sleep


def send_msg():
    msg = 'A'
    s.send(msg)
    s.send(msg)


parser = ArgumentParser()
parser.add_argument("serverIP")
parser.add_argument("serverPort", type=int)
args = parser.parse_args()
s = socket(AF_INET, SOCK_STREAM)
dest_ip = '127.0.0.1'
dest_port = 12345
s.connect((args.serverIP, args.serverPort))
send_msg()
sleep(2)
for x in range(0, 10):
    send_msg()
data = s.recv(4096)
print "Server sent: ", data
s.close()
