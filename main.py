import os, sys
import csv
# import json


ips = ""
#output_string = "edges: ["

# def mac_addr(address):
    # return ':'.join('%02x' % compat_ord(b) for b in address)

# for ts, buf in packets:
    # print(datetime.datetime.utcfromtimestamp(ts))
    # eth = dpkt.ethernet.Ethernet(buf)
    # if isinstance(eth.data, dpkt.ip.IP):
        # ip = eth.data
        # src = socket.inet_ntoa(ip.src)
        # dst = socket.inet_ntoa(ip.dst)
        
        # if src not in ips:
            # ips.append(src)
        # # mac = mac_addr(eth.src)
with open('conversations.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] != "Address A":
           # output_string += '{  source: {id: ' +'"'+ row[0] +'"'+ ', label: "' + row[0] + '"}, target: {id: ' +'"'+ row[1]+'"' + ', label: "'+ row[1]+ '"},value: ' +row[3]+' },'
            if row[0] not in ips:
                ips += row[0] + "\n"
       

#output_string += "]}}"
# print(json.dumps(ip_macs))
output = open("ips", "w")
output.write(ips)
output.close()