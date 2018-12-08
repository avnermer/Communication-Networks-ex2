from socket import socket, AF_INET, SOCK_STREAM
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("serverIP")
parser.add_argument("serverPort", type=int)
args = parser.parse_args()
s = socket(AF_INET, SOCK_STREAM)
dest_ip = '127.0.0.1'
dest_port = 12345
s.connect((args.serverIP,args.serverPort))
msg = 'A' * 15000
s.send(msg)
data = s.recv(1024)
print "Server sent: ", data
#msg = raw_input("Message to send: ")
s.close()
