#!/usr/bin/python3

from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface="br-aeb04590cf6e", filter="net 128.230.0.0/16", prn=print_pkt)

