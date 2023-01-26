#!/usr/bin/python3
from scapy.all import *

def spoof_pkt(pkt):
  if ICMP in pkt:

    print("Original Packet.........")
    print("Source IP : ", pkt[IP].src)
    print("Destination IP :", pkt[IP].dst)
      
    ip = IP(src=pkt[IP].dst, dst=pkt[IP].src, ihl=pkt[IP].ihl, ttl=50)
    icmp = ICMP(type=0, code=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)
    data = pkt[ICMP].load

    newpkt = ip/icmp/data

    print("Spoofed Packet.........")
    print("Source IP : ", newpkt[IP].src)
    print("Destination IP :", newpkt[IP].dst)

    # newpkt.show()
    send(newpkt,verbose=1)

pkt = sniff(iface='br-4177281c6d27', filter='icmp[icmptype] == icmp-echo and src host 10.9.0.5',prn=spoof_pkt)

