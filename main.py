import dpkt 
from dpkt.compat import compat_ord
import os, sys
import socket
import binascii
import json


file = open('20110413_pcap_1.pcap', 'rb')
#ip:mac

binetflow = {}
ip_macs = {}
packets = dpkt.pcap.Reader(file)

def mac_addr(address):
    return ':'.join('%02x' % compat_ord(b) for b in address)

for ts, buf in packets:

    eth = dpkt.ethernet.Ethernet(buf)
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        src = socket.inet_ntoa(ip.src)
        dst = socket.inet_ntoa(ip.dst)
        mac = mac_addr(eth.src)
        if mac not in ip_macs:
            ip_macs[mac] = [src]
        else:
            if src not in ip_macs[mac]:
                ip_macs[mac].append(src)
                
        if src not in binetflow:
            binetflow[src] = {dst: ip.len}
        else:
            if dst in binetflow[src]:
                binetflow[src][dst] = binetflow[src][dst] + ip.len
            else:
                binetflow[src][dst] = ip.len
            
print(json.dumps(ip_macs))
output = open("macaddresses.txt", "w")
output.write(json.dumps(ip_macs))
output.close()