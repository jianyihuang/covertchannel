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



packetlist = []
ip = socket.gethostbyname(str(sys.argv[1]))
packetans = []
counter = 0
# make packets
for i in intlist:
    counter = counter + 1
    packet = IP(dst = ip)/TCP()
    packet.payload.window = i
    if (counter == 2):
        packet.flag = "A"
    packetlist.append(packet)

counter = 0

# send packets
for i in packetlist:
    print (i.payload.window)
    ans,unans = sr(i,verbose = 0)
    packetans.append(ans)
