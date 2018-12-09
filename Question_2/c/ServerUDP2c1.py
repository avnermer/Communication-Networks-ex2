from socket import socket, AF_INET, SOCK_DGRAM
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("myPort", type=int)
args = parser.parse_args()

s = socket(AF_INET, SOCK_DGRAM)
source_ip = "0.0.0.0"
source_port = 12345
s.bind((source_ip, args.myPort))
isAlreadySend = False
count = 0
while True:
    data, sender_info = s.recvfrom(15000)
    print("Received: " + data)
    # count the len of data
    count += len(data)
    if count == 15000:
        s.sendto("B", sender_info)
