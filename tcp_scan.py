# coding=utf-8

import time
import socket


socket_timeout = 0.1


def tcp_scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(socket_timeout)
        c = s.connect_ex((ip, port))

        if c == 0:
            print('%s:%s is open' % (ip, port))
        else:
            pass
    except Exception as e:
        print(e)
    finally:
        s.close()


if __name__ == '__main__':
    start = time.time()
    ip = '61.135.169.125'
    for port in range(0, 1024):
        tcp_scan(ip, port)
    end = time.time()
    print('scan time is %s' % (end - start))
