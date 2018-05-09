from scapy.all import *
import socket
import sys

#parse the list of 0s and 1s.
f = open("testoutput.txt","r")

contents = f.read()

#list of bytes waiting to be send
byteslist = []

for i in range(0,len(contents),8):
    byteslist.append(contents[i:i+8])

#covert them to int
intlist = []


#add it to an int and multiply everything by 128
for i in byteslist:
    intlist.append(int(i,2) * 128)



#Source and Destination
src = "192.168.24.29"  #this
dst = socket.gethostbyname(str(sys.argv[1]))
sport = random.randint(1024,65535)
dport = int(80)


packetlist = []
packetans = []
counter = 0
# make packets and three way handshake
SYN = None
SYNACK = None
sequence = int(2**31 * (random.random()))
for i in intlist:
    #make the syn packet if it is first packet
        # SYN
    SYN=IP(dst = dst)/TCP(flags='S',seq=1000,dport = 80)
    SYN.payload.window = i
    SYNACK = sr1(SYN)
