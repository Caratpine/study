# coding=utf-8

import os
import sys
import threading
import signal
from scrapy.all import conf, sniff, wrpcap, ARP, send


interface = 'en0'
target_ip = ''
gateway_ip = ''
packet_count = 1000


# 设置嗅探的网卡
conf.iface = interface

# 关闭输出
conf.verb = 0

print '[*] Setting up {}'.format(interface)


def restore_target(gateway_ip, gateway_mac, target_ip, target_mac):
    pass


def get_mac(ip_address):
    pass


def poison_target(gateway_ip, gateway_mac, target_ip, target_mac):
    pass


gateway_mac = get_mac(gateway_ip)

if not gateway_mac:
    print '[!!!] Failed to get gateway MAC. Exiting.'
    sys.exit(0)
else:
    print '[*] Gateway {} is at {}'.format(gateway_ip, gateway_mac)

target_mac = get_mac(target_ip)

if not target_mac:
    print '[!!!] Failed to get target MAC. Exiting.'
    sys.exit(0)
else:
    print '[*] Target {} is at {}'.format(target_ip, target_mac)

poison_thread = threading.Thread(target=poison_target,
                                 args=(gateway_ip, gateway_mac, target_ip, target_mac))

poison_thread.start()

try:
    print '[*] Starting sniffer for {} packets'.format(packet_count)

    bpf_filter = 'ip host {}'.format(target_ip)
    packets = sniff(count=packet_count, filter=bpf_filter, iface=interface)

    wrpcap('arper.pcap', packets)
    restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
except KeyboardInterrupt:
    restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
    sys.exit(0)
