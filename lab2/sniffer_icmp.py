#!/usr/bin/python3

from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface="br-aeb04590cf6e", filter="icmp", prn=print_pkt)

