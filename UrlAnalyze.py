# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 19:35
# @Author  : 奥利波德
# @FileName: UrlAnalyze.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
import socket
import DataDispose
import pandas as pd
import time
from urllib.request import urlparse

# urlList = DataDispose.url_list_read()
urlList = []

def get_domain():
    with open("domain.txt", "w") as f:
        for url in urlList:
            domain = urlparse(url).netloc + '\n'
            f.write(domain)


def get_length():
    pass


def get_dns(domains):
    iplist = []
    for domain in domains:
        try:
            myaddr = socket.getaddrinfo(domain[:-1], 'http')
            iplist.append(myaddr[0][4][0])
        except Exception:
            iplist.append(None)
            continue
    return iplist


def to_csv(iplist):
    df = pd.read_csv('urlAnalyze.csv')
    df.insert(2, 'ip', iplist)


if __name__ == '__main__':
    begin = time.time()
    iplist = get_dns()
    print("get dns over")
    with open("ip.txt", "w") as f:
        for ip in iplist:
            if ip is None:
                ip = ''
            f.write(ip + '\n')
    over = time.time()
    cost = over - begin
    print(" cost " + str(cost) + "s")
