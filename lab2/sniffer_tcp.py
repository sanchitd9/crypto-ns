#!/usr/bin/python3

from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface="br-aeb04590cf6e", filter="tcp and src host 10.9.0.5 and dst port 23", prn=print_pkt)

