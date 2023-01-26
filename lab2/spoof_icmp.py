#!/usr/bin/python3

from scapy.all import *

ip = IP(src="1.2.2.1", dst="10.9.0.5")
icmp = ICMP()
pkt = ip/icmp

send(pkt)

