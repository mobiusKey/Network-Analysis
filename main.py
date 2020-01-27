import dpkt 
from dpkt.compat import compat_ord
import os, sys
import socket
import binascii
import json


file = open('20110413_pcap_1.pcap', 'rb')
#ip:mac
output_string = "edges: ["

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
        
        output_string += '{  source: {id: ' + src + ', label: "' + src + '"}, target: {id: ' + dst + ', label: "'+dst+'"},value: "Test" },'
        

output_string += "]}"
print(json.dumps(ip_macs))
output = open("vis", "w")
output.write(output_string)
output.close()