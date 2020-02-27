# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 11:18
# @Author  : 奥利波德
# @FileName: ActionAnalyze.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507

import os
import re
import UrlAnalyze
import DataDispose
import numpy as np

# path = "G:\机器学习-冯\张莹\渥大数据集\PHISH_ARCHIVE"
# dirs = os.listdir(path)
# action = []
# for dir in dirs:
#     if os.path.splitext(dir)[1] == ".html":
#         with open(path + "\\" + dir, "r", encoding='UTF-8') as urlFile:
#             data = urlFile.read()
#         url = re.search(r'(?<=action=").*?(?=")', data)
#         if url and len(url.group()) > 3:
#             action.append(url.group() + '\n')
#         else:
#             action.append('' + '\n')
with open("./data/action.txt", 'r') as f:
    action = f.readlines()
url = UrlAnalyze.get_dns(action)
# with open("./data/actionIp.txt", 'w') as f:
#     f.writelines(url+'/n')
data = DataDispose.toMatrix(url)
np.savetxt("./data/action.csv", data, fmt='%d', delimiter=',')
