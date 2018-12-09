from socket import socket, AF_INET, SOCK_DGRAM
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("myPort", type=int)
args = parser.parse_args()

s = socket(AF_INET, SOCK_DGRAM)
source_ip = "0.0.0.0"
source_port = 12345
s.bind((source_ip, args.myPort))
count = 0
isAlreadySend = False
while True:
    data, sender_info = s.recvfrom(1024)
    count += len(data)
    while not data == '':
        print("Received: " + data)
        data, sender_info = s.recvfrom(1024)
        count += len(data)
        if count == 22 and not isAlreadySend:
            # send to client one time
            s.sendto("B", sender_info)
            isAlreadySend = True

