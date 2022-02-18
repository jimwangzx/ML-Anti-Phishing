from scapy.all import *
from scapy.layers.http import HTTPRequest # import HTTP packet

def process_packet(packet):

    if packet.haslayer(HTTPRequest):
        # if this packet is an HTTP Request
        # get the requested URL
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        # get the requester's IP Address
        ip = packet[IP].src
        # get the request method
        method = packet[HTTPRequest].Method.decode()
        print(ip, " Requested ", url, " with ", method)

#sniff(prn=lambda x: x.summary())
#sniff(filter='port 80', prn=process_packet, store=False)
sniff(iface="wlo1",filter="port 80", prn=process_packet, store=False)
