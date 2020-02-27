# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 16:43
# @Author  : 奥利波德
# @FileName: MatrixFromIp.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
import numpy as np

with open("ip.txt") as f:
    ipList = f.readlines()
size = len(ipList)
matrixForIp = np.zeros((size, size), dtype=int)
for length in range(0, size):
    for wide in range(0, size):
        if ipList[length][:-1] == ipList[wide][:-1] and ipList[length][-1] is not '':
            matrixForIp[length, wide] = 1
np.savetxt('MatrixFormIp.csv', matrixForIp, fmt='%d', delimiter=',')
