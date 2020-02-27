# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 18:41
# @Author  : 奥利波德
# @FileName: DataDispose.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
import os
import pandas as pd
from urllib.request import urlparse
import numpy as np


# 从数据集中取得所有网页的url地址，并保存到url.txt中
def get_url_to_txt():
    with open("url.txt", "a") as outFile:
        path = "G:\机器学习-冯\张莹\渥大数据集\PHISH_ARCHIVE"
        dirs = os.listdir(path)
        for dir in dirs:
            if os.path.splitext(dir)[1] == ".url":
                with open(path + "\\" + dir, "r") as urlFile:
                    data = urlFile.readline()
                    outFile.write(data)


# 返回url数据集  列表类型
def url_list_read():
    with open("url.txt", "r") as f:
        url_list = f.readlines()
    f.close()
    return url_list


def get_domain_list():
    domainList = []
    with open("domain.txt", "r") as f:
        for line in f.readlines():
            line.strip('\n')
            domainList.append(line)
    return domainList


def get_url_to_csv():
    urlList = url_list_read()
    domainList = []
    for url in urlList:
        domainList.append(urlparse(url).netloc)
    file = pd.DataFrame({'url': urlList, 'domain': domainList})
    file.to_csv("urlAnalyze.csv", index=False, sep=',')


def toMatrix(list):
    size = len(list)
    matrix = np.zeros((size, size), dtype=int)
    for length in range(0, size):
        for wide in range(0, size):
            if list[length] is not None and list[length] is not '' and list[length] == list[wide] and length != wide:
                matrix[length, wide] = 1

    return matrix
