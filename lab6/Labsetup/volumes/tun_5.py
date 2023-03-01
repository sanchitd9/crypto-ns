#!/usr/bin/env python3

import fcntl
import struct
import os
import time
from scapy.all import *

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002
IFF_NO_PI = 0x1000

# Create the tun interface
tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'tun%d', IFF_TUN | IFF_NO_PI)
ifname_bytes  = fcntl.ioctl(tun, TUNSETIFF, ifr)

# Get the interface name
ifname = ifname_bytes.decode('UTF-8')[:16].strip("\x00")
print("Interface Name: {}".format(ifname))

# Assign IP address to the interface
os.system("ip addr add 192.168.53.99/24 dev {}".format(ifname))

# Bring up the interface
os.system("ip link set dev {} up".format(ifname))

# Add IP route for 192.168.60.0/24
os.system("ip route add 192.168.60.0/24 dev {}".format(ifname))

while True:
   # Get a packet from the tun interface
   packet = os.read(tun, 2048)
   if packet:
       ip = IP(packet)
       print(ip.summary())

       os.write(tun, b"hello, world")
