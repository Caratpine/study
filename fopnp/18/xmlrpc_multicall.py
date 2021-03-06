#!/usr/bin/env python3

import xmlrpc.client


def main():
    proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:7001")
    multicall = xmlrpc.client.MultiCall(proxy)
    multicall.addtogether('a', 'b', 'c')
    multicall.quadratic(2, -4, 0)
    multicall.remote_repr([1, 2.0, 'three'])
    for answer in multicall():
        print(answer)


if __name__ == '__main__':
    main()
